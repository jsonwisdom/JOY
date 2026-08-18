# RFC 0001: Audit Node Contract

**Status:** DRAFT  
**Version:** 0.1.0  
**Repository:** `jsonwisdom/JOY`  
**Purpose:** Define the immutable evidence anchor used by ReplayOS-compatible systems.

## 1. Core correction

An immutable object cannot contain an append-only array that changes over time without changing its bytes and digest. Therefore RFC 0001 separates:

1. **Audit Node Core** — immutable, canonicalized, hashed once.
2. **Replay Event Receipt** — append-only records that reference the immutable node digest.
3. **Policy Record** — configurable deployment behavior; never embedded as evidence truth.

```text
AUDIT_NODE_CORE        = IMMUTABLE
REPLAY_EVENT_RECEIPTS  = APPEND_ONLY
POLICY                 = VERSIONED_CONFIGURATION
AUTHORITY_CREATED      = FALSE
```

## 2. Audit Node Core

Required fields:

- `version`
- `node_id`
- `event_id`
- `observed_at`
- `recorded_at`
- `source_type`
- `source_ref`
- `content`
- `consent_snapshot`
- `artifact_fingerprint`
- `authority_created`

The node records an observation or claim. It does not certify truth, intent, guilt, identity, or authority.

## 3. Consent snapshot

The snapshot is frozen at node creation. Current consent is checked separately at replay time.

```text
ORIGINAL_SCOPE_COMPATIBLE = required
CURRENT_REPLAY_PERMISSION = required
```

Prior consent never creates future permission.

## 4. Canonicalization

Implementations MUST use RFC 8785 JSON Canonicalization Scheme before computing the node digest.

The digest input is the exact canonical UTF-8 byte sequence of the Audit Node Core excluding any external envelope signature.

## 5. Replay Event Receipt

Replay history is external to the immutable node. Each event receipt contains:

- `event_version`
- `replay_event_id`
- `node_id`
- `node_digest`
- `recorded_at`
- `scope_used`
- `result_type`
- `authority_check`
- `previous_event_digest`
- `event_digest`

No event may modify the Audit Node Core or a prior event.

## 6. Invariants

1. Observation is not interpretation.
2. Completion is not consent.
3. Past permission is not future permission.
4. Trust is not capacity.
5. Care role is not a labor pool.
6. Knowledge is not authority.
7. Replay output is not a new fact.
8. Replay output is not new authority.
9. Replay output is not new consent.
10. Withdrawal is not system failure.

## 7. Validation boundary

JSON Schema validates structure. Runtime code must separately verify:

- RFC 8785 canonical bytes
- node digest
- referenced artifact digest
- optional signature
- current consent
- append-only replay chain continuity

## 8. Status

```text
RFC_STATUS            = DRAFT
SCHEMA_STATUS         = CANDIDATE
REFERENCE_CORPUS      = STARTED
CI_STATUS             = CONFIGURED_NOT_YET_OBSERVED
PRODUCTION_READY      = FALSE
AUTHORITY_CREATED     = FALSE
```
