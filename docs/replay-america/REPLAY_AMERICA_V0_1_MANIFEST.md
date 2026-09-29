# REPLAY_AMERICA_V0_1 — Manifest

Status: PRE_GOV  
Public civic: TRUE  
Government-worthy: FALSE  
Government domain claim: FALSE  
Government endorsement: FALSE  
Government service: FALSE  
Authority created: FALSE  
No Fake Green: TRUE  
Append-only: TRUE

## Boundary

```text
REPLAY_AMERICA
= PUBLIC / CIVIC REPLAY CONTAINER
≠ .GOV AUTHORITY
≠ GOVERNMENT ENDORSEMENT
≠ GOVERNMENT SERVICE
```

## Typed anchors

```text
L1_ANCHOR           = jaywisdom.eth
L1_SEMANTIC_STATUS  = PROJECT_BOUND
L1_CONTROL_PROOF    = SEPARATE_CHECK_REQUIRED
L1_LEGAL_IDENTITY   = NOT_CLAIMED

L2_TEST_LABEL       = zerozerozerozero.base.eth
L2_STATUS           = UNBOUND_TEST
L2_AUTHORITY        = NONE
L2_INHERITS_L1      = FALSE

SENTINEL            = 0xDEADBEEF
SENTINEL_TYPE       = DEBUG_NULL_LIKE_MARKER
SENTINEL_IS_WALLET  = FALSE
SENTINEL_IS_RECEIPT = FALSE
```

## Sentinel rule

`0xDEADBEEF` is a 4-byte debug/null-like sentinel. It is not a valid 20-byte EVM address. It must not receive funds, stand in for control proof, be cited as a receipt, or inherit authority.

## Verification states

```text
UNVERIFIED
SELF_ATTESTED
CONTROL_PROVEN
REPLAY_CONFIRMED
EXTERNALLY_REVIEWED
```

No single badge collapses these states. Context determines whether green requires `CONTROL_PROVEN` or `EXTERNALLY_REVIEWED`.

## Promotion ladder

```text
PRE_GOV
→ PUBLIC_RECEIPTS
→ REPLAYABLE_SOURCES
→ IDENTITY_BINDING
→ SECURITY_REVIEW
→ ACCESSIBILITY
→ PRIVACY_REVIEW
→ HUMAN_GOVERNANCE
→ EXTERNAL_REVIEW
→ .GOV_ELIGIBILITY_QUESTION
```

The terminal state is only:

```text
.GOV_ELIGIBILITY_QUESTION = OPEN
```

It does not mean `.gov` claimed, approved, delegated, or endorsed.

## Invariants

```text
ENS_LABEL ≠ LEGAL_IDENTITY
PROJECT_ANCHOR ≠ CONTROL_PROOF
L1 ≠ L2
L2_TEST_LABEL ≠ AUTHORITY
SENTINEL ≠ ADDRESS
SENTINEL ≠ RECEIPT
SELF_ATTESTED ≠ CONTROL_PROVEN
CONTROL_PROVEN ≠ EXTERNALLY_REVIEWED
BRANDING ≠ AUTHORITY
PUBLIC_CIVIC ≠ GOVERNMENT_SERVICE
APPEND_ONLY ≠ REWRITE
```

## Receipt chaining

Receipts are append-only and may point to the prior receipt hash. A receipt records a bounded claim and its provenance. Control proof remains a separate evidentiary object.

## Authority

This manifest creates no government, legal, financial, signing, deployment, or domain authority.
