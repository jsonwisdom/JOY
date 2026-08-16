# FAMILY DAILY AUDIT — v1.3 (hardened from v1.2)

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
- emit a machine-readable receipt,
- sign the receipt with Sigstore (keyless OIDC) and verify the bundle.

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
ASSERTED EDGE REQUIRES EXPLICIT ORIGIN
```

## Origin rule (v1.3 hardening)

Any asserted edge (predicate ≠ null AND relationship_state ≠ HOLD_UNSPECIFIED) must carry an origin in:

```text
USER_DECLARED
DOCUMENT_SOURCE_BOUND
PERSON_CONFIRMED
```

MACHINE_GENERATED, ADJACENCY_DERIVED, SHARED_CHILD_DERIVED, SOCIAL_EXPECTATION_DERIVED (and any other non-explicit origin) are rejected for every kinship predicate, including PARENT_OF, AUNT_OF, and future predicates.

## Provenance fields (v1.3)

Every receipt records:

- `trigger_sha` — the SHA that triggered the workflow event
- `tested_commit_sha` — the SHA that was actually checked out and executed (`git rev-parse HEAD`)
- `pull_request_head_sha` — present on pull_request events
- `exact_checkout_match` — boolean that the checked-out HEAD matched the intended SHA
- `graph.sha256` — SHA-256 of the exact graph file bytes read by the auditor

The receipt is then signed with cosign keyless (`sign-blob` + OIDC) and the Sigstore bundle is verified before upload.

## Adversarial gates (v1.3)

- legal edge-local synthetic promotion beyond Jay: ACCEPT
- neighboring-edge inheritance: REJECT
- evidence-history erasure: REJECT
- MACHINE_GENERATED PARENT_OF: REJECT
- MACHINE_GENERATED AUNT_OF: REJECT
- shared-child adult-edge synthesis: REJECT
- filling HOLD_UNSPECIFIED without edge evidence: REJECT

## Daily schedule

```text
cron = 15 12 * * *
```

12:15 UTC daily. GitHub scheduled workflows execute only from the default branch; the timer becomes active only after merge to `main`.

## Receipt rule

```text
AUDIT PASS ≠ FAMILY APPROVAL
AUDIT PASS ≠ RELATIONSHIP VERIFICATION
AUDIT PASS ≠ PUBLICATION AUTHORITY
AUDIT PASS = GRAPH OBEYED ITS DECLARED TYPE RULES DURING THIS RUN
```

Sigstore provides an identity-bound signature + transparency-log evidence of the workflow run that produced the receipt. It does not create human authority.
