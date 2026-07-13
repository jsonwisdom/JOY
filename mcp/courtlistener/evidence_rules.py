from __future__ import annotations

from typing import Any

STRONG_CORROBORATION_THRESHOLD = 1.0
MATERIAL_PATHS = (
    "court.docket_number",
    "court.date_filed",
    "content.plain_text",
    "source.event_hash",
    "source.system",
)

EVIDENCE_RULE_CATALOG_V0_1 = [{'rule_id': 'strong_corroboration_exact_match', 'description': "A provenance-bearing source exactly matches the candidate's material court fields.", 'class': 'STRONG_CORROBORATION', 'weight': 1.0, 'required_fields': ['court.docket_number', 'court.date_filed', 'content.plain_text', 'source.event_hash', 'source.system'], 'contradiction': False, 'promotion_eligible': True}, {'rule_id': 'weak_corroboration_partial_match', 'description': 'Evidence matches at least one material field but does not satisfy the strong rule.', 'class': 'WEAK_CORROBORATION', 'weight': 0.4, 'required_fields': [], 'contradiction': False, 'promotion_eligible': False}, {'rule_id': 'contradiction_direct', 'description': 'Evidence directly contradicts a material candidate field.', 'class': 'CONTRADICTION', 'weight': -1.0, 'required_fields': ['content.plain_text'], 'contradiction': True, 'promotion_eligible': False}, {'rule_id': 'provenance_gap_missing_source', 'description': 'Evidence lacks source system or event-hash provenance.', 'class': 'PROVENANCE_GAP', 'weight': -0.5, 'required_fields': ['source.event_hash', 'source.system'], 'contradiction': False, 'promotion_eligible': False}, {'rule_id': 'temporal_mismatch_out_of_range', 'description': 'Evidence filing date differs from the candidate filing date.', 'class': 'TEMPORAL_MISMATCH', 'weight': -0.3, 'required_fields': ['court.date_filed'], 'contradiction': False, 'promotion_eligible': False}]


def get_path(data: dict[str, Any], path: str) -> Any:
    value: Any = data
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def evaluate(candidate: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    missing_required = [path for path in MATERIAL_PATHS if get_path(candidate, path) in (None, "")]
    provenance_gaps = [
        path for path in ("source.event_hash", "source.system")
        if get_path(evidence, path) in (None, "")
    ]

    contradictions = []
    for path in ("court.docket_number", "content.plain_text"):
        left = get_path(candidate, path)
        right = get_path(evidence, path)
        if left not in (None, "") and right not in (None, "") and left != right:
            contradictions.append(path)

    temporal_mismatches = []
    candidate_date = get_path(candidate, "court.date_filed")
    evidence_date = get_path(evidence, "court.date_filed")
    if candidate_date not in (None, "") and evidence_date not in (None, "") and candidate_date != evidence_date:
        temporal_mismatches.append("court.date_filed")

    exact_match = (
        not missing_required
        and not provenance_gaps
        and not contradictions
        and not temporal_mismatches
        and all(get_path(candidate, path) == get_path(evidence, path) for path in MATERIAL_PATHS)
    )

    weak_matches = [
        path for path in MATERIAL_PATHS
        if get_path(candidate, path) not in (None, "")
        and get_path(candidate, path) == get_path(evidence, path)
    ]

    strong_rule_hits = 1 if exact_match else 0
    strong_weight = 1.0 if exact_match else 0.0

    if contradictions:
        disposition = "REJECT"
    elif (
        strong_weight >= STRONG_CORROBORATION_THRESHOLD
        and strong_rule_hits >= 1
        and not provenance_gaps
        and not temporal_mismatches
        and not missing_required
    ):
        disposition = "PROMOTION_APPROVED"
    else:
        disposition = "HOLD"

    return {
        "catalog_version": "0.1",
        "disposition": disposition,
        "strong_weight": strong_weight,
        "strong_rule_hits": strong_rule_hits,
        "weak_rule_hits": len(weak_matches) if not exact_match else 0,
        "contradictions": contradictions,
        "provenance_gaps": provenance_gaps,
        "temporal_mismatches": temporal_mismatches,
        "missing_required": missing_required,
        "required_fields_complete": not missing_required,
        "green": False,
        "authority": False,
    }
