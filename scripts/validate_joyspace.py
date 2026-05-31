#!/usr/bin/env python3
"""
JOYSPACE schema validation runner v0.1

Validates existing JOYSPACE JSON artifacts against local schemas.
This proves schema validation only. It does not prove feeds or end-to-end badge execution.
Authority remains false.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    print("FAIL: missing dependency: jsonschema")
    print("Install with: python -m pip install jsonschema")
    raise SystemExit(2) from exc

ROOT = Path(__file__).resolve().parents[1]

SCHEMA_FILES = {
    "badge_manifest": ROOT / "schemas" / "badge_manifest.schema.json",
    "proof": ROOT / "schemas" / "proof.schema.json",
    "witness": ROOT / "schemas" / "witness.schema.json",
    "award_record": ROOT / "schemas" / "award_record.schema.json",
    "criteria": ROOT / "schemas" / "criteria.schema.json",
}

ARTIFACTS = {
    "badge_manifest": ROOT / "badges" / "badge_manifest.json",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_json(name: str, schema_path: Path, artifact_path: Path) -> bool:
    schema = load_json(schema_path)
    artifact = load_json(artifact_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(artifact), key=lambda e: e.path)
    if errors:
        print(f"FAIL {name}: {artifact_path}")
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            print(f"  - {location}: {error.message}")
        return False
    print(f"PASS {name}: {artifact_path}")
    return True


def check_required_files() -> bool:
    required = list(SCHEMA_FILES.values()) + list(ARTIFACTS.values())
    required += [
        ROOT / "badges" / "criteria" / "criteria_index_v0_1.md",
        ROOT / "badges" / "criteria" / "seed_planter_v0_1.md",
        ROOT / "badges" / "criteria" / "future_protector_v0_1.md",
        ROOT / "badges" / "criteria" / "growth_guardian_v0_1.md",
        ROOT / "badges" / "criteria" / "joy_bringer_v0_1.md",
        ROOT / "badges" / "criteria" / "kindness_keeper_v0_1.md",
        ROOT / "badges" / "images" / "seed_planter.svg",
        ROOT / "badges" / "images" / "future_protector.svg",
        ROOT / "badges" / "images" / "growth_guardian.svg",
        ROOT / "badges" / "images" / "joy_bringer.svg",
        ROOT / "badges" / "images" / "kindness_keeper.svg",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        print("FAIL required files missing:")
        for path in missing:
            print(f"  - {path.relative_to(ROOT)}")
        return False
    print("PASS required files exist")
    return True


def main() -> int:
    print("JOYSPACE_SCHEMA_AUDIT_V0_1")
    print("authority:false")

    ok = check_required_files()
    ok = validate_json("badge_manifest", SCHEMA_FILES["badge_manifest"], ARTIFACTS["badge_manifest"]) and ok

    if ok:
        print("RESULT: PASS")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("end_to_end_badge_execution: PENDING")
        return 0

    print("RESULT: FAIL")
    print("schema_layer: PARTIAL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
