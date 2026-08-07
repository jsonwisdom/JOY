#!/usr/bin/env python3
"""Machine eligibility gate for Atomic JOY Discord consumption.

Fail-closed. No live Discord connection is required. This proves only that the
current checkout is eligible for a GREEN Discord presentation; it does not prove
that a Discord process is running or that a human-visible embed was emitted.

Exit 0 requires:
  LOCAL_STATE      == GREEN
  DISPLAY_STATE    == GREEN
  LOCAL_HEAD       == dynamically derived HEAD (or ATOMIC_JOY_EXPECTED_HEAD)
  CI_STATUS        == MATCH
  CI_HEAD          == LOCAL_HEAD
  CI_RUN_ID        present
  ARTIFACT_ID      present
  ARTIFACT_NAME    == atomic-joy-runtime-<HEAD>
  ARTIFACT_DIGEST  == sha256:<64 lowercase hex>
  NO_FAKE_GREEN    == TRUE

CORE_ELIGIBILITY != END_TO_END_DISCORD
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from bot.discord_bot import truth_snapshot  # noqa: E402

HEAD_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


def current_head() -> str:
    """Return the expected checkout HEAD, optionally pinned by the operator."""
    override = os.getenv("ATOMIC_JOY_EXPECTED_HEAD")
    if override:
        return override.strip()

    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def collect_failures(
    local: dict[str, Any],
    ci: dict[str, Any],
    display: str,
    expected_head: str,
) -> list[str]:
    failures: list[str] = []

    details = local.get("details")
    local_head = details.get("head") if isinstance(details, dict) else None
    local_state = local.get("state")
    ci_status = ci.get("status")
    ci_head = ci.get("head_sha")
    artifact_name = ci.get("artifact_name")
    artifact_digest = ci.get("artifact_digest")

    if not HEAD_RE.fullmatch(expected_head):
        failures.append(f"EXPECTED_HEAD shape invalid: {expected_head!r}")
    if local_state != "GREEN":
        failures.append(f"LOCAL_STATE={local_state!r} (expected GREEN)")
    if display != "GREEN":
        failures.append(f"DISPLAY_STATE={display!r} (expected GREEN)")
    if local_head != expected_head:
        failures.append(f"LOCAL_HEAD={local_head!r} != expected {expected_head!r}")
    if ci_status != "MATCH":
        failures.append(f"CI_STATUS={ci_status!r} — {ci.get('message')}")
    if ci_head != expected_head:
        failures.append(f"CI_HEAD={ci_head!r} != expected {expected_head!r}")
    if ci.get("run_id") is None:
        failures.append("CI_RUN_ID missing")
    if ci.get("artifact_id") is None:
        failures.append("ARTIFACT_ID missing")
    if artifact_name != f"atomic-joy-runtime-{expected_head}":
        failures.append(f"ARTIFACT_NAME={artifact_name!r}")
    if not isinstance(artifact_digest, str) or not DIGEST_RE.fullmatch(artifact_digest):
        failures.append(f"ARTIFACT_DIGEST shape invalid: {artifact_digest!r}")

    if local.get("no_fake_green") is not True:
        failures.append(f"LOCAL_NO_FAKE_GREEN={local.get('no_fake_green')!r} (expected True)")
    if local_state != "GREEN" and display == "GREEN":
        failures.append("NO_FAKE_GREEN violation: non-GREEN local produced GREEN display")

    return failures


def emit_preflight_failure(message: str) -> int:
    receipt = {
        "ARTIFACT_DIGEST": None,
        "ARTIFACT_ID": None,
        "ARTIFACT_NAME": None,
        "CI_HEAD": None,
        "CI_RUN_ID": None,
        "CI_STATUS": "UNAVAILABLE",
        "CORE_ELIGIBILITY": "FAILED",
        "DISPLAY_STATE": None,
        "EXIT_CODE": 1,
        "FAILURES": [message],
        "LOCAL_HEAD": None,
        "LOCAL_STATE": None,
        "NO_FAKE_GREEN": True,
        "NOTE": (
            "CORE_ELIGIBILITY != END_TO_END_DISCORD. "
            "Live Discord presentation remains human-observed."
        ),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 1


async def main() -> int:
    try:
        expected = current_head()
    except (OSError, subprocess.SubprocessError) as exc:
        return emit_preflight_failure(f"Unable to resolve expected HEAD: {exc}")

    try:
        local, ci, display = await truth_snapshot()
    except Exception as exc:  # fail closed at the gate boundary
        return emit_preflight_failure(f"truth_snapshot failed: {type(exc).__name__}: {exc}")

    failures = collect_failures(local, ci, display, expected)
    details = local.get("details")
    local_head = details.get("head") if isinstance(details, dict) else None

    receipt = {
        "ARTIFACT_DIGEST": ci.get("artifact_digest"),
        "ARTIFACT_ID": ci.get("artifact_id"),
        "ARTIFACT_NAME": ci.get("artifact_name"),
        "CI_HEAD": ci.get("head_sha"),
        "CI_RUN_ID": ci.get("run_id"),
        "CI_STATUS": ci.get("status"),
        "CORE_ELIGIBILITY": "CONFIRMED" if not failures else "FAILED",
        "DISPLAY_STATE": display,
        "EXIT_CODE": 0 if not failures else 1,
        "FAILURES": failures,
        "LOCAL_HEAD": local_head,
        "LOCAL_STATE": local.get("state"),
        "NO_FAKE_GREEN": local.get("no_fake_green") is True,
        "NOTE": (
            "CORE_ELIGIBILITY != END_TO_END_DISCORD. "
            "Live Discord presentation remains human-observed."
        ),
    }

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
