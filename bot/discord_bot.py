#!/usr/bin/env python3
"""Discord presentation adapter for the Atomic JOY read-only verifier."""

from __future__ import annotations

import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands

CORE_SCRIPT = Path(__file__).with_name("atomic_joy_verify.py")
REPO_ROOT = Path(__file__).resolve().parents[1]
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

GITHUB_REPOSITORY = os.getenv("ATOMIC_JOY_GITHUB_REPOSITORY", "jsonwisdom/JOY")
GITHUB_WORKFLOW_FILE = os.getenv("ATOMIC_JOY_WORKFLOW_FILE", "atomic-joy-verify.yml")
GITHUB_TOKEN = os.getenv("ATOMIC_JOY_GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")
CI_CACHE_SECONDS = float(os.getenv("ATOMIC_JOY_CI_CACHE_SECONDS", "60"))
CI_TIMEOUT_SECONDS = float(os.getenv("ATOMIC_JOY_CI_TIMEOUT_SECONDS", "10"))

ALLOWED_STATES = {"GREEN", "YELLOW", "RED", "GRAY"}
COLOR_MAP = {
    "GREEN": discord.Color.green(),
    "YELLOW": discord.Color.gold(),
    "RED": discord.Color.red(),
    "GRAY": discord.Color.light_gray(),
}
EMOJI_MAP = {"GREEN": "✅", "YELLOW": "⚠️", "RED": "❌", "GRAY": "⚪"}
CI_EMOJI_MAP = {
    "MATCH": "🧾",
    "PENDING": "⏳",
    "STALE": "🕰️",
    "FAIL": "❌",
    "MISMATCH": "🚫",
    "UNAVAILABLE": "⚪",
}

_ci_cache: dict[str, tuple[float, dict[str, Any]]] = {}


def gray_result(message: str, **details: Any) -> dict[str, Any]:
    return {
        "state": "GRAY",
        "seal_sha256": "unknown",
        "schema_sealed": False,
        "reflection_id": "REFLECTION_0001",
        "reflection_status": "unknown",
        "no_fake_green": True,
        "errors": [message],
        "details": details,
    }


def normalize_result(data: Any, returncode: int, stderr: str) -> dict[str, Any]:
    if not isinstance(data, dict):
        return gray_result("Verifier JSON root is not an object")

    state = data.get("state")
    if state not in ALLOWED_STATES:
        return gray_result(f"Verifier returned invalid state: {state!r}")

    errors = data.get("errors")
    if not isinstance(errors, list):
        errors = ["Verifier returned malformed errors field"]
    errors = [str(item) for item in errors]

    if state == "GREEN" and returncode != 0:
        return gray_result(
            f"Verifier reported GREEN but exited with code {returncode}",
            stderr=stderr[:1000],
        )

    data["errors"] = errors
    data.setdefault("seal_sha256", "unknown")
    data.setdefault("schema_sealed", False)
    data.setdefault("reflection_id", "REFLECTION_0001")
    data.setdefault("reflection_status", "unknown")
    data.setdefault("no_fake_green", True)
    details = data.setdefault("details", {})
    if isinstance(details, dict):
        details["core_exit_code"] = returncode
        if stderr:
            details["core_stderr"] = stderr[:1000]
    return data


async def run_verifier(timeout: float = 15.0) -> dict[str, Any]:
    """Spawn the verifier as an isolated subprocess and parse its JSON contract."""
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            str(CORE_SCRIPT),
            "--json",
            "--repo",
            str(REPO_ROOT),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout_b, stderr_b = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return gray_result(f"Verification timed out after {timeout:.0f}s")
    except (OSError, RuntimeError) as exc:
        return gray_result(f"Unable to start verifier subprocess: {exc}")

    stdout = stdout_b.decode("utf-8", errors="replace")
    stderr = stderr_b.decode("utf-8", errors="replace").strip()
    try:
        parsed = json.loads(stdout)
    except json.JSONDecodeError as exc:
        return gray_result(
            f"Invalid JSON from verifier: {exc}",
            raw_output=stdout[:1000],
            stderr=stderr[:1000],
            core_exit_code=proc.returncode,
        )
    return normalize_result(parsed, proc.returncode or 0, stderr)


def ci_result(status: str, message: str = "", **details: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"status": status, "message": message}
    result.update(details)
    return result


def _github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "atomic-joy-discord-consumer/0.0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


async def fetch_ci_receipt(local_result: dict[str, Any]) -> dict[str, Any]:
    """Read latest Actions receipt metadata for presentation-only corroboration.

    The local verifier is authoritative. CI metadata can corroborate it, but can
    never upgrade RED/YELLOW/GRAY to GREEN and never writes repository state.
    """
    local_head = local_result.get("details", {}).get("head")
    if not isinstance(local_head, str) or len(local_head) != 40:
        return ci_result("UNAVAILABLE", "Local verifier did not provide a usable HEAD SHA")

    cached = _ci_cache.get(local_head)
    now = time.monotonic()
    if cached and now - cached[0] < CI_CACHE_SECONDS:
        return dict(cached[1])

    base = f"https://api.github.com/repos/{GITHUB_REPOSITORY}"
    runs_url = f"{base}/actions/workflows/{GITHUB_WORKFLOW_FILE}/runs"
    timeout = aiohttp.ClientTimeout(total=CI_TIMEOUT_SECONDS)

    try:
        async with aiohttp.ClientSession(headers=_github_headers(), timeout=timeout) as session:
            async with session.get(
                runs_url,
                params={
                    "branch": "main",
                    "event": "push",
                    "status": "completed",
                    "per_page": "5",
                },
            ) as response:
                if response.status != 200:
                    result = ci_result(
                        "UNAVAILABLE",
                        f"GitHub Actions runs API returned HTTP {response.status}",
                    )
                    _ci_cache[local_head] = (now, result)
                    return result
                payload = await response.json()

            runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
            if not isinstance(runs, list) or not runs:
                result = ci_result("PENDING", "No completed main-push CI run is available yet")
                _ci_cache[local_head] = (now, result)
                return result

            run = runs[0]
            run_id = run.get("id")
            run_head = run.get("head_sha")
            conclusion = run.get("conclusion")
            run_url = run.get("html_url")

            if run_head != local_head:
                result = ci_result(
                    "STALE",
                    "Latest completed CI receipt is for a different HEAD",
                    run_id=run_id,
                    head_sha=run_head,
                    local_head=local_head,
                    run_url=run_url,
                )
                _ci_cache[local_head] = (now, result)
                return result

            if conclusion != "success":
                result = ci_result(
                    "FAIL",
                    f"Latest CI run for this HEAD concluded {conclusion!r}",
                    run_id=run_id,
                    head_sha=run_head,
                    run_url=run_url,
                )
                _ci_cache[local_head] = (now, result)
                return result

            artifacts_url = f"{base}/actions/runs/{run_id}/artifacts"
            async with session.get(artifacts_url, params={"per_page": "100"}) as response:
                if response.status != 200:
                    result = ci_result(
                        "UNAVAILABLE",
                        f"GitHub artifacts API returned HTTP {response.status}",
                        run_id=run_id,
                        head_sha=run_head,
                    )
                    _ci_cache[local_head] = (now, result)
                    return result
                artifact_payload = await response.json()

    except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
        result = ci_result("UNAVAILABLE", f"GitHub CI corroboration unavailable: {exc}")
        _ci_cache[local_head] = (now, result)
        return result

    artifacts = artifact_payload.get("artifacts") if isinstance(artifact_payload, dict) else None
    expected_name = f"atomic-joy-runtime-{local_head}"
    matches = [
        item
        for item in artifacts or []
        if isinstance(item, dict)
        and item.get("name") == expected_name
        and item.get("expired") is False
    ]
    if len(matches) != 1:
        result = ci_result(
            "MISMATCH",
            f"Expected one unexpired artifact named {expected_name!r}",
            run_id=run_id,
            head_sha=run_head,
            artifact_count=len(matches),
            run_url=run_url,
        )
        _ci_cache[local_head] = (now, result)
        return result

    artifact = matches[0]
    result = ci_result(
        "MATCH",
        "Latest completed main-push CI run and receipt artifact match local HEAD",
        run_id=run_id,
        head_sha=run_head,
        run_url=run_url,
        artifact_id=artifact.get("id"),
        artifact_name=artifact.get("name"),
        artifact_digest=artifact.get("digest"),
    )
    _ci_cache[local_head] = (now, result)
    return dict(result)


async def truth_snapshot() -> tuple[dict[str, Any], dict[str, Any], str]:
    local_result = await run_verifier()
    ci = await fetch_ci_receipt(local_result)
    local_state = local_result.get("state", "GRAY")

    if local_state != "GREEN":
        display_state = local_state
    elif ci.get("status") == "MATCH":
        display_state = "GREEN"
    else:
        # Presentation confidence degrades, but Discord does not alter verifier truth.
        display_state = "YELLOW"

    return local_result, ci, display_state


def state_color(state: str) -> discord.Color:
    return COLOR_MAP.get(state, COLOR_MAP["GRAY"])


def state_emoji(state: str) -> str:
    return EMOJI_MAP.get(state, EMOJI_MAP["GRAY"])


def ci_emoji(status: str) -> str:
    return CI_EMOJI_MAP.get(status, "⚪")


def add_issue_field(embed: discord.Embed, result: dict[str, Any], limit: int = 5) -> None:
    issues = [str(x) for x in result.get("errors", [])]
    if issues:
        text = "\n".join(f"• {item}" for item in issues[:limit])
        embed.add_field(name="Verifier Errors / Warnings", value=text[:1024], inline=False)


def add_ci_field(embed: discord.Embed, ci: dict[str, Any], full: bool = False) -> None:
    status = str(ci.get("status", "UNAVAILABLE"))
    lines = [
        f"**Status:** {ci_emoji(status)} `{status}`",
        f"**Message:** {ci.get('message', 'none')}",
    ]
    if ci.get("run_id") is not None:
        lines.append(f"**Run:** `{ci.get('run_id')}`")
    if ci.get("head_sha"):
        lines.append(f"**HEAD:** `{ci.get('head_sha')}`")
    if full and ci.get("artifact_id") is not None:
        lines.append(f"**Artifact:** `{ci.get('artifact_id')}`")
    if full and ci.get("artifact_digest"):
        lines.append(f"**Artifact digest:** `{ci.get('artifact_digest')}`")
    embed.add_field(
        name="GitHub Actions Corroboration",
        value="\n".join(lines)[:1024],
        inline=False,
    )


def apply_no_fake_green_footer(
    embed: discord.Embed,
    verifier_state: str,
    ci_status: str,
    display_state: str,
) -> None:
    if verifier_state != "GREEN":
        embed.set_footer(text="🚫 NO_FAKE_GREEN — local verifier is not GREEN")
    elif ci_status != "MATCH":
        embed.set_footer(
            text=f"⚠️ Local verifier GREEN · CI {ci_status} · presentation degraded to {display_state}"
        )
    else:
        embed.set_footer(
            text="🧾 Local verifier GREEN · CI receipt MATCH · Discord is presentation-only"
        )


class AtomicJoyBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.tree.sync()


intents = discord.Intents.default()
intents.message_content = True
bot = AtomicJoyBot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {getattr(bot.user, 'id', 'unknown')})")


@bot.command(name="seal")
async def seal_command(ctx: commands.Context) -> None:
    async with ctx.typing():
        result, ci, display_state = await truth_snapshot()
    verifier_state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(display_state)} Atomic JOY v0.0.1 — Seal Verification",
        color=state_color(display_state),
        description=(
            f"**Verifier:** `{verifier_state}`\n"
            f"**Seal SHA256:** `{result.get('seal_sha256', 'unknown')}`"
        ),
    )
    add_ci_field(embed, ci)
    add_issue_field(embed, result)
    apply_no_fake_green_footer(
        embed, verifier_state, str(ci.get("status", "UNAVAILABLE")), display_state
    )
    await ctx.send(embed=embed)


@bot.command(name="status")
async def status_command(ctx: commands.Context) -> None:
    async with ctx.typing():
        result, ci, display_state = await truth_snapshot()
    verifier_state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(display_state)} Atomic JOY Status",
        color=state_color(display_state),
    )
    embed.add_field(name="Protocol", value=f"`{result.get('protocol', 'unknown')}`", inline=False)
    embed.add_field(name="Version", value=f"`{result.get('version', 'unknown')}`", inline=True)
    embed.add_field(name="Verifier", value=f"`{verifier_state}`", inline=True)
    embed.add_field(
        name="Schema Sealed",
        value=f"`{str(result.get('schema_sealed', False)).upper()}`",
        inline=True,
    )
    embed.add_field(name="Seal SHA256", value=f"`{result.get('seal_sha256', 'unknown')}`", inline=False)
    embed.add_field(
        name="Reflection",
        value=f"`{result.get('reflection_id', 'unknown')} ({result.get('reflection_status', 'unknown')})`",
        inline=False,
    )
    add_ci_field(embed, ci)
    add_issue_field(embed, result)
    apply_no_fake_green_footer(
        embed, verifier_state, str(ci.get("status", "UNAVAILABLE")), display_state
    )
    await ctx.send(embed=embed)


@bot.command(name="receipt")
async def receipt_command(ctx: commands.Context) -> None:
    async with ctx.typing():
        result, ci, display_state = await truth_snapshot()
    verifier_state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{ci_emoji(str(ci.get('status', 'UNAVAILABLE')))} Atomic JOY CI Receipt",
        color=state_color(display_state),
    )
    add_ci_field(embed, ci, full=True)
    embed.add_field(
        name="Local verifier",
        value=f"`{verifier_state}` · `{result.get('seal_sha256', 'unknown')}`",
        inline=False,
    )
    apply_no_fake_green_footer(
        embed, verifier_state, str(ci.get("status", "UNAVAILABLE")), display_state
    )
    await ctx.send(embed=embed)


@bot.tree.command(name="verify", description="Verify the sealed Atomic JOY v0.0.1 receipts")
@app_commands.describe(full="Show verifier issues and CI receipt details")
async def verify_slash(interaction: discord.Interaction, full: bool = False) -> None:
    await interaction.response.defer(thinking=True)
    result, ci, display_state = await truth_snapshot()
    verifier_state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(display_state)} Atomic JOY v0.0.1 — Verification",
        color=state_color(display_state),
    )
    embed.add_field(name="Verifier", value=f"`{verifier_state}`", inline=True)
    embed.add_field(
        name="Schema Sealed",
        value=f"`{str(result.get('schema_sealed', False)).upper()}`",
        inline=True,
    )
    embed.add_field(name="Seal SHA256", value=f"`{result.get('seal_sha256', 'unknown')}`", inline=False)

    issues = result.get("errors", [])
    if issues and full:
        add_issue_field(embed, result, limit=10)
    elif issues:
        embed.add_field(
            name="Issues",
            value=f"{len(issues)} issue(s). Use `/verify full:True` for details.",
            inline=False,
        )

    if full:
        checks = result.get("details", {}).get("checks", {})
        if isinstance(checks, dict):
            passed = sum(1 for ok in checks.values() if ok is True)
            total = len(checks)
            embed.add_field(name="Verifier Checks", value=f"`{passed}/{total}` passed", inline=True)

    add_ci_field(embed, ci, full=full)
    apply_no_fake_green_footer(
        embed, verifier_state, str(ci.get("status", "UNAVAILABLE")), display_state
    )
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="receipt", description="Show the latest Atomic JOY CI receipt metadata")
async def receipt_slash(interaction: discord.Interaction) -> None:
    await interaction.response.defer(thinking=True)
    result, ci, display_state = await truth_snapshot()
    verifier_state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{ci_emoji(str(ci.get('status', 'UNAVAILABLE')))} Atomic JOY CI Receipt",
        color=state_color(display_state),
    )
    add_ci_field(embed, ci, full=True)
    embed.add_field(
        name="Local verifier",
        value=f"`{verifier_state}` · `{result.get('seal_sha256', 'unknown')}`",
        inline=False,
    )
    apply_no_fake_green_footer(
        embed, verifier_state, str(ci.get("status", "UNAVAILABLE")), display_state
    )
    await interaction.followup.send(embed=embed)


def main() -> None:
    if not DISCORD_TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable is not set")
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
