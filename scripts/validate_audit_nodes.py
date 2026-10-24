#!/usr/bin/env python3
"""Validate ReplayOS Audit Node examples and referenced artifact hashes."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/replayos/audit_node_core_v0_1.schema.json"
EXAMPLES_DIR = ROOT / "reference/audit_nodes"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path}: {exc}")


def validate_artifact_hash(node: dict, example_path: Path) -> None:
    fp = node["artifact_fingerprint"]
    location = fp["storage_location"]
    artifact_path = (ROOT / location).resolve()
    try:
        artifact_path.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"{example_path}: artifact path escapes repository root")
    if not artifact_path.is_file():
        fail(f"{example_path}: missing artifact {location}")
    actual = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
    if actual != fp["hash_value"]:
        fail(
            f"{example_path}: artifact hash mismatch; "
            f"expected {fp['hash_value']}, got {actual}"
        )


def validate_semantics(node: dict, example_path: Path) -> None:
    data_type = node["content"]["data_type"]
    allowed = node["consent_snapshot"]["scope"]["data_types"]
    if data_type not in allowed:
        fail(f"{example_path}: content data_type is outside frozen consent scope")
    if node["observed_at"] > node["recorded_at"]:
        fail(f"{example_path}: recorded_at precedes observed_at")
    permitted = set(node["consent_snapshot"]["scope"]["permitted_uses"])
    prohibited = set(node["consent_snapshot"]["scope"]["prohibited_uses"])
    overlap = permitted & prohibited
    if overlap:
        fail(f"{example_path}: permitted/prohibited use overlap: {sorted(overlap)}")


def main() -> None:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    examples = sorted(EXAMPLES_DIR.glob("*.json"))
    if not examples:
        fail("no audit node examples found")

    for example_path in examples:
        node = load_json(example_path)
        errors = sorted(validator.iter_errors(node), key=lambda err: list(err.path))
        if errors:
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "$"
                print(f"FAIL: {example_path}:{location}: {error.message}", file=sys.stderr)
            raise SystemExit(1)
        validate_semantics(node, example_path)
        validate_artifact_hash(node, example_path)
        print(f"PASS: {example_path.relative_to(ROOT)}")

    print(f"VALIDATION_PASS: {len(examples)} audit node example(s)")


if __name__ == "__main__":
    main()
