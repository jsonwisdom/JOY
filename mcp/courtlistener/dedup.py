import os
from pathlib import Path

DEDUP_DIR = Path("mcp/storage/locks")

def claim_event(event_id: str) -> bool:
    DEDUP_DIR.mkdir(parents=True, exist_ok=True)
    lock_file = DEDUP_DIR / f"{event_id}.lock"

    try:
        fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        with os.fdopen(fd, "w") as handle:
            handle.write("claimed")
        return True
    except FileExistsError:
        return False
