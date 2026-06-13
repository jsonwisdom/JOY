# ALMS Base Batches Family Edition V0.1

```json
{
  "artifact_id": "ALMS_BASE_BATCHES_FAMILY_EDITION_V0_1",
  "artifact_type": "family_edition_receipt",
  "repo": "jsonwisdom/JOY",
  "lane": "daughter_publishing_lane",
  "created_at": "2026-06-13",
  "authority": false,
  "verified": false,
  "no_fake_green": true,
  "current_state": "PASSIVE_OBSERVATION",
  "transport_state": "REMOTE_ACCEPTANCE_OBSERVED",
  "truth_state": "PENDING_CID_OR_EAS_ANCHOR",
  "operator_parent_commit": "2ad764f9e4ef4f2c24e7bae276039e3bda2b7060",
  "daughter_receipt_commit": "f46f60b1c6f44e686a0abbecdc97c028d0c01ba6"
}
```

## Purpose

This receipt defines the Base batch family map without promoting GitHub transport into content-addressed truth.

GitHub acceptance proves delivery to the remote repository.
It does not prove IPFS permanence, EAS attestation, CID availability, batch-root validity, or authority.

## Family Map

```text
COMPUTERWISDOM/                 parent / operator workflow
└── JOY/                        daughter / publishing lane
    └── AL/                     engine / schema, validator, replay logic
        └── receipts/base/      Base batch receipt family
```

## Base Batch Family Members

```json
{
  "family": "BASE_BATCHES",
  "edition": "FAMILY_EDITION_V0_1",
  "members": [
    {
      "name": "operator_parent_route",
      "repo": "jsonwisdom/COMPUTERWISDOM",
      "commit": "2ad764f9e4ef4f2c24e7bae276039e3bda2b7060",
      "state": "REMOTE_ACCEPTANCE_OBSERVED",
      "claim_limit": "operator workflow route exists on GitHub"
    },
    {
      "name": "joy_daughter_receipt_lane",
      "repo": "jsonwisdom/JOY",
      "commit": "f46f60b1c6f44e686a0abbecdc97c028d0c01ba6",
      "state": "REMOTE_ACCEPTANCE_OBSERVED",
      "claim_limit": "daughter publishing lane accepted ALMS Base receipt files"
    },
    {
      "name": "al_engine_gate",
      "repo": "jsonwisdom/JOY",
      "path": "AL/",
      "state": "SCHEMA_GATE_DECLARED",
      "claim_limit": "publication lane is structured around AL validation, not authority"
    }
  ]
}
```

## Integrity Boundary

```json
{
  "git_transport_green": true,
  "cid_green": false,
  "eas_green": false,
  "authority_green": false,
  "deployment_green": false,
  "safe_ruling": "GitHub remote accepted the family structure; truth anchors remain pending."
}
```

## Brenda Ruling

Remote acceptance is recorded for the parent and daughter layers.
No CID, EAS UID, transaction hash, or nonzero batch root is inferred.

## Goblin Ruling

GitHub green is not EAS green.
A push is a delivery receipt, not a truth receipt.
The family map is cold until bytes are anchored and replayed.

## Next Gate

Inbound DEED artifact may enter this family only as an observed surface unless accompanied by replayable bytes, hash, CID, EAS UID, transaction hash, or equivalent external witness.
