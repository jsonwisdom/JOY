#!/usr/bin/env python3
"""JOY family security OODA loop: synthetic public-safe drills, no authority.

Offline and read-only except an optional newly created local receipt. Does not
contact anyone, inspect user devices, collect identities, or grant consent.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

CATALOG_SHA256 = "e37c1e83a658e58afa6f7d0c039c66870858aedac7a82d96f82cad1f35119e36"
CATALOG_SCHEMA = "joy/family-security-ooda-scenarios/1"
REQUEST_SCHEMA = "joy/family-security-ooda-request/1"
RECEIPT_SCHEMA = "joy/family-security-ooda-receipt/1"
MAX_REQUEST_BYTES = 2048
MAX_CATALOG_BYTES = 10000
KEYS = {"schema", "scenario_id", "choice", "simulation", "authority",
        "family_gate", "human_approval", "private_data", "external_actions", "signals"}
SIGNALS = {"SYNTHETIC", "UNVERIFIED_ALERT", "REAL_EVENT_PRESENT"}
STATES = ("REJECT", "CONFLICT", "HOLD", "PASS")

class DrillRejected(Exception):
    pass

def require(test, reason):
    if not test:
        raise DrillRejected(reason)

def no_duplicates(pairs):
    doc = {}
    for key, val in pairs:
        require(key not in doc, "duplicate_json_key")
        doc[key] = val
    return doc

def reject_constant(_value):
    raise DrillRejected("nonfinite_json_number")

def strict_json(raw):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=no_duplicates,
                          parse_constant=reject_constant)
    except DrillRejected:
        raise
    except (ValueError, UnicodeError, TypeError) as exc:
        raise DrillRejected("invalid_json") from exc

def canonical(doc):
    return json.dumps(doc, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")

def load_catalog(raw):
    require(len(raw) <= MAX_CATALOG_BYTES, "catalog_size_invalid")
    require(hashlib.sha256(raw).hexdigest() == CATALOG_SHA256, "catalog_sha256_drift")
    data = strict_json(raw)
    require(type(data) is dict and set(data) == {"schema", "simulation_only", "authority", "public_safe", "scenarios"}, "catalog_keys_invalid")
    require(data["schema"] == CATALOG_SCHEMA and data["simulation_only"] is True
            and data["authority"] is False and data["public_safe"] is True, "catalog_boundary_invalid")
    items = data["scenarios"]
    require(type(items) is list and len(items) == 6, "catalog_scenario_count_invalid")
    ids = []
    for item in items:
        require(type(item) is dict and set(item) == {"id", "observe", "orient", "safe_choice", "assessment", "lesson"}, "catalog_scenario_keys_invalid")
        require(all(type(v) is str and v for v in item.values()), "catalog_scenario_values_invalid")
        require(item["assessment"] in {"PASS", "HOLD"}, "catalog_assessment_invalid")
        ids.append(item["id"])
    require(len(set(ids)) == len(ids), "catalog_duplicate_scenario")
    return {x["id"]: x for x in items}

def validate_request(request):
    require(type(request) is dict and set(request) == KEYS, "request_fields_invalid")
    require(request["schema"] == REQUEST_SCHEMA, "request_schema_invalid")
    require(request["simulation"] is True, "not_synthetic")
    require(request["authority"] is False, "authority_claim_rejected")
    require(request["family_gate"] == "SOVEREIGN_UNVERIFIED", "family_gate_rejected")
    require(request["human_approval"] == "NOT_ASSERTED", "approval_claim_rejected")
    require(request["private_data"] is False, "private_data_rejected")
    require(request["external_actions"] is False, "external_action_rejected")
    require(type(request["scenario_id"]) is str and type(request["choice"]) is str, "scenario_or_choice_invalid")
    signals = request["signals"]
    require(type(signals) is list and 0 < len(signals) <= 3 and
            all(type(s) is str and s in SIGNALS for s in signals) and
            len(set(signals)) == len(signals), "signals_invalid")
    require("SYNTHETIC" in signals, "synthetic_signal_missing")
    return signals

def result(state, reason, request_sha256, catalog_sha256):
    require(state in STATES, "internal_invalid_state")
    receipt = {
        "schema": RECEIPT_SCHEMA,
        "mode": "SYNTHETIC_OFFLINE_DRILL_ONLY",
        "ooda": ["OBSERVE", "ORIENT", "DECIDE", "ACT", "RETURN_TO_LEARNER"],
        "simulation_verdict": state,
        "effective_decision": "HOLD" if state == "PASS" else state,
        "reason": reason,
        "request_sha256": request_sha256,
        "catalog_sha256": catalog_sha256,
        "family_gate": "SOVEREIGN_UNVERIFIED",
        "human_approval": "NOT_ASSERTED",
        "heidee_consent": "NOT_INFERRED",
        "authority": False,
        "private_data_collected": False,
        "external_actions": False,
        "contacts": "NONE",
        "account_changes": "NONE",
        "real_emergency_response": "NOT_PERFORMED",
        "live_drill_activation": "HOLD",
    }
    receipt["receipt_sha256"] = hashlib.sha256(canonical(receipt)).hexdigest()
    return receipt

def run(request_raw, catalog_raw):
    rq_sha = hashlib.sha256(request_raw).hexdigest()
    catalog_sha = hashlib.sha256(catalog_raw).hexdigest()
    try:
        require(len(request_raw) <= MAX_REQUEST_BYTES, "request_too_large")
        catalog = load_catalog(catalog_raw)
        req = strict_json(request_raw)
        signals = validate_request(req)
        require(req["scenario_id"] in catalog, "unknown_scenario")
        if "REAL_EVENT_PRESENT" in signals:
            return result("CONFLICT", "stop_synthetic_drill_real_event_signal", rq_sha, catalog_sha)
        if "UNVERIFIED_ALERT" in signals:
            return result("HOLD", "unverified_alert_requires_human_review", rq_sha, catalog_sha)
        scenario = catalog[req["scenario_id"]]
        if req["choice"] != scenario["safe_choice"]:
            return result("REJECT", "unsafe_or_incorrect_practice_choice", rq_sha, catalog_sha)
        return result(scenario["assessment"], "synthetic_choice_checked_no_real_approval", rq_sha, catalog_sha)
    except DrillRejected as e:
        return result("REJECT", str(e), rq_sha, catalog_sha)

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--request", required=True, help="public-safe synthetic JSON only")
    ap.add_argument("--catalog", default="drills/FAMILY_SECURITY_OODA_SCENARIOS_V0_1.json")
    ap.add_argument("--receipt", help="new local deterministic receipt, never overwrite")
    opts = ap.parse_args(argv)
    try:
        request_raw = Path(opts.request).read_bytes()
    except OSError:
        request_raw = b""
    try:
        catalog_raw = Path(opts.catalog).read_bytes()
    except OSError:
        catalog_raw = b""
    receipt = run(request_raw, catalog_raw)
    print("SIMULATION_VERDICT=" + receipt["simulation_verdict"])
    print("EFFECTIVE_DECISION=" + receipt["effective_decision"])
    print("AUTHORITY=false; FAMILY_APPROVAL=NOT_ASSERTED; EXTERNAL_ACTIONS=false")
    print("RECEIPT_SHA256=" + receipt["receipt_sha256"])
    if opts.receipt:
        try:
            with Path(opts.receipt).open("xb") as f:
                f.write(canonical(receipt) + b"\n")
        except OSError:
            print("RECEIPT_WRITE_REJECTED", file=sys.stderr)
            return 2
    return {"REJECT": 2, "CONFLICT": 3, "HOLD": 0, "PASS": 2}[receipt["effective_decision"]]

if __name__ == "__main__":
    raise SystemExit(main())
