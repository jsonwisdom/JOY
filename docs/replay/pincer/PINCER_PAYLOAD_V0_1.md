# PincerPayload v0.1

```text
STATE                     = HOLD_DRAFT
ARTIFACT_CLASS            = REPLAY_ENVELOPE
PRIMARY_DOMAIN            = FAMILY_INTELLIGENCE
SUBJECT_EXAMPLE           = HEIDEE
CALENDARIZED_IN_SCHEMA    = TRUE
LIVE_CALENDAR_EVENTS      = FALSE
CANONIZED                 = FALSE
AUTHORITY_CREATED         = FALSE
IDENTITY_PROOF            = FALSE
CONSENT_INFERRED          = FALSE
SEALED                    = FALSE
REPLAY_READY              = FALSE
LIVE_ENFORCEMENT          = PROHIBITED
PROMOTION                 = PROHIBITED
```

## Purpose

`PincerPayload` is a bounded envelope that carries one artifact through:

```text
IMAGINE
→ CAPTURE
→ CLASSIFY
→ FREEZE EXACT BYTES
→ HASH
→ REPRODUCE INDEPENDENTLY
→ ATTEST
→ COMPARE RAILS
→ ISSUE RESULT
→ REQUEST REPOSITORY ADOPTION SEPARATELY
```

It is designed for JOY family continuity, Attestation JSONs, Heidee JOY replay, CrissCross AppleSauce pointers, and human expressions such as **LoveLoveLoves U** without converting affection, memory, timestamps, hashes, signatures, GitHub checks, ENS names, or blockchain records into authority.

## Time doctrine

At the truth and authority layer:

```text
TIME != TRUTH
TIME != AUTHORSHIP
TIME != CONSENT
TIME != AUTHORITY
TIME != CANON
```

At the replay layer, time remains a coordinate used for:

```text
ORDERING
WINDOW_SELECTION
SOURCE_CUSTODY
EXPIRY
VERSION_COMPARISON
DRIFT_DETECTION
```

So the bounded answer is:

```text
DOES_TIME_CREATE_TRUTH?     NO
DOES_TIME_SELECT_A_REPLAY?  YES
```

A timestamp cannot make a claim true. It can identify which bytes, repository head, source state, or consent state were examined.

## Calendar resolution

The initial payload is anchored to:

```text
ANCHOR_LOCAL = 2026-08-01T22:18:00-05:00
TIMEZONE     = America/Chicago
WEEK_RULE    = ISO_WEEK_MONDAY_THROUGH_SUNDAY
```

Resolved windows:

| Window | Exact range | Initial status |
|---|---|---|
| Last month | 2026-07-01 through 2026-07-31 | HISTORICAL_SELECTION |
| Next month | 2026-09-01 through 2026-09-30 | FUTURE_SELECTION_NOT_RUN |
| Last week | 2026-07-20 through 2026-07-26 | HISTORICAL_SELECTION |
| Current week | 2026-07-27 through 2026-08-02 | ACTIVE_SELECTION |
| Next week | 2026-08-03 through 2026-08-09 | FUTURE_SELECTION_NOT_RUN |
| Yesterday | 2026-07-31 | HISTORICAL_SELECTION |
| Today | 2026-08-01 | ACTIVE_SELECTION |
| Tomorrow | 2026-08-02 | FUTURE_SELECTION_NOT_RUN |
| Now | 2026-08-01T22:18:00-05:00 | OBSERVATION_ANCHOR |

These are payload coordinates only. No external calendar event, reminder, schedule, or automation is created by this draft.

## Calendarized versus canonized

```text
CALENDARIZED_IN_SCHEMA = TRUE
```

means the relative words have been resolved into exact date ranges under a declared timezone and week rule.

```text
LIVE_CALENDAR_EVENTS = FALSE
```

means nothing has been written to Google Calendar, Apple Calendar, or an automation schedule.

```text
CANONIZED = FALSE
```

because JOY canon requires a separate Verification Record followed by an explicit Repository adoption event. A payload, receipt, successful workflow, or draft pull request cannot self-canonize.

## Payload layers

### 1. Identity and family lane

A payload routes through a stable `family_lane_id`.

For the included example:

```text
family_lane_id       = HEIDEE
relation_class       = OPERATOR_DEFINED_DAUGHTER_LANE
relation_proof       = FALSE
public_consent       = FALSE
precise_geolocation  = PROHIBITED_BY_DEFAULT
```

The lane preserves continuity without claiming legal relationship proof, identity proof, custody, public biography, or public consent.

### 2. Imagination Station

`imagination_station` contains proposals, stories, hypotheses, desired futures, and playful logic.

```text
IMAGINATION_IS_ALLOWED       = TRUE
IMAGINATION_IS_EVIDENCE      = FALSE
IMAGINATION_CAN_EXECUTE      = FALSE
IMAGINATION_CAN_SELF_ATTEST  = FALSE
```

Every proposal must remain distinguishable from observation and verified result.

### 3. LoveLoveLoves U

`love_message` carries family affection as human expression.

```text
MESSAGE_CLASS      = FAMILY_AFFECTION
EVIDENTIARY_EFFECT = NONE
EXECUTION_EFFECT   = NONE
CONSENT_EFFECT     = NONE
AUTHORITY_EFFECT   = NONE
```

Love does not need a machine gate to be meaningful. It needs a machine boundary so it is not misused as consent, identity, ownership, or authorization.

### 4. CrissCross AppleSauce

`cross_links` may connect:

- JOY family lane IDs
- repository files and commits
- replay receipts
- external repository pointers
- `jaywisdom.base.eth` as a discovery pointer
- calendar window IDs

The links are pointer-only.

```text
POINTER_ONLY             = TRUE
COPY_PRIVATE_CONTENT     = FALSE
MERGE_IDENTITIES         = FALSE
INHERIT_PERMISSIONS      = FALSE
INHERIT_CONSENT          = FALSE
INHERIT_AUTHORITY        = FALSE
INHERIT_GEOLOCATION      = FALSE
```

### 5. Core payload

`core` contains the claim scope, subject lane, exact window selection, source pointers, requested replay procedure, privacy boundary, and expected result class.

The core must not contain signatures or its own digest.

### 6. Frozen Artifact Rail

The first rail freezes the exact serialized payload bytes.

```text
CANONICAL_JSON_BYTES = UTF8(RFC8785_JCS(core))
PAYLOAD_DIGEST       = SHA256(CANONICAL_JSON_BYTES)
BINDING_DIGEST       = SHA256(
  UTF8("JOY:PINCER_PAYLOAD:CORE:V0.1\n")
  || RAW_PAYLOAD_DIGEST
)
```

`PAYLOAD_DIGEST` binds the exact canonical bytes. `BINDING_DIGEST` binds that raw digest to the PincerPayload protocol domain.

If a non-JSON source artifact is carried, its authoritative digest is SHA-256 of its exact frozen source bytes. A JSON wrapper must never silently replace the original source bytes.

### 7. Verified Execution Rail

The second rail must be executed by an independently identified replay environment using the same:

- artifact scope
- exact source bytes
- canonicalization rule
- hash algorithm
- domain tag
- procedure version
- ordered inputs
- declared dependencies

It returns independently reproduced raw payload and binding digests plus a variance report.

### 8. Attestation JSONs

Attestations are detached objects. They may state what a witness observed, performed, or believes.

They do not alter the frozen core.

Required distinction:

```text
ATTESTATION = SIGNED_OR_UNSIGNED_WITNESS_STATEMENT
ATTESTATION != TRUTH
ATTESTATION != VALIDATION
ATTESTATION != AUTHORITY
```

A signed attestation signs the raw 32-byte payload digest, not the ASCII hexadecimal text.

### 9. Cross-rail binding

The Pincer closes only when:

```text
RAW_PAYLOAD_DIGESTS_MATCH
AND BINDING_DIGESTS_MATCH
AND ARTIFACT_SCOPES_MATCH
AND CANONICALIZATION_RULES_MATCH
AND HASH_ALGORITHMS_MATCH
AND DOMAIN_TAGS_MATCH
AND PROCEDURE_VERSIONS_MATCH
AND ORDERED_INPUTS_MATCH
AND VARIANCE_REPORT_IS_EMPTY
```

A matching displayed hexadecimal string is insufficient when the byte scope or procedure differs.

### 10. Result classes

```text
CLOSED_REPRODUCIBLE
OPEN_MISSING_INPUT
OPEN_DIGEST_MISMATCH
OPEN_SCOPE_MISMATCH
OPEN_PROCEDURE_MISMATCH
OPEN_ATTESTATION_ONLY
DENIED_MALFORMED
DENIED_PRIVACY_BOUNDARY
DENIED_UNAUTHORIZED_EFFECT
```

`CLOSED_REPRODUCIBLE` means the artifact survived independent reproduction. It does not mean the artifact is true, authored by a particular person, legally effective, consensual, or authorized for execution.

## Heidee JOY replay binding

The example payload references four existing JOY records:

```text
FAMILY/HEIDEE/README.md
artifacts/PROFILE_HEIDEE_V0_4.json
artifacts/links/HEIDEE_JOYSPACE_DIRECT_LINK_V0_1.json
docs/joyspace/receipts/JOYSPACE_HEIDEE_MRS_WISDOM_REPLAY_20260614.md
```

Current bounded interpretation:

```text
HEIDEE_FAMILY_LANE_PRESENT         = TRUE
HEIDEE_FAMILY_README_EXPANDED      = FALSE
HEIDEE_STRUCTURAL_PROFILE_RECORDED = TRUE
HEIDEE_EXTERNAL_REPO_LIVE_RECHECK  = NOT_PERFORMED_HERE
HEIDEE_JOY_RECORDED_STATUS         = GREEN_SCOPED
HEIDEE_PUBLIC_HTTP_STATUS          = YELLOW
FULL_BYTE_REPLAY                   = NOT_PASSED
AUTHORITY                          = FALSE
```

This payload does not overwrite the June 14 receipt. It points to it and asks whether the same bounded interpretation survives a new independent replay.

## Ingress membrane

```text
NATURAL LANGUAGE
→ PARSE
→ RESOLVE CALENDAR WINDOWS
→ BUILD CANONICAL CORE
→ DOMAIN CHECK
→ SUBJECT-LANE CHECK
→ PRIVACY CHECK
→ CAPABILITY CHECK
→ CONSENT CHECK
→ FREEZE BYTES
→ HASH
→ POINTER-ONLY RESPONSE OR EXPLICITLY AUTHORIZED ACTION
```

Any failed check returns `DENIED` or an `OPEN_*` state. It must not silently reinterpret names, dates, identities, relationships, consent, location, authority, or desired effects.

## Canon gate

The payload cannot create JOY canon directly.

Required downstream chain:

```text
PINCER RESULT
→ RECEIPT
→ VERIFICATION RECORD
→ REPOSITORY ADOPTION REQUEST
→ ADOPTED | DEFERRED | REJECTED
```

Until a qualifying explicit Repository adoption event exists:

```text
CANONIZED = FALSE
```

## Present state

```text
WHERE_ARE_WE_NOW          = DRAFT_DESIGN_BRANCH
OBSERVATION_ANCHOR        = 2026-08-01T22:18:00-05:00
HEIDEE_JOY_REPLAY         = STRUCTURALLY_PREPARED_NOT_EXECUTED
FROZEN_ARTIFACT_RAIL      = NOT_PASSED
VERIFIED_EXECUTION_RAIL   = NOT_PASSED
CROSS_RAIL_BINDING        = NOT_PROVEN
PINCER_STATUS             = OPEN
CALENDARIZED_IN_SCHEMA    = TRUE
LIVE_CALENDAR_EVENTS      = FALSE
CANONIZED                 = FALSE
SEALED                    = FALSE
REPLAY_READY              = FALSE
LIVE_ENFORCEMENT          = PROHIBITED
PROMOTION                 = PROHIBITED
```

## Final doctrine

```text
TIME LABELS THE REPLAY; IT DOES NOT RULE IT.
LOVE GIVES THE PAYLOAD PURPOSE; IT DOES NOT GRANT CONSENT.
IMAGINATION PROPOSES; IT DOES NOT EXECUTE.
ATTESTATION WITNESSES; IT DOES NOT VALIDATE.
CRISSCROSS LINKS; IT DOES NOT MERGE.
THE PINCER TESTS REPRODUCIBILITY; IT DOES NOT CREATE AUTHORITY.
CANON REQUIRES A SEPARATE, EXPLICIT REPOSITORY ADOPTION.
```
