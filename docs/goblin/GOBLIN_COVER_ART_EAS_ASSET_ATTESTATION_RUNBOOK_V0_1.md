# GOBLIN_COVER_ART_EAS_ASSET_ATTESTATION_RUNBOOK_V0_1

## Status

```json
{
  "artifact": "GOBLIN_COVER_ART_EAS_ASSET_ATTESTATION_RUNBOOK_V0_1",
  "status": "RUNBOOK_ROOTED_NOT_EXECUTED",
  "authority": false,
  "no_fake_green": true
}
```

## Purpose

This runbook prepares an EAS asset attestation for the Goblin Cover Art using the already registered Meme Court / Goblin Court schema `#1578`.

This avoids registering a second schema before the asset is rooted. The attestation reuses the existing precedent schema to record the cover art as a witnessable asset node.

## Existing Schema

```json
{
  "schema_number": 1578,
  "schema_uid": "0x79e6535156a3f4652649dff5e8ba5fd47f5d68cc7573203391ea688a0d15703b",
  "revocable": true,
  "schema_fields": [
    "string precedentId",
    "string Court",
    "string RootAnchor",
    "string lineageAnchor",
    "bytes32 receiptHash",
    "string githubCommit",
    "string ruling",
    "bool authority"
  ]
}
```

## Asset Being Attested

```json
{
  "asset_id": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
  "cid": "ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a",
  "sha256": "0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e",
  "constellation_commit": "1f905307475483764f32ae9951a29147b60424f3"
}
```

## EAS UI Path

Open schema `#1578` on Base EAS Scan and click:

```text
Attest with Schema
```

## Field Values

Enter the following values exactly, one field at a time.

### Field 1 — precedentId

```text
GOBLIN_COVER_ART_SELFIE_STYLE_V0_1
```

### Field 2 — Court

```text
Goblin Court
```

### Field 3 — RootAnchor

```text
ipfs://bafkreigkmn34k444ruy25lvw6ph6goq4lr246qku4uoglkz46kqdfzlf5a
```

### Field 4 — lineageAnchor

```text
jaywisdom.base.eth > Goblin Constellation > Cover Art
```

### Field 5 — receiptHash

```text
0x451d5406c72a0dbce137ea0962d60c6200ad0f7972fb77ab94e27b83c4062e8e
```

### Field 6 — githubCommit

```text
1f905307475483764f32ae9951a29147b60424f3
```

### Field 7 — ruling

```text
Goblin cover art CID is bound to image SHA-256 and rooted in the Goblin Constellation.
```

### Field 8 — authority

```text
false
```

## Wallet Confirmation Rules

Before confirming, verify:

```json
{
  "chain": "Base mainnet",
  "schema": "#1578",
  "attestation_type": "Onchain Attestation",
  "value": "0 or gas only",
  "token_approval": false,
  "permit": false,
  "swap": false,
  "bridge": false,
  "spending_permission": false
}
```

Reject the transaction if the wallet shows token approval, permit, swap, bridge, spending permission, wrong chain, or nonzero value transfer beyond gas.

## Evidence To Return

After execution, return:

```text
GOBLIN_ART_ATTESTATION_UID=0x...
GOBLIN_ART_ATTESTATION_TX=0x...
```

## Court State

```json
{
  "selected_ignition": "EAS_ASSET_ATTESTATION",
  "asset_node": "GOBLIN_COVER_ART_SELFIE_STYLE_V0_1",
  "schema_reuse": "#1578",
  "execution_status": "PENDING_OPERATOR_ATTESTATION",
  "authority": false,
  "no_fake_green": true
}
```
