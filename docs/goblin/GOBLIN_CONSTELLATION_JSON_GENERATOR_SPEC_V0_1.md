# Goblin Constellation JSON Generator Spec V0.1

## Status

GENERATOR_SPEC_SEEDED

## Purpose

Define the deterministic generator that produces the canonical machine-readable constellation JSON consumed by the Goblin Gate at runtime.

The generated JSON is the source of truth for:

- repo nodes
- artifact surfaces
- status labels
- structural signals
- structural classification
- boundary metadata

This spec does not implement the generator.
This spec does not render the homepage.
This spec does not inspect private content.
This spec does not grant semantic authority.

## Output Artifact

The generator must write exactly one output file:

```text
artifacts/goblin_constellation_v0_1.json
```

The output must be deterministic, sorted, replay-safe, authority-false, and free of hidden state.

## Inputs

The generator may consume only:

1. `wisdom-constellation.config.json`
2. Level-0 terrain surface
3. Level-1 path surface

The generator must not scan file contents.
The generator must not infer semantic meaning.
The generator must not modify homepage or component files.

## Canonical JSON Shape

The generated file must match this shape:

```json
{
  "scanner_version": "0.1.0",
  "generated_at": "<ISO_TIMESTAMP>",
  "root_identity": null,
  "repos": [
    {
      "repo": "jsonwisdom/JOY",
      "default_branch": "main",
      "terrain": {
        "exists": true,
        "reachable": true,
        "public": true,
        "default_branch_sha": "<sha>",
        "last_commit_time": "<iso>",
        "tree_sha": "<sha>"
      },
      "paths": [
        "README.md",
        "components/goblin-gate/index.ts",
        "docs/goblin/GOBLIN_REPO_CONSTELLATION_INDEX_V0_1.md"
      ],
      "signals": [
        "filename:GOBLIN",
        "path:components/goblin-gate",
        "path:docs/goblin"
      ]
    }
  ],
  "subjects": ["GOBLIN"],
  "courts": ["GOBLIN_COURT"],
  "classification": {
    "GOBLIN_GATE": "VERIFIED",
    "CONSTELLATION_MAPPER": "VERIFIED",
    "GOBLIN_REPO_CONSTELLATION": "SEEDED",
    "PUBLIC_HUMAN_INDEX": "PRESENT"
  },
  "authority": false,
  "no_fake_green": true
}
```

## Deterministic Rules

The generator must enforce:

1. Sort repos lexicographically by `repo`.
2. Sort paths lexicographically.
3. Sort signals lexicographically.
4. Use stable top-level keys exactly as defined in this spec.
5. Allow only `generated_at` to vary between valid runs.
6. Derive classification from structural signals only.
7. Always emit `authority: false`.
8. Always emit `no_fake_green: true`.
9. Preserve missing or unknown terrain fields as absent or null rather than inferred.

## Structural Signals

Allowed signals are path-level only.

Examples:

- `path:components/goblin-gate`
- `path:docs/goblin`
- `filename:GOBLIN`
- `filename:CONSTELLATION`
- `filename:INDEX`

The generator must not derive signals from file contents.

## Classification Rules

Classification must be derived from structural signals only.

Allowed classification keys:

- `GOBLIN_GATE`
- `CONSTELLATION_MAPPER`
- `GOBLIN_REPO_CONSTELLATION`
- `PUBLIC_HUMAN_INDEX`

Allowed classification values:

- `VERIFIED`
- `SEEDED`
- `PRESENT`
- `HOLD`
- `UNKNOWN`

The generator must not promote status based on narrative meaning, comments, assistant output, or expected future work.

## Forbidden Behavior

The generator must not:

1. Inspect file contents.
2. Infer verification from semantic text.
3. Promote semantic claims.
4. Collapse PRESENT or RECON boundaries.
5. Auto-enable minting.
6. Introduce new subjects or courts.
7. Modify the homepage.
8. Modify the Goblin Gate component.
9. Write to any file outside `artifacts/`.
10. Claim production conformance.

## Required Pure Function Exports

The implementation phase must expose:

- `generateConstellationJSON`
- `loadTerrainSurface`
- `loadPathSurface`
- `deriveSignals`
- `deriveClassification`

These functions must be deterministic and side-effect-free except for the final explicit artifact write in the command wrapper.

## Runtime Boundary

The generated constellation JSON may feed:

- `bindGoblinRepoConstellation()`
- `useGoblinRepoConstellation()`

The JSON must not cause minting to enable by itself.
The JSON must not create verification authority.
The JSON must not replace Court review.

## Expected Generator Result

A valid generator run may produce:

```json
{
  "output": "artifacts/goblin_constellation_v0_1.json",
  "status": "GENERATED",
  "authority": false,
  "no_fake_green": true
}
```

A missing input must produce HOLD rather than inferred success.

## Next Gate

After this spec is anchored, the next lawful gate is:

```text
GOBLIN_CONSTELLATION_JSON_GENERATOR_IMPLEMENTATION
```

## Authority

false

## No Fake Green

true
