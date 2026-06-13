# JOURNAL_TO_REPLAY_TEST_PROTOCOL_V0_1

Status: TEST_PROTOCOL
Authority: false
No Fake Green: true

## Purpose

Upgrade journaling from personal notes into replay-testable records.

A journal entry is allowed to describe memory, intent, theory, frustration, hypothesis, or context. It is not allowed to promote itself into evidence without test surfaces.

This protocol separates:

- narrative
- claim
- observable surface
- external receipt
- replay test
- promotion decision

## Core Rule

```text
Journal first. Replay second. Promotion never automatic.
```

## Evidence Ladder

```text
UNKNOWN
  -> JOURNALED
  -> CLAIMED
  -> OBSERVED
  -> PRESERVED
  -> TESTABLE
  -> REPLAY_TESTED
  -> REPRODUCED
```

## State Definitions

### JOURNALED

A human-authored entry exists.

Allowed proof:

- text file
- markdown note
- JSON note
- screenshot annotation
- commit containing the note

Not enough for:

- delivery proof
- external event proof
- legal conclusion
- public authority

### CLAIMED

The journal asserts something happened.

Required fields:

```json
{
  "claim": "",
  "claimed_actor": "",
  "claimed_time": "",
  "claimed_surface": "",
  "confidence": "low | medium | high"
}
```

### OBSERVED

A surface was observed by the operator or a tool.

Required fields:

```json
{
  "surface_type": "github_pr | email | portal | screenshot | file | web_page | mail_tracking | other",
  "surface_locator": "",
  "observed_at_utc": "",
  "observer": "",
  "capture_method": "",
  "limitations": []
}
```

### PRESERVED

The observed surface was preserved as bytes or a stable reference.

Required fields:

```json
{
  "artifact_path": "",
  "sha256": "",
  "commit_sha": "",
  "preserved_at_utc": ""
}
```

### TESTABLE

A third party can attempt the replay without asking the author what to look at.

Required fields:

```json
{
  "public_entrypoint": "",
  "repo_index_path": "",
  "replay_steps": [],
  "expected_results": [],
  "failure_conditions": []
}
```

### REPLAY_TESTED

A replay attempt was performed and recorded.

Required fields:

```json
{
  "replayer": "self | external",
  "started_at_utc": "",
  "completed_at_utc": "",
  "steps_run": [],
  "matched": [],
  "mismatched": [],
  "result": "PASS | FAIL | PARTIAL"
}
```

### REPRODUCED

An independent actor reproduced the expected result from public surfaces.

Required fields:

```json
{
  "external_replayer": "",
  "external_receipt": "",
  "external_timestamp": "",
  "result": "PASS",
  "authority": false
}
```

## Mandatory Anti-Drift Gates

A journal entry cannot promote unless all gates pass.

```json
{
  "author_memory_required": false,
  "public_entrypoint_present": true,
  "repo_index_present": true,
  "external_surface_separated": true,
  "failure_conditions_defined": true,
  "promotion_rule_declared": true
}
```

## Journal Entry Template

```json
{
  "journal_id": "",
  "title": "",
  "created_at_utc": "",
  "author": "Jay Wisdom",
  "entry_type": "memory | claim | plan | observation | receipt | replay_test",
  "plain_language_entry": "",
  "claims": [],
  "observations": [],
  "preserved_artifacts": [],
  "external_receipts": [],
  "replay_test": {
    "public_entrypoint": "",
    "steps": [],
    "expected": [],
    "fail_if": []
  },
  "current_state": "JOURNALED",
  "promotion_allowed": false,
  "authority": false,
  "no_fake_green": true
}
```

## Replay Test Template

```json
{
  "test_id": "",
  "target_journal_id": "",
  "test_question": "Can a third party reproduce the claimed state without author guidance?",
  "inputs": [],
  "public_entrypoints": [],
  "commands_or_steps": [],
  "expected_outputs": [],
  "observed_outputs": [],
  "mismatches": [],
  "result": "PASS | FAIL | PARTIAL",
  "max_state_after_test": "",
  "notes": "",
  "authority": false,
  "no_fake_green": true
}
```

## MN School Meals Application

For ISD 742 / MN school meals, the current maximum state remains:

```text
PRESERVED_PRE_SEND
```

Promotion to REQUESTED requires one of:

- email delivery proof with headers
- portal submission confirmation
- certified mail tracking
- district acknowledgment
- other external timestamped receipt

GitHub commits alone cannot promote delivery.

## Multi-Repo Replay Requirement

If evidence spans multiple repositories, a canonical index must exist before replay can pass.

Required file:

```text
docs/replay/CANONICAL_REPO_INDEX_V0_1.md
```

The index must list:

- repo name
- role
- latest known default branch SHA
- relevant PRs
- public URL
- missing evidence
- authority=false

## Final Rule

```text
A journal can start a replay. It cannot finish one by itself.
```
