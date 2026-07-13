import errno
import json
import os
from pathlib import Path

SPOOL_DIR = Path("mcp/storage/spool")

def enqueue_for_alms(event: dict, event_id: str) -> None:
    """Atomically persist an event into the ALMS spool."""
    SPOOL_DIR.mkdir(parents=True, exist_ok=True)

    spool_path = SPOOL_DIR / f"{event_id}.json"
    tmp_path = SPOOL_DIR / f".{event_id}.tmp"

    try:
        with tmp_path.open("w", encoding="utf-8") as handle:
            json.dump(event, handle, sort_keys=True, separators=(",", ":"))
            handle.flush()
            os.fsync(handle.fileno())

        tmp_path.replace(spool_path)

        directory_fd = os.open(SPOOL_DIR, os.O_RDONLY)
        try:
            try:
                os.fsync(directory_fd)
            except OSError as exc:
                if exc.errno not in (errno.EINVAL, errno.ENOTSUP):
                    raise
        finally:
            os.close(directory_fd)

    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise
