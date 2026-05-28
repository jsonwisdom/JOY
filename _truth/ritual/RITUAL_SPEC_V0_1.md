# JOY Ritual Spec V0.1 🌈🧵

## Status

CANONICAL_DRAFT

## Purpose

Define how JOY acts.

This spec defines ritual classes, ritual outputs, and ritual invariants. It does not define ontology terms, witness truth conditions, governance rules, receipt schemas, or asset lifecycle expansion.

## Dependency Order

JOY actions must inherit from:

1. Ontology V0.1 — what exists
2. Witness Protocol V0.1 — how JOY knows
3. Ritual Spec V0.1 — how JOY acts

## Core Ritual

### SEVEN_STEP_LOCK

The standard JOY artifact ritual:

1. WITNESS_THE_ASSET
2. WEIGH_THE_THREAD_SHA256
3. BIND_THE_RECEIPT
4. ENTER_THE_MANIFEST
5. MARK_THE_LEDGER
6. COMMIT_TO_THE_LOOM
7. VERIFY_THE_REMOTE_WITNESS

## Ritual Classes

### ASSET_MINT_RITUAL

Creates a new badge instance or creative asset through the seven-step lock.

### RECOVERY_RITUAL

Restores missing or fractured lineage without rewriting history.

### CLOSEOUT_RITUAL

Marks an epoch, issue, recovery cycle, or artifact family as complete.

### ORACLE_RITUAL

Freezes a known-good baseline for future replay verification.

## Ritual Outputs

A valid ritual may produce:

- asset
- hash
- receipt
- manifest_delta
- ledger_entry
- commit
- replay_result

## Ritual Invariants

- ACTION_REQUIRES_WITNESS
- RITUAL_DOES_NOT_CREATE_AUTHORITY
- RECEIPT_BEFORE_CANON
- REMOTE_WITNESS_BEFORE_CLOSEOUT
- RECOVERY_DOES_NOT_REWRITE_HISTORY

## Boundary

Rituals produce evidence.

Rituals do not decide canon alone.

Canon requires successful witness confirmation and repository adoption.

## Closing

JOY acts through rituals only when action can be witnessed, replayed, and bound to receipts.
