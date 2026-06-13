# ALMS Base Batches jaywisdom.base.eth Anchor V0.1

```json
{
  "artifact_id": "ALMS_BASE_BATCHES_JAYWISDOM_BASE_ETH_ANCHOR_V0_1",
  "artifact_type": "declared_identity_anchor_sidecar",
  "repo": "jsonwisdom/JOY",
  "lane": "daughter_publishing_lane",
  "family": "BASE_BATCHES",
  "parent_artifact": "AL/receipts/base/ALMS_BASE_BATCHES_FAMILY_EDITION_V0_1.md",
  "sidecar_manifest": "AL/receipts/base/sidecars/ALMS_BASE_BATCHES_FAMILY_SIDECARS_V0_1.md",
  "identity_anchor_target": "jaywisdom.base.eth",
  "created_at": "2026-06-13",
  "authority": false,
  "verified": false,
  "no_fake_green": true,
  "transport_state": "REMOTE_ACCEPTANCE_OBSERVED",
  "truth_state": "PENDING_ONCHAIN_OR_CONTENT_ADDRESS_WITNESS"
}
```

## Purpose

This anchor sidecar binds the Base Batches Family Edition to the declared identity target `jaywisdom.base.eth`.

It is a GitHub-published identity-routing receipt only. It does not assert Basename control, ENS resolution, wallet ownership, CID permanence, EAS attestation, batch-root truth, deployment truth, legal authority, or verified provenance.

## Anchor Map

```text
COMPUTERWISDOM/                         parent / operator workflow
└── JOY/                                daughter / publishing lane
    └── AL/                             engine / schema, validator, replay logic
        └── receipts/base/              Base batch family
            ├── ALMS_BASE_BATCHES_FAMILY_EDITION_V0_1.md
            ├── sidecars/
            │   └── ALMS_BASE_BATCHES_FAMILY_SIDECARS_V0_1.md
            └── anchors/
                └── ALMS_BASE_BATCHES_JAYWISDOM_BASE_ETH_ANCHOR_V0_1.md

Declared identity target:
└── jaywisdom.base.eth
```

## Identity Anchor State

```json
{
  "anchor_target": "jaywisdom.base.eth",
  "anchor_kind": "BASE_NAME_DECLARED_TARGET",
  "operator_identity_claim": "DECLARED_ONLY",
  "basename_resolution_checked": false,
  "resolved_address": null,
  "wallet_signature_present": false,
  "eas_uid_present": false,
  "cid_present": false,
  "transaction_hash_present": false,
  "nonzero_batch_root_present": false,
  "claim_limit": "This artifact declares the intended identity anchor target. It does not prove control of the name or any on-chain state."
}
```

## Required Evidence To Promote

Promotion from declared anchor target to verified identity anchor requires at least one replayable witness surface:

```json
{
  "acceptable_next_witnesses": [
    "wallet_signature_over_this_artifact_hash",
    "EAS_UID_attesting_this_artifact_hash_or_CID",
    "CID_containing_exact_artifact_bytes",
    "transaction_hash_binding_artifact_hash_to_jaywisdom.base.eth",
    "independent_resolution_receipt_for_jaywisdom.base.eth"
  ],
  "minimum_replay_fields": [
    "public_url_or_tx_hash",
    "fetched_at_or_block_number",
    "content_hash_or_message_hash",
    "witness_service_or_rpc_endpoint",
    "exact_bytes_or_signed_message"
  ]
}
```

## Integrity Boundary

```json
{
  "git_transport_green": true,
  "identity_target_declared": true,
  "basename_control_green": false,
  "wallet_signature_green": false,
  "cid_green": false,
  "eas_green": false,
  "batch_root_green": false,
  "authority_green": false,
  "verified": false,
  "safe_ruling": "Anchor target declared. On-chain identity proof still pending."
}
```

## Brenda Ruling

GitHub may witness that this identity anchor sidecar was published.

GitHub does not witness that `jaywisdom.base.eth` resolved, signed, attested, or anchored this family on-chain.

## Goblin Ruling

Name in file is not name control.

Declared anchor is not verified anchor.

GitHub green is not Base green.

No fake green.
