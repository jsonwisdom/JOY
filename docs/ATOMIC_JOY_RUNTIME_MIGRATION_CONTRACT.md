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

Receipt 2: Delivery receipt. Proves presentation only and contains exactly:

- `original_digest`
- `delivery_id`
- `timestamp`
- `channel_id`
- `discord_message_id`

Receipt 2 never alters or upgrades Receipt 1 authority.

## Runtime state machine

FETCH -> VERIFY_PROVENANCE -> BUILD_DETERMINISTIC_PAYLOAD -> DELIVER -> RECORD

Any failure enters DELIVERY_FAILED and emits no success receipt.

## Delivery/record boundary

Discord and GitHub Actions do not provide a distributed transaction. Therefore strict all-or-nothing atomicity across the Discord API and receipt storage is impossible.

The implementation compensates by:

1. creating a deterministic delivery_id before network delivery;
2. embedding delivery_id and original artifact digest in the Discord payload;
3. writing a pre-delivery intent before POST;
4. writing the final delivery receipt atomically after Discord returns a message id;
5. failing the workflow if final recording fails;
6. never treating an unrecorded delivery as audited success.

This preserves detectability without pretending external APIs provide transactional semantics.

## Secret boundary

Discord credentials are resolved only inside the network delivery function. Artifact verification, provenance checks, deterministic payload construction, and `--dry-run` execute without Discord credentials.

## Pre-merge proof gate

Known-good fixture:

- HEAD: `71e437d2b4c3148033f62236932de3ce2476696b`
- Run: `31176908693`
- Artifact: `8993161146`
- Artifact digest: `sha256:ba0578b39372de5b92b00d6e33a2267bb6f9cba49c28a970402e4db669986cf1`
- Stored verifier stdout SHA256: `c947b6d7fb8759c250a8fcedb5810edcb7111bd5db87e4a62a9647095d76de31`
- Seal SHA256: `f422886213bf194be858f81c63414a563ccac72838255f26b9686ec98ab67da8`

GitHub Actions run `31180955202`, job `92873832412`, completed successfully on PR #70. It downloaded artifact `8993161146`, confirmed the GitHub digest, and passed 9/9 contract tests:

1. known-artifact dry-run without Discord secrets
2. deterministic delivery_id and payload
3. Discord credentials resolved only at delivery time
4. missing `no_fake_green` fails closed
5. exact Receipt 2 schema
6. non-GREEN stored verifier fails closed
7. tampered verifier bytes fail stdout-hash binding
8. wrong artifact digest fails closed
9. wrong HEAD fails closed

PRE_MERGE_CONTRACT_TEST = GREEN
RUNTIME_DISCORD_DELIVERY_PROVEN = FALSE
MERGE_AUTHORIZED = FALSE

## Gate 2 attempt 001

- PR branch commit: `e854a0eba69d57d5e0011421532f747532d0c30c`
- Workflow run: `31181214701`
- Job: `92874678377`
- Known artifact download: PASS
- GitHub source binding: PASS
- Gate 1 contract tests immediately before side effect: 9/9 PASS
- `ATOMIC_JOY_DISCORD_TOKEN` available to GitHub Actions: FALSE
- `ATOMIC_JOY_DISCORD_CHANNEL_ID` available to GitHub Actions: FALSE
- Discord POST attempted: FALSE
- Receipt 2 created: FALSE
- Delivery artifact created: FALSE
- Partial delivery possible from this attempt: FALSE
- Outcome: `DELIVERY_FAILED_PRE_SIDE_EFFECT`

The first Gate 2 attempt failed closed at the credential-presence gate. Both configured GitHub Actions secret references resolved to empty values. The live delivery step and all post-delivery steps were skipped, and the evidence upload reported no delivery files.

## Gate 2 accidental trigger 002

A documentation commit after attempt 001 emitted another `pull_request/synchronize` event. The one-shot workflow therefore started run `31181312508` before the trigger design was disarmed. It encountered the same empty-secret gate and did not reach Discord delivery.

- Discord POST attempted: FALSE
- Receipt 2 created: FALSE
- Delivery side effect: NONE
- Cause: live workflow was bound to every PR `synchronize` event rather than a one-use authorization event
- Corrective action: `.github/workflows/atomic-joy-gate2-live.yml` removed from the PR branch at commit `cbebd1b086b73cb11b3a5915c020f652a078597c`

The duplicate trigger is preserved as an orchestration defect. It did not produce a Discord side effect, but it proves that `pull_request/synchronize` is not an acceptable single-shot authorization mechanism for Gate 2.

GATE2_ATTEMPT_001 = FAILED_PRE_SIDE_EFFECT
GATE2_TRIGGER_002 = FAILED_PRE_SIDE_EFFECT
GATE2_LIVE_WORKFLOW = DISARMED
RUNTIME_DISCORD_DELIVERY_PROVEN = FALSE
MERGE_AUTHORIZED = FALSE

A future Gate 2 attempt requires explicit provisioning of the two repository Actions secrets, a fresh successful Gate 1 contract run, and a genuinely one-use execution mechanism that cannot be retriggered by ordinary PR commits.
