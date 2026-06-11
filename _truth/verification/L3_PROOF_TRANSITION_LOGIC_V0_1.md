# L3 Proof Transition Logic V0.1

## Status

CANONICAL_DRAFT

## Purpose

Define the rulebook for determining whether an L3 runtime payload receipt is eligible to become a runtime proof.

This document does not create a proof.
This document does not execute runtime logic.
This document does not grant authority.

It defines the transition conditions only.

## Core Rule

A runtime payload receipt may become a runtime proof only if all required transition conditions are satisfied.

If any required condition is missing, ambiguous, or false, proof creation is blocked.

## Required Inputs

- L3 runtime payload receipt
- L3 proof transition evaluation
- CI runner evidence
- Repository-pinned receipt
- Explicit transition logic
- Human approval gate, when required

## Required Conditions

A runtime proof is eligible only when:

1. The runtime payload receipt is present.
2. The receipt is pinned in the repository.
3. The CI runner output is referenced.
4. The transition evaluation is present.
5. The transition logic exists.
6. The transition logic is satisfied.
7. No weaker local candidate conflicts with repo-pinned evidence.
8. No execution is inferred from preparation alone.
9. No authority is granted by receipt existence alone.
10. Human approval is present if the transition requires it.

## Blocking Conditions

Proof creation is blocked if:

- transition logic is absent
- CI output is missing
- receipt is local-only
- evaluation is missing
- execution was not performed
- authority would be inferred
- human approval is required but absent
- any evidence is ambiguous
- any candidate would create fake green

## Decision Outputs

The transition logic may produce only one of:

- PROOF_ELIGIBLE
- PROOF_BLOCKED
- NEEDS_HUMAN_APPROVAL
- NEEDS_REPLAY
- INVALID_INPUT

## Default Decision

If uncertainty exists, the decision is:

PROOF_BLOCKED

## Authority Rule

This logic grants no authority.

Authority remains false unless separately established by a valid, explicit, replayable authority artifact.

## No Fake Green Rule

No runtime proof may be created from:

- preparation
- intention
- local-only files
- unverified output
- implied execution
- missing transition logic

## Final Statement

Runner output is evidence.
Repository pinning preserves evidence.
Transition logic evaluates evidence.
Proof is created only after the transition gate passes.

No crown.
No authority jump.
No fake green.
