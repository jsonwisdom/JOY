import os

import pytest

from mcp.courtlistener import consumer


@pytest.fixture
def dirs(tmp_path, monkeypatch):
    monkeypatch.setattr(consumer, "SPOOL_DIR", tmp_path / "spool")
    monkeypatch.setattr(consumer, "PROC_DIR", tmp_path / "processing")
    monkeypatch.setattr(consumer, "DONE_DIR", tmp_path / "processed")
    monkeypatch.setattr(consumer, "FAIL_DIR", tmp_path / "failed")
    monkeypatch.setattr(consumer, "CONSUMER_LOCK", tmp_path / "consumer.lock")

    for directory in (
        consumer.SPOOL_DIR,
        consumer.PROC_DIR,
        consumer.DONE_DIR,
        consumer.FAIL_DIR,
    ):
        directory.mkdir()

    return consumer


def test_success_path(dirs):
    (consumer.SPOOL_DIR / "ok.json").write_text(
        '{"id":"ok"}',
        encoding="utf-8",
    )
    consumer.consume_spool()

    assert (consumer.DONE_DIR / "ok.json").exists()
    assert (consumer.DONE_DIR / "ok.result.json").exists()


def test_lock_rejection_live_pid(dirs):
    consumer.CONSUMER_LOCK.write_text(
        str(os.getpid()),
        encoding="utf-8",
    )
    consumer.consume_spool()

    assert consumer.CONSUMER_LOCK.exists()


def test_lock_recovery_stale_pid(dirs, monkeypatch):
    consumer.CONSUMER_LOCK.write_text("12345", encoding="utf-8")

    def stale_pid(pid, signal):
        raise ProcessLookupError

    monkeypatch.setattr(consumer.os, "kill", stale_pid)
    consumer.consume_spool()

    assert not consumer.CONSUMER_LOCK.exists()


def test_process_failure_path(dirs, monkeypatch):
    def fail_process(event, event_id):
        raise ValueError("Fail")

    monkeypatch.setattr(consumer, "process_event", fail_process)
    (consumer.SPOOL_DIR / "fail.json").write_text(
        "{}",
        encoding="utf-8",
    )
    consumer.consume_spool()

    assert (consumer.FAIL_DIR / "fail.json").exists()
    assert (consumer.FAIL_DIR / "fail.error.json").exists()


def test_invalid_json_handling(dirs):
    (consumer.SPOOL_DIR / "bad.json").write_text(
        "{ invalid }",
        encoding="utf-8",
    )
    consumer.consume_spool()

    assert (consumer.FAIL_DIR / "bad.json").exists()
    assert (consumer.FAIL_DIR / "bad.error.json").exists()


def test_result_receipt_failure(dirs, monkeypatch):
    original_write = consumer.write_json_atomic

    def selective_failure(path, data):
        if path.name == "evt.result.json":
            raise OSError("Disk Full")
        return original_write(path, data)

    monkeypatch.setattr(
        consumer,
        "write_json_atomic",
        selective_failure,
    )

    (consumer.SPOOL_DIR / "evt.json").write_text(
        "{}",
        encoding="utf-8",
    )
    consumer.consume_spool()

    assert (consumer.DONE_DIR / "evt.json").exists()
    assert not (consumer.DONE_DIR / "evt.result.json").exists()
    assert (consumer.FAIL_DIR / "evt.receipt-error.json").exists()
