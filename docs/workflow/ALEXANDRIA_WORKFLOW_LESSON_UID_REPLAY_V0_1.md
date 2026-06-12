# Alexandria Workflow Lesson — UID Replay V0.1

## Lesson

Do not discard workflow failures. Preserve them as operator doctrine when they reveal a reusable pattern.

This lesson was derived from the UID replay search sequence where an initial search used the wrong shape, then corrected into a useful replay pattern:

1. Search by vague artifact class.
2. Detect failure or weak result.
3. Reframe search around exact replay surfaces.
4. Extract candidate files.
5. Fetch file bodies.
6. Separate GitHub-observed claims from externally verified on-chain facts.
7. Preserve the boundary as a reusable workflow lesson.

## Name

**Alexandria Behavior**

Meaning: when the system learns a useful operating pattern, the pattern should be archived for reuse instead of lost in chat flow.

Alexandria is not authority. Alexandria is memory discipline.

## UID Replay Pattern

When asked to find schema UIDs, attestation UIDs, transaction hashes, or similar proof surfaces:

- Do not stop at repository discovery.
- Do not treat search-result paths as file contents.
- Search multiple spellings:
  - `schema uid`
  - `schema_uid`
  - `schemaUID`
  - `attestation_uid`
  - `transaction_hash`
- Prefer receipt-like paths:
  - `receipts/`
  - `replay_registry/`
  - `docs/epoch*/`
  - `schemas/`
- Fetch candidate file bodies before claiming a UID was found.
- Classify GitHub file contents as OBSERVED unless independently verified externally.

## Evidence Boundary

GitHub file exists: OBSERVED.

GitHub file claims UID/tx hash: OBSERVED CLAIM.

On-chain explorer or RPC confirms transaction/UID: VERIFIED.

Independent third-party replay confirms procedure and output: REPLAYABLE.

Never promote OBSERVED directly to VERIFIED or REPLAYABLE.

## Example Boundary

Allowed:

> GitHub file contains a claimed schema UID and transaction hash.

Not allowed:

> The schema is verified on-chain.

Unless an external Base/EAS replay has been performed and preserved.

## Operator Rule

When a bad search teaches a better search, preserve the better search as doctrine.

No fake green.
No authority.
No skipped ladder states.
