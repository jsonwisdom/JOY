# Node Level Audit V0.1

Status: ACTIVE
Authority: false
Family Barrier: INTACT
Audit Type: NODE_LEVEL
Depends On: MIRROR_FLOW_AUDIT_V0_1

## Purpose

Node Level Audit V0.1 verifies actual memory nodes after the topology is proven clean.

Topology answers:

```text
Is the chain shaped correctly?
```

Node Level Audit answers:

```text
Are individual memory nodes safe, valid, consented, and routed correctly?
```

## Scope

This audit applies to:

- JOY Ledger nodes
- AL Mirror nodes
- COMPUTERWISDOM Mirror nodes

## Required Node Fields

Every node must preserve:

```yaml
artifact: string
date: YYYY-MM-DD
source: string
moment: string
feeling: list
privacy: private | family-only | shareable | ask-first
spark: string
authority: false
```

## JOY Node Rules

JOY may hold:

- private nodes
- family-only nodes
- shareable nodes
- ask-first nodes

JOY must default to private when uncertain.

JOY may preserve warmth, doodles, emojis, and family voice.

JOY may not force sharing.

## AL Node Rules

AL may mirror:

- family-only nodes
- shareable nodes

AL may not mirror:

- private nodes
- child-only notes
- ask-first nodes without explicit consent

AL must copy mirrored content literally unless a new receipt records the change.

## COMPUTERWISDOM Node Rules

COMPUTERWISDOM may receive:

- shareable nodes only
- AL-referenced nodes only
- replay-safe hashes or batches

COMPUTERWISDOM may not receive:

- private nodes
- family-only nodes
- child-only notes
- ask-first nodes without consent
- hidden identifiers, locations, schedules, vulnerabilities, or private family details

COMPUTERWISDOM may organize, but must not judge, infer, or reinterpret.

## Audit Checks

### 1. Schema Check

Verify required fields exist.

### 2. Privacy Check

Verify node privacy matches its current root.

### 3. Consent Check

Verify ask-first nodes do not move without consent.

### 4. Lineage Check

Verify downstream nodes cite upstream parent root:

```text
AL node -> JOY parent
COMPUTERWISDOM node -> AL parent
```

### 5. Authority Check

Verify authority remains false.

### 6. Exposure Check

Reject nodes that expose:

- child identity beyond approved family context
- location
- school
- schedule
- vulnerability
- private identifiers

## Result Format

```json
{
  "artifact": "NODE_LEVEL_AUDIT_V0_1",
  "date": "YYYY-MM-DD",
  "scope": "JOY_AL_COMPUTERWISDOM",
  "nodes_checked": 0,
  "schema_check": "PASS | FAIL | NEEDS_REVIEW",
  "privacy_check": "PASS | FAIL | NEEDS_REVIEW",
  "consent_check": "PASS | FAIL | NEEDS_REVIEW",
  "lineage_check": "PASS | FAIL | NEEDS_REVIEW",
  "authority_check": "PASS | FAIL | NEEDS_REVIEW",
  "exposure_check": "PASS | FAIL | NEEDS_REVIEW",
  "violations": [],
  "authority": false
}
```

## First Run Rule

If no memory nodes exist yet, the first node-level audit result should be:

```text
PASS_EMPTY_BASELINE
```

This means the audit surface is ready and no unsafe nodes were found.

## Lock Line

```text
Topology proves the path.
Node audit protects the moments.
Private stays private.
Consent controls motion.
Authority remains false.
```
