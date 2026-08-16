#!/usr/bin/env python3
"""Family Daily Audit v1.2.

Validates the Wisdom family graph without inferring relationships.
Standard-library only. The audit may inspect structure and replay synthetic
transition tests; it may not promote facts or create authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {
    "USER_DECLARED",
    "DOCUMENT_SOURCE_BOUND",
    "PERSON_CONFIRMED",
    "CONFLICTED",
    "UNKNOWN",
}
RELATIONSHIP_STATES = {
    "DECLARED",
    "VERIFIED",
    "HOLD_UNSPECIFIED",
    "DISPUTED",
    "REJECTED",
}
ADULT_RELATIONSHIP_PREDICATES = {
    "SPOUSE_OF",
    "PARTNER_OF",
    "CO_PARENT_OF",
    "HOUSEHOLD_WITH",
    "CUSTODY_WITH",
    "LEGAL_PARENTAGE_WITH",
    "INTERPERSONAL_HISTORY_WITH",
}
EXPLICIT_ORIGINS = {
    "USER_DECLARED",
    "DOCUMENT_SOURCE_BOUND",
    "PERSON_CONFIRMED",
}


def canonical_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_graph(graph: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if graph.get("authority_created") is not False:
        errors.append("graph.authority_created must be false")
    if graph.get("silent_inference") is not False:
        errors.append("graph.silent_inference must be false")

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    constraints = graph.get("identity_constraints", [])

    node_ids = [n.get("node_id") for n in nodes]
    if len(node_ids) != len(set(node_ids)):
        errors.append("node_id values must be unique")
    known_nodes = set(node_ids)

    edge_ids = [e.get("edge_id") for e in edges]
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("edge_id values must be unique")

    evidence_ref_owner: dict[str, str] = {}
    parent_subjects_by_child: dict[str, set[str]] = {}

    for constraint in constraints:
        if constraint.get("authority_created") is not False:
            errors.append(f"{constraint.get('constraint_id')}: authority_created must be false")
        if constraint.get("left") not in known_nodes or constraint.get("right") not in known_nodes:
            errors.append(f"{constraint.get('constraint_id')}: identity constraint references unknown node")

    for edge in edges:
        edge_id = edge.get("edge_id", "<missing-edge-id>")
        subject = edge.get("subject")
        obj = edge.get("object")
        predicate = edge.get("predicate")
        origin = edge.get("origin")
        current = edge.get("current") or {}
        evidence_class = current.get("evidence_class")
        relationship_state = current.get("relationship_state")
        events = edge.get("evidence_events")
        evidence_refs = edge.get("evidence_refs")

        if subject not in known_nodes or obj not in known_nodes:
            errors.append(f"{edge_id}: edge references unknown node")
        if edge.get("authority_created") is not False:
            errors.append(f"{edge_id}: authority_created must be false")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(f"{edge_id}: invalid evidence_class {evidence_class!r}")
        if relationship_state not in RELATIONSHIP_STATES:
            errors.append(f"{edge_id}: invalid relationship_state {relationship_state!r}")
        if not isinstance(events, list):
            errors.append(f"{edge_id}: evidence_events must be an array")
            events = []
        if not isinstance(evidence_refs, list):
            errors.append(f"{edge_id}: evidence_refs must be an array")
            evidence_refs = []

        # Evidence references are edge-local claim receipts. A source document may
        # be reused only through separately scoped edge receipts.
        for ref in evidence_refs:
            prior = evidence_ref_owner.get(ref)
            if prior and prior != edge_id:
                errors.append(f"{edge_id}: evidence_ref {ref!r} already belongs to {prior}")
            evidence_ref_owner[ref] = edge_id

        if relationship_state == "HOLD_UNSPECIFIED":
            if predicate is not None:
                errors.append(f"{edge_id}: HOLD_UNSPECIFIED requires predicate=null")
            if evidence_class != "UNKNOWN":
                errors.append(f"{edge_id}: HOLD_UNSPECIFIED requires evidence_class=UNKNOWN")
            if events:
                errors.append(f"{edge_id}: HOLD_UNSPECIFIED must not fabricate evidence_events")
            if origin != "EXPLICIT_HOLD":
                errors.append(f"{edge_id}: HOLD_UNSPECIFIED requires origin=EXPLICIT_HOLD")
        else:
            if not isinstance(predicate, str) or not predicate:
                errors.append(f"{edge_id}: asserted relationship requires a predicate")
            if origin == "EXPLICIT_HOLD":
                errors.append(f"{edge_id}: EXPLICIT_HOLD cannot carry an asserted predicate")
            if not events:
                errors.append(f"{edge_id}: asserted relationship requires edge-local evidence event history")
            else:
                event_numbers = [event.get("event") for event in events]
                if event_numbers != list(range(1, len(events) + 1)):
                    errors.append(f"{edge_id}: evidence event numbers must be append-only 1..N")
                for event in events:
                    if event.get("class") not in EVIDENCE_CLASSES:
                        errors.append(f"{edge_id}: invalid event evidence class {event.get('class')!r}")
                    if event.get("result") not in RELATIONSHIP_STATES:
                        errors.append(f"{edge_id}: invalid event relationship result {event.get('result')!r}")
                last = events[-1]
                if last.get("class") != evidence_class:
                    errors.append(f"{edge_id}: current evidence_class must equal last event class")
                if last.get("result") != relationship_state:
                    errors.append(f"{edge_id}: current relationship_state must equal last event result")

        if predicate == "PARENT_OF" and relationship_state in {"DECLARED", "VERIFIED", "DISPUTED"}:
            parent_subjects_by_child.setdefault(obj, set()).add(subject)

        if predicate in ADULT_RELATIONSHIP_PREDICATES:
            if origin not in EXPLICIT_ORIGINS:
                errors.append(f"{edge_id}: adult relationship cannot be machine-generated or adjacency-derived")
            if not events:
                errors.append(f"{edge_id}: adult relationship requires evidence on that exact edge")

    shared_child_pairs: list[dict[str, Any]] = []
    for child, parents in sorted(parent_subjects_by_child.items()):
        for left, right in combinations(sorted(parents), 2):
            shared_child_pairs.append({"child": child, "subjects": [left, right]})
            # Sharing a child is only an observation. It authorizes no adult edge.
            for edge in edges:
                if {edge.get("subject"), edge.get("object")} == {left, right}:
                    pred = edge.get("predicate")
                    if pred in ADULT_RELATIONSHIP_PREDICATES and edge.get("origin") not in EXPLICIT_ORIGINS:
                        errors.append(
                            f"{edge.get('edge_id')}: shared child {child} cannot synthesize {pred}"
                        )

    # Nodes are allowed to exist with zero relationship edges. Silence is valid.
    touched_nodes = {e.get("subject") for e in edges} | {e.get("object") for e in edges}
    silent_nodes = sorted(n for n in known_nodes if n not in touched_nodes)

    return {
        "pass": not errors,
        "errors": errors,
        "warnings": warnings,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "shared_child_pairs": shared_child_pairs,
        "silent_nodes": silent_nodes,
        "counts": {
            "declared": sum(1 for e in edges if e.get("current", {}).get("relationship_state") == "DECLARED"),
            "verified": sum(1 for e in edges if e.get("current", {}).get("relationship_state") == "VERIFIED"),
            "hold_unspecified": sum(1 for e in edges if e.get("current", {}).get("relationship_state") == "HOLD_UNSPECIFIED"),
            "disputed": sum(1 for e in edges if e.get("current", {}).get("relationship_state") == "DISPUTED"),
            "rejected": sum(1 for e in edges if e.get("current", {}).get("relationship_state") == "REJECTED"),
        },
    }


def edge_map(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {edge["edge_id"]: edge for edge in graph["edges"]}


def validate_local_transition(before: dict[str, Any], after: dict[str, Any], target_edge_id: str) -> tuple[bool, list[str]]:
    errors: list[str] = []

    if before.get("nodes") != after.get("nodes"):
        errors.append("local edge transition may not modify nodes")
    if before.get("identity_constraints") != after.get("identity_constraints"):
        errors.append("local edge transition may not modify identity constraints")

    bmap = edge_map(before)
    amap = edge_map(after)
    if set(bmap) != set(amap):
        errors.append("local edge transition may not create or delete edges")
        return False, errors
    if target_edge_id not in bmap:
        errors.append("target edge does not exist")
        return False, errors

    for edge_id in bmap:
        if edge_id != target_edge_id and bmap[edge_id] != amap[edge_id]:
            errors.append(f"neighbor edge mutated: {edge_id}")

    old = bmap[target_edge_id]
    new = amap[target_edge_id]
    for immutable_key in ("edge_id", "subject", "predicate", "object", "origin"):
        if old.get(immutable_key) != new.get(immutable_key):
            errors.append(f"target edge immutable field changed: {immutable_key}")

    old_events = old.get("evidence_events", [])
    new_events = new.get("evidence_events", [])
    if len(new_events) < len(old_events):
        errors.append("evidence event history was shortened")
    elif new_events[: len(old_events)] != old_events:
        errors.append("evidence event history prefix was rewritten")

    if new.get("authority_created") is not False:
        errors.append("local transition created authority")

    post_audit = audit_graph(after)
    errors.extend(f"post-transition graph: {e}" for e in post_audit["errors"])
    return not errors, errors


def run_adversarial_tests(graph: dict[str, Any]) -> list[dict[str, Any]]:
    tests: list[dict[str, Any]] = []

    # Legal test intentionally targets Gaga -> MaryDee, proving the audit is not Jay-centric.
    legal = copy.deepcopy(graph)
    target = edge_map(legal)["EDGE-006"]
    target["evidence_events"].append(
        {
            "event": 2,
            "class": "PERSON_CONFIRMED",
            "result": "VERIFIED",
            "receipt": "SYNTHETIC_TEST_ONLY_DO_NOT_PROMOTE",
            "timestamp": None,
        }
    )
    target["current"] = {"evidence_class": "PERSON_CONFIRMED", "relationship_state": "VERIFIED"}
    legal_ok, legal_errors = validate_local_transition(graph, legal, "EDGE-006")
    tests.append({"name": "edge_local_promotion_beyond_jay", "expected": "ACCEPT", "actual": "ACCEPT" if legal_ok else "REJECT", "pass": legal_ok, "errors": legal_errors})

    neighbor = copy.deepcopy(legal)
    edge_map(neighbor)["EDGE-007"]["current"] = {"evidence_class": "PERSON_CONFIRMED", "relationship_state": "VERIFIED"}
    neighbor_ok, neighbor_errors = validate_local_transition(graph, neighbor, "EDGE-006")
    tests.append({"name": "neighbor_edge_inheritance", "expected": "REJECT", "actual": "ACCEPT" if neighbor_ok else "REJECT", "pass": not neighbor_ok, "errors": neighbor_errors})

    erased = copy.deepcopy(legal)
    edge_map(erased)["EDGE-006"]["evidence_events"] = edge_map(erased)["EDGE-006"]["evidence_events"][1:]
    erased_ok, erased_errors = validate_local_transition(graph, erased, "EDGE-006")
    tests.append({"name": "history_erasure", "expected": "REJECT", "actual": "ACCEPT" if erased_ok else "REJECT", "pass": not erased_ok, "errors": erased_errors})

    synthesized = copy.deepcopy(graph)
    synthesized["edges"].append(
        {
            "edge_id": "ATTACK-SHARED-CHILD",
            "subject": "DADDY_JAY",
            "predicate": "SPOUSE_OF",
            "object": "MARYDEE",
            "origin": "MACHINE_GENERATED",
            "current": {"evidence_class": "UNKNOWN", "relationship_state": "DECLARED"},
            "evidence_events": [],
            "authority_created": false if False else False,
            "evidence_refs": [],
        }
    )
    synth_audit = audit_graph(synthesized)
    tests.append({"name": "shared_child_synthesis", "expected": "REJECT", "actual": "REJECT" if not synth_audit["pass"] else "ACCEPT", "pass": not synth_audit["pass"], "errors": synth_audit["errors"]})

    fill_hold = copy.deepcopy(graph)
    hold = edge_map(fill_hold)["HOLD-001"]
    hold["predicate"] = "PARTNER_OF"
    hold["current"] = {"evidence_class": "UNKNOWN", "relationship_state": "DECLARED"}
    hold_audit = audit_graph(fill_hold)
    tests.append({"name": "fill_hold_without_edge_evidence", "expected": "REJECT", "actual": "REJECT" if not hold_audit["pass"] else "ACCEPT", "pass": not hold_audit["pass"], "errors": hold_audit["errors"]})

    return tests


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    graph_path = Path(args.graph)
    out_path = Path(args.out)
    raw = graph_path.read_bytes()
    graph = json.loads(raw.decode("utf-8"))

    baseline = audit_graph(graph)
    adversarial = run_adversarial_tests(graph)
    adversarial_pass = all(test["pass"] for test in adversarial)
    overall_pass = baseline["pass"] and adversarial_pass

    non_jay_edges = [
        e["edge_id"]
        for e in graph["edges"]
        if e.get("subject") != "DADDY_JAY" and e.get("object") != "DADDY_JAY"
    ]

    receipt = {
        "receipt_type": "FAMILY_DAILY_AUDIT_RECEIPT",
        "version": "1.2.0",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": os.environ.get("GITHUB_REPOSITORY", "local"),
        "commit_sha": os.environ.get("GITHUB_SHA", "local"),
        "status": "PASS" if overall_pass else "FAIL",
        "graph": {
            "path": str(graph_path),
            "bytes": len(raw),
            "sha256": sha256_bytes(raw),
            "graph_id": graph.get("graph_id"),
            "version": graph.get("version"),
        },
        "coverage": {
            "node_count": baseline["node_count"],
            "edge_count": baseline["edge_count"],
            "non_jay_edge_count": len(non_jay_edges),
            "non_jay_edges": non_jay_edges,
            "silent_nodes": baseline["silent_nodes"],
            "shared_child_pairs": baseline["shared_child_pairs"],
        },
        "relationship_state_counts": baseline["counts"],
        "baseline_audit": {
            "pass": baseline["pass"],
            "errors": baseline["errors"],
            "warnings": baseline["warnings"],
        },
        "adversarial_tests": adversarial,
        "sealed_invariants": graph.get("sealed_invariants", []),
        "machine_actions": {
            "facts_promoted": 0,
            "nodes_promoted": 0,
            "edges_created": 0,
            "family_wide_promotion": False,
            "authority_created": False,
        },
        "laws": [
            "EVIDENCE_CLASS_NE_RELATIONSHIP_STATE",
            "TRANSITION_EDGE_X_MAY_MUTATE_EDGE_X_ONLY",
            "SHARED_CHILD_NE_ADULT_RELATIONSHIP",
            "SILENCE_IS_VALID_GRAPH_STATE",
            "HOLD_UNSPECIFIED_NE_INVITATION_TO_GUESS",
            "EVIDENCE_IS_NOT_CONTAGIOUS",
        ],
        "authority_created": False,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
