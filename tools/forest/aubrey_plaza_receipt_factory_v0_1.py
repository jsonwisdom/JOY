#!/usr/bin/env python3
"""Aubrey Plaza Forest receipt factory v0.1.

Purpose:
- Keep the canonical JoySpace epistemic receipt schema unchanged.
- Add Forest routing metadata in a sidecar ForestLeafEnvelope.
- Generate a deterministic LEAF -> TREE -> FOREST snapshot.
- Preserve genuine conflicts and avoid false conflicts caused by target collapse.

This fixture uses only public sources plus one explicitly synthetic creative replay.
It creates no authority and makes no private-data claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = (
    "PRIVATE_OR_APPROVED",
    "PUBLIC_LOCAL",
    "BOUNDARY_RECEIPT",
    "CREATIVE",
    "PUBLIC_SOURCE",
)

ROOT_BY_CLASS = {
    "PRIVATE_OR_APPROVED": "family",
    "PUBLIC_LOCAL": "alabama",
    "BOUNDARY_RECEIPT": "apple_blossom",
    "CREATIVE": "leah_prime",
    "PUBLIC_SOURCE": "public_research",
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sha256_hex(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def merkle_root(hex_leaves: list[str]) -> str | None:
    """Bitcoin-style pair duplication for odd levels, SHA-256 over raw hash bytes."""
    if not hex_leaves:
        return None
    level = [bytes.fromhex(x) for x in hex_leaves]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [
            hashlib.sha256(level[i] + level[i + 1]).digest()
            for i in range(0, len(level), 2)
        ]
    return level[0].hex()


def candidate_class(seed: dict[str, Any]) -> str:
    scope = seed["access_scope"]
    kind = seed["source_kind"]

    if scope == "USER_AUTHORIZED_PRIVATE":
        return "PRIVATE_OR_APPROVED"
    if kind == "CREATIVE_REPLAY":
        return "CREATIVE"
    if kind == "BOUNDARY_OBSERVATION":
        return "BOUNDARY_RECEIPT"
    if kind == "PUBLIC_LOCAL_SOURCE":
        return "PUBLIC_LOCAL"
    if scope == "PUBLIC":
        return "PUBLIC_SOURCE"
    raise ValueError(f"unclassifiable seed: {seed['seed_id']}")


def make_epistemic_receipt(seed: dict[str, Any]) -> dict[str, Any]:
    rid = f"er_{sha256_hex(seed)[:16]}"
    classification = candidate_class(seed)
    detail = (
        f"{seed['target_id']} observed as {seed['claim']['value']!r}; "
        f"scope={seed['access_scope']}; source_kind={seed['source_kind']}"
    )
    return {
        "schema_version": "0.1.0",
        "receipt_type": "epistemic_receipt_v0_1",
        "receipt_id": rid,
        "timestamp": seed["retrieved_at"],
        "identity_label": None,
        "quest_family": None,
        "moves": [
            {"code": "M1", "name": "DISCOVER", "detail": seed["source_locator"], "timestamp": seed["retrieved_at"]},
            {"code": "M2", "name": "CLASSIFY", "detail": classification, "timestamp": seed["retrieved_at"]},
            {"code": "M4", "name": "BIND", "detail": detail, "timestamp": seed["retrieved_at"]},
            {"code": "M8", "name": "RECEIPT", "detail": "Forest leaf sidecar may reference this receipt.", "timestamp": seed["retrieved_at"]},
        ],
        "sources": [
            {
                "pointer": seed["source_locator"],
                "access_note": f"{seed['access_scope']} / {seed['source_kind']}",
                "retrieved_at": seed["retrieved_at"],
            }
        ],
        "classifications": [
            {
                "label": classification,
                "scope": seed["target_id"],
                "consent": None,
            }
        ],
        "genesis_status": "NOT_TESTED",
        "dissent_notes": list(seed.get("dissent_notes", [])),
        "result_state": "HOLD" if seed.get("hold", False) else "PASS",
        "replay_instructions": "Re-fetch source pointer, compare the exact target_id and claim semantics, then recompute canonical receipt bytes.",
        "authority": False,
        "scoring": None,
    }


def make_envelope(seed: dict[str, Any], receipt: dict[str, Any]) -> dict[str, Any]:
    classification = candidate_class(seed)
    envelope_body = {
        "schema_version": "0.1.0",
        "envelope_type": "forest_leaf_envelope_v0_1",
        "receipt_ref": receipt["receipt_id"],
        "subject_id": "PERSON.AUBREY_PLAZA",
        "target_id": seed["target_id"],
        "claim": seed["claim"],
        "source_kind": seed["source_kind"],
        "access_scope": seed["access_scope"],
        "operation": seed["operation"],
        "source_locator": seed["source_locator"],
        "published_at": seed.get("published_at"),
        "retrieved_at": seed["retrieved_at"],
        "candidate_class": classification,
        "root_name": ROOT_BY_CLASS[classification],
        "conflict_group": seed.get("conflict_group"),
        "evidence_weight": seed.get("evidence_weight", 1.0),
        "synthetic": bool(seed.get("synthetic", False)),
        "may_resolve_factual_conflict": not bool(seed.get("synthetic", False)),
        "authority_created": False,
    }
    envelope_id = f"fle_{sha256_hex(envelope_body)[:16]}"
    return {"envelope_id": envelope_id, **envelope_body}


def detect_conflicts(envelopes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for e in envelopes:
        if e["synthetic"] or not e["may_resolve_factual_conflict"]:
            continue
        groups.setdefault(e["target_id"], []).append(e)

    conflicts: list[dict[str, Any]] = []
    for target_id, items in sorted(groups.items()):
        values: dict[str, list[str]] = {}
        for item in items:
            key = json.dumps(item["claim"]["value"], sort_keys=True, ensure_ascii=False)
            values.setdefault(key, []).append(item["envelope_id"])
        if len(values) > 1:
            conflicts.append(
                {
                    "target_id": target_id,
                    "verdict": "CONFLICT",
                    "values": [
                        {"value": json.loads(value), "envelopes": ids}
                        for value, ids in sorted(values.items())
                    ],
                    "resolution": "HOLD",
                    "authority_created": False,
                }
            )
    return conflicts


def build(seed_doc: dict[str, Any]) -> dict[str, Any]:
    receipts = [make_epistemic_receipt(seed) for seed in seed_doc["seeds"]]
    envelopes = [
        make_envelope(seed, receipt)
        for seed, receipt in zip(seed_doc["seeds"], receipts, strict=True)
    ]

    envelope_hashes = {
        e["envelope_id"]: sha256_hex(e)
        for e in envelopes
    }

    roots: dict[str, dict[str, Any]] = {}
    for evidence_class in EVIDENCE_CLASSES:
        root_name = ROOT_BY_CLASS[evidence_class]
        members = [
            e for e in envelopes
            if e["candidate_class"] == evidence_class
        ]
        member_hashes = [envelope_hashes[e["envelope_id"]] for e in members]
        roots[root_name] = {
            "class": evidence_class,
            "leaf_count": len(members),
            "root": merkle_root(member_hashes),
            "leaf_envelopes": [e["envelope_id"] for e in members],
        }

    manifest_body = {
        "system": "AppleBlossomAwesomeLeahPrimeMerkleForest",
        "version": "0.1",
        "replay": "AubreyPlazaChaosAgent",
        "subject_id": "PERSON.AUBREY_PLAZA",
        "roots": roots,
        "cross_tree_inference": False,
        "shared_authority": False,
        "authority_created": False,
    }
    manifest_hash = sha256_hex(manifest_body)

    return {
        "fixture": "aubrey_plaza_public_receipts_v0_1",
        "fixture_semantics": {
            "public_interview_is_private": False,
            "series_start_year_equals_participation_year": False,
            "synthetic_creative_replay_is_factual_evidence": False,
            "cross_tree_inference": False,
            "authority_created": False,
        },
        "epistemic_receipts": receipts,
        "forest_envelopes": envelopes,
        "boxdee": {
            "conflicts": detect_conflicts(envelopes),
            "notes": [
                "Stroke-age receipts share one exact target_id and disagree, so they remain CONFLICT/HOLD.",
                "White Lotus series-start year and Plaza participation year use different target_ids, so no false conflict is created.",
                "Synthetic creative replay is routed to CREATIVE with evidence_weight=0 and cannot resolve factual conflicts.",
            ],
            "authority_created": False,
        },
        "forest_manifest": {
            **manifest_body,
            "forest_manifest_hash": manifest_hash,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    seed_doc = json.loads(args.seed.read_text(encoding="utf-8"))
    result = build(seed_doc)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
