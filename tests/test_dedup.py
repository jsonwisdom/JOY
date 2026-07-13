from mcp.courtlistener import dedup

def test_claim_event_first_time(tmp_path):
    dedup.DEDUP_DIR = tmp_path
    assert dedup.claim_event("evt_123") is True
    assert (tmp_path / "evt_123.lock").exists()

def test_claim_event_duplicate(tmp_path):
    dedup.DEDUP_DIR = tmp_path
    assert dedup.claim_event("evt_456") is True
    assert dedup.claim_event("evt_456") is False
