#!/usr/bin/env python3
"""AppleBlossomAwesome Evidence Class Registry + LEAF -> TREE -> FOREST v0.1.

Routing is deterministic and non-authoritative. Exact EvidenceClass labels on the
JoySpace epistemic receipt are required for automatic tree mutation. Legacy
source/operation/output mappings are preserved as HINT-ONLY suggestions.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Any, Iterable

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

LEGACY_SOURCE_MAP = {
    "method": "PRIVATE_OR_APPROVED",
    "operator": "PUBLIC_LOCAL",
    "language": "BOUNDARY_RECEIPT",
    "story": "CREATIVE",
    "source": "PUBLIC_SOURCE",
}

LEGACY_OPERATION_MAP = {
    "SEE": "BOUNDARY_RECEIPT",
    "HEAR": "CREATIVE",
    "APPLE_SAUCE": "PRIVATE_OR_APPROVED",
    "CONFIRM": "PUBLIC_LOCAL",
    "SAY": "PUBLIC_SOURCE",
    "CONTEXT": "CREATIVE",
}

LEGACY_OUTPUT_HINT_MAP = {
    "vernacular": "BOUNDARY_RECEIPT",
    "translation": "BOUNDARY_RECEIPT",
    "confidence": "PUBLIC_LOCAL",
    "score": "PUBLIC_LOCAL",
    "creative": "CREATIVE",
    "narrative": "CREATIVE",
    "source": "PUBLIC_SOURCE",
    "citation": "PUBLIC_SOURCE",
}


@dataclass(frozen=True)
class EvidenceWeight:
    level: int
    label: str


@dataclass(frozen=True)
class EvidenceClassification:
    decision: str
    primary_class: str | None
    routing_confidence: float
    alternative_classes: list[str]
    evidence_weight: EvidenceWeight
    root_candidate: str | None
    reason_codes: list[str]
    cross_tree_inference: bool = False
    authority_created: bool = False


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _hash(domain: str, *parts: bytes) -> bytes:
    h = hashlib.sha256()
    h.update(domain.encode("utf-8"))
    h.update(b"\x00")
    for part in parts:
        h.update(len(part).to_bytes(8, "big"))
        h.update(part)
    return h.digest()


def receipt_leaf_hash(receipt: dict[str, Any]) -> str:
    return _hash("JOY_LEAF_V0_1", canonical_json_bytes(receipt)).hex()


def _merkle_body_root(leaf_hashes: Iterable[str]) -> bytes:
    level = [bytes.fromhex(x) for x in leaf_hashes]
    if not level:
        return _hash("JOY_MERKLE_EMPTY_V0_1")

    while len(level) > 1:
        next_level: list[bytes] = []
        for i in range(0, len(level), 2):
            left = level[i]
            if i + 1 < len(level):
                next_level.append(_hash("JOY_MERKLE_NODE_V0_1", left, level[i + 1]))
            else:
                # Domain-separated unary promotion avoids the duplicate-last
                # ambiguity where [A,B,C] can share a body root with [A,B,C,C].
                next_level.append(_hash("JOY_MERKLE_PROMOTE_V0_1", left))
        level = next_level
    return level[0]


def tree_root(evidence_class: str, leaf_hashes: list[str]) -> str:
    if evidence_class not in EVIDENCE_CLASSES:
        raise ValueError(f"unknown evidence class: {evidence_class}")
    body = _merkle_body_root(leaf_hashes)
    count = len(leaf_hashes).to_bytes(8, "big")
    return _hash("JOY_TREE_ROOT_V0_1", evidence_class.encode("utf-8"), count, body).hex()


def forest_manifest_hash(manifest: dict[str, Any]) -> str:
    body = copy.deepcopy(manifest)
    body.pop("forest_manifest_hash", None)
    return _hash("JOY_FOREST_MANIFEST_V0_1", canonical_json_bytes(body)).hex()


def evidence_weight(receipt: dict[str, Any]) -> EvidenceWeight:
    """Measure receipt completeness, never truth or authority."""
    sources = receipt.get("sources") or []
    move_names = {m.get("name") for m in receipt.get("moves") or [] if isinstance(m, dict)}
    if sources and "BIND" in move_names and "REPLAY" in move_names:
        return EvidenceWeight(2, "REPLAYED")
    if sources and "BIND" in move_names:
        return EvidenceWeight(1, "SOURCE_BOUND")
    return EvidenceWeight(0, "UNBOUND")


def classify(receipt: dict[str, Any]) -> EvidenceClassification:
    """Classify a canonical JoySpace epistemic receipt.

    Automatic mutation requires exactly one explicit EvidenceClass label in the
    receipt's classifications array. This prevents weak heuristics from silently
    moving a receipt across provenance membranes.
    """
    explicit: list[str] = []
    for item in receipt.get("classifications") or []:
        if isinstance(item, dict) and item.get("label") in EVIDENCE_CLASSES:
            label = item["label"]
            if label not in explicit:
                explicit.append(label)

    weight = evidence_weight(receipt)

    if len(explicit) == 1:
        primary = explicit[0]
        return EvidenceClassification(
            decision="ROUTE",
            primary_class=primary,
            routing_confidence=1.0,
            alternative_classes=[],
            evidence_weight=weight,
            root_candidate=ROOT_BY_CLASS[primary],
            reason_codes=["EXPLICIT_EVIDENCE_CLASS"],
        )

    if len(explicit) > 1:
        return EvidenceClassification(
            decision="HOLD",
            primary_class=None,
            routing_confidence=0.0,
            alternative_classes=explicit,
            evidence_weight=weight,
            root_candidate=None,
            reason_codes=["CONFLICTING_EXPLICIT_CLASSES"],
        )

    return EvidenceClassification(
        decision="HOLD",
        primary_class=None,
        routing_confidence=0.0,
        alternative_classes=[],
        evidence_weight=weight,
        root_candidate=None,
        reason_codes=["NO_EXPLICIT_EVIDENCE_CLASS"],
    )


def legacy_hint_suggestion(
    source_type: str,
    operation: str,
    output_keys: Iterable[str],
) -> dict[str, Any]:
    """Preserve the user's source/operation/output mapping as non-mutating hints."""
    votes: dict[str, int] = {}
    reasons: list[str] = []

    base = LEGACY_SOURCE_MAP.get(source_type)
    if base:
        votes[base] = votes.get(base, 0) + 2
        reasons.append(f"SOURCE:{source_type}->{base}:2")

    op = LEGACY_OPERATION_MAP.get(operation)
    if op:
        votes[op] = votes.get(op, 0) + 1
        reasons.append(f"OP:{operation}->{op}:1")

    for key in output_keys:
        hint = LEGACY_OUTPUT_HINT_MAP.get(key)
        if hint:
            votes[hint] = votes.get(hint, 0) + 1
            reasons.append(f"OUTPUT:{key}->{hint}:1")

    if not votes:
        return {
            "decision": "HINT_ONLY",
            "suggested_class": None,
            "routing_confidence": 0.0,
            "alternatives": [],
            "reason_codes": reasons or ["NO_HINTS"],
            "authority_created": False,
        }

    ordered = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))
    top_score = ordered[0][1]
    winners = [c for c, score in ordered if score == top_score]
    total = sum(votes.values())
    return {
        "decision": "HINT_ONLY",
        "suggested_class": winners[0] if len(winners) == 1 else None,
        "routing_confidence": round(top_score / total, 6),
        "alternatives": winners if len(winners) > 1 else [c for c, _ in ordered[1:]],
        "reason_codes": reasons,
        "authority_created": False,
    }


def new_forest_state() -> dict[str, Any]:
    trees = {name: {"class": klass, "leaves": []} for klass, name in ROOT_BY_CLASS.items()}
    roots = {
        name: {
            "class": tree["class"],
            "root": tree_root(tree["class"], []),
            "leaf_count": 0,
        }
        for name, tree in trees.items()
    }
    manifest = {
        "system": "AppleBlossomAwesomeLeahPrimeMerkleForest",
        "version": "0.1.0",
        "replay": "AlabamaJammaSlamma",
        "roots": roots,
        "cross_tree_inference": False,
        "shared_authority": False,
        "authority_created": False,
    }
    manifest["forest_manifest_hash"] = forest_manifest_hash(manifest)
    return {"manifest": manifest, "trees": trees}


def route_receipt(state: dict[str, Any], receipt: dict[str, Any]) -> dict[str, Any]:
    classification = classify(receipt)
    before_manifest_hash = state["manifest"]["forest_manifest_hash"]

    if classification.decision != "ROUTE" or classification.primary_class is None:
        return {
            "status": "HOLD",
            "classification": _classification_dict(classification),
            "leaf_hash": receipt_leaf_hash(receipt),
            "root_mutated": None,
            "forest_manifest_hash_before": before_manifest_hash,
            "forest_manifest_hash_after": before_manifest_hash,
            "authority_created": False,
        }

    root_name = ROOT_BY_CLASS[classification.primary_class]
    tree = state["trees"][root_name]
    leaf = receipt_leaf_hash(receipt)

    if leaf in tree["leaves"]:
        return {
            "status": "NOOP_DUPLICATE",
            "classification": _classification_dict(classification),
            "leaf_hash": leaf,
            "root_mutated": None,
            "forest_manifest_hash_before": before_manifest_hash,
            "forest_manifest_hash_after": before_manifest_hash,
            "authority_created": False,
        }

    before_roots = {name: item["root"] for name, item in state["manifest"]["roots"].items()}
    tree["leaves"].append(leaf)
    root_entry = state["manifest"]["roots"][root_name]
    root_entry["leaf_count"] = len(tree["leaves"])
    root_entry["root"] = tree_root(classification.primary_class, tree["leaves"])
    state["manifest"]["forest_manifest_hash"] = forest_manifest_hash(state["manifest"])

    after_roots = {name: item["root"] for name, item in state["manifest"]["roots"].items()}
    mutated = [name for name in before_roots if before_roots[name] != after_roots[name]]
    if mutated != [root_name]:
        raise AssertionError(f"cross-tree mutation detected: expected {[root_name]}, got {mutated}")

    return {
        "status": "ROUTED",
        "classification": _classification_dict(classification),
        "leaf_hash": leaf,
        "root_mutated": root_name,
        "tree_root_after": root_entry["root"],
        "leaf_count_after": root_entry["leaf_count"],
        "forest_manifest_hash_before": before_manifest_hash,
        "forest_manifest_hash_after": state["manifest"]["forest_manifest_hash"],
        "cross_tree_inference": False,
        "authority_created": False,
    }


def _classification_dict(value: EvidenceClassification) -> dict[str, Any]:
    out = asdict(value)
    out["evidence_weight"] = asdict(value.evidence_weight)
    return out


if __name__ == "__main__":
    demo_receipt = {
        "schema_version": "0.1.0",
        "receipt_type": "epistemic_receipt_v0_1",
        "receipt_id": "er_apple_blossom_demo_001",
        "timestamp": "2026-08-21T04:38:00Z",
        "moves": [
            {"code": "M1", "name": "DISCOVER"},
            {"code": "M2", "name": "CLASSIFY"},
            {"code": "M4", "name": "BIND"},
            {"code": "M7", "name": "REPLAY"},
            {"code": "M8", "name": "RECEIPT"},
        ],
        "sources": [{"pointer": "user://apple-blossom/demo"}],
        "classifications": [{"label": "BOUNDARY_RECEIPT", "scope": "apple_blossom", "consent": "CONSENT_EXPLICIT"}],
        "genesis_status": "NOT_TESTED",
        "dissent_notes": [],
        "result_state": "PASS",
        "authority": False,
    }
    state = new_forest_state()
    result = route_receipt(state, demo_receipt)
    print(json.dumps({"route_receipt": result, "manifest": state["manifest"]}, indent=2, sort_keys=True))
