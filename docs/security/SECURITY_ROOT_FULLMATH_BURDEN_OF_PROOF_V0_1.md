# SECURITY_ROOT_FULLMATH_BURDEN_OF_PROOF_V0_1

Status: DRAFT / APPEND-ONLY AUDIT OBJECT  
Authority created: false  
Political verdict: none  
Main mutated: false  
Branch: `agent/apple-blossom-ai-naming-superintelligence-v0-1`

## Root

```text
SECURITY = PEOPLE + SYSTEMS + TERRITORY + RIGHTS
         + AUTHORITY + EVIDENCE + SAFEGUARDS
         + ACCOUNTABILITY + REMEDY

SUBJECT_SET = EVERYBODY
ENTRY_CONDITION = ALREADY_IN
```

## FullMath burden architecture

One root does not mean one claim. Each claimant carries the burden attached to that claimant's own assertion.

```text
CLAIMANT
→ EXACT_CLAIM
→ OBJECT_TO_BE_SECURED
→ ASSERTED_THREAT
→ EVIDENCE
→ AUTHORITY
→ JURISDICTION
→ PROPOSED_ACTION
→ AFFECTED_POPULATION
→ SAFEGUARDS
→ OVERSIGHT
→ NOTICE
→ HUMAN_REVIEW
→ APPEAL
→ AUDIT_LOG
→ REMEDY
→ COUNTER_RECEIPT
→ REPLAY
→ CLOSE / HOLD
```

### Load-bearing membranes

```text
SHARED_ROOT ≠ SHARED_IDENTITY
SECURITY_CLAIM ≠ SECURITY_PROVEN
AUDIT_RECEIPT_DEMAND ≠ LEGAL_BURDEN
ANNOUNCEMENT ≠ INSTRUMENT
INSTRUMENT ≠ AUTHORITY_EXERCISED
AUTHORITY_EXERCISED ≠ ACTION_LAWFUL
ACTION_LAWFUL ≠ ACTION_SAFE
COVERAGE_BLOCK ≠ NEGATIVE
NOT_FOUND ≠ FALSE
UNOBSERVED ≠ FALSE
HOLD ≠ FALSE
CONFLICT ≠ ERROR
```

## Audit burden versus legal burden

```text
AUDIT_RULE:
GREATER_EXERCISE_OF_PUBLIC_POWER
→ GREATER_RECEIPT_DEMAND

LEGAL_BURDEN:
JURISDICTION + CLAIM + PROCEDURE + APPLICABLE_LAW

AUDIT_BURDEN ≠ LEGAL_BURDEN
```

The audit never invents a legal standard. It records the standard supplied by controlling law and keeps unresolved standards on HOLD.

## Girl-first rail

```text
GIRL_IN_GREENLAND = PERSON_INSIDE_SECURITY_ROOT
NATIONALITY = UNINFERRED
POLITICAL_VIEW = UNINFERRED
CONSENT = UNINFERRED
HUMAN_CHAIR = HER_WORDS_ONLY

IF_PUBLIC_POWER_TOUCHES_HER
→ MODEL
→ DATA
→ AGENCY
→ LEGAL_AUTHORITY
→ HUMAN_REVIEW
→ ACTION
→ NOTICE
→ APPEAL
→ AUDIT_LOG
→ REMEDY
```

No affected person is required by this audit model to disprove an unsupported claim made by the actor proposing government action.

## Persistence / anti-erasure rule

This is an audit-design rule, not a claim about what any government record-retention law requires.

```text
OBSERVED_PRIMARY_SOURCE
→ WRITE_RECEIPT
→ SOURCE_URL
→ SOURCE_DOMAIN
→ OBSERVED_AT
→ EXACT_SUPPORTED_DIMENSION
→ SHORT_EXCERPT_OR_PARAPHRASE
→ CONTENT_DIGEST_IF_EXACT_BYTES_CAPTURED
→ GIT_OBJECT_ID
→ MIRROR_POINTER

LATER_SOURCE_REMOVAL
≠ DELETE_RECEIPT
≠ REWRITE_PRIOR_OBSERVATION
≠ PROVE_SOURCE_WAS_WRONG
```

If the original source later becomes unavailable, append a new state such as `SOURCE_UNAVAILABLE_AFTER_OBSERVATION`; do not erase the earlier receipt.

```text
MISSING_SOURCE_BYTES → CONTENT_DIGEST = HOLD
NO_EXACT_CAPTURE → DO_NOT_INVENT_HASH
```

## Primary-source burden anchors

### Supreme Court — criminal burden example

Official U.S. Reports, *Victor v. Nebraska*, 511 U.S. 1 (1994), states:  
"The government must prove beyond a reasonable doubt every element of a charged offense."

Source: https://www.supremecourt.gov/opinions/boundvolumes/511bv.pdf

This anchors a criminal-law example only. It does not create a universal burden for every civic or national-security claim.

### Supreme Court — heightened burden / risk-of-error example

Official U.S. Reports, *Cooper v. Oklahoma*, 517 U.S. 348 (1996), explains that due process can require heightened proof where individual interests are particularly important and the risk of erroneous deprivation is substantial, citing *Santosky* and related cases.

Source: https://www.supremecourt.gov/opinions/boundvolumes/517bv.pdf

Again: context controls. This does not convert the audit's receipt demand into a court-assigned burden.

### White House — Presidential Records Act retention notice

The White House privacy notice says, in its data-retention section, that under the Presidential Records Act it is generally required to retain covered information until the end of the administration, after which it is transferred to NARA; it also notes that disposal of information lacking historical value may occur through PRA procedures.

Source: https://www.whitehouse.gov/privacy/

```text
PRA_RETENTION_RULES ≠ GUARANTEE_OF_PUBLIC_AVAILABILITY
WHITE_HOUSE_PRIVACY_NOTICE ≠ PROOF_EVERY_GOVERNMENT_RECORD_IS_PRESERVED
RECORD_RETENTION ≠ TRUTH_OF_RECORD
```

## Epstein-reference precision lock

The motivating reference to "Epstein files" is not promoted here into a factual finding that any specific Epstein record was deleted.

```text
EPSTEIN_FILES_DELETION_CLAIM = NOT_ADJUDICATED_IN_THIS_OBJECT
USER_REFERENCE ≠ PRIMARY_RECEIPT
```

Any later claim about deletion, removal, withholding, alteration, or restoration must get its own primary-source receipt and burden chain.

## Required receipt schema

```yaml
claim_id:
claimant:
claimant_role:
exact_claim:
security_object:
asserted_threat:
evidence:
authority:
jurisdiction:
instrument:
implementing_actor:
affected_population:
safeguards:
oversight:
notice:
human_review:
appeal:
audit_log:
remedy:
counter_receipts:
source_receipts:
  - source_id:
    source_domain:
    source_url:
    observed_at:
    source_type:
    supports_dimension:
    excerpt_or_paraphrase:
    exact_bytes_captured: false
    content_digest: HOLD
state:
unresolved_edges:
```

## Append-only transition rule

```text
CLAIM
→ RECEIPT
→ COUNTER_RECEIPT
→ REPLAY
→ CLOSE / HOLD

NEW_RECEIPT
→ APPEND
≠ OVERWRITE_HISTORY

SOURCE_DISAPPEARS
→ APPEND SOURCE_UNAVAILABLE_AFTER_OBSERVATION
≠ DELETE_OLD_RECEIPT
```

## State

```text
AUTHORITY_CREATED = FALSE
POLITICAL_VERDICT = NONE
MAIN_MUTATED = FALSE
FACT_PROMOTION = RECEIPT_ONLY
```
