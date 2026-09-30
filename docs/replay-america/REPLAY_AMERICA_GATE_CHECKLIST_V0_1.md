# REPLAY_AMERICA_V0_1 — Gate Checklist

Status: PRE_GOV  
Authority created: FALSE  
No Fake Green: TRUE

Use this checklist sequentially. A later gate must not erase, rewrite, or silently promote an earlier state.

| Gate | Required evidence | Fail / HOLD condition | State |
|---|---|---|---|
| PRE_GOV | Public civic container with explicit no-government-authority boundary | Any implied government authority, endorsement, or service claim | OPEN |
| PUBLIC_RECEIPTS | Hashable, timestamped, source-linked records | Screenshot-only or source-less artifact presented as proof | HOLD until bound |
| REPLAYABLE_SOURCES | Deterministic build/replay instructions and retrievable source objects | "Trust me" artifact, inaccessible source, or non-reproducible path | HOLD |
| IDENTITY_BINDING | Separate control proof for any ENS/Base anchor used as identity/control evidence | ENS label treated as legal identity; unbound test label promoted | HOLD |
| SECURITY_REVIEW | Threat model, key-management boundary, signing-key handling, disclosure path | Unreviewed signing keys, undefined compromise path, hidden irreversible actions | HOLD |
| ACCESSIBILITY | Plain-language path plus keyboard/screen-reader compatible public surface | Civic participation requires inaccessible interface or jargon-only path | HOLD |
| PRIVACY_REVIEW | Data minimization, PII boundary, no default public exposure of private data | Doxxing by default, unnecessary PII, private data written on-chain without justified consent | HOLD |
| HUMAN_GOVERNANCE | Named human stewards, conflict rules, appeal/correction path, bounded authority | Unaccountable root, persona/model treated as decision authority | HOLD |
| EXTERNAL_REVIEW | Independent review object with published scope, method, findings, and unresolved items | Self-certification only | HOLD |
| .GOV_ELIGIBILITY_QUESTION | Every prior gate has an admissible receipt and unresolved HOLDs are surfaced | Government branding or eligibility claim before the ladder is complete | CLOSED |

## Promotion law

```text
PASS_CURRENT_GATE
≠ PASS_NEXT_GATE

CONTROL_PROVEN
≠ EXTERNALLY_REVIEWED

REPLAY_CONFIRMED
≠ LEGAL_IDENTITY

PUBLIC_CIVIC
≠ GOVERNMENT_SERVICE
```

Only after the complete ladder may this state change:

```text
.GOV_ELIGIBILITY_QUESTION = OPEN
```

That change does not mean eligibility was established, a domain was granted, an endorsement exists, or government authority was created.

## Anchor checks

### L1 — `jaywisdom.eth`

```text
SEMANTIC_STATUS   = PROJECT_BOUND
CONTROL_PROOF     = SEPARATE_CHECK_REQUIRED
LEGAL_IDENTITY    = NOT_CLAIMED
```

### L2 — `zerozerozerozero.base.eth`

```text
STATUS            = UNBOUND_TEST
AUTHORITY         = NONE
INHERITS_L1       = FALSE
```

### Sentinel — `0xDEADBEEF`

```text
TYPE              = DEBUG_NULL_LIKE_MARKER
IS_EVM_ADDRESS    = FALSE
IS_WALLET         = FALSE
IS_RECEIPT        = FALSE
MAY_RECEIVE_FUNDS = FALSE
```

## No Fake Green

Allowed verification states:

```text
UNVERIFIED
SELF_ATTESTED
CONTROL_PROVEN
REPLAY_CONFIRMED
EXTERNALLY_REVIEWED
```

Do not use one generic `VERIFIED` state to collapse them.

## Append-only correction rule

If any gate, receipt, anchor, or interpretation changes:

```text
OLD_STATE
→ PRESERVE
→ APPEND_CORRECTION
→ LINK_SUPERSEDING_RECEIPT
→ REPLAY
```

Never silently rewrite the historical state.
