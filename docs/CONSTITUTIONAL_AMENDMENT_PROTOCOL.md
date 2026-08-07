# JOY Constitutional Amendment Protocol

VERSION = 0.1.1-DRAFT
STATUS = PROPOSED_BOOTSTRAP_PROTOCOL
SUPERSEDES = 0.1.0-DRAFT

## Purpose

This protocol governs changes to JOY's epistemic constitution. Constitutional rules are not changed by convenience edits, environment-variable overrides, silent rewrites, or undocumented exceptions.

The protocol separates four acts:

1. PROPOSE — state exactly what rule is changing and why.
2. PROVE — provide semantic evidence that the proposed rule behaves as claimed.
3. REVIEW — evaluate completeness, clarity, amendability, and failure-domain effects.
4. RATIFY — merge, record the ratification receipt, and tag the resulting constitutional baseline.

Automation may validate structure and evidence references. Automation may not substitute for human ratification.

## Section A — Quorum

### A.1 Bootstrap quorum

Until a separately ratified governance roster exists, bootstrap ratification requires:

- at least two ACTIVE bootstrap reviewer identities in `constitutional/bootstrap-reviewers.json`;
- at least one explicit APPROVE sign-off from a reviewer with repository authority;
- all mandatory review criteria recorded PASS;
- all required semantic proof jobs GREEN;
- zero unresolved constitutional review failures.

A reviewer identity is valid only when it is a GitHub login or other explicitly registered identifier that resolves to a human authority record. Placeholder or pending identities do not count toward quorum.

### A.2 Post-bootstrap quorum

After bootstrap, each amendment MUST declare the `governing_protocol_version` and MUST satisfy the quorum rule in force under that version. Until amended by a ratified amendment, the default post-bootstrap quorum is two distinct ACTIVE constitutional reviewers, with at least one repository-authority reviewer, plus all mandatory review criteria PASS and all required semantic proofs GREEN.

CI success alone is never quorum.

## Section B — Amendment lifecycle and failed dispositions

Valid amendment states are:

`DRAFT`, `REVIEWED`, `RATIFIED`, `REJECTED`, `WITHDRAWN`, `ABANDONED`, `SUPERSEDED`.

- `DRAFT`: proposal may evolve through append-only revision artifacts.
- `REVIEWED`: required review completed; this does not imply ratification.
- `RATIFIED`: binding only after all ratification requirements complete.
- `REJECTED`: review or ratification explicitly failed. Historical artifacts remain preserved.
- `WITHDRAWN`: proposer voluntarily stops the amendment before ratification. Historical artifacts remain preserved.
- `ABANDONED`: amendment becomes inactive without ratification after an explicit abandonment record. Historical artifacts remain preserved.
- `SUPERSEDED`: later ratified amendment replaces the current rule while preserving historical references.

A failed, rejected, withdrawn, or abandoned amendment MUST NOT be deleted or silently rewritten. Its disposition MUST be recorded append-only.

## Section C — Human reviewer identity and multiplicity

A human reviewer MUST be represented in the constitutional reviewer registry with:

- stable reviewer id;
- human identity handle;
- authority basis;
- status (`ACTIVE`, `INACTIVE`, or `PENDING_ASSIGNMENT`);
- effective timestamp.

A valid sign-off MUST identify the reviewer, decision, reviewed amendment id or bootstrap PR, and timestamp. CI, bots, workflow identities, and unassigned placeholders cannot produce human sign-off.

One human MAY perform all four substantive review criteria, but quorum still requires the minimum number of distinct ACTIVE reviewer identities specified by the governing protocol version.

## Section D — Bootstrap reviewer authority

Bootstrap reviewer authority is limited to review and ratification of the one-time adoption of this protocol.

- Minimum ACTIVE identities: 2.
- At least one MUST have repository authority.
- Bootstrap authority begins only when the registry entry is ACTIVE.
- Bootstrap authority expires immediately when the bootstrap protocol is ratified or rejected.
- Bootstrap authority does not automatically confer post-bootstrap constitutional office.

The bootstrap exception MUST NOT be reused as precedent.

## Section E — Self-amendment temporal rule

After initial ratification, this protocol MAY be changed only by an amendment that conforms to the protocol version in force at the time the amendment is proposed.

Every amendment modifying this protocol MUST:

- set `self_amendment = true`;
- declare `governing_protocol_version`;
- declare `proposal_timestamp`;
- identify the exact protocol clauses affected;
- satisfy the quorum and review rules of the declared governing version.

A proposal cannot change its governing protocol version retroactively.

## Section F — Revocation provenance authority model

Every constitutional revocation rule adopted under this protocol MUST select exactly one authority model:

`ISSUER_CENTRIC` XOR `CONSTITUTIONAL_OVERRIDE`.

Issuer-centric authority requires an issuer signature and registered issuer key reference bound to the original claim issuance metadata.

Constitutional override authority requires a resolvable constitutional authority identity, machine-resolvable constitutional ground reference, written rationale, timestamp, and a distinct co-ratifier.

Mixed-model revocations are invalid. Revocation is append-only: the original claim remains immutable and current status is derived from the revocation event.

The structural schema for this model is `schema/claim_revocation.schema.json`. Cryptographic and reference-resolution enforcement remains subject to separate semantic proof before any revocation implementation is ratified.

## Amendment artifact

Every amendment MUST be represented by an append-only JSON artifact conforming to `schema/constitutional_amendment.schema.json`.

Canonical path:

`constitutional/amendments/AMENDMENT_<NNNN>.json`

Each amendment MUST identify amendment id, protocol version, governing protocol version, proposal timestamp, title and rationale, affected rules, exact change summary, semantic proof references, review record, lifecycle state, self-amendment state, and supersession effects if any.

## Review requirements

Ratification requires explicit review against all four criteria:

- COMPLETENESS — does the amendment cover the claimed failure mode without silently creating new ungoverned behavior?
- CLARITY — can a contributor understand the rule, rejection behavior, and remediation path without reverse-engineering the implementation?
- AMENDABILITY — can a later defect be corrected through this protocol without bypassing the rule being changed?
- FAILURE_DOMAIN_ISOLATION — is the amendment scoped so failure or revocation of one claim does not silently rewrite unrelated earned guarantees?

Each criterion MUST be recorded PASS or FAIL with rationale. Any FAIL blocks ratification.

## Ratification mechanism

An amendment becomes binding only when all of the following are true:

1. amendment artifact validates against schema;
2. required semantic proofs are present and pass;
3. constitutional review criteria all pass;
4. governing quorum is satisfied;
5. amendment PR is merged;
6. `constitutional/CHANGELOG.md` receives an append-only ratification entry;
7. the resulting constitutional baseline commit is tagged.

Recommended tag format:

`v<major>.<minor>.<patch>-epistemic-<name>`

## Deprecation and supersession

Constitutional rules are never silently deleted. A superseding amendment MUST identify superseded rules or artifacts, preserve historical references, state the replacement rule, state the effective baseline/tag, and append a changelog entry.

## Bootstrap clause

PR #73 is the one-time bootstrap act that establishes this amendment protocol before the protocol exists as binding law. This bootstrap exception expires immediately upon ratification or rejection and MUST NOT be reused as precedent.

## Core invariant

> The constitution may evolve, but the path by which it evolves must itself remain visible, reviewable, evidence-bound, and governed by the rules in force when the change was proposed.
