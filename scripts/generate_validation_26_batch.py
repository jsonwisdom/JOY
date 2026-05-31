#!/usr/bin/env python3
"""
Generate JoySpace Validation #26 production-scale batch artifacts.

Creates 10 instances for each of 5 badge families across:
- proofs/*.json
- witnesses/*.json
- awards/*.json

Authority remains false.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FAMILIES = [
    "seed_planter",
    "future_protector",
    "growth_guardian",
    "joy_bringer",
    "kindness_keeper",
]

PROOF_TYPES = [
    "reflection",
    "screenshot",
    "drawing",
    "commit",
    "trusted_witness",
    "photo",
    "journal_entry",
]

WITNESS_TYPES = [
    "self",
    "friend",
    "mentor",
    "family",
    "teacher",
    "guide",
    "community",
]

PRIVACY_VALUES = ["private", "family-only", "shareable"]

FORBIDDEN_FIELDS = {"score", "rank", "grade", "quality_score", "status_power"}


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def assert_clean(payload: dict) -> None:
    forbidden_found = FORBIDDEN_FIELDS.intersection(payload.keys())
    if forbidden_found:
        raise ValueError(f"Forbidden fields found: {sorted(forbidden_found)}")
    if payload.get("authority") is not False:
        raise ValueError("authority must be false")


def make_timestamp(offset_minutes: int) -> str:
    base = datetime(2026, 5, 31, 20, 0, 0, tzinfo=timezone.utc)
    return (base + timedelta(minutes=offset_minutes)).isoformat().replace("+00:00", "Z")


def main() -> int:
    proofs_count = 0
    witnesses_count = 0
    awards_count = 0

    for family_index, family in enumerate(FAMILIES):
        for instance in range(1, 11):
            instance_id = f"{family}_{instance:03d}"
            proof_id = instance_id
            witness_id = f"{instance_id}_witness"
            award_id = f"{instance_id}_award"
            offset = family_index * 20 + instance

            proof = {
                "proof_id": proof_id,
                "badge_id": family,
                "type": PROOF_TYPES[(instance - 1) % len(PROOF_TYPES)],
                "submitted_by": "jaywisdom",
                "timestamp": make_timestamp(offset),
                "content": f"Validation #26 proof instance {instance:03d} for {family}: production-scale batch artifact generated for schema validation.",
                "privacy": PRIVACY_VALUES[(instance - 1) % len(PRIVACY_VALUES)],
                "authority": False,
            }

            witness_type = WITNESS_TYPES[(instance - 1) % len(WITNESS_TYPES)]
            witness = {
                "witness_id": witness_id,
                "witness_type": witness_type,
                "confirmed": True,
                "statement": f"Observed Validation #26 proof artifact {proof_id} for {family}.",
                "quality_scored": False,
                "ranked": False,
                "graded": False,
                "authority": False,
            }

            award = {
                "artifact": "JOYSPACE_BADGE_AWARD_RECORD_V0_1",
                "award_id": award_id,
                "badge_id": family,
                "recipient": "jaywisdom",
                "awarded_at": make_timestamp(offset + 1000),
                "proof_id": proof_id,
                "witness": {
                    "witness_type": witness_type,
                    "confirmed": True,
                    "quality_scored": False,
                    "ranked": False,
                    "authority": False,
                },
                "celebration_note": f"Validation #26 {family} batch instance {instance:03d} recorded.",
                "privacy": "shareable",
                "authority": False,
            }

            for payload in (proof, witness, award):
                assert_clean(payload)

            write_json(ROOT / "proofs" / f"{proof_id}.json", proof)
            write_json(ROOT / "witnesses" / f"{witness_id}.json", witness)
            write_json(ROOT / "awards" / f"{award_id}.json", award)

            proofs_count += 1
            witnesses_count += 1
            awards_count += 1

    print("JOYSPACE_VALIDATION_26_BATCH_GENERATOR")
    print("authority:false")
    print(f"generated_families_count: {len(FAMILIES)}")
    print("generated_instances_per_family: 10")
    print(f"generated_proofs_count: {proofs_count}")
    print(f"generated_witnesses_count: {witnesses_count}")
    print(f"generated_awards_count: {awards_count}")
    print("forbidden_fields_found: 0")
    print("authority_violations: 0")
    print("RESULT: GENERATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
