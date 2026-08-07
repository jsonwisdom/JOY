# JOY Constitutional Amendment Protocol

VERSION = 0.1.0-DRAFT
STATUS = PROPOSED_BOOTSTRAP_PROTOCOL

## Purpose

This protocol governs changes to JOY's epistemic constitution. Constitutional rules are not changed by convenience edits, environment-variable overrides, silent rewrites, or undocumented exceptions.

The protocol separates four acts:

1. PROPOSE — state exactly what rule is changing and why.
2. PROVE — provide semantic evidence that the proposed rule behaves as claimed.
3. REVIEW — evaluate completeness, clarity, amendability, and failure-domain effects.
4. RATIFY — merge, record the ratification receipt, and tag the resulting constitutional baseline.

Automation may validate structure and evidence references. Automation may not substitute for human ratification.

## Amendment artifact

Every amendment MUST be represented by an append-only JSON artifact conforming to `schema/constitutional_amendment.schema.json`.

Canonical path:

`constitutional/amendments/AMENDMENT_<NNNN>.json`

Each amendment MUST identify:

- amendment id and protocol version;
- title and rationale;
- affected constitutional rules/artifacts;
- exact proposed change summary;
- semantic proof references;
- review record;
- ratification state;
- deprecation/supersession effects, if any.

A proposal MAY be edited while its `status` is `DRAFT` only by appending a replacement proposal artifact with a new amendment id or revision id. Once ratified, the ratified artifact is immutable.

## Review requirements

Ratification requires explicit review against all four criteria:

- COMPLETENESS — does the amendment cover the claimed failure mode without silently creating new ungoverned behavior?
- CLARITY — can a contributor understand the rule, rejection behavior, and remediation path without reverse-engineering the implementation?
- AMENDABILITY — can a later defect be corrected through this protocol without bypassing the rule being changed?
- FAILURE_DOMAIN_ISOLATION — is the amendment scoped so that failure or revocation of one claim does not silently rewrite unrelated earned guarantees?

Each criterion MUST be recorded as `PASS` or `FAIL` with rationale. Any `FAIL` blocks ratification.

## Bootstrap quorum

Until JOY has a separately ratified governance roster, the bootstrap quorum is:

- at least one explicit human repository-authority sign-off recorded in the amendment review record; and
- all required semantic proof jobs GREEN for the amendment's stated claims; and
- zero unresolved constitutional review failures.

CI success alone is never quorum.

The bootstrap quorum itself is amendable only through this protocol after this protocol is ratified.

## Ratification mechanism

An amendment becomes binding only when all of the following are true:

1. amendment artifact validates against schema;
2. required semantic proofs are present and pass;
3. constitutional review criteria all pass;
4. bootstrap/governance quorum is satisfied;
5. amendment PR is merged;
6. `constitutional/CHANGELOG.md` receives an append-only ratification entry;
7. the resulting constitutional baseline commit is tagged.

Recommended tag format:

`v<major>.<minor>.<patch>-epistemic-<name>`

The amendment artifact MUST record the ratified merge commit and tag before its status may be considered `RATIFIED` in any subsequent state artifact.

## Deprecation and supersession

Constitutional rules are never silently deleted.

A superseding amendment MUST:

- identify each superseded rule or artifact;
- preserve the historical reference;
- state the replacement rule;
- state the effective baseline/tag;
- append a changelog entry.

Superseded material remains part of the historical record even when it is no longer current law.

## Self-reference clause

After initial ratification, this protocol MAY be changed only by an amendment that conforms to this protocol.

A proposed change to this protocol MUST explicitly set:

`self_amendment = true`

and MUST identify the exact protocol clauses affected.

No emergency environment variable, commit-message keyword, CI bypass, administrator shortcut, or undocumented manual exception has constitutional authority.

## Bootstrap clause

PR #73 is the one-time bootstrap act that establishes this amendment protocol before the protocol exists as binding law.

This bootstrap exception expires immediately upon ratification. It MUST NOT be reused as precedent for future constitutional changes.

## Core invariant

> The constitution may evolve, but the path by which it evolves must itself remain visible, reviewable, and evidence-bound.
