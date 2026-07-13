from mcp.courtlistener.evidence_rules import evaluate


def candidate():
    return {
        "court": {"docket_number": "1:26-cv-001", "date_filed": "2026-04-01"},
        "content": {"plain_text": "Filed complaint."},
        "source": {"event_hash": "abc123", "system": "courtlistener"},
    }


def test_strong_exact_match_promotes():
    assert evaluate(candidate(), candidate())["disposition"] == "PROMOTION_APPROVED"


def test_weak_only_holds():
    evidence = {"court": {"docket_number": "1:26-cv-001"}}
    result = evaluate(candidate(), evidence)
    assert result["disposition"] == "HOLD"
    assert result["weak_rule_hits"] >= 1


def test_contradiction_rejects():
    evidence = candidate()
    evidence["content"] = {"plain_text": "Different filing."}
    assert evaluate(candidate(), evidence)["disposition"] == "REJECT"


def test_provenance_gap_holds():
    evidence = candidate()
    evidence["source"] = {}
    result = evaluate(candidate(), evidence)
    assert result["disposition"] == "HOLD"
    assert result["provenance_gaps"]


def test_temporal_mismatch_holds():
    evidence = candidate()
    evidence["court"] = dict(evidence["court"], date_filed="2026-04-02")
    result = evaluate(candidate(), evidence)
    assert result["disposition"] == "HOLD"
    assert result["temporal_mismatches"]


def test_missing_required_field_holds():
    incomplete = candidate()
    incomplete["content"] = {}
    result = evaluate(incomplete, candidate())
    assert result["disposition"] == "HOLD"
    assert "content.plain_text" in result["missing_required"]
