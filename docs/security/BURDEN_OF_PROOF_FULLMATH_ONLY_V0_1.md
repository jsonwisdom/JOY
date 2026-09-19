# BURDEN_OF_PROOF_FULLMATH_ONLY_V0_1

Status: DRAFT / APPEND-ONLY AUDIT OBJECT  
Authority created: false  
Political verdict: none  
Main mutated: false  
Branch: `agent/apple-blossom-ai-naming-superintelligence-v0-1`  
Drive mirror: https://docs.google.com/document/d/1A4Y9HMnbYCWiacJLdS50glBtc6PA-AynzA_fmQpIpig/edit

## Root

```text
BURDEN_OF_PROOF
= CLAIM
+ CLAIMANT
+ CLAIM_TYPE
+ STANDARD
+ STANDARD_AUTHORITY
+ JURISDICTION
+ EVIDENCE
+ COUNTER_EVIDENCE
+ AFFECTED_POPULATION
+ DECISION_MAKER
+ PROCEDURE
+ RESULT
+ REMEDY
+ RECEIPT
+ REPLAY
```

## FullMath-only rule

```text
ONE_CLAIM → ONE_TYPED_BURDEN_OBJECT

CLAIMANT_A_CARRIES_CLAIM_A
CLAIMANT_B_CARRIES_CLAIM_B

AFFECTED_PERSON
≠ AUTOMATIC_BURDEN_BEARER
≠ REQUIRED_TO_DISPROVE_UNSUPPORTED_ACTOR_CLAIM
```

## Legal burden membrane

```text
AUDIT_RECEIPT_DEMAND ≠ LEGAL_BURDEN

LEGAL_BURDEN
= JURISDICTION
+ CLAIM_TYPE
+ PROCEDURE
+ CONTROLLING_AUTHORITY
+ STANDARD_OF_PROOF

NO_SOURCE_FOR_STANDARD
→ STANDARD = HOLD

NO_JURISDICTION
→ LEGAL_BURDEN = HOLD

NO_PROCEDURAL_POSTURE
→ LEGAL_BURDEN = HOLD
```

The audit may demand receipts for replay. It may not manufacture a court-assigned burden of proof.

## Burden tuple

```yaml
BURDEN_TUPLE:
  claim_id:
  claimant:
  claimant_role:
  exact_claim:
  claim_type:
  jurisdiction:
  procedural_posture:
  standard_of_proof:
  standard_authority:
  burden_bearer:
  burden_scope:
  evidence_required:
  evidence_present:
  counter_evidence:
  affected_population:
  decision_maker:
  notice:
  opportunity_to_respond:
  human_review:
  appeal:
  audit_log:
  remedy:
  source_receipts:
  unresolved_edges:
  state:
```

## Proof transition

```text
ASSERTION
→ IDENTIFY_CLAIMANT
→ TYPE_CLAIM
→ IDENTIFY_JURISDICTION
→ IDENTIFY_PROCEDURE
→ BIND_STANDARD
→ BIND_AUTHORITY_FOR_STANDARD
→ IDENTIFY_BURDEN_BEARER
→ BIND_EVIDENCE
→ BIND_COUNTER_EVIDENCE
→ COUNT_AFFECTED_POPULATION
→ TEST_PROCEDURE
→ TEST_REMEDY
→ REPLAY
→ CLOSE / HOLD / CONFLICT
```

Every arrow is separately receipt-gated.

```text
ONE_EDGE_CLOSED
≠ WHOLE_CLAIM_PROVEN
```

## Missing-data math

```text
MISSING ≠ ZERO
UNOBSERVED ≠ FALSE
NOT_FOUND_IN_SCOPE ≠ FALSE
COVERAGE_BLOCK ≠ NEGATIVE
HOLD ≠ FALSE
CONFLICT ≠ ERROR
CLASSIFIED ≠ PROVEN
RESTRICTED ≠ PROVEN
```

## Evidence math

```text
CLAIM ≠ RECEIPT
RECEIPT ≠ SOURCE
SOURCE ≠ TRUTH_BY_DEFINITION
OFFICIAL ≠ INFALLIBLE
SECONDARY ≠ FALSE_BY_DEFINITION
COUNTER_RECEIPT ≠ DISLOYALTY
```

Conflicting receipts are preserved as conflict until a defined resolution rule closes the edge.

## Affected-population completeness

```text
NOT_NAMED ≠ NOT_AFFECTED
CHILD ≠ ROUNDING_ERROR
GIRL ≠ AFTERTHOUGHT
WOMAN ≠ OMITTABLE
UNIDENTIFIED_PERSON ≠ ZERO_PERSON
```

The burden object must state the population it actually covers. It may not silently generalize from an unrepresentative subset.

## Anti-erasure / anti-overwrite

```text
NEW_RECEIPT
→ APPEND

NEW_COUNTER_RECEIPT
→ APPEND

SOURCE_LATER_UNAVAILABLE
→ APPEND SOURCE_UNAVAILABLE_AFTER_OBSERVATION

CORRECTION
→ APPEND CORRECTION
+ LINK_SUPERSEDED_RECEIPT

NEVER:
SILENT_OVERWRITE
SILENT_DELETE
SILENT_STATUS_PROMOTION
```

## Persistence limits — FullMath correction

```text
GIT_HISTORY ≠ UNDELETABLE
DRIVE_MIRROR ≠ UNDELETABLE
REDUNDANCY ≠ IMMUTABILITY
TAMPER_EVIDENT ≠ TAMPER_PROOF
BRANCH_EXISTS ≠ BRANCH_PROTECTED
REVISION_HISTORY ≠ PERMANENT_ARCHIVE
```

Therefore:

```text
NO_SILENT_OVERWRITE = DESIGN_REQUIREMENT
NO_HISTORY_REWRITE = AUDIT_REQUIREMENT
NOT = GUARANTEE_OF_PHYSICAL_OR_PROVIDER_IMMUTABILITY
```

If stronger preservation is required, it needs independently administered copies and retention controls outside this two-surface corridor.

## Receipt identity

```yaml
RECEIPT_IDENTITY:
  source_url:
  source_domain:
  observed_at:
  exact_supported_dimension:
  exact_bytes_captured:
  sha256:
  git_blob_id:
  drive_mirror_id:
  supersedes:
  superseded_by:
  deletion_or_unavailability_event:
```

```text
exact_bytes_captured = FALSE
→ sha256 = HOLD

NO_EXACT_BYTES
→ DO_NOT_INVENT_CONTENT_HASH
```

## State machine

```text
UNOBSERVED
→ OBSERVED
→ RECEIPT_BOUND
→ STANDARD_BOUND
→ EVIDENCE_TESTED
→ COUNTER_RECEIPT_TESTED
→ PROCEDURE_TESTED
→ REMEDY_TESTED
→ CLOSE

ANY_MISSING_REQUIRED_EDGE
→ HOLD

CONTRADICTORY_VALID_RECEIPTS
→ CONFLICT
```

## Final invariant

```text
BURDEN_OF_PROOF_FULLMATH
=
WHO_MAKES_THE_CLAIM
+ WHAT_EXACTLY_IS_CLAIMED
+ WHO_LEGALLY_CARRIES_THE_BURDEN
+ WHAT_STANDARD_APPLIES
+ WHAT_AUTHORITY_SUPPLIES_THAT_STANDARD
+ WHAT_EVIDENCE_SATISFIES_IT
+ WHAT_COUNTER_EVIDENCE_EXISTS
+ WHO_IS_AFFECTED
+ WHAT_PROCESS_TESTS_THE_CLAIM
+ WHAT_REMEDY_EXISTS_IF_WRONG
+ WHAT_RECEIPTS_SURVIVE_REPLAY
+ WHAT_REMAINS_HOLD
```

## State

```text
AUTHORITY_CREATED = FALSE
POLITICAL_VERDICT = NONE
MAIN_MUTATED = FALSE
FACT_PROMOTION = RECEIPT_ONLY
PERSISTENCE_MODE = REDUNDANT / NOT_IMMUTABLE
```
