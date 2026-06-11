# Automated Scanner Spec V0.1 — Terrain-First Constellation Scanner 🛰️👺⚙️

## Status

CANONICAL_DRAFT

## Purpose

The scanner's job is not to interpret lore, courts, or subjects first.

Its job is to map the terrain:

- repos
- paths
- artifacts
- signals

Everything else is derived.

The scanner produces the map, not the story.

## Level 0 — Repository Existence Layer

Before scanning files, the scanner must confirm the repo exists and is readable.

For each repo:

```json
{
  "repo_exists": true,
  "default_branch": "main",
  "last_commit": "<sha>",
  "public": true,
  "reachable": true
}
```

If `repo_exists` is false, the scanner must not proceed to deeper levels.

This is the Repo Health Check.

## Level 1 — Path Discovery Layer

Once the repo is confirmed healthy, the scanner enumerates paths.

```json
{
  "paths_discovered": [],
  "artifact_count": 0,
  "repo": "jsonwisdom/JOY"
}
```

This layer is purely structural.

No Goblin logic.
No subject inference.
No heuristics.

This is the Path Surface.

## Level 2 — Subject and Court Detection Layer

Only after paths exist do we detect subjects and courts.

For V0.1, the only subject is GOBLIN.

Detection rules:

- `**/goblin*`
- `**/GOBLIN*`
- `court/`
- `docket/`
- `_truth/constitution/`
- `schemas/*goblin*`
- `components/goblin-gate/**`

Content markers:

- `"subject": "GOBLIN"`
- `GOBLIN_COURT`

Output:

```json
{
  "subjects": ["GOBLIN"],
  "courts": ["GOBLIN_COURT"],
  "signals": []
}
```

This is the Subject Surface.

## Level 3 — Verification Layer

This layer assigns non-authoritative labels.

```json
{
  "verified": true,
  "reason": "artifact + evidence",
  "status": "VERIFIED"
}
```

Rules:

- VERIFIED = exists on default branch + stable commit
- SEEDED = discovered but not referenced in constellation
- RECON = referenced but missing
- UNKNOWN = insufficient signals

This is the Evidence Surface.

## Scanner Inputs V0.1

Required:

- list of repos

Initial repo set:

- jsonwisdom/JOY
- jsonwisdom/AL
- jsonwisdom/COMPUTERWISDOM

Optional:

- GitHub token
- organization name for future repo auto-discovery

Config file:

```text
scripts/wisdom-constellation.config.json
```

## Scanner Outputs

Primary JSON output:

```text
docs/goblin/goblin_constellation_v0_1.json
```

Shape:

```json
{
  "scanner_version": "0.1.0",
  "generated_at": "...",
  "root_identity": null,
  "repos": [],
  "subjects": [],
  "courts": [],
  "classification": {},
  "authority": false,
  "no_fake_green": true
}
```

`root_identity` remains null in V0.1. `jaywisdom.base.eth` belongs in V0.2 or later.

Derived Markdown output:

```text
docs/goblin/GOBLIN_REPO_CONSTELLATION_INDEX_V0_1.md
```

Rules:

- stable ordering
- stable section boundaries
- only update machine-generated sections
- manual sections protected by `<!-- MANUAL_START -->` and `<!-- MANUAL_END -->`

## Safety and Replay Rules

- idempotent: same input produces same output except timestamped generation metadata
- scanner never sets authority true
- dry-run first by default
- write mode writes JSON and Markdown but never commits
- PR mode may emit patch output later
- scanner version embedded in JSON and Markdown footer

## Future Hooks

- repo auto-discovery
- subject expansion
- court inference
- precedent counting
- on-chain receipts
- identity overlay

Future identity overlay:

```json
{
  "root_identity": "jaywisdom.base.eth"
}
```

Not in V0.1.

## Minimal Pipeline

1. loadConfig()
2. scanRepos()
3. scanPaths()
4. detectSubjects()
5. classifyArtifacts()
6. emitJSON()
7. emitMarkdown()
8. dryRunOrWrite()

## Constitutional State

```json
{
  "artifact": "AUTOMATED_SCANNER_SPEC_V0_1",
  "mode": "TERRAIN_FIRST",
  "authority": false,
  "no_fake_green": true
}
```
