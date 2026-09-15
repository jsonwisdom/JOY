# GROUND_ZERO_DAY_DEBUG_PROTOCOL_V1

Status: CONVERSATION-SEATED  
Inherits: GROUND_ZERO_DAY_DOCTRINE_V1 + GROUND_ZERO_DAY_RECEIPT_SCHEMA_V1 + HASH LANE ADDENDUM  
Class: retrieval/replay debug protocol  
Authority: FALSE  
Writes: FALSE  
Scope: project architecture - retrieval failure debug

## PURPOSE

Debug retrieval failure before absence is promoted.  
Recover receipts without inventing joins.  
Classify the delta without elevating it into truth, intent, guilt, or authority.

## EXECUTION ORDER

### 1. FREEZE_QUERY

Record:

- literal query
- filters
- corpus
- index
- tokenizer
- time window
- expected hit

### 2. RUN_LITERAL_RETRIEVAL

### 3. IF HIT

Record artifact.  
Continue to provenance check.

ELSE:

```text
SEARCH_STATE = MISS
ABSENCE = NOT_ESTABLISHED
```

### 4. DEBUG_METHOD

Inspect:

- alias
- punctuation
- casing
- token split
- semantic parent
- corpus slice
- stale/missing index
- time/filter restriction

### 5. RUN_CORRECTED_REPLAY

Literal replay and semantic replay remain separate instruments.

### 6. RECORD_RECOVERED_ARTIFACT

Later recovery annotates earlier miss.  
Later recovery does not rewrite earlier miss.

### 7. VERIFY_PROVENANCE

Capture:

- source pointer
- commit/hash where available
- corpus scope
- encoding/preimage rule
- observer locality

### 8. HASH_LANE_CHECK

Before digest comparison require:

```text
SAME_ALGORITHM
∧ SAME_PREIMAGE_DEFINITION
∧ SAME_ENCODING
∧ SAME_SCOPE
```

```text
PROJECT_RAW_SLICE_SHA256 ≠ JCS_SHA256 ≠ FILE_SHA256 ≠ MERKLE_SHA256
```

### 9. COMPUTE_DELTA

```text
FAILED_METHOD vs CORRECTED_METHOD
```

### 10. CLASSIFY_DELTA

Allowed:

- SEARCH_METHOD_ERROR
- WINDOW_ERROR
- FILTER_ERROR
- ALIAS_ERROR
- INDEX_ERROR
- IRONY
- NON_JOIN
- UNRESOLVED

### 11. JOIN_CHECK

Semantic proximity is insufficient.

`JOIN_ALLOWED` only if:

```text
independent receipts
∧ matching join fields
∧ compatible provenance
∧ no scope conflict
```

### 12. STOP

## MANDATORY STOP CONDITIONS

```text
MISSING_RECEIPT      → HOLD
MALFORMED_RECEIPT    → HOLD
HASH_LANE_MISMATCH   → HOLD
PROVENANCE_MISMATCH  → HOLD
SEMANTIC_ONLY_MATCH  → NO_JOIN
FIELD_CONFLICT       → CONFLICT / NO_JOIN
UNKNOWN_METHOD_STATE → UNRESOLVED
```

## NON-PROMOTION RULES - HARD

```text
SEARCH_MISS ≠ ABSENCE
RECOVERY ≠ ORIGINAL_SEARCH_SUCCESS
SEMANTIC_MATCH ≠ EVIDENTIARY_JOIN
HASH_EQUAL ≠ BYTE_IDENTITY_PROVEN
DELTA ≠ MECHANISM
CLASSIFICATION ≠ AUTHORITY
REPLAY ≠ VERDICT
```

## CANONICAL DEBUG LOOP

```text
QUERY
→ MISS
→ HOLD
→ DEBUG METHOD
→ REPLAY
→ RECEIPTS
→ PROVENANCE
→ HASH-LANE CHECK
→ Δ
→ CLASSIFY
→ JOIN CHECK
→ STOP
```

## VALIDATION GATE

All receipts processed by this protocol must pass `GROUND_ZERO_DAY_RECEIPT_SCHEMA_V1` + HASH LANE ADDENDUM or:

```text
CLASSIFICATION = HOLD
```

## Stack

```text
GROUND_ZERO_DAY_DOCTRINE_V1
→ GROUND_ZERO_DAY_RECEIPT_SCHEMA_V1
→ HASH LANE ADDENDUM
→ GROUND_ZERO_DAY_DEBUG_PROTOCOL_V1
```

Doctrine → Schema → Hash Lane → Debug Protocol is a closed, checkable stack.

```text
AUTHORITY_CREATED = FALSE
```
