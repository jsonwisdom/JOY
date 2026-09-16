# ADDENDUM_V0.1h_TIEBREAK_AND_CLOCK_IDENTITY

STATUS = DRAFT_UNBOUND  
PARENT = ADDENDUM_V0.1g_VERIFICATION_RECIPE_HARDENING  
CHANGE_CLASS = PATCH  
AUTHORITY_CREATED = FALSE  
VERIFICATION_RESULT = HOLD

## 1. Recipe Hash Binds Procedure, Not Lifecycle State

```text
recipe_content_hash
= identity of the immutable procedure definition
```

It does NOT bind mutable lifecycle state.

Therefore:

```text
RECIPE_PROCEDURE_HASH
!= RECIPE_LIFECYCLE_STATE
```

Lifecycle transitions are tracked externally through the kernel index and its append-only lineage:

```text
DRAFT_UNBOUND
→ BOUND
→ VERIFIED
```

without changing `recipe_content_hash` solely because lifecycle status changed.

```text
STATUS_CHANGE
!= PROCEDURE_CHANGE
```

If the procedure itself changes:

```text
PROCEDURE_CHANGE
→ NEW_RECIPE_VERSION
→ NEW_RECIPE_CONTENT_HASH
```

not:

```text
PROCEDURE_CHANGE
→ MUTATE_EXISTING_HASHED_RECIPE
```

---

## 2. Verification Result Precedence

When multiple verification conditions exist simultaneously, result selection MUST follow deterministic precedence.

```text
REQUIRED_FAILURE
dominates
REQUIRED_HOLD
```

Evaluation rule:

```text
IF any REQUIRED_STEP_FAILED
OR any REQUIRED_ASSERTION_FAILED
THEN
  VERIFICATION_RESULT = FAILED

ELSE IF any REQUIRED_INPUT unresolved
OR any REQUIRED_DEPENDENCY unresolved
OR any REQUIRED_STEP skipped
OR any REQUIRED_OUTPUT unavailable
THEN
  VERIFICATION_RESULT = HOLD

ELSE IF all required conditions succeed
THEN
  VERIFICATION_RESULT = VERIFIED
```

Equivalent precedence:

```text
FAILED > HOLD > VERIFIED
```

where `>` means outcome-selection precedence, not severity or truth value.

Critical membrane:

```text
FAILED
= reproducible required contradiction

HOLD
= unresolved required condition

VERIFIED
= all required conditions satisfied
```

Therefore:

```text
UNRESOLVED
!= FAILED

FAILED
!= FALSE_CLAIM

HOLD
!= VERIFIED
```

---

## 3. Clock Identity

A verification result MUST identify its temporal reference sufficiently for later comparison.

Extended schema:

```json
{
  "verified_at": "...",
  "clock_source": "...",
  "clock_id": "...",
  "clock_description": "..."
}
```

For registered clock classes:

```text
clock_source ∈ {
  MEDIA_TIME,
  COURT_TIME,
  SYSTEM_TIME,
  FAMILY_CLOCK,
  OTHER
}
```

`clock_id` identifies the specific clock instance or declared temporal reference.

Examples:

```text
SYSTEM_TIME:
  clock_id = "executor-host-clock-v1"

COURT_TIME:
  clock_id = "court-docket-clock:<identifier>"

MEDIA_TIME:
  clock_id = "source-publication-clock:<identifier>"

FAMILY_CLOCK:
  clock_id = "<declared-family-clock-id>"
```

For:

```text
clock_source = OTHER
```

both are REQUIRED:

```text
clock_id
clock_description
```

Therefore:

```text
CLOCK_SOURCE
!= CLOCK_ID

CLOCK_ID
!= TIMESTAMP

TIMESTAMP
!= CLOCK_AUTHORITY
```

Two results may claim the same `clock_source` while using different `clock_id` values.

They MUST NOT be treated as temporally equivalent solely because the source enum matches.

---

## 4. Clock Comparability

Clock equality requires explicit identity or a declared mapping.

```text
CLOCK_A == CLOCK_B
IFF
clock_id_A == clock_id_B
OR
DECLARED_CLOCK_MAPPING(A,B) is verified
```

Otherwise:

```text
CLOCK_COMPARABILITY = HOLD
```

No silent conversion is permitted.

```text
SAME_TIMESTAMP_FORMAT
!= SAME_TEMPORAL_REFERENCE

SAME_CLOCK_SOURCE
!= SAME_CLOCK_INSTANCE
```

---

## 5. Procedure Identity and Lifecycle Lineage

A recipe entry should expose both:

```text
recipe_content_hash
lifecycle_event_lineage
```

so an observer can distinguish:

```text
WHAT_PROCEDURE_WAS_DEFINED?
```

from:

```text
WHAT_LIFECYCLE_STATE_WAS_IT_IN?
```

The index remains responsible for lifecycle history:

```text
INDEX_EVENT:
  recipe_id
  recipe_content_hash
  old_status
  new_status
  receipt
  timestamp
  prior_index_hash
```

This preserves:

```text
PROCEDURE_IDENTITY
+ LIFECYCLE_HISTORY
```

without forcing lifecycle mutation into the procedure hash.

---

## Final Invariants

```text
RECIPE_HASH
= PROCEDURE_IDENTITY

RECIPE_HASH
!= LIFECYCLE_STATUS

PROCEDURE_CHANGE
→ NEW_HASH

STATUS_CHANGE
→ INDEX_EVENT

REQUIRED_FAILURE
→ FAILED

ELSE REQUIRED_UNRESOLVED
→ HOLD

ELSE
→ VERIFIED

CLOCK_SOURCE
!= CLOCK_ID

OTHER_CLOCK
→ CLOCK_ID_REQUIRED
→ CLOCK_DESCRIPTION_REQUIRED

CLOCK_COMPARISON
REQUIRES
IDENTITY_OR_DECLARED_MAPPING
```

STATUS = DRAFT_UNBOUND  
ARTIFACT_CONTENT_HASH = HOLD  
GIT_COMMIT_SHA = HOLD  
DRIVE_REVISION_ID = HOLD  
VERIFICATION_RESULT = HOLD  
AUTHORITY_CREATED = FALSE
