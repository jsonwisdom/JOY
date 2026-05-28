# JOY Witness Protocol V0.1 🌈🧾

## Status

CANONICAL_DRAFT

## Purpose

Define how JOY knows.

This protocol defines witness classes, witness states, and witness invariants. It does not define rituals, governance rules, receipt schemas, or asset lifecycle rules.

## Boundary

Observation is not confirmation. Confirmation is not canon.

## Witness Classes

### LOCAL_WITNESS

Observes local repository state.

### REMOTE_WITNESS

Observes GitHub remote state.

### ORACLE_WITNESS

Observes known-good baseline state.

### REPLAY_WITNESS

Observes deterministic reconstruction.

### RECOVERY_WITNESS

Observes continuity repair events.

## Witness States

### OBSERVED

Something was seen.

### CONFIRMED

Something matched rules.

### REJECTED

Something failed rules.

### DRIFT_DETECTED

Something diverged from expected state.

### RECOVERY_VERIFIED

A repair event was confirmed without rewriting history.

## Witness Invariants

- OBSERVATION_IS_NOT_CONFIRMATION
- CONFIRMATION_IS_NOT_CANON
- RECOVERY_DOES_NOT_REWRITE_HISTORY

## Closing

JOY witnesses do not create authority.

They classify evidence so replay can decide what is admissible.
