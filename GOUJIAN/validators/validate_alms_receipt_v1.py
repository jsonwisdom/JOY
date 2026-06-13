#!/usr/bin/env python3
"""
validate_alms_receipt_v1.py

Core validator for ALMS_RECEIPT_SCHEMA_V1 custody receipts.
This intentionally enforces the No Fake Green teeth without claiming full JSON Schema coverage.

Usage:
  python3 GOUJIAN/validators/validate_alms_receipt_v1.py path/to/receipt.json
"""

import json
import re
import sys
from pathlib import Path

HEX64 = re.compile(r"^[a-fA-F0-9]{64}$")
TX = re.compile(r"^0x[a-fA-F0-9]{64}$")

REQUIRED_TOP = [
    "schema_name",
    "schema_version",
    "receipt_id",
    "claim_id",
    "pipeline",
    "identity_anchor",
    "claim",
    "state",
    "requires_human_approval",
    "witness_chain",
    "integrity",
    "surface_rules",
    "no_fake_green",
]


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main(path):
    p = Path(path)
    data = json.loads(p.read_text())

    for key in REQUIRED_TOP:
        if key not in data:
            return fail(f"missing required field: {key}")

    if data["schema_name"] != "ALMS_RECEIPT_SCHEMA_V1":
        return fail("schema_name mismatch")

    anchor = data["identity_anchor"]
    if anchor.get("immutable_seal") != "jaywisdom.eth":
        return fail("immutable_seal must be jaywisdom.eth")
    if anchor.get("mutable_engine") != "jaywisdom.base.eth":
        return fail("mutable_engine must be jaywisdom.base.eth")
    if anchor.get("l1_anchor_executed") is True and not TX.match(anchor.get("l1_anchor_tx_hash", "")):
        return fail("l1_anchor_executed true requires valid l1_anchor_tx_hash")

    state = data["state"]
    pipeline = data["pipeline"]
    nfg = data["no_fake_green"]
    surface = data["surface_rules"]

    if surface.get("surface_may_read_mcp") is not False:
        return fail("surface_may_read_mcp must be false for green")
    if surface.get("surface_may_read_alms") is not True:
        return fail("surface_may_read_alms must be true")
    if surface.get("green_requires_alms") is not True:
        return fail("green_requires_alms must be true")

    witnesses = data["witness_chain"]
    if len(witnesses) < 3:
        return fail("witness_chain must contain at least 3 witnesses")

    witness_names = {w.get("witness_name") for w in witnesses}
    required_witnesses = {"mrs_wisdom_gate", "jq_doctrine", "sha_witness"}
    missing = sorted(required_witnesses - witness_names)
    if missing:
        return fail(f"missing required witnesses: {missing}")

    if data.get("requires_human_approval") is True:
        approval = data.get("human_approval") or {}
        if approval.get("approved") is not True:
            return fail("human approval required but not approved")
        if not approval.get("approved_at"):
            return fail("human approval required but approved_at missing")
        if not approval.get("signature"):
            return fail("human approval required but signature missing")

    integrity = data["integrity"]
    if not HEX64.match(integrity.get("source_sha256", "")):
        return fail("invalid source_sha256")
    if not HEX64.match(integrity.get("receipt_sha256", "")):
        return fail("invalid receipt_sha256")

    render_green = state.get("render_green") is True
    if render_green:
        if state.get("truth_state") != "GREEN":
            return fail("render_green true requires truth_state GREEN")
        if state.get("claim_state") != "VERIFIED":
            return fail("render_green true requires claim_state VERIFIED")
        if pipeline.get("mcp_ingested") is not True or pipeline.get("cav_checked") is not True or pipeline.get("alms_archived") is not True:
            return fail("render_green true requires MCP+CAV+ALMS all true")
        if nfg.get("active") is not True or nfg.get("status") != "PASS":
            return fail("render_green true requires NO_FAKE_GREEN PASS")
        failed = [w for w in witnesses if w.get("status") != "PASS"]
        if failed:
            return fail("render_green true requires all witnesses PASS")

    print("PASS: ALMS_RECEIPT_SCHEMA_V1 core custody rules satisfied")
    print(f"receipt_id={data['receipt_id']}")
    print(f"claim_state={state.get('claim_state')}")
    print(f"render_green={state.get('render_green')}")
    print("NO_FAKE_GREEN=ACTIVE")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.strip())
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
