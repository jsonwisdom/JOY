#!/usr/bin/env python3
"""Artifact-first Atomic JOY Discord delivery adapter.

This program never reruns eligibility logic. It consumes a previously produced
Atomic JOY CI artifact plus GitHub artifact metadata, verifies all provenance
bindings, builds a deterministic presentation payload, optionally emits a
secret-free dry-run proof, delivers to Discord, and records Receipt 2.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import NoReturn


def fail(message: str) -> NoReturn:
    print(f"ATOMIC_JOY_DELIVERY_FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        fail(f"required environment variable missing: {name}")
    return value


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
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def source_context() -> dict[str, str]:
    return {
        "head": required_env("ATOMIC_JOY_EXPECTED_HEAD"),
        "run_id": required_env("ATOMIC_JOY_EXPECTED_RUN_ID"),
        "artifact_id": required_env("ATOMIC_JOY_ARTIFACT_ID"),
        "artifact_digest": required_env("ATOMIC_JOY_ARTIFACT_DIGEST"),
    }


def verify_source(input_dir: Path, ctx: dict[str, str]) -> tuple[dict, str]:
    manifest_path = input_dir / "receipt_manifest.json"
    stdout_path = input_dir / "verifier_stdout.json"
    exit_path = input_dir / "exit_code.txt"
    metadata_path = input_dir / "github_artifact_metadata.json"
    for path in (manifest_path, stdout_path, exit_path, metadata_path):
        if not path.is_file():
            fail(f"artifact file missing: {path}")

    manifest = load_json(manifest_path)
    metadata = load_json(metadata_path)
    stdout_raw = stdout_path.read_bytes()
    verifier = load_json(stdout_path)

    expected_name = f"atomic-joy-runtime-{ctx['head']}"
    if metadata.get("head_sha") != ctx["head"]:
        fail("GitHub artifact metadata HEAD mismatch")
    if str(metadata.get("run_id")) != ctx["run_id"]:
        fail("GitHub artifact metadata run id mismatch")
    if str(metadata.get("artifact_id")) != ctx["artifact_id"]:
        fail("GitHub artifact metadata id mismatch")
    if metadata.get("artifact_name") != expected_name:
        fail("GitHub artifact metadata name mismatch")
    if metadata.get("artifact_digest") != ctx["artifact_digest"]:
        fail("GitHub artifact metadata digest mismatch")

    digest = ctx["artifact_digest"]
    if not digest.startswith("sha256:") or len(digest) != 71:
        fail("GitHub artifact digest is malformed")

    if manifest.get("protocol") != "ATOMIC_JOY_CI_RECEIPT":
        fail("unexpected receipt protocol")
    if manifest.get("head_sha") != ctx["head"]:
        fail("manifest HEAD mismatch")
    if str(manifest.get("run_id")) != ctx["run_id"]:
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

    return verifier, stdout_sha


def delivery_id_for(ctx: dict[str, str]) -> str:
    material = "|".join(
        (ctx["head"], ctx["run_id"], ctx["artifact_id"], ctx["artifact_digest"])
    )
    return "AJD-" + hashlib.sha256(material.encode()).hexdigest()[:24]


def build_payload(
    verifier: dict, stdout_sha: str, ctx: dict[str, str]
) -> tuple[dict, str, str]:
    delivery_id = delivery_id_for(ctx)
    seal_sha = str(verifier.get("seal_sha256", "unknown"))
    description = (
        f"**CI_STATUS:** `MATCH`\n"
        f"**CI_RUN_ID:** `{ctx['run_id']}`\n"
        f"**CI_HEAD:** `{ctx['head']}`\n"
        f"**ARTIFACT_ID:** `{ctx['artifact_id']}`\n"
        f"**ARTIFACT_DIGEST:** `{ctx['artifact_digest']}`\n"
        f"**VERIFIER_STDOUT_SHA256:** `{stdout_sha}`\n"
        f"**SOURCE_VERIFIER:** `GREEN`\n"
        f"**SEAL_SHA256:** `{seal_sha}`\n"
        f"**DELIVERY_ID:** `{delivery_id}`"
    )
    payload = {
        "allowed_mentions": {"parse": []},
        "embeds": [
            {
                "title": "✅ Atomic JOY — Verified CI Receipt",
                "description": description,
                "color": 5763719,
                "footer": {
                    "text": "🧾 CI artifact GREEN · delivery is presentation-only · NO_FAKE_GREEN"
                },
            }
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return payload, delivery_id, sha256_bytes(canonical)


def discord_post(payload: dict) -> tuple[str, str]:
    # Delivery credentials are intentionally resolved only here.
    token = required_env("DISCORD_TOKEN")
    channel_id = required_env("DISCORD_CHANNEL_ID")
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    body = json.dumps(payload, separators=(",", ":")).encode()
    request = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json",
            "User-Agent": "AtomicJOYDelivery/0.0.1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:500]
        fail(f"Discord HTTP {exc.code}: {detail}")
    except Exception as exc:
        fail(f"Discord delivery error: {exc}")
    if not isinstance(result, dict) or not result.get("id"):
        fail("Discord response missing message id")
    return channel_id, str(result["id"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_dir = Path(os.getenv("ATOMIC_JOY_INPUT_DIR", "artifacts/input"))
    output_dir = Path(
        os.getenv("ATOMIC_JOY_DELIVERY_DIR", "artifacts/atomic_joy/delivery")
    )
    ctx = source_context()
    verifier, stdout_sha = verify_source(input_dir, ctx)
    payload, delivery_id, payload_sha = build_payload(verifier, stdout_sha, ctx)

    if args.dry_run:
        proof = {
            "artifact_digest": ctx["artifact_digest"],
            "delivery_id": delivery_id,
            "payload": payload,
            "payload_sha256": payload_sha,
        }
        print(json.dumps(proof, sort_keys=True))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    intent = {
        "delivery_id": delivery_id,
        "head_sha": ctx["head"],
        "source_run_id": ctx["run_id"],
        "source_artifact_id": ctx["artifact_id"],
        "source_artifact_digest": ctx["artifact_digest"],
        "payload_sha256": payload_sha,
        "no_fake_green": True,
    }
    atomic_json(output_dir / "delivery_intent.json", intent)

    channel_id, message_id = discord_post(payload)
    receipt = {
        "original_digest": ctx["artifact_digest"],
        "delivery_id": delivery_id,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "channel_id": channel_id,
        "discord_message_id": message_id,
    }
    atomic_json(output_dir / "delivery_receipt.json", receipt)
    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
