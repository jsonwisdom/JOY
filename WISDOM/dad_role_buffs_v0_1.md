# Dad Role Buffs V0.1

Status: ACTIVE
Authority: false
Family Barrier: INTACT
Dad Role: Receipt Machine With Love

## Purpose

Dad Role Buffs are funny, non-authority perks for Wisdom Family Game Night.

They help Dad participate, support the table, preserve receipts, and make people laugh without becoming the boss layer.

## Core Rule

```text
Dad may help.
Dad may record.
Dad may joke.
Dad may not overrule the family barrier.
Authority remains false.
```

## Principles

```json
{
  "authority": false,
  "dad_role": "receipt_machine_with_love",
  "family_barrier": "INTACT",
  "kids_agency": "PRESERVED",
  "mrs_wisdom_shield": "SUPERSEDES_DAD_BUFFS",
  "buffs": "funny_optional_non_authority"
}
```

## Buff Set V0.1

### 1. Dad Joke Critical Hit

Dad may tell one bad joke.

Effect:

```text
If everyone groans, the joke succeeds.
```

Limit:

```text
Dad may not explain the joke unless asked.
```

### 2. Receipt Wizard

Dad may write one memory note exactly as spoken.

Effect:

```text
One sentence enters the Replay Script.
```

Limit:

```text
No editing family voice.
```

### 3. Emergency Snack Summon

Dad may suggest snacks when energy drops.

Effect:

```text
Pause. Snack. Resume softer.
```

Limit:

```text
Mrs Wisdom may veto or upgrade snack protocol.
```

### 4. Rule Simplifier

Dad may reduce a confusing rule to one sentence.

Effect:

```text
Less confusion, more play.
```

Limit:

```text
The girls may reject the simplification.
```

### 5. Lore Keeper

Dad may ask: should we save this as family lore?

Effect:

```text
Creates a possible memory note.
```

Limit:

```text
Privacy choice controls everything.
```

### 6. Reroll One Family Rule

Dad may ask the table to rewrite one rule for fun.

Effect:

```text
Family gets agency over the game.
```

Limit:

```text
No rule may reduce safety, consent, or kindness.
```

### 7. Tiny Victory Announcer

Dad may celebrate a small win loudly but briefly.

Effect:

```text
Makes progress visible.
```

Limit:

```text
No teasing. No pressure. No scoreboard of worth.
```

### 8. Carry the Box

Dad handles setup and cleanup when possible.

Effect:

```text
The family gets more play with less friction.
```

Limit:

```text
This is service, not control.
```

## Supremacy Rule

Mrs Wisdom Shield Moves override Dad Role Buffs.

Kids agency overrides Dad Role Buffs.

Privacy Shield overrides Dad Role Buffs.

## Output Format

Use this format for optional Replay and Ledger surfaces:

```json
{
  "artifact": "DAD_ROLE_BUFFS_V0_1",
  "date": "YYYY-MM-DD",
  "buff_used": "",
  "effect": "",
  "memory_note": "",
  "privacy": "private | family-only | shareable",
  "authority": false
}
```

## Lock Line

```text
Dad supports the game.
Dad does not become the game.
The family keeps agency.
Mrs Wisdom keeps the cozy shield.
Authority remains false.
```
