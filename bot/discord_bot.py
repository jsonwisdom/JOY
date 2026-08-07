#!/usr/bin/env python3
"""Discord presentation adapter for the Atomic JOY read-only verifier."""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any

import discord
from discord import app_commands
from discord.ext import commands

CORE_SCRIPT = Path(__file__).with_name("atomic_joy_verify.py")
REPO_ROOT = Path(__file__).resolve().parents[1]
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

ALLOWED_STATES = {"GREEN", "YELLOW", "RED", "GRAY"}
COLOR_MAP = {
    "GREEN": discord.Color.green(),
    "YELLOW": discord.Color.gold(),
    "RED": discord.Color.red(),
    "GRAY": discord.Color.light_gray(),
}
EMOJI_MAP = {"GREEN": "✅", "YELLOW": "⚠️", "RED": "❌", "GRAY": "⚪"}


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


def state_color(state: str) -> discord.Color:
    return COLOR_MAP.get(state, COLOR_MAP["GRAY"])


def state_emoji(state: str) -> str:
    return EMOJI_MAP.get(state, EMOJI_MAP["GRAY"])


def add_issue_field(embed: discord.Embed, result: dict[str, Any], limit: int = 5) -> None:
    issues = [str(x) for x in result.get("errors", [])]
    if issues:
        text = "\n".join(f"• {item}" for item in issues[:limit])
        embed.add_field(name="Errors / Warnings", value=text[:1024], inline=False)


def apply_no_fake_green_footer(embed: discord.Embed, state: str) -> None:
    if state != "GREEN":
        embed.set_footer(text="🚫 NO_FAKE_GREEN — verification is not GREEN")
    else:
        embed.set_footer(text="🧾 NO_FAKE_GREEN — every required check passed")


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
        result = await run_verifier()
    state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(state)} Atomic JOY v0.0.1 — Seal Verification",
        color=state_color(state),
        description=(
            f"**State:** `{state}`\n"
            f"**Seal SHA256:** `{result.get('seal_sha256', 'unknown')}`"
        ),
    )
    add_issue_field(embed, result)
    apply_no_fake_green_footer(embed, state)
    await ctx.send(embed=embed)


@bot.command(name="status")
async def status_command(ctx: commands.Context) -> None:
    async with ctx.typing():
        result = await run_verifier()
    state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(state)} Atomic JOY Status",
        color=state_color(state),
    )
    embed.add_field(name="Protocol", value=f"`{result.get('protocol', 'unknown')}`", inline=False)
    embed.add_field(name="Version", value=f"`{result.get('version', 'unknown')}`", inline=True)
    embed.add_field(name="Verification", value=f"`{state}`", inline=True)
    embed.add_field(name="Schema Sealed", value=f"`{str(result.get('schema_sealed', False)).upper()}`", inline=True)
    embed.add_field(name="Seal SHA256", value=f"`{result.get('seal_sha256', 'unknown')}`", inline=False)
    embed.add_field(
        name="Reflection",
        value=f"`{result.get('reflection_id', 'unknown')} ({result.get('reflection_status', 'unknown')})`",
        inline=False,
    )
    add_issue_field(embed, result)
    apply_no_fake_green_footer(embed, state)
    await ctx.send(embed=embed)


@bot.tree.command(name="verify", description="Verify the sealed Atomic JOY v0.0.1 receipts")
@app_commands.describe(full="Show verifier issues and a compact audit summary")
async def verify_slash(interaction: discord.Interaction, full: bool = False) -> None:
    await interaction.response.defer(thinking=True)
    result = await run_verifier()
    state = result.get("state", "GRAY")
    embed = discord.Embed(
        title=f"{state_emoji(state)} Atomic JOY v0.0.1 — Verification",
        color=state_color(state),
    )
    embed.add_field(name="State", value=f"`{state}`", inline=True)
    embed.add_field(name="Schema Sealed", value=f"`{str(result.get('schema_sealed', False)).upper()}`", inline=True)
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
            embed.add_field(name="Audit Checks", value=f"`{passed}/{total}` passed", inline=True)

    apply_no_fake_green_footer(embed, state)
    await interaction.followup.send(embed=embed)


def main() -> None:
    if not DISCORD_TOKEN:
        raise RuntimeError("DISCORD_TOKEN environment variable is not set")
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
