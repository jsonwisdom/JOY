# GOBLIN_COVER_ART_FARCASTER_SIGNAL_WITNESS_V0_1

## Status

```json
{
  "artifact": "GOBLIN_COVER_ART_FARCASTER_SIGNAL_WITNESS_V0_1",
  "status": "FARCASTER_SIGNAL_WITNESS_USER_RETURNED",
  "verification_status": "OPERATOR_RETURNED_NOT_EXTERNALLY_FETCHED_BY_ASSISTANT",
  "authority": false,
  "no_fake_green": true
}
```

## Farcaster Witness

```json
{
  "network": "Farcaster",
  "cast_hash": "0xcc49d298",
  "handle": "@cmptrwsdm",
  "surface": "first_public_amplification_surface",
  "signal_class": "decentralized_social_amplification",
  "status": "witness_returned"
}
```

## Canonical Spine

```json
{
  "object": {
    "asset": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
    "title": "WITNESS ME, GOBLIN",
    "cid": "ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a",
    "sha256": "0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e"
  },
  "truth": {
    "eas_schema": 1578,
    "identity_attestation_uid": "0x2a4d436665af872f2a72adf08c112b1dd10b7333f5299f4048d96cd887fb6973",
    "asset_attestation_uid": "0x026e0083273494017264e7fd1841a11d3d7f4c690334cf425d7cf87e2a21026b"
  },
  "graph": {
    "github_replay_root": "bb159db68948e0312a81d973533b4079b728f83b"
  },
  "signal": {
    "zora_coin": "base:0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97",
    "zora_tx": "0x8d74015f66d4294c8d559404e672f4fb296d5e858515e9fc4511a40045f72998",
    "farcaster_cast": "0xcc49d298"
  }
}
```

## Classification

```json
{
  "ignition_priority": "AMPLIFY_SEALED_REPLAY_MD",
  "farcaster_signal": true,
  "zora_signal": true,
  "cross_social_amplification": true,
  "external_verification_by_assistant": false,
  "authority": false,
  "no_fake_green": true
}
```

## Boundary

This receipt records the Farcaster cast witness returned by the operator. The assistant did not independently fetch or verify the Farcaster cast content in this receipt. The cast is therefore classified as operator-returned and replay-eligible.

The deterministic spine remains:

```text
Object -> Truth -> Graph -> Signal
```

No synthetic render blocks, non-chain artifacts, or unverifiable generated witness surfaces are admitted into the canonical spine.
