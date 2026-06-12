# THE_RECEIPTS_SAW_YOU_ZORA_WITNESS_V0_1

## Status

```json
{
  "artifact": "THE_RECEIPTS_SAW_YOU_ZORA_WITNESS_V0_1",
  "status": "SECOND_MINT_ZORA_WITNESS_USER_RETURNED",
  "verification_status": "OPERATOR_RETURNED_NOT_EXTERNALLY_FETCHED_BY_ASSISTANT",
  "authority": false,
  "no_fake_green": true
}
```

## Zora Witness

```json
{
  "chain": "Base",
  "title": "THE RECEIPTS SAW YOU",
  "transaction_hash": "0x0113754fc69dd33a3c7a31595a9d069bfb3a5f143163fab56c63fdeceb2283a7",
  "zora_coin": "base:0x704dce5048ab2593a92a2fa9ab8465ba2a30b8fc",
  "coin_address": "0x704dce5048ab2593a92a2fa9ab8465ba2a30b8fc",
  "referrer": "0x829adfedbe565f9885a7ea6bc78912acaef055e2"
}
```

## Parent Lineage

```json
{
  "parent_lane": "WITNESS_ME_GOBLIN",
  "parent_coin": "base:0xa67faf61779c5c9adfd08ea6eaea60a27f8f2d97",
  "parent_zora_tx": "0x8d74015f66d4294c8d559404e672f4fb296d5e858515e9fc4511a40045f72998",
  "full_replay_root_commit": "bb159db68948e0312a81d973533b4079b728f83b",
  "second_mint_plan_commit": "a6b6103c36f965f903ad32616db6465693dfdef2"
}
```

## Classification

```json
{
  "mint_number": 2,
  "artifact_class": "replay_receipt_signal_mint",
  "object_truth_graph_signal_inheritance": true,
  "zora_signal": true,
  "operator_returned": true,
  "external_verification_by_assistant": false,
  "authority": false,
  "no_fake_green": true
}
```

## Boundary

This receipt records the second Zora witness returned by the operator for `THE RECEIPTS SAW YOU`. The assistant did not independently fetch or verify the Zora page or Base transaction in this receipt. The witness is therefore classified as operator-returned and replay-eligible.

```text
Object -> Truth -> Graph -> Signal -> Second Signal
```
