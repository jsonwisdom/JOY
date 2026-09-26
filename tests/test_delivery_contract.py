#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "deliver_discord_receipt.py"
FIXTURE = Path(os.environ.get("ATOMIC_JOY_TEST_ARTIFACT_DIR", ROOT / "artifacts" / "known-good"))

HEAD = "71e437d2b4c3148033f62236932de3ce2476696b"
RUN_ID = "31176908693"
ARTIFACT_ID = "8993161146"
ARTIFACT_DIGEST = "sha256:ba0578b39372de5b92b00d6e33a2267bb6f9cba49c28a970402e4db669986cf1"
ARTIFACT_NAME = f"atomic-joy-runtime-{HEAD}"


def base_env(input_dir: Path) -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "ATOMIC_JOY_INPUT_DIR": str(input_dir),
            "ATOMIC_JOY_EXPECTED_HEAD": HEAD,
            "ATOMIC_JOY_EXPECTED_RUN_ID": RUN_ID,
            "ATOMIC_JOY_ARTIFACT_ID": ARTIFACT_ID,
            "ATOMIC_JOY_ARTIFACT_DIGEST": ARTIFACT_DIGEST,
        }
    )
    env.pop("DISCORD_TOKEN", None)
    env.pop("DISCORD_CHANNEL_ID", None)
    return env


def run_dry(input_dir: Path, env_override: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    env = base_env(input_dir)
    if env_override:
        env.update(env_override)
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run"],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def write_metadata(path: Path, **changes: object) -> None:
    metadata = {
        "head_sha": HEAD,
        "run_id": RUN_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_name": ARTIFACT_NAME,
        "artifact_digest": ARTIFACT_DIGEST,
    }
    metadata.update(changes)
    (path / "github_artifact_metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


class DeliveryContractTests(unittest.TestCase):
    def setUp(self) -> None:
        if not FIXTURE.is_dir():
            self.fail(f"known-good artifact fixture missing: {FIXTURE}")
        self.tmp = tempfile.TemporaryDirectory()
        self.input_dir = Path(self.tmp.name) / "input"
        shutil.copytree(FIXTURE, self.input_dir)
        write_metadata(self.input_dir)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_known_artifact_dry_run_without_discord_secrets(self) -> None:
        result = run_dry(self.input_dir)
        self.assertEqual(result.returncode, 0, result.stderr)
        proof = json.loads(result.stdout)
        self.assertEqual(proof["artifact_digest"], ARTIFACT_DIGEST)
        self.assertEqual(proof["payload"]["embeds"][0]["title"], "✅ Atomic JOY — Verified CI Receipt")
        self.assertIn(ARTIFACT_DIGEST, proof["payload"]["embeds"][0]["description"])

    def test_delivery_id_and_payload_are_deterministic(self) -> None:
        first = run_dry(self.input_dir)
        second = run_dry(self.input_dir)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        one = json.loads(first.stdout)
        two = json.loads(second.stdout)
        self.assertEqual(one["delivery_id"], two["delivery_id"])
        self.assertEqual(one["payload_sha256"], two["payload_sha256"])
        self.assertEqual(one["payload"], two["payload"])

    def assert_closed(self, expected_error: str) -> None:
        result = run_dry(self.input_dir)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ATOMIC_JOY_DELIVERY_FAILED", result.stderr)
        self.assertIn(expected_error, result.stderr)
        self.assertEqual(result.stdout, "")

    def test_wrong_head_fails_closed(self) -> None:
        write_metadata(self.input_dir, head_sha="0" * 40)
        self.assert_closed("metadata HEAD mismatch")

    def test_wrong_digest_fails_closed(self) -> None:
        write_metadata(self.input_dir, artifact_digest="sha256:" + "0" * 64)
        self.assert_closed("metadata digest mismatch")

    def test_missing_manifest_no_fake_green_fails_closed(self) -> None:
        manifest_path = self.input_dir / "receipt_manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["no_fake_green"] = False
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        self.assert_closed("source manifest lacks no_fake_green=true")

    def test_stored_verifier_not_green_fails_closed(self) -> None:
        verifier_path = self.input_dir / "verifier_stdout.json"
        verifier = json.loads(verifier_path.read_text(encoding="utf-8"))
        verifier["state"] = "YELLOW"
        verifier_path.write_text(json.dumps(verifier, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        self.assert_closed("stored verifier result is not GREEN")

    def test_tampered_verifier_bytes_fail_hash_binding(self) -> None:
        verifier_path = self.input_dir / "verifier_stdout.json"
        verifier_path.write_bytes(verifier_path.read_bytes() + b" ")
        self.assert_closed("verifier stdout digest mismatch")

    def test_receipt2_schema_is_exact(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        expected_keys = {
            "original_digest",
            "delivery_id",
            "timestamp",
            "channel_id",
            "discord_message_id",
        }
        marker = "receipt = {"
        start = source.index(marker)
        end = source.index("    }", start)
        receipt_block = source[start:end]
        for key in expected_keys:
            self.assertIn(f'"{key}"', receipt_block)
        forbidden = {
            "protocol",
            "version",
            "head_sha",
            "source_run_id",
            "source_artifact_id",
            "payload_sha256",
            "no_fake_green",
            "delivery_status",
        }
        for key in forbidden:
            self.assertNotIn(f'"{key}"', receipt_block)

    def test_discord_credentials_only_resolved_in_delivery_function(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        prefix, delivery = source.split("def discord_post(payload: dict)", 1)
        self.assertNotIn("DISCORD_TOKEN", prefix)
        self.assertNotIn("DISCORD_CHANNEL_ID", prefix)
        self.assertIn('required_env("DISCORD_TOKEN")', delivery)
        self.assertIn('required_env("DISCORD_CHANNEL_ID")', delivery)


if __name__ == "__main__":
    unittest.main(verbosity=2)
