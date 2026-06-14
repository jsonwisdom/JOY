# REPO CHAIN — ALMS THESIS APPLICATION V0.1

**Status:** REPO_CHAIN_RULE_DRAFT  
**Truth State:** GREEN_FOR_DOCTRINE / YELLOW_FOR_FULL_CHAIN_EXECUTION  
**NO_FAKE_GREEN:** ACTIVE  
**Root Doctrine:** ALMS OPERATING THESIS V1  
**Date:** 2026-06-13

## Purpose

Apply the ALMS Operating Thesis V1 to the repository chain.

The thesis states:

```text
Source → Hash → Receipt → Witness → Verification
```

This file turns that doctrine into a repo-chain operating rule for JOY, AL, COMPUTERWISDOM, ALABAMA ALMS, Wisdom Family, and future workflow batches.

## Root Witness

```text
ARTIFACT:
ALMS_OPERATING_THESIS_V1

COMMIT:
2787cb7a2d99045419dcee89cb6878910d4f9ba3

CID:
bafkreibek27v65svqbbmpmqytmu4t7vsdibp2lk7q7sk7xqb5vpmtwc5fu

SCHEMA_UID:
0x60b411ae490910a5c647b725969e425b9c4dfc4ffdc2e9bd591709e9614d21dd

ATTESTATION_UID:
0xbaf61464a091f8fe6f2e7ba9ff0bcb68855535cd61be7be3f2432afc9fdd4cd2

TX_HASH:
0xa85186db33785e25b9bfcd319fb1a653da803bf82d27ab372bb7b35f96323a0a
```

## Repo Chain Rule

A repository claim may not be promoted to GREEN unless it can produce the following chain:

```text
1. Source artifact exists in repo
2. Commit SHA records the artifact
3. Hash or CID identifies the content
4. Receipt records the claim and evidence
5. Witness exists when promotion requires independent verification
6. Replay path is clear enough for another observer to verify
```

## Chain States

```text
DRAFT      = idea exists, no source artifact required yet
SOURCE     = file exists in repo
HASHED     = content hash or CID exists
RECEIPTED  = human-readable receipt exists
WITNESSED  = independent witness exists, such as EAS UID or equivalent
GREEN      = replay path complete
YELLOW     = preserved but missing at least one promotion requirement
RED        = contradiction, mismatch, or failed replay
```

## Repo Roles

```text
JOY:
Meaning, family memory, public receipts, human context

Wisdom Family:
Personal memory, emotional artifacts, love-first lanes

COMPUTERWISDOM:
Verification posture, machine witness framing, operating proofs

AL:
Execution engine, schemas, validators, workflows, reproducible checks

ALABAMA ALMS:
Civic audit lane, receipts, public accountability, replay doctrine

ALMS:
Doctrine, witness rules, source/hash/receipt/witness/verification path
```

## Promotion Rule

```text
No receipt = No authority
No witness = No promotion
No replay = No green
```

## Tool Neutrality

GitHub is a source and execution clock.

CID is content-addressed memory.

EAS is an independent witness layer.

JSON schemas are machine-readable constraint surfaces.

None of these tools are the thesis.

The thesis is the requirement that claims preserve enough evidence to be independently verified.

## Mechanical Clock Pattern

Every workflow batch should produce:

```text
batch_id
repo
branch
commit_sha
workflow_run_id
artifact_paths
artifact_hashes_or_cids
truth_state
no_fake_green
optional_schema_uid
optional_attestation_uid
optional_tx_hash
```

## Immediate Application

This rule applies first to:

```text
jsonwisdom/JOY
jsonwisdom/AL
COMPUTERWISDOM lanes
Wisdom Family receipts
ALABAMA ALMS civic audit receipts
future workflow batch receipts
```

## Closing

Verification is stronger than assertion.

Replay is stronger than memory.

Evidence is stronger than narrative.

Every future repo claim routes through:

```text
Source → Hash → Receipt → Witness → Verification
```
