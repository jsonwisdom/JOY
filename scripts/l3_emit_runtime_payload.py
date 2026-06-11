import hashlib, json, os, pathlib

paths = [
  "artifacts/L0_ATOMIC_RECEIPT_V0_1.json",
  "artifacts/L2_JAYWISDOM_TOKEN_CHALLENGE_100K_STAGING_V0_1.json",
  "artifacts/L2_100K_CHALLENGE_PROGRESS_TRACKER_V0_1.json",
  "artifacts/L3_EMISSION_RULES_STAGING_V0_1.json",
  "artifacts/L3_VERIFIER_TELEMETRY_MANIFEST_V0_1.json",
  "artifacts/L3_HASH_INTAKE_GEOMETRY_V0_1.json",
  "artifacts/L3_PROOF_TRANSITION_LOGIC_V0_1.json",
  "artifacts/L3_TELEMETRY_LAYER_FREEZE_V0_1.json",
]

blob = b""
for p in paths:
    data = pathlib.Path(p).read_bytes()
    blob += p.encode() + b"\n" + data + b"\n"

payload = {
  "RUN_ID": os.environ.get("GITHUB_RUN_ID", "LOCAL"),
  "COMPUTED_HASHES": {
    "sha256_replay_hash": hashlib.sha256(blob).hexdigest(),
    "sha3_256_bridge_hash": hashlib.sha3_256(blob).hexdigest()
  },
  "CI_STATUS_PASS": True
}

print("L3_RUNTIME_PAYLOAD_BEGIN")
print(json.dumps(payload, indent=2))
print("L3_RUNTIME_PAYLOAD_END")

pathlib.Path("artifacts").mkdir(exist_ok=True)
pathlib.Path("artifacts/L3_RUNTIME_PAYLOAD_CANDIDATE.json").write_text(
    json.dumps(payload, indent=2) + "\n"
)
