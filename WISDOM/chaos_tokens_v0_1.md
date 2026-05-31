# Chaos Tokens V0.1

Status: ACTIVE
Authority: false
Family Barrier: INTACT
Cozy Shield: ACTIVE
Chaos Absorption: ENABLED

## Purpose

Chaos Tokens turn wild family energy into safe game fuel.

They help Game Night stay playful when the room gets loud, silly, tired, distracted, hungry, or emotionally wobbly.

Chaos is not failure.

Chaos is a signal.

## Core Rule

```text
Absorb chaos.
Do not punish people.
Protect the cozy field.
Authority remains false.
```

## How to Use

At the start of Game Night, place 3 to 5 Chaos Tokens on the table.

Anyone may spend one when the room needs a reset, laugh, pause, snack, movement break, or privacy check.

Mrs. Wisdom may always activate Cozy Shield.

Dad may record only one sentence after the moment settles.

## Token Set

### 1. Mulligan Token

Use when someone wants a do-over.

Effect:

```text
Replay the turn without shame.
```

### 2. Dance Break Token

Use when bodies need to move.

Effect:

```text
30 seconds of movement. No scoring. No judging.
```

### 3. Cookie Token

Use when snack energy would improve the table.

Effect:

```text
Pause. Snack. Resume softer.
```

### 4. Wild Story Token

Use when someone wants to tell a silly or unexpected story.

Effect:

```text
Story gets the floor for one minute.
```

### 5. Ask Grandma Token

Use when a story, recipe, saying, or family memory needs elder wisdom.

Effect:

```text
Mark as FAMILY_FOLLOWUP. Ask later.
```

### 6. Dad Joke Override Token

Use when Dad makes a joke so bad it becomes part of the game.

Effect:

```text
Everyone may groan. Dad may not explain the joke.
```

### 7. Mrs. Wisdom Cozy Shield Token

Use when the game needs softness, safety, or lower stack pressure.

Effect:

```text
Reduce rules. Lower volume. Protect feelings. Continue only if cozy.
```

### 8. Privacy Shield Token

Use when someone is unsure whether a memory should be saved or shared.

Effect:

```text
Default to private.
```

## Output Format

Use this format for Replay and Ledger surfaces:

```json
{
  "artifact": "CHAOS_TOKENS_V0_1",
  "date": "YYYY-MM-DD",
  "token_used": "",
  "reason": "",
  "result": "",
  "privacy": "private | family-only | shareable",
  "memory_note": "",
  "authority": false
}
```

## Safety Rules

- Tokens are never used to shame someone.
- Tokens are never used to force sharing.
- Tokens are never used to score human worth.
- Tokens can pause the game.
- Tokens can end the game.
- Cozy beats completion.

## Replay Hook

If a token creates a memory worth saving, feed exactly one sentence into:

```text
GAME_NIGHT_REPLAY_SCRIPT_V0_1
```

If the moment should stay private, mark:

```text
PRIVATE_NOTE
```

## Lock Line

```text
Chaos becomes play.
Play becomes memory.
Memory stays protected.
The family stays human.
Authority remains false.
```
