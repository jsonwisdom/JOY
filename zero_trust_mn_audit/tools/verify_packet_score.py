#!/usr/bin/env python3
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)

if len(sys.argv) != 2:
    fail("usage: verify_packet_score.py claims/ALPHA_DEED_001.json")

packet_path = Path(sys.argv[1])
if not packet_path.exists():
    fail(f"missing packet: {packet_path}")

packet = json.loads(packet_path.read_text())
score = packet.get("score")
packet_id = packet.get("packet_id", "")

if packet.get("authority") is not False:
    fail("authority must be false")

if score == 1 and packet.get("claim_status") != "UNVERIFIED_CLAIM":
    fail("score 1 must be labeled UNVERIFIED_CLAIM")

receipt_required = {
    2: ROOT / "requests",
    3: ROOT / "requests",
    4: ROOT / "received",
    5: ROOT / "preserved",
    6: ROOT / "verified",
    7: ROOT / "replayable",
}

if score in receipt_required:
    folder = receipt_required[score]
    matches = list(folder.glob(f"*{packet_id}*"))
    if not matches:
        fail(f"score {score} requires matching receipt in {folder}")

print("PASS:", packet_id, "score", score)
