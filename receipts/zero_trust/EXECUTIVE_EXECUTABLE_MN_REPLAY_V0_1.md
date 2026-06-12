# EXECUTIVE EXECUTABLE — MINNESOTA FIRST REPLAY PIPELINE

Timestamp: 2026-06-12 America/Chicago
Artifact ID: EXECUTIVE_EXECUTABLE_MN_REPLAY_V0_1
Operator: Jay Wisdom
Public Name: jaywisdom.base.eth
Repository: jsonwisdom/JOY
Lane: ZERO_TRUST_MN_AUDIT
Active Packet: ALPHA_DEED_001

## Purpose

Establish a Minnesota-first civic audit pipeline that converts claims into requests, requests into records, records into preserved evidence, and preserved evidence into replayable verification.

This artifact is operational. It does not assert government authority, judicial authority, agency fault, verified wrongdoing, or evidentiary completion.

## Core Invariants

```json
{
  "authority": false,
  "verification_over_narrative": true,
  "no_fake_green": true,
  "observable_facts_only": true,
  "replay_before_promotion": true,
  "public_name": "jaywisdom.base.eth"
}
```

## State Machine

```text
UNKNOWN
  ↓
CLAIMED
  ↓
REQUESTED
  ↓
RECEIVED
  ↓
PRESERVED
  ↓
VERIFIED
  ↓
REPLAYABLE
```

## Current Active Packet

```json
{
  "packet": "ALPHA_DEED_001",
  "agency": "Minnesota DEED",
  "subject_lane": "Unemployment Insurance Treasury Offset Program records",
  "state": "REQUESTED",
  "mode": "PASSIVE_WITNESS",
  "watch_status": "ACTIVE",
  "event_detected": false,
  "state_transition": false,
  "verified_claims": 0,
  "inference": false,
  "authority": false
}
```

## Replay Chain

```text
Request Submitted
  ↓
Agency Response OR Documented Non-Response Event
  ↓
Records Received
  ↓
Records Preserved
  ↓
Verification Started
  ↓
Verification Completed
  ↓
Replayable Public Record
```

## Authorized Actions

1. Preserve request receipts.
2. Preserve timestamps.
3. Record inbound agency communications.
4. Record records-production events.
5. Record non-response events only when documented.
6. Preserve local chain of custody.
7. Classify observable state transitions.
8. Produce replay artifacts only after preservation.

## Unauthorized Actions

- Infer missing facts.
- Assign motive.
- Assert agency fault without records.
- Assert compliance without records.
- Assert non-compliance without records or deadline analysis.
- Promote REQUESTED to RECEIVED.
- Promote RECEIVED to VERIFIED.
- Treat silence as a finding.
- Imply authority.
- Claim green without replay.

## Ledger Distinctions

```text
REQUESTED ≠ RECEIVED
RECEIVED ≠ VERIFIED
REPORTED ≠ CONFIRMED
SILENCE ≠ FINDING
```

## Passive Witness Hold

```json
{
  "action": "HOLD",
  "analysis": "IDLE",
  "evidence_intake": "OPEN",
  "polling": false,
  "stored_baseline_in_chat": false,
  "custody": "OFFLINE_LOCAL",
  "perimeter": "INTACT"
}
```

## Non-Response Event Rule

A non-response event may be logged only as an observation that no response was received as of a specific observation date. It is not, by itself, a finding of violation, motive, or misconduct.

Template:

```json
{
  "event": "NON_RESPONSE_EVENT",
  "packet": "ALPHA_DEED_001",
  "request_date": "YYYY-MM-DD",
  "observation_date": "YYYY-MM-DD",
  "response_received": false,
  "notes": "No agency response observed as of observation date.",
  "authority": false,
  "finding": false
}
```

## Success Criteria

A claim becomes replayable only when an independent observer can:

1. Review the request.
2. Review the response or documented non-response event.
3. Review the records, if produced.
4. Review the preservation chain.
5. Recompute or inspect the same evidence path.
6. Reach the same state classification from the same materials.

## Current Directive

```json
{
  "packet": "ALPHA_DEED_001",
  "state": "REQUESTED",
  "mode": "PASSIVE_WITNESS",
  "directive": "HOLD",
  "next_transition": "INBOUND_RECEIPT_OR_DOCUMENTED_NON_RESPONSE_EVENT",
  "authority": false,
  "no_fake_green": true
}
```

No receipt.  
No promotion.  
No conclusion.  
Replay waits for signal.
