# RCB_00001_00002_RUN_ATTEMPT_CLASSIFICATION_V0_1

## STATUS: RUN_ATTEMPT_CLASSIFIED
## AUTHORITY: FALSE
## NO_FAKE_GREEN: TRUE

```json
{
  "repo": "jsonwisdom/JOY",
  "trigger_commit": "32e9dfb1d121e9638f6aac597ba579c484733274",
  "workflow": ".github/workflows/rcb-00001-00002-parse-witness.yml",
  "workflow_file_changed": true,
  "workflow_trigger": "OBSERVED",
  "workflow_run": "NOT_OBSERVED_BY_CONNECTOR",
  "step_4_full_parse": "BLOCKED",
  "constitution_executed": false,
  "authority": false,
  "no_fake_green": true
}
```

## Run-Attempt Classification

| Node | State |
| --- | --- |
| Trigger Commit | GREEN |
| Workflow File Changed | GREEN |
| Parse Run Output | NOT_OBSERVED |
| Step 4 Full Content Parse | BLOCKED |
| No Fake Green | ACTIVE |

## Continuity Graph

```text
workflow_file_verified
↓
packaging_verified
↓
trigger_commit_observed
↓
RUN_NOT_OBSERVED
↓
step_4_full_content_parse
↓
step_5_sha256_verification
```

## Boundary Enforcement

```text
Connector Witness != Local Validation
Push Trigger != Run Receipt
Workflow File Diff != Workflow Execution
GitHub Blob SHA != SHA256 Raw Bytes
Connector Lookup != Ground Truth of Runner Behavior
NO_FAKE_GREEN_ACTIVE
```

## Next Admissible Receipts

Only one of the following can advance the graph:

```text
workflow_run_success
workflow_run_failure
workflow_infra_failure
```

## Ruling

Trigger commit observed.
Workflow file changed.
Run output not witnessed by connector.
Step 4 remains blocked.
No authority implied.
No fake green.
