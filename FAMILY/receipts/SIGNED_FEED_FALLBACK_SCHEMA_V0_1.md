# SIGNED_FEED_FALLBACK_SCHEMA_V0_1

## Status

```text
SIGNED_FEED_FALLBACK_SCHEMA_INDEXED
AUDIT_PREREQUISITE_REQUIRED
FALLBACK_SECOND_ANCHOR_LAST
SIGNED_FEED_COLD_BACKUP_ONLY
PUBKEY_PLACEHOLDER_BLOCKS_EXECUTION
PAYLOAD_GENERATION_FALSE
TX_SKELETON_GENERATION_FALSE
BROADCAST_FALSE
TXID_CLAIMED_FALSE
AUTHORITY_FALSE
NO_FAKE_GREEN_ACTIVE
```

## Signal Core

This schema defines the signed-feed fallback path after replay audit passes and before any future live anchor path is considered.

Audit first.

Fallback second.

Anchor last.

This receipt does not execute a signed feed.

This receipt does not generate an OP_RETURN payload.

This receipt does not generate a transaction skeleton.

This receipt does not broadcast anything.

This receipt does not claim a txid.

## Prerequisite

```text
REPLAY_AUDIT_OK must be true.
If REPLAY_AUDIT_FAIL, fallback is unreachable.
```

Parent audit:

```text
FAMILY/receipts/REPLAY_AUDIT_SPEC_V0_1.md
FAMILY/receipts/REPLAY_AUDIT_SPEC_INDEX_V0_1.json
FAMILY/receipts/replay_replay_audit_spec_v0_1.sh
```

## Required Fields

```text
feed_url = HTTPS endpoint serving signed feed
pubkey = signer public key as hex or PEM
signature = detached signature over canonical feed payload
epoch = UTC Unix epoch; must be >= audit_epoch
mirror_root = 64 hex chars; must match audit mirror_root if audit mirror_root is present
payload = canonical feed payload
```

## Canonical Feed Payload

```json
{
  "schema_version": "SIGNED_FEED_FALLBACK_SCHEMA_V0_1",
  "feed_id": "string_required",
  "mirror_root": "64_hex_required",
  "epoch": "10_digit_unix_utc_required",
  "audit_ref": "REPLAY_AUDIT_SPEC_V0_1",
  "anchor_execution": false,
  "payload_generation": false,
  "tx_skeleton_generation": false,
  "broadcast": false,
  "txid_claimed": false,
  "authority": false,
  "no_fake_green": true
}
```

## Validation Checks

```text
1. Audit prerequisite:
   - replay_audit_status must equal REPLAY_AUDIT_OK

2. Signature:
   - verify(pubkey, signature, canonical_payload) must pass

3. HTTPS feed:
   - feed_url must start with https://

4. No staleness:
   - abs(now_utc - epoch) <= MAX_SKEW_SECONDS
   - default MAX_SKEW_SECONDS = 900

5. Root consistency:
   - feed.mirror_root == audit.mirror_root when audit.mirror_root exists
   - otherwise feed.mirror_root is recorded as fallback mirror root only

6. Boundary enforcement:
   - anchor_execution=false
   - payload_generation=false
   - tx_skeleton_generation=false
   - broadcast=false
   - txid_claimed=false
   - authority=false
   - no_fake_green=true
```

## Pseudocode Stub

```text
function validate_signed_feed_fallback(input):
    require input.replay_audit_status == "REPLAY_AUDIT_OK"
    require input.feed_url starts_with "https://"
    require input.pubkey present
    require input.signature present
    require input.payload present
    require canonicalize(input.payload) stable
    require verify(input.pubkey, input.signature, canonicalize(input.payload)) == true
    require abs(now_utc - input.payload.epoch) <= 900
    if input.audit_mirror_root exists:
        require input.payload.mirror_root == input.audit_mirror_root
    require input.payload.anchor_execution == false
    require input.payload.payload_generation == false
    require input.payload.tx_skeleton_generation == false
    require input.payload.broadcast == false
    require input.payload.txid_claimed == false
    require input.payload.authority == false
    require input.payload.no_fake_green == true
    return SIGNED_FEED_FALLBACK_OK
```

## Output Format

```text
SIGNED_FEED_FALLBACK_OK
```

or

```text
SIGNED_FEED_FALLBACK_FAIL reason=<explicit_reason>
```

No partial pass is allowed.

## Hard Boundaries

```text
SIGNED_FEED_FALLBACK_SCHEMA != SIGNED_FEED_EXECUTION
SIGNED_FEED_FALLBACK_SCHEMA != ANCHOR_EXECUTION
SIGNED_FEED_FALLBACK_SCHEMA != PAYLOAD_GENERATOR
SIGNED_FEED_FALLBACK_SCHEMA != TX_SKELETON_GENERATOR
SIGNED_FEED_FALLBACK_SCHEMA != BROADCAST
SIGNED_FEED_FALLBACK_SCHEMA != TXID_CLAIM
SIGNED_FEED_FALLBACK_SCHEMA != WALLET_OPERATION
SIGNED_FEED_FALLBACK_SCHEMA != PRIVATE_KEY_REQUEST
SIGNED_FEED_FALLBACK_SCHEMA != SEED_PHRASE_REQUEST
SIGNED_FEED_FALLBACK_SCHEMA != AUTHORITY_TRUE
SIGNED_FEED_FALLBACK_SCHEMA = COLD_BACKUP_VALIDATION_SCHEMA
```

## Replay Result

```text
signed_feed_fallback_schema=PASS
replay_audit_required=true
fallback_second=true
anchor_last=true
max_skew_seconds=900
feed_url_https_required=true
signature_required=true
mirror_root_consistency_required=true
signed_feed_execution=false
payload_generation=false
tx_skeleton_generation=false
broadcast=false
txid_claimed=false
authority=false
no_fake_green=true
next_packet=SIGNED_FEED_FALLBACK_TEST_VECTOR_V0_1_OR_ANCHOR_PATH_REVIEW
```

## Closing Receipt

Signed Feed Fallback Schema V0.1 indexed.

Audit first.

Fallback second.

Anchor last.

Cold backup only.

No payload.

No tx skeleton.

No broadcast.

No txid.

No authority=true.

No fake green.

JAYWISDOM.eth 🟣⚙️