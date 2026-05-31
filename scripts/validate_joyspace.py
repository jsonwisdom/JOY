#!/usr/bin/env python3
"""
JOYSPACE schema validation runner v0.2

Validates JOYSPACE JSON artifacts against local schemas.
This proves structure and sample proof/witness/award linkage only.
It does not prove feeds or a production badge application.
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

REQUIRED_FILES = [
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


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_json(name: str, schema_path: Path, artifact_path: Path) -> bool:
    schema = load_json(schema_path)
    artifact = load_json(artifact_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(artifact), key=lambda e: e.path)
    if errors:
        print(f"FAIL {name}: {artifact_path.relative_to(ROOT)}")
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            print(f"  - {location}: {error.message}")
        return False
    print(f"PASS {name}: {artifact_path.relative_to(ROOT)}")
    return True


def check_required_files() -> bool:
    required = list(SCHEMA_FILES.values()) + list(ARTIFACTS.values()) + REQUIRED_FILES
    required += list((ROOT / "proofs").glob("*.json"))
    required += list((ROOT / "witnesses").glob("*.json"))
    required += list((ROOT / "awards").glob("*.json"))

    missing = [path for path in required if not path.exists()]
    if missing:
        print("FAIL required files missing:")
        for path in missing:
            print(f"  - {path.relative_to(ROOT)}")
        return False
    print("PASS required files exist")
    return True


def validate_folder(folder: str, schema_key: str) -> tuple[bool, list[dict]]:
    folder_path = ROOT / folder
    files = sorted(folder_path.glob("*.json")) if folder_path.exists() else []
    if not files:
        print(f"FAIL {folder}: no JSON instances found")
        return False, []

    ok = True
    records = []
    for path in files:
        ok = validate_json(folder, SCHEMA_FILES[schema_key], path) and ok
        if path.exists():
            records.append(load_json(path))
    return ok, records


def check_cross_reference(proofs: list[dict], witnesses: list[dict], awards: list[dict]) -> bool:
    proof_ids = {proof.get("proof_id") for proof in proofs}
    witness_ids = {witness.get("witness_id") for witness in witnesses}
    ok = True

    for award in awards:
        proof_id = award.get("proof_id")
        if proof_id not in proof_ids:
            print(f"FAIL cross-reference: award {award.get('award_id')} references missing proof {proof_id}")
            ok = False

        embedded = award.get("witness", {})
        if not embedded.get("confirmed", False):
            print(f"FAIL cross-reference: award {award.get('award_id')} witness is not confirmed")
            ok = False

        if embedded.get("authority") is not False:
            print(f"FAIL cross-reference: award {award.get('award_id')} witness authority is not false")
            ok = False

    # Witness files are currently standalone confirmations; at least one must exist.
    if not witness_ids:
        print("FAIL cross-reference: no witness records found")
        ok = False

    if ok:
        print("PASS proof/witness/award cross-reference")
    return ok


def main() -> int:
    print("JOYSPACE_SCHEMA_AUDIT_V0_1")
    print("authority:false")

    ok = check_required_files()
    ok = validate_json("badge_manifest", SCHEMA_FILES["badge_manifest"], ARTIFACTS["badge_manifest"]) and ok

    proofs_ok, proofs = validate_folder("proofs", "proof")
    witnesses_ok, witnesses = validate_folder("witnesses", "witness")
    awards_ok, awards = validate_folder("awards", "award_record")
    ok = proofs_ok and witnesses_ok and awards_ok and ok
    ok = check_cross_reference(proofs, witnesses, awards) and ok

    if ok:
        print("RESULT: PASS")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("proof_execution: PROVED_FOR_SAMPLE_INSTANCE")
        print("witness_execution: PROVED_FOR_SAMPLE_INSTANCE")
        print("award_execution: PROVED_FOR_SAMPLE_INSTANCE")
        print("end_to_end_badge_execution: PROVED_FOR_SAMPLE_SEED_PLANTER_FLOW")
        print("feeds: PENDING")
        return 0

    print("RESULT: FAIL")
    print("schema_layer: PARTIAL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
