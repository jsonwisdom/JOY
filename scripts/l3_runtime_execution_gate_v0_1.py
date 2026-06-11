import json, hashlib, pathlib, datetime, sys

FILES = {
  "approval": pathlib.Path("artifacts/HUMAN_L3_APPROVAL_V0_1.json"),
  "replay": pathlib.Path("artifacts/L3_PROOF_TRANSITION_REPLAY_EVALUATION_V0_1.json"),
  "logic": pathlib.Path("_truth/verification/L3_PROOF_TRANSITION_LOGIC_V0_1.md"),
  "receipt": pathlib.Path("artifacts/L3_VERIFIER_RUNTIME_PAYLOAD_RECEIPT_V0_1.json"),
  "evaluation": pathlib.Path("artifacts/L3_PROOF_TRANSITION_EVALUATION_V0_1.json")
}

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

missing = [k for k,p in FILES.items() if not p.exists()]
if missing:
    print(json.dumps({"L3_RUNTIME_EXECUTION":"FAIL","missing":missing}, indent=2))
    sys.exit(1)

approval = json.loads(FILES["approval"].read_text())
replay = json.loads(FILES["replay"].read_text())

checks = {
  "approval_present": True,
  "approval_status_approved": approval.get("status") == "APPROVED",
  "approval_target_matches": approval.get("target") == "L3_PROOF_TRANSITION_REPLAY_EVALUATION_V0_1",
  "replay_evaluation_present": True,
  "transition_logic_present": True,
  "runtime_payload_receipt_present": True,
  "prior_evaluation_present": True,
  "authority_not_granted": approval.get("authority") is False,
  "membrane_intact": "membrane_intact" in approval.get("conditions_met", [])
}

passed = all(checks.values())

proof = {
  "artifact": "L3_RUNTIME_PROOF_V0_1",
  "version": "0.1",
  "layer": "L3",
  "timestamp": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
  "status": "PROOF_CREATED" if passed else "PROOF_BLOCKED",
  "execution": "L3_RUNTIME_EXECUTION_GATE_V0_1",
  "inputs": {k: str(p) for k,p in FILES.items()},
  "input_sha256": {k: sha256(p) for k,p in FILES.items()},
  "checks": checks,
  "runtime_execution_performed": True,
  "runtime_proof_created": passed,
  "proof_eligible": passed,
  "authority": False,
  "emission_eligible": False,
  "no_fake_green": True,
  "membrane": "INTACT",
  "decision": "RUNTIME_PROOF_CREATED" if passed else "RUNTIME_PROOF_BLOCKED",
  "note": "Proof records execution of the L3 transition gate only. It grants no authority and performs no emission."
}

state = {
  "artifact": "L3_TRANSITION_STATE_V0_2",
  "layer": "L3",
  "runtime_execution_gate": "EXECUTED",
  "human_approval": "PRESENT",
  "runtime_proof": proof["status"],
  "proof_eligible": passed,
  "runtime_proof_created": passed,
  "authority": False,
  "emission_eligible": False,
  "no_fake_green": True,
  "membrane": "INTACT",
  "next_lawful_move": "REVIEW_RUNTIME_PROOF_AND_DECIDE_L4_OR_EMISSION_GATE"
}

pathlib.Path("artifacts/L3_RUNTIME_PROOF_V0_1.json").write_text(json.dumps(proof, indent=2) + "\n")
pathlib.Path("artifacts/L3_TRANSITION_STATE_V0_2.json").write_text(json.dumps(state, indent=2) + "\n")

print(json.dumps({
  "L3_RUNTIME_EXECUTION": "PASS" if passed else "BLOCKED",
  "proof": "artifacts/L3_RUNTIME_PROOF_V0_1.json",
  "state": "artifacts/L3_TRANSITION_STATE_V0_2.json",
  "authority": False,
  "no_fake_green": True
}, indent=2))
