# CRP Replay Registry Update Protocol v0.1

## Purpose

Define who may update the replay registry, how updates are encoded, and which invariants must hold so that:

- Data stays append-only.
- Validation remains deterministic and replayable.
- Governance is explicit, inspectable, and non-inflationary.

This protocol governs `CRP_REPLAY_REGISTRY_V0_1.json` under schema `CRP_REPLAY_REGISTRY_SCHEMA_V0_1.json`.

## Core invariants

- **I1: Append only** — Existing entries are never mutated or deleted. All changes are realized as new entries or superseding entries.
- **I2: `authority == false`** — The registry never self-elevates to an ultimate source of truth.
- **I3: `no_fake_green == true`** — No entry may claim GREEN without a replayable, externally verifiable basis.
- **I4: Deterministic validation** — Every update must validate against the current schema version.
- **I5: Git-visible history** — Every update is a Git commit touching only:
  - `artifacts/crp/CRP_REPLAY_REGISTRY_V0_1.json`
  - Optional schema or protocol files when versioning.

## Key enums and fields

These are normative for V0.1. Future versions may extend but not break them.

### Registry state

`current_registry_state` values:

- `EMPTY` — no entries or only placeholder.
- `ACTIVE` — at least one non-placeholder entry.
- `SEALED` — no further entries allowed under this version.

### Replay outcome

`replay_outcome` values:

- `UNKNOWN` — no replay performed or not reported.
- `YELLOW_NO_BYTES` — witness lacked raw seed bytes.
- `YELLOW_INCOMPLETE` — partial replay, missing steps.
- `GREEN_MATCH` — replayed and hash matched.
- `RED_MISMATCH` — replayed and hash did not match.

### Witness scope

`witness_scope` values:

- `SELF` — same actor that produced the seed.
- `INDEPENDENT` — cryptographically or operationally distinct actor.
- `AGGREGATOR` — summarizes multiple underlying witnesses.

### Witness claim

`witness_claim` values:

- `OBSERVED_ONLY` — saw claims, did not replay.
- `REPLAY_EXECUTED` — performed full canonical replay.
- `ATTESTED_ELSEWHERE` — relies on external attestation such as EAS or notarized log.

## Version lineage and timestamps

Each entry must include:

- `schema_version`, for example `CRP_REPLAY_REGISTRY_SCHEMA_V0_1`
- `protocol_version`, for example `CRP_REPLAY_REGISTRY_UPDATE_PROTOCOL_V0_1`
- `registry_entry_created_at`, as an ISO-8601 UTC timestamp string
- `registry_entry_commit_sha`, the Git commit SHA that introduced this entry

These fields bind the data row to the schema/protocol version and to a specific Git commit.

## Entry structure

Each entry in `entries[]` must conform to the following normative V0.1 shape:

```json
{
  "seed_cid": "string | null",
  "seed_hash": "string | null",
  "canonicalization_rule": "string | null",
  "witnesses": [
    {
      "witness_id": "string",
      "witness_scope": "SELF | INDEPENDENT | AGGREGATOR",
      "witness_claim": "OBSERVED_ONLY | REPLAY_EXECUTED | ATTESTED_ELSEWHERE",
      "replay_outcome": "UNKNOWN | YELLOW_NO_BYTES | YELLOW_INCOMPLETE | GREEN_MATCH | RED_MISMATCH",
      "notes": "string | null"
    }
  ],
  "sealed": false,
  "current_registry_state": "EMPTY | ACTIVE | SEALED",
  "schema_version": "CRP_REPLAY_REGISTRY_SCHEMA_V0_1",
  "protocol_version": "CRP_REPLAY_REGISTRY_UPDATE_PROTOCOL_V0_1",
  "registry_entry_created_at": "2026-06-11T20:00:00Z",
  "registry_entry_commit_sha": "be38d44f308885ec6c813ca1260cf259ecefe5ec",
  "authority": false,
  "no_fake_green": true
}
```

Global top-level fields:

```json
{
  "artifact": "CRP_REPLAY_REGISTRY_V0_1",
  "version": "0.1",
  "authority": false,
  "no_fake_green": true,
  "append_only": true,
  "entries": []
}
```

## Allowed operations

### OP1: Append new entry

Description: Add a new registry entry for a seed or witness set.

Preconditions:

- `current_registry_state != "SEALED"`.
- New entry validates against schema.
- `authority == false` and `no_fake_green == true` in both:
  - top-level object
  - new entry

Steps:

1. Pull latest `main` branch.
2. Edit `CRP_REPLAY_REGISTRY_V0_1.json`:
   - Append a new entry object to `entries[]`.
   - Set `current_registry_state` to `ACTIVE` if previously `EMPTY`.
3. Set:
   - `schema_version` and `protocol_version` to current values.
   - `registry_entry_created_at` to current UTC timestamp.
   - `registry_entry_commit_sha` temporarily to `TBD`.
4. Run validation:
   - JSON schema validation must pass.
5. Commit:
   - Commit message should include `CRP_REPLAY_REGISTRY: append entry for <seed_hash or seed_cid>`.
6. Amend `registry_entry_commit_sha` in optional strict mode:
   - After commit SHA is known, a follow-up commit may update the field to the actual SHA.

### OP2: Supersede via new entry

Description: Record a new fact, such as a later replay, without mutating prior entries.

Rule: Never edit the old entry. Add a new entry that references it.

Optional V0.1 extension fields:

- `supersedes_entry_index`: integer index of prior entry.
- `supersedes_reason`: string.

Preconditions:

- Same as OP1.
- `supersedes_entry_index` must be a valid index in `entries[]`.

Effect:

- History remains fully replayable.
- Consumers can compute the effective state by following supersede chains.

### OP3: Seal registry

Description: Mark this registry version as closed to further entries.

Preconditions:

- Governance decision recorded elsewhere, such as a GitHub issue or EAS attestation.

Steps:

1. Add a final entry with:
   - `current_registry_state: "SEALED"`
   - `sealed: true`
   - `witness_claim: "OBSERVED_ONLY"` or `witness_claim: "ATTESTED_ELSEWHERE"`
2. Commit with message:
   - `CRP_REPLAY_REGISTRY: SEALED V0_1`

After sealing:

- OP1 and OP2 are disallowed for this version.
- Future changes must occur in `CRP_REPLAY_REGISTRY_V0_2` as a new artifact.

## Governance hooks

### GitHub evidence chain

Every update should be linked to:

- a PR,
- an issue,
- or an external attestation such as EAS schema plus UID.

### External attestations

A witness with `witness_claim: "ATTESTED_ELSEWHERE"` should include a reference in `notes`, such as EAS schema UID plus attestation UID.

### Review protocol

At least one `INDEPENDENT` witness should review entries that claim:

- `replay_outcome: "GREEN_MATCH"`
- `replay_outcome: "RED_MISMATCH"`

## Minimal constitutional triad

Under this protocol, the registry satisfies:

1. **Data** — `CRP_REPLAY_REGISTRY_V0_1.json`, append-only entries.
2. **Validation** — `CRP_REPLAY_REGISTRY_SCHEMA_V0_1.json`, strict schema.
3. **Governance** — `CRP_REPLAY_REGISTRY_UPDATE_PROTOCOL_V0_1.md`, this document.

From here, the registry can support:

- an EAS schema for registry entries,
- GitHub commit to EAS attestation wiring,
- and a replayable constitutional history rather than a single proof.
