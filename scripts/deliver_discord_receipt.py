#!/usr/bin/env python3
"""Artifact-first Atomic JOY Discord delivery adapter.

This program does NOT rerun eligibility logic. It consumes a previously produced
Atomic JOY CI artifact, verifies provenance bindings, builds a deterministic
presentation payload, delivers it to Discord, and records a delivery receipt.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

INPUT_DIR = Path(os.getenv("ATOMIC_JOY_INPUT_DIR", "artifacts/input"))
OUTPUT_DIR = Path(os.getenv("ATOMIC_JOY_DELIVERY_DIR", "artifacts/atomic_joy/delivery"))
EXPECTED_HEAD = os.environ["ATOMIC_JOY_EXPECTED_HEAD"]
EXPECTED_RUN_ID = str(os.environ["ATOMIC_JOY_EXPECTED_RUN_ID"])
ARTIFACT_ID = str(os.environ["ATOMIC_JOY_ARTIFACT_ID"])
ARTIFACT_DIGEST = os.environ["ATOMIC_JOY_ARTIFACT_DIGEST"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
DISCORD_CHANNEL_ID = os.environ["DISCORD_CHANNEL_ID"]


def fail(message: str) -> "NoReturn":
    print(f"ATOMIC_JOY_DELIVERY_FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path} JSON root is not an object")
    return value


def atomic_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode()
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def verify_source() -> tuple[dict, dict, str]:
    manifest_path = INPUT_DIR / "receipt_manifest.json"
    stdout_path = INPUT_DIR / "verifier_stdout.json"
    exit_path = INPUT_DIR / "exit_code.txt"
    for path in (manifest_path, stdout_path, exit_path):
        if not path.is_file():
            fail(f"artifact file missing: {path}")

    manifest = load_json(manifest_path)
    stdout_raw = stdout_path.read_bytes()
    verifier = load_json(stdout_path)

    if manifest.get("protocol") != "ATOMIC_JOY_CI_RECEIPT":
        fail("unexpected receipt protocol")
    if manifest.get("head_sha") != EXPECTED_HEAD:
        fail("manifest HEAD mismatch")
    if str(manifest.get("run_id")) != EXPECTED_RUN_ID:
        fail("manifest run id mismatch")
    if manifest.get("exit_code") != 0 or exit_path.read_text().strip() != "0":
        fail("source CI artifact is not exit-code GREEN")
    if manifest.get("no_fake_green") is not True:
        fail("source manifest lacks no_fake_green=true")
    if verifier.get("state") != "GREEN":
        fail("stored verifier result is not GREEN")
    if verifier.get("no_fake_green") is not True:
        fail("stored verifier result lacks no_fake_green=true")

    stdout_sha = sha256_bytes(stdout_raw)
    if manifest.get("stdout_sha256") != stdout_sha:
        fail("verifier stdout digest mismatch")
    if not ARTIFACT_DIGEST.startswith("sha256:") or len(ARTIFACT_DIGEST) != 71:
        fail("GitHub artifact digest is malformed")

    return manifest, verifier, stdout_sha


def build_payload(verifier: dict, stdout_sha: str) -> tuple[dict, str, str]:
    seal_sha = str(verifier.get("seal_sha256", "unknown"))
    material = "|".join((EXPECTED_HEAD, EXPECTED_RUN_ID, ARTIFACT_ID, ARTIFACT_DIGEST, DISCORD_CHANNEL_ID))
    delivery_id = "AJD-" + hashlib.sha256(material.encode()).hexdigest()[:24]

    description = (
        f"**CI_STATUS:** `MATCH`\n"
        f"**CI_RUN_ID:** `{EXPECTED_RUN_ID}`\n"
        f"**CI_HEAD:** `{EXPECTED_HEAD}`\n"
        f"**ARTIFACT_ID:** `{ARTIFACT_ID}`\n"
        f"**ARTIFACT_DIGEST:** `{ARTIFACT_DIGEST}`\n"
        f"**VERIFIER_STDOUT_SHA256:** `{stdout_sha}`\n"
        f"**SOURCE_VERIFIER:** `GREEN`\n"
        f"**SEAL_SHA256:** `{seal_sha}`\n"
        f"**DELIVERY_ID:** `{delivery_id}`"
    )
    payload = {
        "embeds": [{
            "title": "✅ Atomic JOY — Verified CI Receipt",
            "description": description,
            "color": 5763719,
            "footer": {"text": "🧾 CI artifact GREEN · delivery is presentation-only · NO_FAKE_GREEN"},
        }],
        "allowed_mentions": {"parse": []},
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return payload, delivery_id, sha256_bytes(canonical)


def discord_post(payload: dict) -> dict:
    url = f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"
    body = json.dumps(payload, separators=(",", ":")).encode()
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bot {DISCORD_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "AtomicJOYDelivery/0.0.1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:500]
        fail(f"Discord HTTP {exc.code}: {detail}")
    except Exception as exc:
        fail(f"Discord delivery error: {exc}")
    if not isinstance(result, dict) or not result.get("id"):
        fail("Discord response missing message id")
    return result


def main() -> int:
    _, verifier, stdout_sha = verify_source()
    payload, delivery_id, payload_sha = build_payload(verifier, stdout_sha)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    common = {
        "delivery_id": delivery_id,
        "head_sha": EXPECTED_HEAD,
        "source_run_id": EXPECTED_RUN_ID,
        "source_artifact_id": ARTIFACT_ID,
        "source_artifact_digest": ARTIFACT_DIGEST,
        "discord_channel_id": DISCORD_CHANNEL_ID,
        "payload_sha256": payload_sha,
        "no_fake_green": True,
    }
    intent = {
        "protocol": "ATOMIC_JOY_DELIVERY_INTENT",
        "version": "0.0.1",
        **common,
    }
    atomic_json(OUTPUT_DIR / "delivery_intent.json", intent)

    message = discord_post(payload)
    receipt = {
        "protocol": "ATOMIC_JOY_DELIVERY_RECEIPT",
        "version": "0.0.1",
        **common,
        "discord_message_id": str(message["id"]),
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "delivery_status": "DELIVERED_AND_RECORDED",
    }
    atomic_json(OUTPUT_DIR / "delivery_receipt.json", receipt)
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
