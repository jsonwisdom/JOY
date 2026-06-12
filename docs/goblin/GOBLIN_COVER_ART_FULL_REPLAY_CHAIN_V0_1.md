# GOBLIN_COVER_ART_FULL_REPLAY_CHAIN_V0_2

## Status

```json
{
  "artifact": "GOBLIN_COVER_ART_FULL_REPLAY_CHAIN_V0_2",
  "status": "FULL_REPLAY_CHAIN_EXTENDED_WITH_SECOND_SIGNAL",
  "authority": false,
  "no_fake_green": true
}
```

## Object Anchor

```json
{
  "asset": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
  "public_title": "WITNESS ME, GOBLIN",
  "cid": "ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a",
  "sha256": "0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e",
  "binding_class": "sha256_cid_binding",
  "replay_status": "deterministic"
}
```

## Truth / Attestation Spine

```json
{
  "chain": "Base mainnet",
  "schema_number": 1578,
  "schema_uid": "0x79e6535156a3f4652649dff5e8ba5fd47f5d68cc7573203391ea688a0d15703b",
  "identity_attestation_uid": "0x2a4d436665af872f2a72adf08c112b1dd10b7333f5299f4048d96cd887fb6973",
  "identity_attestation_tx": "0x591f8c950f3f1e54b71b1dc2050baaabffded0e2021e347700c85268e8ef75b7",
  "asset_attestation_uid": "0x026e0083273494017264e7fd1841a11d3d7f4c690334cf425d7cf87e2a21026b",
  "asset_attestation_tx": "0xfa8e27fe27b26a48f16d6be9ef223f28a56b762447a0b883aa0ca6f14bb5638a",
  "asset_attestation_from": "0xC345B26094c63C69222Ee775189a3d3eaead5a84",
  "asset_attestation_to": "No recipient",
  "recipient_bound": false,
  "textual_root_anchor": "jaywisdom.base.eth"
}
```

## GitHub / Constellation Spine

```json
{
  "repo": "jsonwisdom/JOY",
  "constellation_entry_commit": "1f905307475483764f32ae9951a29147b60424f3",
  "asset_attestation_receipt_commit": "89def01f8f8a13fdb038a618c68685bbb6f1de8d",
  "zora_witness_commit": "241afb5e573e75af89dc27877cca0c2e9731250f",
  "farcaster_signal_commit": "c4c5cf2b06b4519003c53a5e17ad2c45a714b652",
  "second_mint_plan_commit": "a6b6103c36f965f903ad32616db6465693dfdef2",
  "second_signal_witness_commit": "d76c6ba8e50566742071bb7db8a5ef1f6bc5df1a"
}
```

## Signal Layer / Zora Witness

```json
{
  "zora_tx": "0x8d74015f66d4294c8d559404e672f4fb296d5e858515e9fc4511a40045f72998",
  "zora_coin": "base:0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97",
  "coin_address": "0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97",
  "referrer": "0x829adfedbe565f9885a7ea6bc78912acaef055e2",
  "signal_class": "zora_creator_attention_coin_witness"
}
```

## Farcaster Amplification Witness

```json
{
  "network": "Farcaster",
  "cast_hash": "0xcc49d298",
  "handle": "@cmptrwsdm",
  "signal_class": "decentralized_social_amplification",
  "witness_commit": "c4c5cf2b06b4519003c53a5e17ad2c45a714b652"
}
```

## Second Signal / Zora Witness

```json
{
  "title": "THE RECEIPTS SAW YOU",
  "transaction_hash": "0x0113754fc69dd33a3c7a31595a9d069bfb3a5f143163fab56c63fdeceb2283a7",
  "zora_coin": "base:0x704dce5048ab2593a92a2fa9ab8465ba2a30b8fc",
  "coin_address": "0x704dce5048ab2593a92a2fa9ab8465ba2a30b8fc",
  "referrer": "0x829adfedbe565f9885a7ea6bc78912acaef055e2",
  "parent_coin": "base:0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97",
  "parent_replay_root": "bb159db68948e0312a81d973533b4079b728f83b",
  "signal_class": "second_zora_creator_attention_coin_witness"
}
```

## Deterministic Chain

```text
object: CID + SHA256
  -> truth: EAS schema #1578 + identity/asset attestations
  -> graph: GitHub constellation + replay receipts
  -> signal: Zora coin witness on Base
  -> amplification: Farcaster public signal
  -> second_signal: THE RECEIPTS SAW YOU Zora witness
```

## Boundary

```json
{
  "cid_bound": true,
  "eas_attested": true,
  "github_rooted": true,
  "zora_witness_returned": true,
  "farcaster_witness_returned": true,
  "second_zora_witness_returned": true,
  "recipient_bound": false,
  "external_zora_fetch_by_assistant": false,
  "external_farcaster_fetch_by_assistant": false,
  "authority": false,
  "no_fake_green": true
}
```

This replay chain seals the Goblin Cover Art as a deterministic object-truth-signal artifact and extends it with `THE RECEIPTS SAW YOU` as the second signal.

It does not claim recipient binding where the EAS witness shows `TO: No recipient`, and it does not claim assistant-side external Zora or Farcaster verification.
