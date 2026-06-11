# Goblin Unified Surface Generation Blueprint V0.1

## Status

SURFACE_GENERATION_BLUEPRINT_SEEDED

## Purpose

Define the deterministic process for regenerating Level-0 terrain and Level-1 path surfaces at the required artifact locations so the Goblin constellation generator can run truthfully.

This artifact is a blueprint only.
It is not scanner output.
It is not runtime evidence.
It does not replace generated terrain or path surfaces.
It does not promote the constellation from HOLD.

## Required Outputs

The scanner process must generate exactly these files:

```text
artifacts/goblin_constellation_terrain_v0_1.json
artifacts/goblin_constellation_paths_v0_1.json
```

Both outputs must be generated, not manually reconstructed.

## Inputs

The unified scanner may consume only:

1. `scripts/wisdom-constellation.config.json`
2. Public GitHub repository metadata
3. Public GitHub repository tree data

No file content scanning is allowed.
No semantic inference is allowed.
No homepage mutation is allowed.
No Goblin Gate mutation is allowed.

## Level-0 Terrain Surface Requirements

`artifacts/goblin_constellation_terrain_v0_1.json` must contain repo-level metadata for each configured repo:

- repo
- exists
- reachable
- public
- default_branch
- default_branch_sha
- last_commit_time
- tree_sha
- status

The terrain scanner must preserve missing or unreachable repos as explicit non-green records rather than omitting them.

## Level-1 Path Surface Requirements

`artifacts/goblin_constellation_paths_v0_1.json` must contain blob-only public path entries for each reachable configured repo.

Each path entry must include:

- repo
- path
- sha
- size
- url

The path surface must be sorted lexicographically by repo, then path.

## Deterministic Rules

1. Sort repos lexicographically by full repo name.
2. Sort path entries lexicographically by repo and path.
3. Use stable key ordering.
4. Preserve unavailable data as null, false, or status fields.
5. Never infer from file contents.
6. Never mark a repo healthy unless GitHub metadata and tree retrieval both succeed.
7. Always emit `authority: false`.
8. Always emit `no_fake_green: true`.

## Failure Semantics

If a repo is missing or unreachable, the terrain output must include:

```json
{
  "exists": false,
  "reachable": false,
  "public": false,
  "status": "UNREACHABLE"
}
```

If a repo tree cannot be enumerated, the path output must include no fabricated paths and must record the repo in a failure list.

## Required Scanner Functions

The implementation phase should expose:

- `loadWisdomConstellationConfig`
- `fetchRepoTerrain`
- `fetchRepoTreePaths`
- `buildTerrainSurface`
- `buildPathSurface`
- `writeSurfaceArtifacts`

Network calls are permitted only in the scanner command wrapper.
Transform functions must remain deterministic.

## Forbidden Behavior

The scanner must not:

1. Inspect blob contents.
2. Classify semantic meaning.
3. Promote any claim to VERIFIED.
4. Enable minting.
5. Modify homepage files.
6. Modify `components/goblin-gate/index.ts`.
7. Modify any docs except by explicit separate spec action.
8. Write outside `artifacts/` during the scanner run.

## Expected Surface Generation Receipt

A successful scanner run should produce a receipt object shaped like:

```json
{
  "surface_generation": "COMPLETE",
  "terrain_output": "artifacts/goblin_constellation_terrain_v0_1.json",
  "path_output": "artifacts/goblin_constellation_paths_v0_1.json",
  "repos_checked": "<NUMBER>",
  "path_entries": "<NUMBER>",
  "authority": false,
  "no_fake_green": true
}
```

A partial scanner run must produce HOLD, not green.

## Next Gate

After this blueprint is anchored, the lawful next gate is:

```text
UNIFIED_SURFACE_GENERATOR_IMPLEMENTATION
```

## Authority

false

## No Fake Green

true
