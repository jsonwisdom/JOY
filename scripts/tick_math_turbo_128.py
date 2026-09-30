#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

BPM = 128
TICK_NS = 468_750_000

ALLOWED = {
    ("OPEN", "OPERATE"),
    ("OPERATE", "CAPTURE"),
    ("CAPTURE", "RECONCILE"),
    ("RECONCILE", "CLOSE"),
    ("CLOSE", "LEARN"),
    ("LEARN", "VERSION"),
    ("VERSION", "OPEN"),
}

CORE_FIELDS = (
    "receipt_id",
    "tick",
    "state",
    "authority_created",
    "mutates_prior",
    "prev_hash",
)

def digest(event):
    core = {k: event.get(k) for k in CORE_FIELDS}
    raw = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def validate(doc):
    events = doc.get("events", [])
    checks = {
        "TEMPO_PASS": doc.get("bpm") == BPM and doc.get("tick_ns") == TICK_NS,
        "MONOTONIC_PASS": True,
        "ARC_PASS": True,
        "HASH_CHAIN_PASS": True,
        "FORWARD_ONLY_PASS": True,
        "AUTHORITY_PASS": True,
        "RECEIPT_PASS": True,
    }
    errors = []

    if not events:
        checks["RECEIPT_PASS"] = False
        errors.append("events must not be empty")

    seen_receipts = set()
    for i, event in enumerate(events):
        rid = event.get("receipt_id")
        if not isinstance(rid, str) or not rid or rid in seen_receipts:
            checks["RECEIPT_PASS"] = False
            errors.append(f"event[{i}] invalid or duplicate receipt_id")
        else:
            seen_receipts.add(rid)

        if event.get("authority_created") is not False:
            checks["AUTHORITY_PASS"] = False
            errors.append(f"event[{i}] authority_created must be false")

        if event.get("mutates_prior") is not False:
            checks["FORWARD_ONLY_PASS"] = False
            errors.append(f"event[{i}] mutates_prior must be false")

        if event.get("event_hash") != digest(event):
            checks["HASH_CHAIN_PASS"] = False
            errors.append(f"event[{i}] event_hash mismatch")

        if i == 0:
            if event.get("prev_hash") is not None:
                checks["HASH_CHAIN_PASS"] = False
                errors.append("event[0] prev_hash must be null")
            continue

        prev = events[i - 1]
        if not isinstance(event.get("tick"), int) or event["tick"] <= prev.get("tick", -1):
            checks["MONOTONIC_PASS"] = False
            errors.append(f"event[{i}] tick must strictly increase")

        if (prev.get("state"), event.get("state")) not in ALLOWED:
            checks["ARC_PASS"] = False
            errors.append(
                f"event[{i}] illegal arc {prev.get('state')} -> {event.get('state')}"
            )

        if event.get("prev_hash") != prev.get("event_hash"):
            checks["HASH_CHAIN_PASS"] = False
            errors.append(f"event[{i}] prev_hash does not bind event[{i-1}]")

    result = {
        "protocol": "TICK_MATH_TURBO_128_V0_1",
        "bpm": BPM,
        "tick_ns": TICK_NS,
        "checks": checks,
        "MULTIPASS": all(checks.values()),
        "errors": errors,
    }
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "path",
        nargs="?",
        default="fixtures/apple-blossom/tick_math_turbo_128_v0_1.json",
    )
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    doc = json.loads(Path(args.path).read_text(encoding="utf-8"))
    result = validate(doc)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["MULTIPASS"] else 1)

if __name__ == "__main__":
    main()
