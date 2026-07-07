# JOY to ReceiptOS Handoff v0.1

JOY emits semantic continuity artifacts. ReceiptOS judges canonical verification. AL remains blocked until verified state exists.

## Purpose

This handoff spec defines how `WISDOM/joy_root_candidate_001.json` leaves JOY as a candidate and enters the ReceiptOS verification domain without JOY claiming cryptographic truth.

## Status triad

```text
JOY_STATUS: CANDIDATE_DECLARED
RECEIPTOS_STATUS: PENDING
AL_STATUS: BLOCKED_UNTIL_VERIFIED
```

## Boundary

JOY may:

- Declare a semantic candidate.
- Link leaf qualification rules.
- Link manifest root protocol artifacts.
- Preserve a candidate pointer.
- Preserve `authority=false`, `execution=false`, and `verification=false`.

JOY must not:

- Compute or claim a verified Merkle root.
- Assert cryptographic truth.
- Trigger downstream automation.
- Promote a candidate into verified state.

ReceiptOS may:

- Ingest the candidate artifact.
- Reconstruct the referenced leaf set.
- Compute or reject a candidate Merkle root.
- Produce a verification receipt.

AL may:

- Consume only ReceiptOS-verified artifacts.
- Remain blocked while ReceiptOS status is pending.

## First handoff object

```text
WISDOM/joy_root_candidate_001.json
```

This object is a loving declaration and candidate pointer only. It is not a proof.

## No fake green

A JOY root candidate is not green. It is not verified. It is not executable. It is a clear invitation for ReceiptOS to judge.

The only valid terminal states after ReceiptOS review are:

```text
VERIFIED_BY_RECEIPTOS
REJECTED_BY_RECEIPTOS
```

Until then, the candidate remains:

```text
PENDING_RECEIPTOS_VERIFICATION
```
