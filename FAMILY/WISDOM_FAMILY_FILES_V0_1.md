# WISDOM FAMILY FILES v0.1

**Namespace:** `WISDOM_FAMILY_FILES`  
**Status:** `CANDIDATE_CANON / RECEIPT_BOUND`  
**Authority:** `false`  
**Privacy:** `PUBLIC_SAFE_NAMES_AND_ROLES_ONLY`  
**Updated:** 2026-08-18 (America/Chicago)

## Scope law

```text
FAMILY_FILES != WISDOM_FAMILY_FILES
REPO != PERSON
BRANCH != REPO
ONE_SURFACE != WHOLE_FAMILY
GITHUB_PROVES_TRANSPORT_AND_CONTENT
GITHUB_DOES_NOT_PROVE_GENEALOGY
USER_BOUND_RELATION != PUBLIC_RECORD_PROVEN_RELATION
```

`WISDOM FAMILY FILES` is the named family continuity namespace. Generic `Family Files` must not be used as a substitute when referring to this registry.

## Canonical member registry — 12 nodes

| # | Canonical node | Type | Current binding |
|---:|---|---|---|
| 1 | `DADDY_JAY` | family member | USER_BOUND |
| 2 | `HEIDEE` | family member | USER_BOUND + repo surface observed |
| 3 | `JAYCEE` | family member | USER_BOUND + repo surface observed |
| 4 | `BRIANNA` | family member | USER_BOUND + JOY surface observed |
| 5 | `MARYDEE` | family member | USER_BOUND + repo surface observed |
| 6 | `GAGA` | family member | USER_BOUND + repo surface observed |
| 7 | `GRAMMY` | family member | USER_BOUND + repo surface observed |
| 8 | `LEANNE` | family member | USER_BOUND |
| 9 | `BRAE` | family member | USER_BOUND |
| 10 | `BRE` | family member | USER_BOUND |
| 11 | `MRS_WISDOM` | family member | USER_BOUND + JOY surface observed |
| 12 | `MS_WISDOM` | distinct family member node | USER_BOUND + JOY surface observed |

## User-bound relationship edges

These edges preserve the operator-declared family model. They are continuity bindings, not claims that GitHub independently proves civil or biological relationship records.

```text
GAGA
├── MARYDEE
│   ├── HEIDEE
│   └── JAYCEE
└── LEANNE
    ├── BRAE
    └── BRE

DADDY_JAY
├── HEIDEE
├── JAYCEE
└── BRIANNA

MRS_WISDOM != MS_WISDOM
```

## Canonical label corrections

```text
LEEANN  -> LEANNE   [absorbed legacy label]
BE      -> BRAE     [replaced legacy node label]
BOSSBRE -> BRE      [absorbed legacy label]

MRS_WISDOM != MS_WISDOM
```

`BOSS_BRENDA` is **not promoted here as a canonical member label**. Existing artifacts using that label remain historical surfaces pending an explicit binding decision.

## Cross-repo family surfaces

The Wisdom Family is a graph, not a single repository. Known family-bearing surfaces include, at minimum:

- `jsonwisdom/JOY` — family registry, receipts, Wisdom namespace, JoySpace surfaces
- `jsonwisdom/COMPUTERWISDOM` — family system index, living family ledger, coordination/index layer
- `jsonwisdom/HEIDEE`
- `jsonwisdom/JAYCEE`
- `jsonwisdom/MARYDEE`
- `jsonwisdom/GAGA`
- `jsonwisdom/GRAMMY`
- `jsonwisdom/LEEANN` — legacy spelling repository surface; canonical registry label remains `LEANNE`
- `jsonwisdom/BRAELEE` — legacy repository surface; canonical registry label remains `BRAE`
- `jsonwisdom/BREANN` — legacy repository surface; canonical registry label remains `BRE`

Repository names are evidence of repository surfaces only. They do not override the canonical member labels above.

## Replay rule

```text
WISDOM_FAMILY_FILES
  -> MEMBER NODE
  -> SURFACE(S)
  -> RECEIPT(S)
  -> REPLAY
  -> CORRECTION HISTORY

NO SINGLE REPO MAY IMPERSONATE THE WHOLE FAMILY GRAPH.
```

## Disposition

```text
MEMBER_COUNT = 12
NAMESPACE = WISDOM_FAMILY_FILES
AUTHORITY_CREATED = FALSE
GENEALOGY_PUBLICLY_PROVEN = FALSE
USER_BOUND_CONTINUITY = TRUE
LEGACY_LABELS_PRESERVED = TRUE
NO_FAKE_GREEN = TRUE
```
