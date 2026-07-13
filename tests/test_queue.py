import json
from mcp.courtlistener import queue

def test_enqueue_creates_file(tmp_path):
    queue.SPOOL_DIR = tmp_path
    queue.enqueue_for_alms({"test":"data"}, "evt_001")

    p = tmp_path / "evt_001.json"
    assert p.exists()

    with p.open() as f:
        assert json.load(f) == {"test":"data"}

def test_enqueue_replaces_existing_event(tmp_path):
    queue.SPOOL_DIR = tmp_path

    queue.enqueue_for_alms({"version":1}, "evt_002")
    queue.enqueue_for_alms({"version":2}, "evt_002")

    with (tmp_path/"evt_002.json").open() as f:
        assert json.load(f) == {"version":2}
