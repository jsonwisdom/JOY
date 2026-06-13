# ALMS Base Batches Family Sidecars V0.1

```json
{
  "artifact_id": "ALMS_BASE_BATCHES_FAMILY_SIDECARS_V0_1",
  "artifact_type": "family_sidecar_manifest",
  "repo": "jsonwisdom/JOY",
  "lane": "daughter_publishing_lane",
  "parent_artifact": "AL/receipts/base/ALMS_BASE_BATCHES_FAMILY_EDITION_V0_1.md",
  "created_at": "2026-06-13",
  "authority": false,
  "verified": false,
  "no_fake_green": true,
  "current_state": "PASSIVE_OBSERVATION",
  "transport_state": "REMOTE_ACCEPTANCE_OBSERVED",
  "truth_state": "PENDING_CID_OR_EAS_ANCHOR"
}
```

## Purpose

This sidecar manifest extends the Base Batches Family Edition with explicit companion lanes.

Sidecars preserve relationship metadata without promoting GitHub delivery into CID permanence, EAS attestation, batch-root truth, deployment truth, or legal authority.

## Sidecar Map

```text
COMPUTERWISDOM/                         parent / operator workflow
└── JOY/                                daughter / publishing lane
    └── AL/                             engine / schema, validator, replay logic
        └── receipts/base/              Base batch family
            ├── ALMS_BASE_BATCHES_FAMILY_EDITION_V0_1.md
            └── sidecars/
                └── ALMS_BASE_BATCHES_FAMILY_SIDECARS_V0_1.md
```

## Family Sidecars

```json
{
  "family": "BASE_BATCHES",
  "edition": "FAMILY_SIDECARS_V0_1",
  "sidecars": [
    {
      "sidecar_id": "PARENT_ROUTE_SIDECAR",
      "surface": "COMPUTERWISDOM_PARENT_ROUTE",
      "repo": "jsonwisdom/COMPUTERWISDOM",
      "commit": "2ad764f9e4ef4f2c24e7bae276039e3bda2b7060",
      "state": "REMOTE_ACCEPTANCE_OBSERVED",
      "claim_limit": "operator route exists on GitHub; no content truth is inferred"
    },
    {
      "sidecar_id": "JOY_DAUGHTER_LANE_SIDECAR",
      "surface": "JOY_DAUGHTER_PUBLISHING_LANE",
      "repo": "jsonwisdom/JOY",
      "commit": "f46f60b1c6f44e686a0abbecdc97c028d0c01ba6",
      "state": "REMOTE_ACCEPTANCE_OBSERVED",
      "claim_limit": "daughter receipt lane exists on GitHub; no anchor truth is inferred"
    },
    {
      "sidecar_id": "AL_ENGINE_GATE_SIDECAR",
      "surface": "AL_SCHEMA_VALIDATOR_REPLAY_GATE",
      "repo": "jsonwisdom/JOY",
      "path": "AL/",
      "state": "DECLARED_GATE",
      "claim_limit": "engine route declared; validation still requires replayable bytes"
    },
    {
      "sidecar_id": "BASE_ANCHOR_PENDING_SIDECAR",
      "surface": "CID_EAS_BATCH_ROOT_PENDING",
      "repo": "jsonwisdom/JOY",
      "state": "YELLOW_PENDING",
      "claim_limit": "no CID, EAS UID, transaction hash, or nonzero batch root is asserted"
    }
  ]
}
```

## Integrity Boundary

```json
{
  "git_transport_green": true,
  "sidecar_manifest_green": true,
  "cid_green": false,
  "eas_green": false,
  "batch_root_green": false,
  "authority_green": false,
  "deployment_green": false,
  "verified": false,
  "safe_ruling": "Sidecars map family relationships only. They do not prove truth anchors."
}
```

## Brenda Ruling

Sidecars are admitted as relationship metadata.

They can organize receipt lanes, parent routes, daughter routes, and engine gates.
They cannot promote an observed GitHub push into content-addressed permanence.

## Goblin Ruling

Sidecar exists does not mean anchor exists.
Anchor pending does not mean failure.
GitHub green is not EAS green.

No fake green.
No authority creep.
No truth-by-folder-name.

## Next Gate

Inbound DEED artifact may attach to this family through a sidecar only as an observed surface unless accompanied by exact bytes, stable serialization, content hash, CID, EAS UID, transaction hash, or another replayable external witness.
