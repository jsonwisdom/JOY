# ATOMIC_JOY_RUNTIME_MIGRATION_CONTRACT

VERSION = 0.0.1-EXPERIMENTAL
STATUS = CANONICAL_MIGRATION_SPEC

## Authority boundary

- SOURCE_OF_TRUTH = VERIFIED_GITHUB_ARTIFACT
- DELIVERY_LAYER = PRESENTATION_ONLY
- DELIVERY_MAY_REVALIDATE = FALSE
- ORIGINAL_DIGEST_REQUIRED = TRUE
- TRANSFORMATION = DETERMINISTIC
- FALSE_GREEN_ALLOWED = FALSE

The delivery service MAY verify transport/provenance invariants (run id, HEAD, artifact identity, manifest hash binding, stored GREEN result). It MUST NOT rerun or independently reproduce eligibility logic.

## Fail-closed behavior

- AUTH_FAILURE = DELIVERY_FAILED
- ARTIFACT_MISSING = NO_OUTPUT
- DIGEST_MISMATCH = NO_OUTPUT
- NETWORK_FAILURE = NO_OUTPUT
- PROVENANCE_FAILURE = NO_OUTPUT
- MALFORMED_ARTIFACT = NO_OUTPUT

No failure state may emit a GREEN receipt.

## Two-receipt architecture

Receipt 1: CI artifact receipt. Proves eligibility and binds HEAD, verifier stdout bytes, run id, and artifact identity.

Receipt 2: Delivery receipt. Proves the exact source digest presented, destination channel, Discord message id, payload hash, delivery id, and timestamp. Delivery receipts are append-only artifacts and never alter Receipt 1.

## Runtime state machine

FETCH -> VERIFY_PROVENANCE -> BUILD_DETERMINISTIC_PAYLOAD -> DELIVER -> RECORD

Any failure enters DELIVERY_FAILED and emits no success receipt.

## Delivery/record boundary

Discord and GitHub Actions do not provide a distributed transaction. Therefore strict all-or-nothing atomicity across the Discord API and receipt storage is impossible.

The implementation compensates by:

1. creating a deterministic delivery_id before network delivery;
2. embedding delivery_id and original artifact digest in the Discord payload;
3. writing a pre-delivery intent receipt before POST;
4. writing the final delivery receipt atomically after Discord returns a message id;
5. failing the workflow if final recording fails;
6. never treating an unrecorded delivery as audited success.

This preserves detectability without pretending external APIs provide transactional semantics.
