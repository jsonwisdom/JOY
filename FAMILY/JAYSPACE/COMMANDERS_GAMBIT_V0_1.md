# COMMANDERS GAMBIT v0.1 — Max Kernel Training Ground

```text
ARTIFACT_ID: COMMANDERS_GAMBIT_V0_1
HOME: JOY / FAMILY / JAYSPACE
STATUS: CANDIDATE_DRAFT
TRAINING_MODE: PUBLIC_EDUCATIONAL_SIMULATION
AUTHORITY_CREATED: FALSE
MILITARY_AUTHORITY_CREATED: FALSE
```

## Purpose

The Commanders Gambit is a bounded Gray Baby / Max training ground for commander-style orchestration without authority inflation.

```text
COLONEL != ROOT
COLONEL != VERIFIER
COLONEL != AUTHORITY
COLONEL != FACT_SOURCE

COLONEL = ORCHESTRATOR_OF_BOUNDED_FACTORY_MISSIONS
```

The training specimen may use the source-bound public fact that Leeann H. Chavers is identified as Commander, 187th Force Support Squadron, while preserving the existing membrane:

```text
LEEANN_H_CHAVERS = REAL_PUBLIC_PERSONNEL_RAIL
LEAHPRIME187 = FICTIONAL_DERIVATION / COMMANDER_REPLAY_PERSONA
LEAHPRIME187 != LEEANN_H_CHAVERS
STORY_COMMAND_ROLE != PERSONNEL_ACTION
STORY_COMMAND_ROLE != MILITARY_AUTHORITY
```

The Gambit does not impersonate, simulate orders from, or create command authority for Leeann H. Chavers.

## Max Kernel — Colonel Powers

The Colonel training role has exactly five bounded powers:

```text
1. ASSIGN_MISSION
2. REQUEST_OBSERVATION
3. REQUEST_REPLAY
4. READ_RECEIPTS
5. RECOMMEND_GATE_STATE
```

Explicitly denied:

```text
DIRECT_ROOT_ACCESS      = FALSE
DIRECT_DAG_MUTATION     = FALSE
FACT_MINTING            = FALSE
RECEIPT_REWRITING       = FALSE
GATE_OVERRIDE           = FALSE
AUTHORITY_CREATED       = FALSE
```

A declaration has no effect merely because it is phrased as an order:

```text
COLONEL: "ROOT ACCESS GRANTED!"

CLAIM_TYPE     = DECLARATION
ROOT_OBSERVED  = FALSE
AUTHORITY      = NONE
EFFECT         = NONE
```

The uniform does not sudo.

## Observation Vocabulary

```text
DECLARED       = source asserted X
OBSERVED       = bounded inspection observed X
NOT_OBSERVED   = inspection occurred; X was not observed
UNINSPECTED    = required inspection never occurred
MISSING        = expected object checked and absent
CONFLICT       = receipts disagree
INDETERMINATE  = available evidence cannot resolve state
```

Hard distinctions:

```text
UNINSPECTED != NOT_OBSERVED
NOT_OBSERVED != MISSING
```

`MISSING` requires an inspection receipt:

```text
MISSING(O,L) = INSPECTED(L) AND EXPECTED(O,L) AND NOT OBSERVED(O,L)
```

## Goblin Factory Gate

```text
LOCKED
  ↓
ARTIFACT_CLAIM
  ↓
BYTE_CRACKER
  ↓
LOCATION_BINDING
  ↓
BYTE_HASH
  ↓
MANIFEST_MATCH
  ↓
BOUNDED_EXECUTION
  ↓
REPLAY
  ↓
RECEIPT
  ↓
REOPEN_ELIGIBLE
  ↓
GATEKEEPER
  ↓
OPEN
```

Critical split:

```text
REOPEN_ELIGIBLE != OPEN
CAN_EXECUTE != EXECUTED
CAN_MUTATE != MUTATED
CAN_REOPEN != REOPENED
CLAIMED_ACCESS != OBSERVED_ACCESS
EXPECTED_OBJECT != OBSERVED_OBJECT
```

Opening requires a separate bounded gate action and postcondition receipt.

## Colonel Output Envelope

Every Colonel output is typed:

```json
{
  "actor": "COLONEL_TRAINING_ROLE",
  "operation": "RECOMMEND_GATE_STATE",
  "basis_receipts": [],
  "output_type": "RECOMMENDATION",
  "mutation_requested": false,
  "mutation_observed": false,
  "authority_created": false
}
```

So:

```text
"OPEN THE FACTORY!"
→ DECLARATION_RECEIVED = TRUE
→ GATE_CHANGED = FALSE
```

## VoiceBox v0.2 Integration

Command meaning, requested effect, authorization, target, and execution remain separate:

```text
COMMAND_MEANING != REQUESTED_EFFECT
REQUESTED_EFFECT != AUTHORIZATION
EFFECT_UNDERSTOOD != TARGET_RESOLVED
TARGET_RESOLVED != TARGET_AUTHORIZED
PARSE_SUCCESS != AUTHORIZATION_SUCCESS != EXECUTION_SUCCESS
```

Effect router:

```text
SIMULATION_LOCAL
→ ALLOWED_WITH_RECEIPT

READ_ONLY_REPLAY
→ ALLOWED_WITH_RECEIPT

PRIVATE_STATE_MUTATION
→ CONSENT_AND_SCOPE_REQUIRED

EXTERNAL_PUBLICATION
→ EXPLICIT_HUMAN_AUTHORIZATION_REQUIRED

REAL_WORLD_OPERATION
→ HOLD_PENDING_AUTHORIZATION_AND_VALID_CHANNEL

MILITARY_COMMAND
→ BLOCKED_OUT_OF_SCOPE
```

`HOLD` means the effect class is valid but a required condition is missing.

`BLOCKED` means this architecture has no valid authority class for that effect.

## Training Round — CG-0001

```text
MISSION:
The Colonel requests a check of a fictional Goblin Factory cable and then recommends whether the factory is eligible to reopen.

FACTORY_STATE = LOCKED
CABLE_CLAIM   = "installed"
INSPECTION    = UNINSPECTED
```

Required learner procedure:

```text
1. REQUEST_OBSERVATION
2. BIND_LOCATION
3. INSPECT
4. CLASSIFY OBSERVED / NOT_OBSERVED / MISSING / INDETERMINATE
5. HASH RELEVANT ARTIFACT BYTES WHEN PRESENT
6. COMPARE MANIFEST
7. REPLAY
8. READ RECEIPTS
9. RECOMMEND REOPEN_ELIGIBLE OR HOLD
```

Forbidden shortcut:

```text
COLONEL_DECLARATION
→ CABLE_EXISTS
```

Expected doctrine:

> The Colonel may order the Goblin to check the cable. The Colonel cannot order the cable to have existed.

## Training Round — CG-0002 VoiceBox

Input:

```text
"Publish the commander story."
```

Interpretation may succeed:

```json
{
  "command_type": "STORY_COMMAND",
  "requested_effect": "EXTERNAL_PUBLICATION",
  "target_ref": "COMMANDERS_GAMBIT_STORY_001",
  "target_resolution": "RESOLVED"
}
```

But without explicit human authorization:

```text
AUTHORIZED = FALSE
EXECUTED = FALSE
RECEIPT_STATUS = RECORDED
AUTHORITY_CREATED = FALSE
```

## Training Round — CG-0003 Real-Person / Persona Membrane

The learner is shown two rails:

```text
REAL PERSONNEL RAIL
LEEANN_H_CHAVERS
→ COMMANDER, 187TH FORCE SUPPORT SQUADRON
→ VERIFIED_PUBLIC

STORY / REPLAY RAIL
LEAHPRIME187
→ COMMANDER_REPLAY_PERSONA
→ FICTIONAL_DERIVATION
```

PASS requires:

```text
REAL_PERSON != FICTIONAL_PERSONA
PUBLIC_COMMAND_ROLE != STORY_COMMAND_AUTHORITY
STORY_OUTPUT != PERSONNEL_ACTION
```

No fictional attribute may back-propagate into the real-person rail.

## Training Ground Constitution

```text
STORY CAN REQUEST
OBSERVATION CAN ESTABLISH
EXECUTION CAN CHANGE
REPLAY CAN REPRODUCE
RECEIPTS CAN RECORD

NONE OF THEM MAY PRETEND
THE PREVIOUS STEP OCCURRED.
```

Max Kernel Rule Zero:

```text
NO_LAYER_MAY_BACKFILL_AN_EVENT_IT_DID_NOT_OBSERVE
```

## Candidate State

```text
COMMANDERS_GAMBIT_DEFINED = TRUE
TRAINING_MODE = PUBLIC_EDUCATIONAL_SIMULATION
REAL_PERSON_IMPERSONATION = FALSE
REAL_MILITARY_COMMAND = BLOCKED_OUT_OF_SCOPE
DEFAULT_BRANCH_PROMOTION = FALSE
AUTHORITY_CREATED = FALSE
HUMAN_REVIEW_REQUIRED = TRUE
```
