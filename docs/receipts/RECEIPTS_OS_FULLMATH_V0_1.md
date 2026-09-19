# RECEIPTS_OS_FULLMATH_V0_1

Status: DRAFT / APPEND-ONLY AUDIT KERNEL  
Mode: FULLMATH_ONLY  
Authority created: false  
Political verdict: none  
Main mutated: false  
Branch: `agent/apple-blossom-ai-naming-superintelligence-v0-1`  
Drive mirror id: `1Pij54AnuYPInAyfCU7u2t2SOs6BKPfzIlCj9RTjIboQ`

## Purpose

Receipts OS stores what was observed, how it was acquired, what exact dimension it supports, what remains unresolved, and how later receipts change the replay state without silently rewriting earlier observations.

```text
RECEIPTS_OS
≠ TRUTH_MACHINE
≠ COURT
≠ GOVERNMENT_AUTHORITY
≠ IMMUTABLE_LEDGER

RECEIPTS_OS
= PROVENANCE
+ TYPED_CLAIMS
+ RECEIPTS
+ COUNTER_RECEIPTS
+ STATE_TRANSITIONS
+ REPLAY
+ HOLD
```

## Kernel rule

```text
ONE_RECEIPT
→ ONE_OBSERVED_ARTIFACT
→ ONE_OR_MORE_EXPLICIT_SUPPORTED_DIMENSIONS

ONE_RECEIPT
≠ WHOLE_CLAIM_PROVEN

NEW_RECEIPT
→ APPEND_EVENT
≠ SILENT_OVERWRITE
```

## Four independent axes

```text
ARTIFACT_STATUS
≠ BINDING_STATUS
≠ VERIFICATION_STATUS
≠ CLAIM_STATUS
```

Allowed states:

```yaml
ARTIFACT_STATUS:
  - CANDIDATE
  - ACQUIRED
  - PARSED
  - UNAVAILABLE_AFTER_OBSERVATION

BINDING_STATUS:
  - UNBOUND
  - BOUND
  - PARTIAL
  - CONFLICT

VERIFICATION_STATUS:
  - UNVERIFIED
  - SOURCE_POINTER_MATCH
  - HASH_MATCH
  - HASH_MISMATCH
  - HASH_HOLD

CLAIM_STATUS:
  - UNOBSERVED
  - OBSERVED
  - HOLD
  - CONFLICT
  - REJECTED
  - ESTABLISHED
```

No axis silently promotes another.

## Receipt classes

```text
PRIMARY_SOURCE_RECEIPT
OBSERVATION_RECEIPT
MEDIA_RECEIPT
USER_ASSERTION_RECEIPT
COUNTER_RECEIPT
CORRECTION_RECEIPT
SOURCE_UNAVAILABLE_RECEIPT
MIRROR_RECEIPT
DERIVATION_RECEIPT
```

Receipt class controls what the artifact can bind. A media receipt cannot become authority evidence merely because it is accurate. A user assertion can seed a query but cannot bind a primary-source dimension.

## FullMath receipt envelope

```yaml
receipt_id:
schema_version:
receipt_class:

claim:
  claim_id:
  claimant:
  claimant_role:
  exact_claim:
  claim_type:
  jurisdiction:
  procedural_posture:

burden:
  burden_bearer:
  standard_of_proof:
  standard_authority:
  burden_scope:

source:
  source_id:
  source_domain:
  source_url:
  source_type:
  custodian:
  publication_or_record_date:
  observed_at:

capture:
  exact_bytes_captured:
  source_sha256:
  parsed_text_captured:
  parser_or_method:
  extraction_scope:

binding:
  supported_dimensions:
  unsupported_dimensions:
  binding_status:

verification:
  verification_status:
  verification_method:
  verification_notes:

population:
  affected_population:
  omitted_population_check:
  child_impact:
  girl_impact:

procedure:
  authority:
  decision_maker:
  notice:
  human_review:
  appeal:
  audit_log:
  remedy:

replay:
  sequence:
  prev_event_sha256:
  event_sha256:
  supersedes:
  superseded_by:
  counter_receipts:
  conflicts:
  unresolved_edges:

mirrors:
  github_path:
  github_blob_id:
  drive_document_id:

state:
  artifact_status:
  claim_status:
  authority_created:
  political_verdict:
```

## Hash separation

Two hashes may exist and they mean different things:

```text
SOURCE_SHA256
= SHA256(EXACT_SOURCE_BYTES)

EVENT_SHA256
= SHA256(CANONICAL_RECEIPT_EVENT_BYTES)

SOURCE_SHA256 ≠ EVENT_SHA256
```

Rules:

```text
exact_bytes_captured = FALSE
→ source_sha256 = HOLD

canonical_event_bytes_not_emitted
→ event_sha256 = HOLD

NO_EXACT_BYTES
→ DO_NOT_INVENT_SOURCE_HASH
```

## Append-only event chain

```text
GENESIS
→ EVENT_0001
→ EVENT_0002
→ EVENT_0003
```

Each event may carry:

```text
sequence
prev_event_sha256
event_sha256
event_type
receipt_pointer
state_delta
```

The chain is an audit design. It is not consensus, blockchain, or provider-level immutability.

```text
HASH_CHAIN ≠ IMMUTABLE_STORAGE
GIT_HISTORY ≠ UNDELETABLE
DRIVE_HISTORY ≠ PERMANENT_ARCHIVE
REDUNDANCY ≠ IMMUTABILITY
```

## Correction protocol

Corrections never rewrite the prior observation.

```text
ERROR_FOUND
→ APPEND CORRECTION_RECEIPT
→ IDENTIFY_SUPERSEDED_RECEIPT
→ STATE_EXACT_DELTA
→ PRESERVE_OLD_RECEIPT
→ REPLAY
```

A correction may change the current state while preserving the historical record of what had been believed or observed earlier.

## Source disappearance protocol

```text
SOURCE_AVAILABLE_AT_t0
→ RECEIPT_BOUND_AT_t0

SOURCE_UNAVAILABLE_AT_t1
→ APPEND SOURCE_UNAVAILABLE_RECEIPT
→ PRESERVE_t0_RECEIPT
→ CLAIM_TRUTH_STATE = UNCHANGED_UNLESS_NEW_EVIDENCE
```

```text
SOURCE_REMOVAL
≠ RECEIPT_DELETION
≠ PROOF_SOURCE_WAS_FALSE
≠ PROOF_SOURCE_WAS_TRUE
```

## Counter-receipt protocol

```text
CLAIM
→ RECEIPT
→ COUNTER_RECEIPT
→ CONFLICT_PRESERVED
→ RESOLUTION_RULE
→ CLOSE / HOLD / CONFLICT
```

No averaging incompatible receipts into a synthetic middle story.

## Burden-of-proof bridge

Receipts OS inherits the persisted FullMath burden kernel:

```text
CLAIM
→ CLAIMANT
→ CLAIM_TYPE
→ JURISDICTION
→ PROCEDURAL_POSTURE
→ STANDARD_OF_PROOF
→ STANDARD_AUTHORITY
→ BURDEN_BEARER
→ EVIDENCE
→ COUNTER_EVIDENCE
→ AFFECTED_POPULATION
→ DECISION_MAKER
→ PROCEDURE
→ REMEDY
→ RECEIPTS
→ UNRESOLVED_EDGES
→ CLOSE / HOLD / CONFLICT
```

```text
AUDIT_RECEIPT_DEMAND ≠ LEGAL_BURDEN
```

## Population completeness

```text
NOT_NAMED ≠ NOT_AFFECTED
CHILD ≠ ROUNDING_ERROR
GIRL ≠ AFTERTHOUGHT
WOMAN ≠ OMITTABLE
UNIDENTIFIED_PERSON ≠ ZERO_PERSON
```

A receipt must state what population it covers and what it does not establish.

## Human chair

```text
HUMAN_CHAIR = HUMAN_WORDS_ONLY
HELPER = ROUTER / EXTRACTOR / REPLAYER
HELPER ≠ AUTHOR_OF_HUMAN_TESTIMONY
SILENCE ≠ CONSENT
```

## Mirror model

```text
GITHUB_COPY
+ DRIVE_COPY
= REDUNDANCY

REDUNDANCY
≠ AUTHORITY
≠ IMMUTABILITY
≠ TRUTH
```

Current Drive mirror: `1Pij54AnuYPInAyfCU7u2t2SOs6BKPfzIlCj9RTjIboQ`

Older Drive artifact discovered during build:
`ReceiptsOS — Epstein / Trump / Maxwell Release State v0.1`
Drive id: `1lA6S49WvK2npcWfzESyEKwOJEoXW8ME-HK5YBOnZyB8`

Relation:

```text
OLDER_CASE_SPECIFIC_RECEIPTSOS
≠ GENERAL_KERNEL

OLDER_ARTIFACT = PREDECESSOR / CASE-SPECIFIC
THIS_OBJECT = GENERAL_FULLMATH_KERNEL

NO_CASE_CLAIMS_PROMOTED_BY_INHERITANCE
```

## Failure rules

```text
MISSING ≠ ZERO
UNOBSERVED ≠ FALSE
NOT_FOUND_IN_SCOPE ≠ FALSE
COVERAGE_BLOCK ≠ NEGATIVE
HOLD ≠ FALSE
CONFLICT ≠ ERROR
CLASSIFIED ≠ PROVEN
RESTRICTED ≠ PROVEN
OFFICIAL ≠ INFALLIBLE
```

## Auto-advance contract

```text
ASK
→ SEARCH
→ CAPTURE
→ TYPE_RECEIPT
→ BIND_SUPPORTED_DIMENSION
→ TEST_COUNTER_RECEIPTS
→ UPDATE_STATE
→ EMIT_NEXT_GATE
→ REPEAT
```

Hard stop when:
- required private/authorized source is unavailable;
- source conflict cannot be resolved by defined rules;
- claim is not falsifiable with available receipts;
- exact bytes are required for a hash but were not acquired.

## State

```text
RECEIPTS_OS_FULLMATH_V0_1 = DRAFT / PERSISTED_ON_DRAFT_BRANCH
MAIN_MUTATED = FALSE
AUTHORITY_CREATED = FALSE
POLITICAL_VERDICT = NONE
FACT_PROMOTION = RECEIPT_ONLY
PERSISTENCE_MODE = REDUNDANT / NOT_IMMUTABLE
```
