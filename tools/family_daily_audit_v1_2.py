#!/usr/bin/env python3
"""Family Daily Audit v1.3 — edge-local, append-only, no silent inference, hardened origin + provenance."""

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

EVIDENCE_CLASSES = {"USER_DECLARED", "DOCUMENT_SOURCE_BOUND", "PERSON_CONFIRMED", "CONFLICTED", "UNKNOWN"}
RELATIONSHIP_STATES = {"DECLARED", "VERIFIED", "HOLD_UNSPECIFIED", "DISPUTED", "REJECTED"}
ADULT_PREDICATES = {
    "SPOUSE_OF", "PARTNER_OF", "CO_PARENT_OF", "HOUSEHOLD_WITH",
    "CUSTODY_WITH", "LEGAL_PARENTAGE_WITH", "INTERPERSONAL_HISTORY_WITH",
}
# Explicit origins that may assert any kinship edge. Everything else is rejected.
EXPLICIT_ORIGINS = {"USER_DECLARED", "DOCUMENT_SOURCE_BOUND", "PERSON_CONFIRMED"}


def edge_map(graph: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {e["edge_id"]: e for e in graph["edges"]}


def audit_graph(graph: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    constraints = graph.get("identity_constraints", [])
    node_ids = [n.get("node_id") for n in nodes]
    known_nodes = set(node_ids)

    if graph.get("authority_created") is not False:
        errors.append("graph authority_created must be false")
    if graph.get("silent_inference") is not False:
        errors.append("silent_inference must be false")
    if len(node_ids) != len(set(node_ids)):
        errors.append("node_id values must be unique")

    ids = [e.get("edge_id") for e in edges]
    if len(ids) != len(set(ids)):
        errors.append("edge_id values must be unique")

    for c in constraints:
        if c.get("authority_created") is not False:
            errors.append(f"{c.get('constraint_id')}: authority created")
        if c.get("left") not in known_nodes or c.get("right") not in known_nodes:
            errors.append(f"{c.get('constraint_id')}: unknown identity node")

    ref_owner: dict[str, str] = {}
    parents_by_child: dict[str, set[str]] = {}

    for e in edges:
        eid = e.get("edge_id", "<missing>")
        current = e.get("current") or {}
        ec = current.get("evidence_class")
        rs = current.get("relationship_state")
        events = e.get("evidence_events")
        refs = e.get("evidence_refs")
        pred = e.get("predicate")
        origin = e.get("origin")

        if e.get("subject") not in known_nodes or e.get("object") not in known_nodes:
            errors.append(f"{eid}: unknown node reference")
        if e.get("authority_created") is not False:
            errors.append(f"{eid}: authority_created must be false")
        if ec not in EVIDENCE_CLASSES:
            errors.append(f"{eid}: invalid evidence class {ec!r}")
        if rs not in RELATIONSHIP_STATES:
            errors.append(f"{eid}: invalid relationship state {rs!r}")
        if not isinstance(events, list):
            errors.append(f"{eid}: evidence_events must be array")
            events = []
        if not isinstance(refs, list):
            errors.append(f"{eid}: evidence_refs must be array")
            refs = []

        for ref in refs:
            if ref in ref_owner and ref_owner[ref] != eid:
                errors.append(f"{eid}: edge-local evidence ref reused from {ref_owner[ref]}")
            ref_owner[ref] = eid

        if rs == "HOLD_UNSPECIFIED":
            if pred is not None:
                errors.append(f"{eid}: HOLD_UNSPECIFIED requires predicate=null")
            if ec != "UNKNOWN":
                errors.append(f"{eid}: HOLD_UNSPECIFIED requires UNKNOWN evidence")
            if events:
                errors.append(f"{eid}: HOLD_UNSPECIFIED cannot fabricate event history")
            if origin != "EXPLICIT_HOLD":
                errors.append(f"{eid}: HOLD_UNSPECIFIED requires EXPLICIT_HOLD origin")
        else:
            # Asserted edge (any non-null predicate, non-HOLD state)
            if not isinstance(pred, str) or not pred:
                errors.append(f"{eid}: asserted edge requires predicate")
            if origin == "EXPLICIT_HOLD":
                errors.append(f"{eid}: EXPLICIT_HOLD cannot assert predicate")
            # Strong future-proof rule: any asserted kinship edge needs explicit origin
            if origin not in EXPLICIT_ORIGINS:
                errors.append(
                    f"{eid}: asserted edge origin {origin!r} not in EXPLICIT_ORIGINS; "
                    "MACHINE_GENERATED / ADJACENCY_DERIVED / SHARED_CHILD_DERIVED / SOCIAL_EXPECTATION_DERIVED rejected"
                )
            if not events:
                errors.append(f"{eid}: asserted edge requires evidence history")
            else:
                nums = [x.get("event") for x in events]
                if nums != list(range(1, len(events) + 1)):
                    errors.append(f"{eid}: event history must be append-only 1..N")
                for x in events:
                    if x.get("class") not in EVIDENCE_CLASSES:
                        errors.append(f"{eid}: invalid event evidence class")
                    if x.get("result") not in RELATIONSHIP_STATES:
                        errors.append(f"{eid}: invalid event relationship state")
                if events[-1].get("class") != ec or events[-1].get("result") != rs:
                    errors.append(f"{eid}: current state must match last evidence event")

        if pred == "PARENT_OF" and rs in {"DECLARED", "VERIFIED", "DISPUTED"}:
            parents_by_child.setdefault(e.get("object"), set()).add(e.get("subject"))

        # Adult predicates retain the extra local-evidence requirement (already covered by EXPLICIT_ORIGINS)
        if pred in ADULT_PREDICATES:
            if not events:
                errors.append(f"{eid}: adult edge requires evidence on that exact edge")

    shared_pairs: list[dict[str, Any]] = []
    for child, parents in sorted(parents_by_child.items()):
        for left, right in combinations(sorted(parents), 2):
            shared_pairs.append({"child": child, "subjects": [left, right]})
            for e in edges:
                if {e.get("subject"), e.get("object")} == {left, right}:
                    if e.get("predicate") in ADULT_PREDICATES and e.get("origin") not in EXPLICIT_ORIGINS:
                        errors.append(f"{e.get('edge_id')}: shared child {child} synthesized adult edge")

    touched = {e.get("subject") for e in edges} | {e.get("object") for e in edges}
    silent_nodes = sorted(known_nodes - touched)
    counts = {state.lower(): sum(1 for e in edges if e.get("current", {}).get("relationship_state") == state)
              for state in RELATIONSHIP_STATES}

    return {
        "pass": not errors,
        "errors": errors,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "shared_child_pairs": shared_pairs,
        "silent_nodes": silent_nodes,
        "counts": counts,
    }


def validate_local_transition(before: dict[str, Any], after: dict[str, Any], target_id: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if before.get("nodes") != after.get("nodes"):
        errors.append("local transition changed nodes")
    if before.get("identity_constraints") != after.get("identity_constraints"):
        errors.append("local transition changed identity constraints")

    b, a = edge_map(before), edge_map(after)
    if set(b) != set(a):
        return False, errors + ["local transition created or deleted an edge"]
    if target_id not in b:
        return False, errors + ["target edge missing"]

    for eid in b:
        if eid != target_id and b[eid] != a[eid]:
            errors.append(f"neighbor edge mutated: {eid}")

    old, new = b[target_id], a[target_id]
    for key in ("edge_id", "subject", "predicate", "object", "origin"):
        if old.get(key) != new.get(key):
            errors.append(f"target immutable field changed: {key}")

    old_events, new_events = old.get("evidence_events", []), new.get("evidence_events", [])
    if len(new_events) < len(old_events) or new_events[:len(old_events)] != old_events:
        errors.append("evidence history was erased or rewritten")
    if new.get("authority_created") is not False:
        errors.append("transition created authority")

    errors.extend(f"post-transition: {x}" for x in audit_graph(after)["errors"])
    return not errors, errors


def adversarial_tests(graph: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []

    # Legal synthetic transition deliberately targets Gaga -> MaryDee to prove
    # the workflow audits the family beyond Jay. It does not alter the source graph.
    legal = copy.deepcopy(graph)
    t = edge_map(legal)["EDGE-006"]
    t["evidence_events"].append({
        "event": 2,
        "class": "PERSON_CONFIRMED",
        "result": "VERIFIED",
        "receipt": "SYNTHETIC_TEST_ONLY_DO_NOT_PROMOTE",
        "timestamp": None,
    })
    t["current"] = {"evidence_class": "PERSON_CONFIRMED", "relationship_state": "VERIFIED"}
    ok, errs = validate_local_transition(graph, legal, "EDGE-006")
    out.append({"name": "edge_local_promotion_beyond_jay", "expected": "ACCEPT", "actual": "ACCEPT" if ok else "REJECT", "pass": ok, "errors": errs})

    neighbor = copy.deepcopy(legal)
    edge_map(neighbor)["EDGE-007"]["current"] = {"evidence_class": "PERSON_CONFIRMED", "relationship_state": "VERIFIED"}
    ok, errs = validate_local_transition(graph, neighbor, "EDGE-006")
    out.append({"name": "neighbor_edge_inheritance", "expected": "REJECT", "actual": "ACCEPT" if ok else "REJECT", "pass": not ok, "errors": errs})

    erased = copy.deepcopy(legal)
    edge_map(erased)["EDGE-006"]["evidence_events"] = edge_map(erased)["EDGE-006"]["evidence_events"][1:]
    ok, errs = validate_local_transition(graph, erased, "EDGE-006")
    out.append({"name": "history_erasure", "expected": "REJECT", "actual": "ACCEPT" if ok else "REJECT", "pass": not ok, "errors": errs})

    # ATTACK: MACHINE_GENERATED PARENT_OF (must REJECT under the stronger rule)
    attack_parent = copy.deepcopy(graph)
    attack_parent["edges"].append({
        "edge_id": "ATTACK-MACHINE-PARENT",
        "subject": "DADDY_JAY",
        "predicate": "PARENT_OF",
        "object": "JAYCEE",
        "origin": "MACHINE_GENERATED",
        "current": {"evidence_class": "USER_DECLARED", "relationship_state": "DECLARED"},
        "evidence_events": [{"event": 1, "class": "USER_DECLARED", "result": "DECLARED", "receipt": None, "timestamp": None}],
        "authority_created": False,
        "evidence_refs": [],
    })
    check = audit_graph(attack_parent)
    out.append({
        "name": "machine_generated_parent_of",
        "expected": "REJECT",
        "actual": "REJECT" if not check["pass"] else "ACCEPT",
        "pass": not check["pass"],
        "errors": check["errors"],
    })

    # ATTACK: MACHINE_GENERATED AUNT_OF
    attack_aunt = copy.deepcopy(graph)
    attack_aunt["edges"].append({
        "edge_id": "ATTACK-MACHINE-AUNT",
        "subject": "AUNT_MAY",
        "predicate": "AUNT_OF",
        "object": "JAYCEE",
        "origin": "MACHINE_GENERATED",
        "current": {"evidence_class": "UNKNOWN", "relationship_state": "DECLARED"},
        "evidence_events": [{"event": 1, "class": "UNKNOWN", "result": "DECLARED", "receipt": None, "timestamp": None}],
        "authority_created": False,
        "evidence_refs": [],
    })
    check = audit_graph(attack_aunt)
    out.append({
        "name": "machine_generated_aunt_of",
        "expected": "REJECT",
        "actual": "REJECT" if not check["pass"] else "ACCEPT",
        "pass": not check["pass"],
        "errors": check["errors"],
    })

    # Shared-child adult synthesis (still required)
    synth = copy.deepcopy(graph)
    synth["edges"].append({
        "edge_id": "ATTACK-SHARED-CHILD",
        "subject": "DADDY_JAY",
        "predicate": "SPOUSE_OF",
        "object": "MARYDEE",
        "origin": "MACHINE_GENERATED",
        "current": {"evidence_class": "UNKNOWN", "relationship_state": "DECLARED"},
        "evidence_events": [],
        "authority_created": False,
        "evidence_refs": [],
    })
    check = audit_graph(synth)
    out.append({"name": "shared_child_synthesis", "expected": "REJECT", "actual": "REJECT" if not check["pass"] else "ACCEPT", "pass": not check["pass"], "errors": check["errors"]})

    filled = copy.deepcopy(graph)
    h = edge_map(filled)["HOLD-001"]
    h["predicate"] = "PARTNER_OF"
    h["current"] = {"evidence_class": "UNKNOWN", "relationship_state": "DECLARED"}
    check = audit_graph(filled)
    out.append({"name": "fill_hold_without_edge_evidence", "expected": "REJECT", "actual": "REJECT" if not check["pass"] else "ACCEPT", "pass": not check["pass"], "errors": check["errors"]})
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--graph", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    path = Path(args.graph)
    raw = path.read_bytes()
    graph = json.loads(raw.decode("utf-8"))
    baseline = audit_graph(graph)
    attacks = adversarial_tests(graph)
    passed = baseline["pass"] and all(x["pass"] for x in attacks)

    non_jay = [e["edge_id"] for e in graph["edges"] if e.get("subject") != "DADDY_JAY" and e.get("object") != "DADDY_JAY"]

    # Provenance: prefer actual checked-out HEAD when available; fall back to env
    tested_commit_sha = os.environ.get("TESTED_COMMIT_SHA") or os.environ.get("GITHUB_SHA", "local")
    trigger_sha = os.environ.get("TRIGGER_SHA") or os.environ.get("GITHUB_SHA", "local")
    pr_head_sha = os.environ.get("PULL_REQUEST_HEAD_SHA") or ""
    exact_match = os.environ.get("EXACT_CHECKOUT_MATCH", "unknown")

    receipt = {
        "receipt_type": "FAMILY_DAILY_AUDIT_RECEIPT",
        "version": "1.3.0",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": os.environ.get("GITHUB_REPOSITORY", "local"),
        "trigger_sha": trigger_sha,
        "tested_commit_sha": tested_commit_sha,
        "pull_request_head_sha": pr_head_sha or None,
        "exact_checkout_match": exact_match == "true",
        "status": "PASS" if passed else "FAIL",
        "graph": {
            "path": str(path),
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "graph_id": graph.get("graph_id"),
            "version": graph.get("version"),
        },
        "coverage": {
            "node_count": baseline["node_count"],
            "edge_count": baseline["edge_count"],
            "non_jay_edge_count": len(non_jay),
            "non_jay_edges": non_jay,
            "silent_nodes": baseline["silent_nodes"],
            "shared_child_pairs": baseline["shared_child_pairs"],
        },
        "relationship_state_counts": baseline["counts"],
        "baseline_audit": {"pass": baseline["pass"], "errors": baseline["errors"]},
        "adversarial_tests": attacks,
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
            "ASSERTED_EDGE_REQUIRES_EXPLICIT_ORIGIN",
        ],
        "authority_created": False,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
