# Goblin Repo Constellation Index V0.1 👺📚⚙️

## Status

SEEDED_INDEX

## Purpose

This document records the first public replay index for the Goblin constellation across Wisdom repositories.

Goblin is treated as:

- one word
- one subject
- one court system
- one navigable artifact constellation

This index is human-readable. It does not grant authority. It does not verify claims by itself. It records mapped evidence surfaces for replay.

## Constitutional Rule

```json
{
  "subject": "GOBLIN",
  "court": "GOBLIN_COURT",
  "authority": false,
  "no_fake_green": true
}
```

## Source Binding

The machine-readable mapper is implemented at:

```text
components/goblin-gate/index.ts
```

Primary exported bindings:

```text
bindGoblinRepoConstellation()
useGoblinRepoConstellation()
mapWisdomArtifacts()
```

## Seeded Repositories

```json
{
  "repos": [
    "jsonwisdom/JOY",
    "jsonwisdom/AL",
    "jsonwisdom/COMPUTERWISDOM"
  ]
}
```

## Seeded Goblin Artifacts

| Repo | Artifact | Role | Status |
|---|---|---|---|
| jsonwisdom/JOY | components/goblin-gate/index.ts | Homepage gate + constellation mapper | VERIFIED |
| jsonwisdom/AL | verify_goblin_stack.py | Goblin stack verifier | SEEDED |
| jsonwisdom/AL | docs/goblin_gap_map_batch_007.md | Gap map artifact | SEEDED |
| jsonwisdom/AL | _truth/constitution/goblin_full_stack_report.json | Stack report | SEEDED |
| jsonwisdom/COMPUTERWISDOM | docs/goblin_verifier_v0_1.md | Verifier document | SEEDED |
| jsonwisdom/COMPUTERWISDOM | docket/GOBLIN_DOCKET_V0_1.md | Court docket | SEEDED |
| jsonwisdom/COMPUTERWISDOM | docs/GOBLIN_PRECEDENT_INDEX_V0_1.md | Precedent index | SEEDED |
| jsonwisdom/COMPUTERWISDOM | schemas/goblin_court_v0_1.schema.json | Court schema | SEEDED |
| jsonwisdom/COMPUTERWISDOM | court/goblin_precedent_engine_anchor_packet_v0_1.json | Anchor packet | SEEDED |

## Evidence Labels

- VERIFIED = confirmed by public commit, PR, receipt, UID, transaction, or replay log
- LOCAL = exists locally but not confirmed public
- RECON = designed or discovered but not yet artifacted
- UNKNOWN = needs audit

## Time Boxes

- PAST = already happened / evidence exists / replayable
- PRESENT = active branch, PR, recon, or current decision surface
- FUTURE = not built yet / unknowns / roadmap

## Current Classification

```json
{
  "GOBLIN_GATE": "VERIFIED",
  "CONSTELLATION_MAPPER": "VERIFIED",
  "GOBLIN_REPO_CONSTELLATION": "SEEDED",
  "WISDOM_WORKS_INDEX": "FOUNDATION_PRESENT",
  "PUBLIC_HUMAN_INDEX": "PRESENT",
  "AUTHORITY": false,
  "NO_FAKE_GREEN": true
}
```

## Next Step

Create an automated scanner that walks Wisdom repositories and updates the constellation graph without relying on manually seeded artifacts.

Suggested future artifact:

```text
scripts/scan-wisdom-constellation.mjs
```
