# WITNESS_FINGERPRINT_PROTOCOL_V0_1

## Status

```text
WITNESS_FINGERPRINT_PROTOCOL_INDEXED
OFFLINE_WITNESS_SOURCE_OF_TRUTH
DIGITAL_SIDE_OBSERVER_ONLY
PHYSICAL_GOLD_ANCHOR_ONLY
COMMITMENT_BOUND_TO_PROTOCOL_VERSION
PHASH_TOLERANCE_SET
QR_TRANSFER_COMPRESSED_AND_BLINDED
ANCHOR_MEDIUM_SELECTED_BITCOIN_OP_RETURN_PREFERRED
ANCHOR_EXECUTION_FALSE
AUTHORITY_FALSE
NO_FAKE_GREEN_ACTIVE
```

## Signal Core

This protocol defines how an offline family journal witness may produce a privacy-preserving fingerprint that the Digital ABI Domain can read without creating witness truth.

The digital mirror cannot lie to the physical gold.

The digital side observes.

The offline witnessed receipt remains the source of truth.

## V0.1 Defaults Locked

```text
anchor_medium = bitcoin_op_return_preferred
anchor_execution = false
pHash_hamming_distance_tolerance <= 5
qr_payload_max_chars = 512
paper_size = US_LETTER_OR_A4
minimum_scan_dpi = 300
protocol_version = WITNESS_FINGERPRINT_PROTOCOL_V0_1
```

## Fingerprint Generation

```text
1. Start with an offline family journal receipt.
2. Confirm witness statement is present.
3. Confirm physical execution hash phrase/symbol is present.
4. Capture only safe visual/structural features.
5. Compute perceptual hash over the allowed zones.
6. Blind the fingerprint before any digital transfer.
7. Transfer only blinded payload.
8. Digital side reads only; it never creates witness truth.
```

## Physical Receipt Constraints

```text
paper_size_allowed = US Letter or A4
minimum_scan_dpi = 300
photo_allowed = true if readable and stable
lighting = even, no heavy glare
orientation = upright preferred
color_required = false
private_details = must be redacted or omitted before digital mirroring
```

## Invariant Zones

```text
ZONE_A: Receipt ID
ZONE_B: Date
ZONE_C: Mission Name
ZONE_D: Execution Type checkbox
ZONE_E: Witness Initials / Role
ZONE_F: Physical Execution Hash Phrase / Symbol
ZONE_G: Purpose Layer Review State
ZONE_H: Signature / Mark
```

## pHash Tolerance

```text
pHash_hamming_distance_threshold = 5

PASS if observed_distance <= 5
REVIEW if observed_distance > 5 and <= 10
REJECT if observed_distance > 10
```

Reason: paper ages, phone cameras differ, scanners differ, and zero tolerance creates false negatives.

Manual sovereign re-anchor is required for REVIEW or REJECT states.

## Commitment Structure

```text
commitment = H(blinded_fp || mirror_root || epoch || protocol_version)
```

Required fields:

```text
blinded_fp
mirror_root
epoch
protocol_version
commitment
```

Protocol version is included to block old witness commitments from silently replaying into future protocol versions.

## QR Transfer Rule

```text
QR payload = base64url(blinded_fp || epoch || checksum)
max_payload_chars = 512
plaintext_forbidden = true
metadata_forbidden = true
```

The QR moves only a compressed blinded payload.

It does not carry names, stories, addresses, private details, witness text, or family truth.

## Anchor Medium

```text
selected_anchor_medium = bitcoin_op_return_preferred
anchor_execution = false
alternate_anchor_medium = signed_append_only_feed
ct_log_option = deferred
```

Bitcoin OP_RETURN is selected as the preferred V0.1 anchor medium for sovereignty-oriented commitment anchoring.

This receipt does not broadcast a Bitcoin transaction.

This receipt does not claim an OP_RETURN txid.

The actual anchor requires a future explicit execution receipt.

## Verification Flow

```text
1. Read blinded QR payload.
2. Decode base64url payload.
3. Validate checksum.
4. Verify payload length <= 512 characters.
5. Confirm protocol_version = WITNESS_FINGERPRINT_PROTOCOL_V0_1.
6. Recompute commitment = H(blinded_fp || mirror_root || epoch || protocol_version).
7. Compare pHash distance if a scan/photo is supplied.
8. If hamming_distance <= 5, mark fingerprint_match=true.
9. If hamming_distance > 5, require manual sovereign re-anchor.
10. Digital side may mirror status only.
```

## Leakage Controls

```text
air_gap_required = true
one_way_transfer = true
plaintext_forbidden = true
private_metadata_forbidden = true
sensitive_content_upload_allowed = false
qr_payload_max_chars = 512
blinded_payload_only = true
```

## Hard Boundaries

```text
WITNESS_FINGERPRINT_PROTOCOL != WITNESS_CREATION
WITNESS_FINGERPRINT_PROTOCOL != PURPOSE_LAYER_APPROVAL
WITNESS_FINGERPRINT_PROTOCOL != GOLD_AUTHORIZATION
WITNESS_FINGERPRINT_PROTOCOL != FAMILY_TRUTH_CREATOR
WITNESS_FINGERPRINT_PROTOCOL != BITCOIN_TX_EXECUTED
WITNESS_FINGERPRINT_PROTOCOL != OP_RETURN_TXID
WITNESS_FINGERPRINT_PROTOCOL != AUTHORITY_TRUE
WITNESS_FINGERPRINT_PROTOCOL = READ_ONLY_COMMITMENT_PROTOCOL
```

## Replay Result

```text
witness_fingerprint_protocol=PASS
anchor_medium=bitcoin_op_return_preferred
anchor_execution=false
pHash_hamming_distance_threshold=5
qr_payload_max_chars=512
commitment_bound_to_protocol_version=true
digital_side_observer_only=true
offline_receipt_source_of_truth=true
authority=false
no_fake_green=true
next_packet=WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_V0_1_OR_SIGNED_FEED_FALLBACK
```

## Closing Receipt

Witness Fingerprint Protocol V0.1 indexed.

The mirror cannot lie to the gold.

The digital side observes only.

No plaintext QR.

No metadata leak.

No anchor execution claim.

No OP_RETURN txid claim.

No authority=true.

No fake green.

JAYWISDOM.eth 🟣📓🏈🌹⚙️