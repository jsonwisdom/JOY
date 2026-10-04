# MR_WISDOM — Family Information Flow Policy V0.1

**Status:** review candidate  
**Authority:** false  
**Purpose:** make family communications, directionality, ordering, timestamps, and replay visible without turning roles into authority.

## Core Model

Family continuity is represented as timestamped information flow between bounded roles.

```text
ACTOR
  ↓
PURPOSE
  ↓
PAYLOAD
  ↓
DESTINATION
  ↓
RECEIVED_AT
  ↓
REVIEW / RESPONSE
  ↓
REPLAY RECEIPT
```

Every movement must preserve:

- `from`
- `to`
- `purpose`
- `sent_at`
- `received_at` when observed
- `payload_hash` when bytes are available
- `source_surface`
- `response_surface` when applicable
- `authority_created: false`

## Daddy / Mr. Wisdom Role

MR_WISDOM is a builder/operator lane. It may package public-safe family or project material for another family lane to review.

MR_WISDOM does not silently speak for another family member and does not convert a family relationship into technical, legal, financial, medical, parental, or publishing authority.

## Current Family Flow

```text
MR_WISDOM / DADDY
  |
  | public-safe payload
  | timestamp + purpose + receipt
  v
HEIDEE / JOYSPACE
  |
  | child-facing selection / design
  v
MRS_WISDOM
  |
  | observer / steward review when human-directed
  v
JOYSPACE RESPONSE
```

The HEIDEE repository remains the child-specific JoySpace implementation. JOY remains the shared family/protection pattern.

## Mary D External Review Lane

After a payload is prepared, MR_WISDOM may submit the exact manifest, download list, hashes, or changed-file list to a user-operated external reviewer such as a Grok Mary D bot.

Mary D review output is classified as:

```text
RECOMMENDATION
OBSERVATION
QUESTION
DELTA
HOLD
```

It is never promoted automatically to fact or authority.

A recommendation may return to MR_WISDOM or be routed to another family lane only by an explicit human decision.

## Scene Grammar

The movie/game layer may render the same flow as scenes:

```text
SCENE 1 — DADDY BUILDS
SCENE 2 — DADDY PACKS PAYLOAD
SCENE 3 — HEIDEE / JOYSPACE RECEIVES
SCENE 4 — MOM OBSERVES / HELPS
SCENE 5 — MARY D REVIEWS THE EXACT PAYLOAD
SCENE 6 — RESPONSE RETURNS
SCENE 7 — REPLAY COMPARES BEFORE / AFTER
```

The scene is presentation. The receipt is evidence.

## Authentication / Platform Event Policy

Login and platform events may be recorded as machine observations:

```text
platform
account_label
observed_at
device_or_client_if_provided_by_platform
source_ip_if_provided_by_platform
auth_result
risk_signal_if_provided_by_platform
raw_event_hash
```

Unknown location, device, IP, or actor remains `UNKNOWN`.

Passwords are not treated as permanent proof of identity. Strong authentication should use platform-supported protections such as password managers, MFA/passkeys, device/session review, and revocation when compromise is suspected.

### Security escalation

A suspicious login may produce a **law-enforcement-ready incident package**, but JOY must not automatically accuse, identify, locate, or dispatch police against a person or device.

```text
SUSPICIOUS_AUTH_EVENT
  ↓
PRESERVE RAW EVIDENCE
  ↓
HASH + TIMESTAMP
  ↓
ACCOUNT / PLATFORM SECURITY ACTION
  ↓
HUMAN REVIEW
  ↓
OPTIONAL REPORT TO APPROPRIATE AUTHORITY
```

This prevents an automated false positive from becoming a real-world accusation.

## Government Mirror / Gen-Z Question Lane

Public government artifacts may be mirrored forward as versioned, source-linked technical material so a person can ask a real-life question against the exact public state observed at that time.

The system should return:

- the source artifact
- its timestamp/version
- what changed
- what is known
- what is unknown
- applicable technical standards when established
- a response or `HOLD`

No government source is assumed correct merely because it is official; no source is declared unlawful merely because it disagrees with another source. Differences become replayable DELTAs.

## Invariants

```text
FAMILY_FIRST = true
DIRECTIONALITY_EXPLICIT = true
TIMESTAMPS_REQUIRED_WHEN_OBSERVED = true
NO_SILENT_INFERENCE = true
NO_AUTOMATIC_ACCUSATION = true
NO_AUTOMATIC_POLICE_DISPATCH = true
STORY_IS_NOT_EVIDENCE = true
AUTHORITY_CREATED = false
```
