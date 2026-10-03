#!/usr/bin/env python3
"""Standard-library validator for Living Ledger JOIN_RECEIPT_V0_1."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_STATUS = {"JOINED", "HOLD", "NO_JOIN", "CONFLICT", "SCOPE_MISMATCH"}
ALLOWED_COMPARISON = {"EQUAL", "COMPATIBLE"}


def fail(message: str) -> None:
    raise ValueError(message)


def require_keys(obj: dict, keys: set[str], where: str) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        fail(f"{where}: missing required keys: {', '.join(missing)}")


def parse_datetime(value: object, where: str) -> None:
    if not isinstance(value, str):
        fail(f"{where}: must be an RFC3339 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        datetime.fromisoformat(normalized)
    except ValueError as exc:
        fail(f"{where}: invalid date-time: {value}") from exc


def validate_receipt(data: object) -> None:
    if not isinstance(data, dict):
        fail("root: expected object")

    required = {
        "join_receipt_id", "version", "valid_time", "transaction_time", "status",
        "source_receipts", "matching_join_fields", "independent_provenance",
        "compatible_provenance", "scope_conflict", "reason", "authority",
    }
    require_keys(data, required, "root")
    extras = sorted(set(data) - required)
    if extras:
        fail("root: unexpected keys: " + ", ".join(extras))

    if not isinstance(data["join_receipt_id"], str) or not data["join_receipt_id"]:
        fail("join_receipt_id: must be a non-empty string")
    if data["version"] != "0.1":
        fail("version: must equal 0.1")
    parse_datetime(data["valid_time"], "valid_time")
    parse_datetime(data["transaction_time"], "transaction_time")

    status = data["status"]
    if status not in ALLOWED_STATUS:
        fail(f"status: unsupported value: {status}")
    if data["authority"] is not False:
        fail("authority: must be false")

    for key in ("independent_provenance", "compatible_provenance", "scope_conflict"):
        if not isinstance(data[key], bool):
            fail(f"{key}: must be boolean")

    if not isinstance(data["reason"], str) or not data["reason"]:
        fail("reason: must be a non-empty string")

    receipts = data["source_receipts"]
    if not isinstance(receipts, list) or not receipts:
        fail("source_receipts: must contain at least one receipt")

    receipt_ids: set[str] = set()
    roots: list[str] = []
    for i, receipt in enumerate(receipts):
        where = f"source_receipts[{i}]"
        if not isinstance(receipt, dict):
            fail(f"{where}: expected object")
        receipt_required = {"receipt_id", "source_uri", "content_sha256", "provenance_root"}
        require_keys(receipt, receipt_required, where)
        extras = sorted(set(receipt) - receipt_required)
        if extras:
            fail(f"{where}: unexpected keys: {', '.join(extras)}")

        rid = receipt["receipt_id"]
        if not isinstance(rid, str) or not rid:
            fail(f"{where}.receipt_id: must be a non-empty string")
        if rid in receipt_ids:
            fail(f"{where}.receipt_id: duplicate receipt_id: {rid}")
        receipt_ids.add(rid)

        if not isinstance(receipt["source_uri"], str) or not receipt["source_uri"]:
            fail(f"{where}.source_uri: must be a non-empty string")
        if not isinstance(receipt["content_sha256"], str) or not SHA256_RE.fullmatch(receipt["content_sha256"]):
            fail(f"{where}.content_sha256: must be lowercase 64-hex SHA-256")
        root = receipt["provenance_root"]
        if not isinstance(root, str) or not root:
            fail(f"{where}.provenance_root: must be a non-empty string")
        roots.append(root)

    fields = data["matching_join_fields"]
    if not isinstance(fields, list):
        fail("matching_join_fields: must be an array")
    for i, field in enumerate(fields):
        where = f"matching_join_fields[{i}]"
        if not isinstance(field, dict):
            fail(f"{where}: expected object")
        field_required = {"field", "left", "right", "comparison"}
        require_keys(field, field_required, where)
        extras = sorted(set(field) - field_required)
        if extras:
            fail(f"{where}: unexpected keys: {', '.join(extras)}")
        if not isinstance(field["field"], str) or not field["field"]:
            fail(f"{where}.field: must be a non-empty string")
        if field["comparison"] not in ALLOWED_COMPARISON:
            fail(f"{where}.comparison: unsupported value")

    if status == "JOINED":
        if len(receipts) < 2:
            fail("JOINED: requires at least two source receipts")
        if len(set(roots)) < 2:
            fail("JOINED: requires at least two independent provenance roots")
        if data["independent_provenance"] is not True:
            fail("JOINED: independent_provenance must be true")
        if not fields:
            fail("JOINED: requires at least one matching join field")
        if data["compatible_provenance"] is not True:
            fail("JOINED: compatible_provenance must be true")
        if data["scope_conflict"] is not False:
            fail("JOINED: scope_conflict must be false")

    if status == "SCOPE_MISMATCH" and data["scope_conflict"] is not True:
        fail("SCOPE_MISMATCH: scope_conflict must be true")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            validate_receipt(data)
            print(f"PASS {path}")
        except Exception as exc:
            failed = True
            print(f"FAIL {path}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
