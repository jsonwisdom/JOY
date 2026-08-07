# Atomic JOY Bot

Read-only verification and presentation layer for the sealed `ATOMIC_JOY_REFLECTION_PROTOCOL` v0.0.1.

## Truth states

- `GREEN` — every required Git, hash, schema, anchor, and immutability check passes.
- `YELLOW` — verification completes with non-fatal warnings.
- `RED` — a deterministic integrity check fails.
- `GRAY` — verification cannot be completed from the available source/runtime.

`NO_FAKE_GREEN` is enforced: missing dependencies, missing historical commits, malformed JSON, timeouts, and unexpected verifier failures can never produce `GREEN`.

## Install

```bash
python -m pip install -r bot/requirements.txt
```

## Verify from the CLI

```bash
python bot/atomic_joy_verify.py --json
python bot/atomic_joy_verify.py
```

The verifier is read-only. It checks the frozen Commit A/B/C receipts, exact schema and manifest bytes, RFC 8785 seal recipe, two-phase anchor, `REFLECTION_0001` content/receipt immutability, and the declared JAY `3 / 6 / 9` author mark (`cryptographic_signature=false`).

## Discord

Set a bot token in the environment:

```bash
export DISCORD_TOKEN="..."
python -m bot.discord_bot
```

Commands:

- `!seal`
- `!status`
- `/verify`

Prefix commands require the **Message Content Intent** to be enabled for the Discord application. Slash commands do not rely on prefix parsing.

The Discord adapter contains no seal-verification logic. It spawns `atomic_joy_verify.py --json` as a subprocess and renders only the truth state returned by that core.
