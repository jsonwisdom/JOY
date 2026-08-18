# FAMILY_NINE_TO_JOY_MAIN_V0_1

```text
STATUS = MIGRATION_STAGED
TARGET_REPOSITORY = jsonwisdom/JOY
TARGET_BRANCH = main
STAGING_BRANCH = migration/family-nine-to-joy-main
SOURCE_REPOS = 9
SOURCE_BYTES_MUTATED = FALSE
SOURCE_REPOS_DELETED = FALSE
IDENTITY_MERGING = FALSE
PUBLIC_LIKENESS_PROMOTION = FALSE
AUTHORITY_CREATED = FALSE
NO_FAKE_GREEN = TRUE
```

## Canonical Direction

JOY is the family root. Standalone family repositories become preserved lanes under `JOY/FAMILY/<LANE>/`.

```text
jsonwisdom/JOY
└── FAMILY/
    ├── BRAELEE/
    ├── BREANN/
    ├── DESTINEE/
    ├── GAGA/
    ├── GRAMMY/
    ├── HEIDEE/
    ├── JAYCEE/
    ├── LEEANN/
    └── MARYDEE/
```

## Source Freeze Map

| Lane | Source repository | Source main/master tip | Target path | Public import posture |
|---|---|---|---|---|
| BRAELEE | `jsonwisdom/BRAELEE` | `3336e0929af34367ead4830ac2055b3879090b4d` | `FAMILY/BRAELEE/` | text/index eligible |
| BREANN | `jsonwisdom/BREANN` | `64dba8504a73790b26e63b741fd4bdc6787ef2f1` | `FAMILY/BREANN/` | text/index eligible |
| DESTINEE | `jsonwisdom/DESTINEE` | `d38d277d0cea236ab4e72a0d012a68586e91d015` | `FAMILY/DESTINEE/` | text eligible |
| GAGA | `jsonwisdom/GAGA` | `4d2324de91791e18d9e743efaf0d5ec55b1ac7a9` | `FAMILY/GAGA/` | text/index eligible |
| GRAMMY | `jsonwisdom/GRAMMY` | `a6b824e04aa17093b54e8f6224ac6ba00e287cbe` | `FAMILY/GRAMMY/` | code/docs eligible after path review |
| HEIDEE | `jsonwisdom/HEIDEE` | `2c826db06313b6edcc789620ae0b3ba0905f2036` | `FAMILY/HEIDEE/` | text/config eligible after workflow isolation |
| JAYCEE | `jsonwisdom/JAYCEE` | `a85ba7dfec5e9e9d996293f630c2483d3fec44f4` | `FAMILY/JAYCEE/` | README/index eligible; likeness media HOLD |
| LEEANN | `jsonwisdom/LEEANN` | `0eeb6ce6c662e650953226ca8c83df52c0bc7cc0` | `FAMILY/LEEANN/` | requires workflow/pages/path review |
| MARYDEE | `jsonwisdom/MARYDEE` | `44fdfa24056e2c8b4ad51f4454f2861bf206a69b` | `FAMILY/MARYDEE/` | text/schema/fixture eligible after path review |

## Branch Normalization State

A `main` branch has been created in each source repository at the exact prior `master` tip.

```text
MAIN_BRANCH_EXISTS_9_OF_9 = TRUE
SOURCE_CONTENT_CHANGED = FALSE
MASTER_DELETED = FALSE
DEFAULT_BRANCH_CHANGED = NOT_VERIFIED
```

`main exists` is not the same claim as `main is repository default`.

## JAYCEE Likeness Hold

The JAYCEE source tree contains seven JPEG photographs in addition to `README.md` and `index.json`.

Because JOY is public, the photographs are not promoted into the JOY public root by this migration without explicit human likeness/publication approval.

```text
JAYCEE_README_INDEX = IMPORT_ELIGIBLE
JAYCEE_PHOTO_BLOBS = HOLD
PUBLIC_LIKENESS_CONSENT = NOT_INFERRED
EXISTING_PUBLIC_SOURCE != NEW_PUBLICATION_AUTHORIZATION
```

## Workflow Isolation

Repository-scoped workflows from HEIDEE and LEEANN must not be copied directly into `JOY/.github/workflows/` as part of a directory migration. If preserved, they remain inert source artifacts under each family lane until separately adapted and reviewed for JOY.

```text
SOURCE_WORKFLOW != JOY_WORKFLOW
COPY != ACTIVATE
MIGRATION != EXECUTION_AUTHORITY
```

## Migration Order

```text
1. Freeze source commit IDs.
2. Create/verify source `main` refs.
3. Inventory files and privacy/execution boundaries.
4. Import eligible source snapshots under `JOY/FAMILY/<LANE>/`.
5. Preserve source commit/tree/blob provenance in migration receipts.
6. Replay file counts and digests.
7. Review JAYCEE likeness HOLD and workflow isolation.
8. Merge one audited migration PR into JOY/main.
9. Only after readback, mark standalone repos legacy/archival; do not delete history.
```

## Invariants

```text
ONE_FAMILY_ROOT = JOY
NINE_LANES != NINE_AUTHORITIES
MOVED_CONTENT != MERGED_IDENTITY
REPO_HISTORY != FAMILY_BIOGRAPHY
PUBLIC_REPO != FAMILY_CONSENT
SOURCE_COMMIT != JOY_COMMIT
RECEIPT != AUTHORITY
NO_FAKE_GREEN = TRUE
```
