# WITNESS_ME_GOBLIN_SECOND_MINT_PLAN_V0_1

## Status

```json
{
  "artifact": "WITNESS_ME_GOBLIN_SECOND_MINT_PLAN_V0_1",
  "status": "SECOND_MINT_PLAN_ROOTED_NOT_EXECUTED",
  "authority": false,
  "no_fake_green": true
}
```

## Purpose

Mint #2 should not be a duplicate of the Goblin Cover Art image. It should mint the sealed replay root as a receipt artifact.

The first mint/signaled artifact established the image/coin surface.

The second mint should establish the replay proof surface.

## Recommended Mint

```json
{
  "mint_number": 2,
  "title": "THE RECEIPTS SAW YOU",
  "artifact_class": "replay_receipt_mint",
  "parent_signal": "WITNESS_ME_GOBLIN",
  "authority": false,
  "no_fake_green": true
}
```

## Canonical Spine

```json
{
  "object": {
    "asset": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
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
    "farcaster_cast": "0xcc49d298"
  }
}
```

## Zora Mint Payload

### Title

```text
THE RECEIPTS SAW YOU
```

### Description

```text
Second signal in the WITNESS ME, GOBLIN lane.

The first goblin looked at the chain.
This one records that the chain looked back.

Object -> Truth -> Graph -> Signal

CID: ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a
EAS Schema: #1578
Replay Root: bb159db68948e0312a81d973533b4079b728f83b
Zora Coin: base:0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97

No fake green.
Proof, not promises.
```

## Boundary

```json
{
  "second_mint_executed": false,
  "requires_user_zora_action": true,
  "no_new_onchain_claim_until_tx_returned": true,
  "authority": false,
  "no_fake_green": true
}
```

## Return Witness After Mint

```text
SECOND_GOBLIN_MINT_TX=0x...
SECOND_GOBLIN_ZORA_URL=https://zora.co/...
```
