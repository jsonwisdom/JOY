# GOBLIN_COVER_ART_EAS_ASSET_ATTESTATION_RECEIPT_V0_1

## Status

```json
{
  "artifact": "GOBLIN_COVER_ART_EAS_ASSET_ATTESTATION_RECEIPT_V0_1",
  "status": "ONCHAIN_ATTESTATION_RECORDED",
  "chain": "Base mainnet",
  "authority": false,
  "no_fake_green": true
}
```

## Attestation Witness

```json
{
  "schema_number": 1578,
  "schema_uid": "0x79e6535156a3f4652649dff5e8ba5fd47f5d68cc7573203391ea688a0d15703b",
  "attestation_uid": "0x026e0083273494017264e7fd1841a11d3d7f4c690334cf425d7cf87e2a21026b",
  "attestation_tx": "0xfa8e27fe27b26a48f16d6be9ef223f28a56b762447a0b883aa0ca6f14bb5638a",
  "created": "2026-06-11T21:17:41-05:00",
  "expiration": "Never",
  "revoked": false,
  "revocable": true,
  "from": "0xC345B26094c63C69222Ee775189a3d3eaead5a84",
  "to": "No recipient",
  "referenced_attestation": "No reference"
}
```

## Decoded Data

```json
{
  "precedentId": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
  "Court": "Goblin Court",
  "RootAnchor": "jaywisdom.base.eth",
  "lineageAnchor": "ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a",
  "receiptHash": "0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e",
  "githubCommit": "1f905307475483764f32ae9951a29147b60424f3",
  "ruling": "Goblin cover art CID is bound to image SHA-256 and rooted in the Goblin Constellation.",
  "authority": false
}
```

## Classification

```json
{
  "asset": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
  "attestation_type": "cover_art_asset_attestation",
  "asset_cid": "ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a",
  "asset_sha256": "0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e",
  "recipient_bound": false,
  "textual_root_anchor": "jaywisdom.base.eth",
  "binding_strength": "TEXTUAL_ROOT_ANCHOR_WITH_SIGNER_ATTESTATION_NO_RECIPIENT",
  "authority": false,
  "no_fake_green": true
}
```

## Boundary

This receipt records the executed EAS asset attestation for the Goblin Cover Art. The decoded data correctly binds the asset id, CID, SHA-256, constellation commit, and ruling under schema #1578.

The attestation screen shows `TO: No recipient`; therefore this is not classified as recipient-bound to a Jay wallet address. It remains a valid onchain asset attestation made by the signing wallet and textually anchored to `jaywisdom.base.eth`.
