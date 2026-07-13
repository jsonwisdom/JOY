import json
import os
import re
import time
import traceback
from pathlib import Path

SPOOL_DIR = Path("mcp/storage/spool")
PROC_DIR = Path("mcp/storage/processing")
DONE_DIR = Path("mcp/storage/processed")
FAIL_DIR = Path("mcp/storage/failed")
CONSUMER_LOCK = Path("mcp/storage/consumer.lock")

ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]+\.json$")


def write_json_atomic(path: Path, data: dict) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    try:
        with tmp.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, sort_keys=True, separators=(",", ":"))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def build_error(exc: Exception, event_id: str) -> dict:
    return {
        "event_id": event_id,
        "exception": type(exc).__name__,
        "message": str(exc),
        "timestamp": time.time(),
        "traceback": traceback.format_exc(),
    }


def acquire_lock() -> bool:
    CONSUMER_LOCK.parent.mkdir(parents=True, exist_ok=True)

    if CONSUMER_LOCK.exists():
        try:
            pid = int(CONSUMER_LOCK.read_text().strip())
            os.kill(pid, 0)
            return False
        except PermissionError:
            return False
        except (ProcessLookupError, ValueError):
            CONSUMER_LOCK.unlink(missing_ok=True)

    try:
        with CONSUMER_LOCK.open("x", encoding="utf-8") as handle:
            handle.write(str(os.getpid()))
        return True
    except FileExistsError:
        return False


def recover_processing() -> None:
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    SPOOL_DIR.mkdir(parents=True, exist_ok=True)

    for path in PROC_DIR.glob("*.json"):
        os.replace(path, SPOOL_DIR / path.name)


def process_event(event: dict, event_id: str) -> dict:
    return {"status": "candidate_emitted", "event_id": event_id}


def consume_spool() -> None:
    if not acquire_lock():
        return

    try:
        for directory in (SPOOL_DIR, PROC_DIR, DONE_DIR, FAIL_DIR):
            directory.mkdir(parents=True, exist_ok=True)

        recover_processing()

        for file_path in SPOOL_DIR.glob("*.json"):
            if not ID_PATTERN.fullmatch(file_path.name):
                continue

            event_id = file_path.stem
            proc_path = PROC_DIR / file_path.name

            try:
                os.replace(file_path, proc_path)
            except OSError:
                continue

            try:
                with proc_path.open("r", encoding="utf-8") as handle:
                    event = json.load(handle)
                result = process_event(event, event_id)
            except Exception as exc:
                os.replace(proc_path, FAIL_DIR / file_path.name)
                write_json_atomic(
                    FAIL_DIR / f"{event_id}.error.json",
                    build_error(exc, event_id),
                )
                continue

            os.replace(proc_path, DONE_DIR / file_path.name)

            try:
                write_json_atomic(
                    DONE_DIR / f"{event_id}.result.json",
                    result,
                )
            except Exception as exc:
                fallback = {
                    "event_id": event_id,
                    "status": "processed_receipt_missing",
                    "exception": type(exc).__name__,
                    "message": str(exc),
                    "timestamp": time.time(),
                }
                try:
                    write_json_atomic(
                        FAIL_DIR / f"{event_id}.receipt-error.json",
                        fallback,
                    )
                except Exception:
                    print(json.dumps(fallback), flush=True)
    finally:
        CONSUMER_LOCK.unlink(missing_ok=True)
