#!/usr/bin/env python3
"""Verify JoySpace sister sidecars against exact parent bytes.

The 3/6/9 values are deterministic display/process math. They create no
authority and cannot approve, merge, publish, or establish evidence.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "artifacts" / "SUPER_SECRET_SISTER_SYNTAX_SIDECARS.json"
PHASES = (3, 6, 9)


def digest(path: Path) -> tuple[str, bytes, int]:
    payload = path.read_bytes()
    raw = hashlib.sha256(payload).digest()
    return raw.hex(), raw, len(payload)


def jitter(raw: bytes) -> list[dict[str, int]]:
    return [
        {
            "phase": phase,
            "jigger": (phase * (index + 1) + raw[index]) % 10,
            "scabies_jitter": (raw[index + 3] % 19) - 9,
        }
        for index, phase in enumerate(PHASES)
    ]


def main() -> int:
    pack = json.loads(PACK.read_text(encoding="utf-8"))
    errors: list[str] = []

    if pack.get("authority_created") is not False:
        errors.append("authority_created must remain false")
    for forbidden in ("sidecar_may_approve", "sidecar_may_merge", "sidecar_may_publish"):
        if pack.get(forbidden) is not False:
            errors.append(f"{forbidden} must remain false")

    for item in pack["sidecars"]:
        parent = ROOT / item["parent_path"]
        if not parent.is_file():
            errors.append(f"missing parent: {item['parent_path']}")
            continue
        actual_hash, raw, byte_count = digest(parent)
        if actual_hash != item["parent_sha256"]:
            errors.append(f"parent hash mismatch: {item['id']}")
        if byte_count != item["parent_byte_count"]:
            errors.append(f"parent byte-count mismatch: {item['id']}")
        if jitter(raw) != item["jitter_369"]:
            errors.append(f"3/6/9 jitter mismatch: {item['id']}")

    if errors:
        print("SIDECAR_SEAL=HOLD")
        for error in errors:
            print(f"ERROR={error}")
        return 1

    print("SIDECAR_SEAL=PASS")
    print("JITTER_369=DETERMINISTIC_PROCESS_ONLY")
    print("AUTHORITY_CREATED=false")
    print("PROMOTION=NONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
