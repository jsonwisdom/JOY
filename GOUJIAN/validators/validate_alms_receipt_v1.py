#!/usr/bin/env python3
"""
validate_alms_receipt_v1.py

Core validator for ALMS_RECEIPT_SCHEMA_V1 custody receipts.
CAV means CSV Audit Verification: the CSV / Microsoft Excel-style row witness engine.
This intentionally enforces the No Fake Green teeth without claiming full JSON Schema coverage.

Usage:
  python3 GOUJIAN/validators/validate_alms_receipt_v1.py path/to/receipt.json
"""

import hashlib
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
    "csv_engine",
    "claim",
    "state",
    "requires_human_approval",
    "witness_chain",
    "integrity",
    "surface_rules",
    "no_fake_green",
]

REQUIRED_CSV = [
    "enabled",
    "engine_name",
    "source_type",
    "workbook_name",
    "sheet_name",
    "row_number",
    "source_csv_sha256",
    "row_sha256",
    "canonical_row",
    "formula_policy",
]


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def main(path):
    p = Path(path)
    data = json.loads(p.read_text())

    for key in REQUIRED_TOP:
        if key not in data:
            return fail(f"missing required field: {key}")

    if data["schema_name"] != "ALMS_RECEIPT_SCHEMA_V1":
        return fail("schema_name mismatch")

    if data.get("schema_version") not in {"1.1.0", "1.0.0"}:
        return fail("unsupported schema_version")

    anchor = data["identity_anchor"]
    if anchor.get("immutable_seal") != "jaywisdom.eth":
        return fail("immutable_seal must be jaywisdom.eth")
    if anchor.get("mutable_engine") != "jaywisdom.base.eth":
        return fail("mutable_engine must be jaywisdom.base.eth")
    if anchor.get("l1_anchor_executed") is True and not TX.match(anchor.get("l1_anchor_tx_hash", "")):
        return fail("l1_anchor_executed true requires valid l1_anchor_tx_hash")

    csv_engine = data["csv_engine"]
    for key in REQUIRED_CSV:
        if key not in csv_engine:
            return fail(f"missing csv_engine field: {key}")

    if csv_engine.get("enabled") is not True:
        return fail("csv_engine.enabled must be true")
    if csv_engine.get("engine_name") != "CAV_CSV_AUDIT_VERIFICATION":
        return fail("csv_engine.engine_name must be CAV_CSV_AUDIT_VERIFICATION")
    if not HEX64.match(csv_engine.get("source_csv_sha256", "")):
        return fail("invalid csv_engine.source_csv_sha256")
    if not HEX64.match(csv_engine.get("row_sha256", "")):
        return fail("invalid csv_engine.row_sha256")
    if int(csv_engine.get("row_number", 0)) < 1:
        return fail("csv_engine.row_number must be >= 1")
    if csv_engine.get("formula_policy") not in {
        "FORMULA_POLICY_VALUES_ONLY",
        "FORMULA_POLICY_REJECT_FORMULAS",
        "FORMULA_POLICY_REQUIRE_SIGNED_EXPORT",
    }:
        return fail("invalid csv_engine.formula_policy")

    computed_row_hash = sha256_text(csv_engine.get("canonical_row", ""))
    if computed_row_hash.lower() != csv_engine.get("row_sha256", "").lower():
        return fail("csv_engine.row_sha256 does not match sha256(canonical_row)")

    state = data["state"]
    pipeline = data["pipeline"]
    nfg = data["no_fake_green"]
    surface = data["surface_rules"]

    if surface.get("surface_may_read_mcp") is not False:
        return fail("surface_may_read_mcp must be false for green")
    if surface.get("surface_may_read_csv_for_green") is not False:
        return fail("surface_may_read_csv_for_green must be false")
    if surface.get("surface_may_read_alms") is not True:
        return fail("surface_may_read_alms must be true")
    if surface.get("green_requires_alms") is not True:
        return fail("green_requires_alms must be true")

    witnesses = data["witness_chain"]
    if len(witnesses) < 4:
        return fail("witness_chain must contain at least 4 witnesses for CAV CSV green")

    witness_names = {w.get("witness_name") for w in witnesses}
    required_witnesses = {
        "mrs_wisdom_gate",
        "csv_shape_witness",
        "row_sha_witness",
        "receipt_link_witness",
    }
    missing = sorted(required_witnesses - witness_names)
    if missing:
        return fail(f"missing required CAV CSV witnesses: {missing}")

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

    print("PASS: ALMS_RECEIPT_SCHEMA_V1 CAV CSV custody rules satisfied")
    print(f"receipt_id={data['receipt_id']}")
    print(f"claim_state={state.get('claim_state')}")
    print(f"render_green={state.get('render_green')}")
    print(f"csv_engine={csv_engine.get('engine_name')}")
    print(f"row_number={csv_engine.get('row_number')}")
    print("NO_FAKE_GREEN=ACTIVE")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.strip())
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
