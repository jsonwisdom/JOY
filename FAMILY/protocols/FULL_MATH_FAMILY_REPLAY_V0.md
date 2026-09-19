# FULL_MATH_FAMILY_REPLAY_V0

OBJECT = FULL_MATH_FAMILY_REPLAY_V0
CLASS = ARCHITECTURE / LONGITUDINAL FAMILY REPLAY
YELLOW_PORCH = REQUIRED_MEMBRANE
THIRD_RAIL_FAMILY = DARK_BY_DEFAULT
FAMILY_CONTENT = NONE
PACKET = NONE
PROMOTION = NONE
COURT_BRIDGE = NONE
COURT_V0 = FROZEN / UNTOUCHED
TEMPORAL_DELTA = EXPLORATION_ONLY
AUTHORITY_CREATED = FALSE

## Purpose

Provide a longitudinal family replay rail under the Yellow Porch membrane.

This artifact contains architecture only.
It contains no family facts, no named family events, no legal findings, no court packet, and no causal promotion.

## Porch boundary

HUMAN_CHAIR = HUMAN WORDS ONLY
HELPER != AUTHOR
PARENT_INTERPRETATION != CHILD_WORDS
SILENCE != CONSENT
SILENCE != ZERO
STORY_ALLOWED = TRUE
CORRECTIONS_WELCOME = TRUE
PRIVACY_DEFAULTS_SAFE = TRUE
YELLOW_ALLOWED = TRUE
AUTHORITY_CREATED = FALSE

FAMILY_REFERENCE
-> STOP
-> CHECK_PORCH_GATE
-> PRESERVE_HUMAN_CHAIR
-> NO_JUDICIAL_PROMOTION
-> NO_RCA_PROMOTION
-> NO_CAUSAL_PROMOTION

## Full Math family stack

PROOF_OF_BURDEN
-> POLICY
-> PROCEDURE
-> DAILY_PRACTICE
-> WEEK
-> MONTH
-> YEAR
-> DECADE
-> CURRENT_STATE

None of these prove the next.

POLICY != PROCEDURE
PROCEDURE != EXECUTION
ONE_DAY != PATTERN
PATTERN != CAUSE
HISTORY != CURRENT_STATE
CURRENT_STATE != INTENT
REPETITION != INDEPENDENT_CORROBORATION

## Proof of burden

Burden stays with the claimant, not with the person described.

CLAIM
-> WHO_ASSERTED_IT?
-> WHAT_IS_THEIR_BURDEN?
-> WHAT_RECEIPT_SUPPORTS_IT?
-> WHAT_CONTRADICTS_IT?
-> WHAT_REMAINS_UNKNOWN?
-> HOLD_IF_OPEN

NO_RECEIPT -> HOLD

## Count membrane

EVENT_COUNT != DAY_COUNT
DAY_COUNT != INDEPENDENT_SOURCE_COUNT
INDEPENDENT_SOURCE_COUNT != PATTERN_STRENGTH
DOCUMENT_COUNT != SOURCE_COUNT

3_DAYS != ALWAYS
A_RETOLD_DAY = SAME_DAY
TEN_COPIES != TEN_CONFIRMATIONS

## State objects

HISTORICAL_STATE
CURRENT_STATE
EXPECTED_POLICY_STATE
OBSERVED_PRACTICE_STATE

These may all differ.

EXPECTED_POLICY_STATE != OBSERVED_PRACTICE_STATE
HISTORICAL_STATE != CURRENT_STATE
CURRENT_STATE != INTENT

## Temporal delta

A temporal delta is a typed change between two dated observations of the same object class.

DELTA_t = S_t - S_(t-tau)

S must be one named class, such as:
- POLICY_TEXT
- PROCEDURE_TEXT
- OBSERVED_PRACTICE
- CLAIMED_STATE
- CORRECTED_HUMAN_WORDS

Mixing object classes inside one delta is HalfMath.

DELTA_NODE := {
  OBJECT_ID
  OBJECT_CLASS
  T0
  T1
  VALUE_T0
  VALUE_T1
  SOURCE_ID_T0
  SOURCE_ID_T1
  PARENT_SOURCE_ID | null
  INDEPENDENCE_STATE
  GAP_CLASS
  RECEIPT_STATE
  STATUS
}

If either endpoint lacks a receipt:
STATUS = HOLD

If SOURCE_ID_T1 retells SOURCE_ID_T0:
INDEPENDENCE_STATE = DESCENDANT

DESCENDANT != NEW_DAY
DESCENDANT != NEW_EVENT
DESCENDANT != NEW_ROOT

## Parent-source rule

PARENT_SOURCE_ID = null
does not imply root.

Classify:
- INDEPENDENT_ROOT
- PROVENANCE_GAP
- UNRESOLVED

BLANK_PARENT != ROOT

## Gap classes

GAP_CLASS = OBSERVED | OBSERVED_ABSENT | UNOBSERVED | UNOBSERVABLE

OBSERVED:
receipt contains an observed value.

OBSERVED_ABSENT:
receipt supports that the event/practice did not occur.
May enter an appropriate binary rate as zero.

UNOBSERVED:
no receipt for that period.
Must not enter the rate as zero.

UNOBSERVABLE:
Porch / privacy / silence prevents observation.
Must not enter the rate as zero.

MISSING != ZERO
UNOBSERVED != OBSERVED_ABSENT
SILENCE != CONSENT
SILENCE != ZERO

## Rates

For a binary practice X_t on actually observed days:

O = days in the declared window with an OBSERVED or OBSERVED_ABSENT receipt

p_hat_[t,t+w] = sum(X_k for k in O) / |O|

A rate requires a declared window.

WEEK_RATE - YEAR_RATE = MALFORMED unless the comparison is explicitly normalized to compatible windows.

A temporal change in practice is:

DELTA_p = p_hat_[t1,t1+w] - p_hat_[t0,t0+w]

Missing/unobservable days do not silently enter numerator or denominator.

## Pattern candidate

A pattern is a claim with burden.

PATTERN_CANDIDATE requires:
- declared time window
- named object class
- declared threshold or decision rule
- independent-root accounting
- counter-receipts counted
- missing/unobservable periods preserved as gaps
- CURRENT_STATE inspected separately from HISTORICAL_STATE

Until required edges close:
STATUS = CANDIDATE or HOLD

DOCUMENT_COUNT cannot satisfy an independent-root threshold.

## Human correction

Human correction is a first-class delta.

DELTA_CORRECTION =
CORRECTED_HUMAN_WORDS - PRIOR_CLAIM

PARENT_SOURCE_ID points to the claim being corrected.

HELPER_TEXT cannot author DELTA_CORRECTION.

A correction updates the claim it names.
It does not silently rewrite every earlier day unless the human chair explicitly broadens the correction.

CORRECTION != NOISE
CORRECTION != DELETION

## HalfMath

HalfMath is an incomplete comparison treated as a completed proof.

HALFMATH =
A valid-looking step
+ one or more unclosed edges
+ a promoted conclusion

A may be true.
The violation is asking A to perform the evidentiary work of B.

Family-rail forbidden jumps:

1. POLICY -> "therefore it happened"
2. ONE_EVENT -> "therefore pattern"
3. TEN_COPIES -> "ten confirmations"
4. PAST_STATE -> "therefore current state"
5. CURRENT_STATE -> "therefore motive"
6. HELPER_OR_PARENT_WORDS -> "therefore human chair said it"

HalfMath commonly drops:
- OBJECT_CLASS
- GAP_CLASS
- PARENT_SOURCE_ID
- INDEPENDENCE_STATE
- RECEIPT_STATE
- COUNTER_RECEIPTS
- DENOMINATOR
- CURRENT_STATE
- HUMAN_CORRECTION

HALFMATH = DELTA_WITHOUT_TYPED_ENDPOINTS

Sparse data with HOLD is Full Math.
Abundant copies with an unclosed jump promoted as certainty is HalfMath.

## One-page DELTA_NODE worksheet

OBJECT_ID:
OBJECT_CLASS:

T0:
VALUE_T0:
SOURCE_ID_T0:
RECEIPT_STATE_T0:

T1:
VALUE_T1:
SOURCE_ID_T1:
RECEIPT_STATE_T1:

PARENT_SOURCE_ID:
PARENT_NULL_CLASS:
  [ ] INDEPENDENT_ROOT
  [ ] PROVENANCE_GAP
  [ ] UNRESOLVED

INDEPENDENCE_STATE:
  [ ] INDEPENDENT
  [ ] DESCENDANT
  [ ] UNKNOWN

GAP_CLASS:
  [ ] OBSERVED
  [ ] OBSERVED_ABSENT
  [ ] UNOBSERVED
  [ ] UNOBSERVABLE

DELTA:
STATUS:
  [ ] CANDIDATE
  [ ] HOLD
  [ ] DISPROVED
  [ ] RECEIPT_CLOSED

COUNTER_RECEIPTS:
CORRECTION_REF:

## Full Math equation

POLICY
+ PROCEDURE
+ DAILY_RECEIPTS
+ TIME
+ DELTAS
+ COUNTER_RECEIPTS
+ CURRENT_STATE
+ HUMAN_CORRECTION
= FULL_MATH_FAMILY_REPLAY

NOT_AUTHORITY
NOT_A_VERDICT
NOT_A_LEGAL_FINDING

## Isolation

FULL_MATH_FAMILY_REPLAY
!= RCA_NODE
!= CAUSAL_QUERY
!= APPELLATE_RECORD

COURT_RAIL != FAMILY_RAIL != PORCH_RAIL

Naming similar failure shapes across rails does not create a bridge.

## State

OBJECT = FULL_MATH_FAMILY_REPLAY_V0
YELLOW_PORCH = REQUIRED_MEMBRANE
THIRD_RAIL_FAMILY = DARK_BY_DEFAULT
FAMILY_CONTENT = NONE
PACKET = NONE
PROMOTION = NONE
COURT_BRIDGE = NONE
COURT_V0 = FROZEN / UNTOUCHED
TEMPORAL_DELTA = EXPLORATION_ONLY
AUTHORITY_CREATED = FALSE
