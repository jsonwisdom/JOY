#!/usr/bin/env python3
"""
JOYSPACE schema validation runner v0.3

Validates JOYSPACE JSON artifacts against local schemas.
Prints explicit counts so sample-scale and production-scale receipts can be distinguished.
Authority remains false.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    print("FAIL: missing dependency: jsonschema")
    print("Install with: python -m pip install jsonschema")
    raise SystemExit(2) from exc

ROOT = Path(__file__).resolve().parents[1]

FAMILIES_REQUIRED = 5
INSTANCES_PER_FAMILY_REQUIRED = 10
PROOFS_REQUIRED = 50
WITNESSES_REQUIRED = 50
AWARDS_REQUIRED = 50

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

KNOWN_FAMILIES = {"seed_planter", "future_protector", "growth_guardian", "joy_bringer", "kindness_keeper"}


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

    if not witness_ids:
        print("FAIL cross-reference: no witness records found")
        ok = False

    if ok:
        print("PASS proof/witness/award cross-reference")
    return ok


def family_from_record(record: dict) -> str | None:
    badge_id = record.get("badge_id")
    if badge_id in KNOWN_FAMILIES:
        return badge_id

    for key in ("proof_id", "witness_id", "award_id"):
        value = record.get(key)
        if not isinstance(value, str):
            continue
        for family in KNOWN_FAMILIES:
            if value.startswith(f"{family}_"):
                return family
    return None


def instance_key_from_id(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = re.sub(r"_witness$|_award$", "", value)
    return cleaned


def count_instances_by_family(proofs: list[dict], witnesses: list[dict], awards: list[dict]) -> dict[str, set[str]]:
    instances: dict[str, set[str]] = defaultdict(set)

    for proof in proofs:
        family = family_from_record(proof)
        key = instance_key_from_id(proof.get("proof_id"))
        if family and key:
            instances[family].add(key)

    for witness in witnesses:
        family = family_from_record(witness)
        key = instance_key_from_id(witness.get("witness_id"))
        if family and key:
            instances[family].add(key)

    for award in awards:
        family = family_from_record(award)
        key = instance_key_from_id(award.get("award_id"))
        if family and key:
            instances[family].add(key)

    return instances


def print_counts(proofs: list[dict], witnesses: list[dict], awards: list[dict]) -> bool:
    instances_by_family = count_instances_by_family(proofs, witnesses, awards)
    instance_counts = [len(instances_by_family.get(family, set())) for family in sorted(KNOWN_FAMILIES)]

    families_count = sum(1 for count in instance_counts if count > 0)
    instances_min = min(instance_counts) if instance_counts else 0
    instances_max = max(instance_counts) if instance_counts else 0
    proofs_count = len(proofs)
    witnesses_count = len(witnesses)
    awards_count = len(awards)
    total_json_artifacts = len(ARTIFACTS) + proofs_count + witnesses_count + awards_count

    production_scale_proved = (
        families_count >= FAMILIES_REQUIRED
        and instances_min >= INSTANCES_PER_FAMILY_REQUIRED
        and proofs_count >= PROOFS_REQUIRED
        and witnesses_count >= WITNESSES_REQUIRED
        and awards_count >= AWARDS_REQUIRED
    )

    print(f"families_count: {families_count}")
    print(f"instances_per_family_min: {instances_min}")
    print(f"instances_per_family_max: {instances_max}")
    print(f"proofs_count: {proofs_count}")
    print(f"witnesses_count: {witnesses_count}")
    print(f"awards_count: {awards_count}")
    print(f"total_json_artifacts: {total_json_artifacts}")
    print(
        "production_scale_threshold: "
        f"families>={FAMILIES_REQUIRED}; "
        f"instances_per_family>={INSTANCES_PER_FAMILY_REQUIRED}; "
        f"proofs>={PROOFS_REQUIRED}; "
        f"witnesses>={WITNESSES_REQUIRED}; "
        f"awards>={AWARDS_REQUIRED}"
    )
    print(f"production_scale_result: {'PROVED' if production_scale_proved else 'UNPROVED'}")
    return production_scale_proved


def main() -> int:
    print("JOYSPACE_SCHEMA_AUDIT_V0_3")
    print("authority:false")

    ok = check_required_files()
    ok = validate_json("badge_manifest", SCHEMA_FILES["badge_manifest"], ARTIFACTS["badge_manifest"]) and ok

    proofs_ok, proofs = validate_folder("proofs", "proof")
    witnesses_ok, witnesses = validate_folder("witnesses", "witness")
    awards_ok, awards = validate_folder("awards", "award_record")
    ok = proofs_ok and witnesses_ok and awards_ok and ok
    ok = check_cross_reference(proofs, witnesses, awards) and ok

    production_scale_proved = print_counts(proofs, witnesses, awards)

    if ok and production_scale_proved:
        print("RESULT: PASS_PRODUCTION_SCALE")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("proof_execution: PROVED_FOR_BATCH_INSTANCES")
        print("witness_execution: PROVED_FOR_BATCH_INSTANCES")
        print("award_execution: PROVED_FOR_BATCH_INSTANCES")
        print("feeds: NOT_CLAIMED")
        return 0

    if ok:
        print("RESULT: PASS_SAMPLE_SCALE")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("proof_execution: PROVED_FOR_EXISTING_INSTANCES")
        print("witness_execution: PROVED_FOR_EXISTING_INSTANCES")
        print("award_execution: PROVED_FOR_EXISTING_INSTANCES")
        print("feeds: NOT_CLAIMED")
        return 0

    print("RESULT: FAIL")
    print("schema_layer: PARTIAL")
    print("feeds: NOT_CLAIMED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
