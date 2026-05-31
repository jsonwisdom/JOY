#!/usr/bin/env python3
"""
Generate JoySpace Validation #27 multi-user dry-run artifacts.

Creates one proof/witness/award chain for each of 5 recipients across 5 badge families.
Authority remains false.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CASES = [
    ("joy_user_alpha", "seed_planter", "reflection", "self", "private"),
    ("joy_user_beta", "future_protector", "screenshot", "friend", "family-only"),
    ("joy_user_gamma", "growth_guardian", "drawing", "mentor", "shareable"),
    ("joy_user_delta", "joy_bringer", "commit", "family", "shareable"),
    ("joy_user_epsilon", "kindness_keeper", "journal_entry", "community", "family-only"),
]

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


def timestamp(offset_minutes: int) -> str:
    base = datetime(2026, 5, 31, 22, 0, 0, tzinfo=timezone.utc)
    return (base + timedelta(minutes=offset_minutes)).isoformat().replace("+00:00", "Z")


def main() -> int:
    proofs_count = 0
    witnesses_count = 0
    awards_count = 0
    recipients = set()

    for index, (recipient, family, proof_type, witness_type, privacy) in enumerate(CASES, start=1):
        instance_id = f"v27_{recipient}_{family}_{index:03d}"
        proof_id = instance_id
        witness_id = f"{instance_id}_witness"
        award_id = f"{instance_id}_award"
        recipients.add(recipient)

        proof = {
            "proof_id": proof_id,
            "badge_id": family,
            "type": proof_type,
            "submitted_by": recipient,
            "timestamp": timestamp(index),
            "content": f"Validation #27 multi-user proof for {recipient} in badge family {family}.",
            "privacy": privacy,
            "authority": False,
        }

        witness = {
            "witness_id": witness_id,
            "witness_type": witness_type,
            "confirmed": True,
            "statement": f"Observed Validation #27 proof artifact {proof_id} for {recipient}.",
            "quality_scored": False,
            "ranked": False,
            "graded": False,
            "authority": False,
        }

        award = {
            "artifact": "JOYSPACE_BADGE_AWARD_RECORD_V0_1",
            "award_id": award_id,
            "badge_id": family,
            "recipient": recipient,
            "awarded_at": timestamp(index + 100),
            "proof_id": proof_id,
            "witness": {
                "witness_type": witness_type,
                "confirmed": True,
                "quality_scored": False,
                "ranked": False,
                "authority": False,
            },
            "celebration_note": f"Validation #27 multi-user dry-run award for {recipient} in {family}.",
            "privacy": privacy,
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

    print("JOYSPACE_VALIDATION_27_MULTI_USER_GENERATOR")
    print("authority:false")
    print(f"generated_recipients_count: {len(recipients)}")
    print(f"generated_families_count: {len(CASES)}")
    print(f"generated_proofs_count: {proofs_count}")
    print(f"generated_witnesses_count: {witnesses_count}")
    print(f"generated_awards_count: {awards_count}")
    print("forbidden_fields_found: 0")
    print("authority_violations: 0")
    print("RESULT: GENERATED_MULTI_USER_DRY_RUN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
