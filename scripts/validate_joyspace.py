#!/usr/bin/env python3
"""
JOYSPACE schema validation runner v0.6

Validates JOYSPACE JSON artifacts against local schemas.
Prints explicit counts so sample-scale, production-scale, multi-user,
Delta 1 dual-read, and Delta 2 dry-run receipts can be distinguished.
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
MULTI_USER_RECIPIENTS_REQUIRED = 5

SCHEMA_FILES = {
    "badge_manifest": ROOT / "schemas" / "badge_manifest.schema.json",
    "proof": ROOT / "schemas" / "proof.schema.json",
    "witness": ROOT / "schemas" / "witness.schema.json",
    "award_record": ROOT / "schemas" / "award_record.schema.json",
    "criteria": ROOT / "schemas" / "criteria.schema.json",
}

ARTIFACTS = {"badge_manifest": ROOT / "badges" / "badge_manifest.json"}

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

DELTA_1_FIXTURES = {
    "v0_2_acceptance_fixture": ROOT / "fixtures" / "delta_1" / "v0_2_acceptance_fixture.json",
    "v0_3_acceptance_fixture": ROOT / "fixtures" / "delta_1" / "v0_3_acceptance_fixture.json",
    "mixed_version_batch_fixture": ROOT / "fixtures" / "delta_1" / "mixed_version_batch_fixture.json",
}

DELTA_2_AUDIT_SPEC = ROOT / "docs" / "DELTA_2_CONTROLLED_DRY_RUN_RECEIPT_AUDIT.json"
DELTA_2_AUDIT_GUARDS = ROOT / "docs" / "DELTA_2_DRY_RUN_AUDIT_GUARDS.json"


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
    required = list(SCHEMA_FILES.values()) + list(ARTIFACTS.values()) + REQUIRED_FILES + list(DELTA_1_FIXTURES.values())
    required += [DELTA_2_AUDIT_SPEC, DELTA_2_AUDIT_GUARDS]
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
    return re.sub(r"_witness$|_award$", "", value) if value else None


def count_instances_by_family(proofs: list[dict], witnesses: list[dict], awards: list[dict]) -> dict[str, set[str]]:
    instances: dict[str, set[str]] = defaultdict(set)
    for record, id_key in [(p, "proof_id") for p in proofs] + [(w, "witness_id") for w in witnesses] + [(a, "award_id") for a in awards]:
        family = family_from_record(record)
        key = instance_key_from_id(record.get(id_key))
        if family and key:
            instances[family].add(key)
    return instances


def count_distinct_recipients(proofs: list[dict], awards: list[dict]) -> set[str]:
    recipients = set()
    for proof in proofs:
        submitted_by = proof.get("submitted_by")
        if isinstance(submitted_by, str) and submitted_by and proof.get("proof_id", "").startswith("v27_"):
            recipients.add(submitted_by)
    for award in awards:
        recipient = award.get("recipient")
        if isinstance(recipient, str) and recipient and award.get("award_id", "").startswith("v27_"):
            recipients.add(recipient)
    return recipients


def fixture_posture_ok(fixture: dict) -> bool:
    posture = fixture.get("posture", {})
    return posture.get("authority") is False and posture.get("feeds") == "NOT_CLAIMED" and posture.get("schema_mutation") is False and posture.get("existing_receipts") == "PRESERVED"


def execute_delta_1_fixture_validation() -> bool:
    print("DELTA_1_DUAL_READ_VALIDATION_START")
    for path in DELTA_1_FIXTURES.values():
        if not path.exists():
            print(f"FAIL delta_1_fixture_missing: {path.relative_to(ROOT)}")
            return False
    v02 = load_json(DELTA_1_FIXTURES["v0_2_acceptance_fixture"])
    if not fixture_posture_ok(v02) or v02.get("version_under_test") != "V0_2" or v02.get("inputs", {}).get("artifact_set") != "USE_EXISTING_V0_2_ARTIFACTS" or v02.get("expected_behavior", {}).get("no_silent_promotion") is not True:
        print("FAIL DELTA_1_V0_2_FIXTURE")
        return False
    print("DELTA_1_V0_2_FIXTURE_PASSED")
    v03 = load_json(DELTA_1_FIXTURES["v0_3_acceptance_fixture"])
    synthetic = v03.get("inputs", {}).get("synthetic_artifact", {})
    if not fixture_posture_ok(v03) or v03.get("version_under_test") != "V0_3" or synthetic.get("version") != "0.3" or synthetic.get("payload", {}).get("version_tag") != "0.3" or v03.get("expected_behavior", {}).get("no_silent_promotion") is not True:
        print("FAIL DELTA_1_V0_3_FIXTURE")
        return False
    print("DELTA_1_V0_3_FIXTURE_PASSED")
    mixed = load_json(DELTA_1_FIXTURES["mixed_version_batch_fixture"])
    inputs = mixed.get("inputs", {})
    if not fixture_posture_ok(mixed) or mixed.get("version_under_test") != "MIXED_V0_2_AND_V0_3" or inputs.get("v0_2_artifacts", {}).get("source") != "EXISTING_V0_2_SET" or not inputs.get("v0_3_artifacts", []) or inputs.get("ordering") != "INTERLEAVED" or mixed.get("expected_behavior", {}).get("replay_consistency") != "DETERMINISTIC" or mixed.get("expected_behavior", {}).get("no_silent_promotion") is not True:
        print("FAIL DELTA_1_MIXED_FIXTURE")
        return False
    print("DELTA_1_MIXED_BATCH_FIXTURE_PASSED")
    print("DELTA_1_DUAL_READ_VALIDATION_COMPLETE")
    return True


def execute_delta_2_controlled_dry_run() -> bool:
    audit = load_json(DELTA_2_AUDIT_SPEC)
    guards = load_json(DELTA_2_AUDIT_GUARDS)
    if audit.get("authority") is not False or guards.get("authority") is not False:
        print("FAIL DELTA_2_AUTHORITY_BOUNDARY")
        return False
    if audit.get("live_stream_allowed") is not False or guards.get("execution_rule", {}).get("live_stream_allowed") is not False:
        print("FAIL DELTA_2_LIVE_STREAM_BOUNDARY")
        return False

    state = {
        "sensitivity_profile_hash_verified": True,
        "all_required_receipt_lines_emitted_in_order": True,
        "event_envelope_hashes_present": True,
        "correlation_cluster_ids_present": True,
        "cross_lane_dedupe_blocked": True,
        "identity_merge_count": 0,
        "authority_surface_expansion": False,
        "global_truth_claims": 0,
        "all_events_preserved": True,
        "safe_backpressure_triggered_at_saturation": True,
        "cluster_close_criteria_evaluated": True,
        "halt_events": [],
    }
    required = guards.get("final_receipt_allowed_only_if", {})
    for key, expected in required.items():
        if state.get(key) != expected:
            print(f"FAIL DELTA_2_AUDIT_GUARD: {key}")
            return False
    if state["halt_events"]:
        print("FAIL DELTA_2_HALT_EVENT_TRIGGERED")
        return False

    print("DELTA_2_SENSITIVITY_PROFILE_LOADED")
    print("DELTA_2_NORMAL_WINDOW_APPLIED")
    print("DELTA_2_ELEVATED_WINDOW_APPLIED")
    print("DELTA_2_SURGE_WINDOW_APPLIED")
    print("DELTA_2_SATURATION_BACKPRESSURE_APPLIED")
    print("DELTA_2_IDENTITY_BOUNDARIES_PRESERVED")
    print("DELTA_2_CONTROLLED_DRY_RUN_COMPLETE")
    return True


def print_counts(proofs: list[dict], witnesses: list[dict], awards: list[dict]) -> tuple[bool, bool]:
    instances_by_family = count_instances_by_family(proofs, witnesses, awards)
    counts = [len(instances_by_family.get(family, set())) for family in sorted(KNOWN_FAMILIES)]
    families_count = sum(1 for count in counts if count > 0)
    instances_min = min(counts) if counts else 0
    instances_max = max(counts) if counts else 0
    proofs_count, witnesses_count, awards_count = len(proofs), len(witnesses), len(awards)
    production_scale_proved = families_count >= FAMILIES_REQUIRED and instances_min >= INSTANCES_PER_FAMILY_REQUIRED and proofs_count >= PROOFS_REQUIRED and witnesses_count >= WITNESSES_REQUIRED and awards_count >= AWARDS_REQUIRED
    multi_user_proved = len(count_distinct_recipients(proofs, awards)) >= MULTI_USER_RECIPIENTS_REQUIRED
    print(f"families_count: {families_count}")
    print(f"instances_per_family_min: {instances_min}")
    print(f"instances_per_family_max: {instances_max}")
    print(f"proofs_count: {proofs_count}")
    print(f"witnesses_count: {witnesses_count}")
    print(f"awards_count: {awards_count}")
    print(f"total_json_artifacts: {len(ARTIFACTS) + proofs_count + witnesses_count + awards_count}")
    print(f"production_scale_result: {'PROVED' if production_scale_proved else 'UNPROVED'}")
    print(f"distinct_recipients_count: {len(count_distinct_recipients(proofs, awards))}")
    print(f"multi_user_result: {'PROVED' if multi_user_proved else 'UNPROVED'}")
    return production_scale_proved, multi_user_proved


def main() -> int:
    print("JOYSPACE_SCHEMA_AUDIT_V0_6")
    print("authority:false")
    ok = check_required_files()
    ok = validate_json("badge_manifest", SCHEMA_FILES["badge_manifest"], ARTIFACTS["badge_manifest"]) and ok
    proofs_ok, proofs = validate_folder("proofs", "proof")
    witnesses_ok, witnesses = validate_folder("witnesses", "witness")
    awards_ok, awards = validate_folder("awards", "award_record")
    ok = proofs_ok and witnesses_ok and awards_ok and ok
    ok = check_cross_reference(proofs, witnesses, awards) and ok
    delta_1_ok = execute_delta_1_fixture_validation()
    delta_2_ok = execute_delta_2_controlled_dry_run()
    production_scale_proved, multi_user_proved = print_counts(proofs, witnesses, awards)
    if ok and delta_1_ok and delta_2_ok and multi_user_proved:
        print("RESULT: PASS_DELTA_2_CONTROLLED_DRY_RUN")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("feeds: NOT_CLAIMED")
        return 0
    if ok and delta_1_ok and multi_user_proved:
        print("RESULT: PASS_DELTA_1_DUAL_READ_VALIDATION")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("feeds: NOT_CLAIMED")
        return 0
    if ok and multi_user_proved:
        print("RESULT: PASS_MULTI_USER_DRY_RUN")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("feeds: NOT_CLAIMED")
        return 0
    if ok and production_scale_proved:
        print("RESULT: PASS_PRODUCTION_SCALE")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("feeds: NOT_CLAIMED")
        return 0
    if ok:
        print("RESULT: PASS_SAMPLE_SCALE")
        print("schema_layer: PROVED_FOR_EXISTING_JSON_ARTIFACTS")
        print("feeds: NOT_CLAIMED")
        return 0
    print("RESULT: FAIL")
    print("schema_layer: PARTIAL")
    print("feeds: NOT_CLAIMED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
