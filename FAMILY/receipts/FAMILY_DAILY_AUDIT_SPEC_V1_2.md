# FAMILY DAILY AUDIT — v1.2

**Repository:** `jsonwisdom/JOY`  
**Mode:** `REPLAY / VALIDATION ONLY`  
**Scope:** whole declared family graph, not Jay-only  
**Authority created:** `false`

## Purpose

Run a repeatable audit over the family edge graph while preserving the rule that evidence and relationship state belong to each edge independently.

The workflow may:

- parse declared nodes and edges,
- validate edge-local evidence history,
- detect illegal neighboring-edge mutation,
- detect shared-child synthesis attempts,
- preserve `HOLD_UNSPECIFIED`,
- prove that nodes may remain intentionally without asserted relationship edges,
- run synthetic adversarial transitions against a copy of the graph,
- emit a machine-readable receipt.

The workflow may not:

- create kinship,
- infer spouse, partner, household, custody, legal-parentage, or interpersonal-history edges,
- promote a node because one edge was verified,
- promote neighboring edges,
- rewrite prior evidence events,
- treat an empty edge as an error,
- create family, legal, institutional, or machine authority.

## Canonical laws

```text
EVIDENCE_CLASS ≠ RELATIONSHIP_STATE
KNOWN NODE ≠ KNOWN EDGE
KNOWN EDGE ≠ ADJACENT EDGE
SHARED OBJECT ≠ RELATIONSHIP BETWEEN SUBJECTS
EVIDENCE FOR EDGE A ≠ EVIDENCE FOR EDGE B
SILENCE = VALID GRAPH STATE
HOLD_UNSPECIFIED ≠ INVITATION TO GUESS
```

## Current baseline coverage

The v1.1 graph includes declared parent edges across multiple branches/generations and intentionally includes family nodes that have no asserted relationship edge in this fixture. Those silent nodes are expected to remain valid.

The adversarial transition test deliberately targets `GAGA → PARENT_OF → MARYDEE`, rather than a Jay edge, to prove that the validator is whole-family and edge-local.

## Daily schedule

The workflow contains:

```text
cron = 15 12 * * *
```

That is **12:15 UTC daily**. GitHub scheduled workflows execute only from the repository default branch, so the daily timer does not become active until the workflow is merged to `main`.

Pushes and pull requests run the validator immediately before merge.

## Receipt rule

Every run emits:

```text
FAMILY_DAILY_AUDIT_RECEIPT.json
```

with graph SHA-256, node/edge counts, non-Jay coverage, silent nodes, shared-child pairs, relationship-state counts, baseline errors, adversarial-test results, and explicit zero-promotion / zero-authority fields.

```text
AUDIT PASS ≠ FAMILY APPROVAL
AUDIT PASS ≠ RELATIONSHIP VERIFICATION
AUDIT PASS ≠ PUBLICATION AUTHORITY
AUDIT PASS = GRAPH OBEYED ITS DECLARED TYPE RULES DURING THIS RUN
```
