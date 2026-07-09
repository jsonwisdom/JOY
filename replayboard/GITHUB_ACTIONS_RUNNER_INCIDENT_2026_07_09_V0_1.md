---
receipt_id: GITHUB_ACTIONS_RUNNER_INCIDENT_2026_07_09_V0_1
artifact_type: REPLAYBOARD_INCIDENT_NOTE
classification: EXTERNAL_RUNNER_DEGRADATION
adapter: GITHUB_ACTIONS_HOSTED_RUNNER
affected_surface: GitHub Actions
affected_workflow_class: JOY Governance Rails v0.1
runner_class: ubuntu-latest
authority: false
no_fake_green: true
joy_core_failure: false
external_adapter_drift: true
public_render_allowed: false
consent_required: false
receipt_status: INCIDENT_NOTE_DRAFT
hash_status: UNHASHED_PENDING_COMMIT
created_after_pr_44: true
---

# GITHUB_ACTIONS_RUNNER_INCIDENT_2026_07_09_V0_1

JOY ReplayBoard — External Adapter Incident Note

## Classification

- Incident ID: `GITHUB_ACTIONS_RUNNER_INCIDENT_2026_07_09_V0_1`
- Type: `EXTERNAL_RUNNER_DEGRADATION`
- Adapter: `GITHUB_ACTIONS_HOSTED_RUNNER`
- Affected surface: GitHub Actions
- Affected workflow class: JOY Governance Rails v0.1
- Runner class: `ubuntu-latest`
- Authority: false
- No Fake Green: true
- JOY core failure: false
- External adapter drift: true

## Summary

On 2026-07-09, JOY observed required GitHub Actions checks remaining in a queued state during governance PR processing.

Affected checks included:

- `JOY Governance Rails v0.1`
- `Zero Trust Audit`
- related GitHub-hosted runner checks

The observed behavior matched a public GitHub Actions platform incident involving delayed starts for GitHub-hosted runner jobs.

This note does not treat GitHub as a source of truth for JOY. It records GitHub Actions as an external execution adapter whose availability may delay JOY governance execution but cannot override JOY semantics.

## External Evidence

GitHub Status reported an unresolved incident titled:

`Delays starting Actions runs`

GitHub classified Actions as degraded performance and reported that some GitHub-hosted runner jobs experienced start delays, with mitigation in progress.

Source: githubstatus.com public incident feed.

## JOY Observation

During the incident window, JOY governance PR checks:

- entered queued state
- did not receive hosted runners immediately
- emitted no workflow logs before runner assignment
- showed no job-level failure during the queued state
- showed no repo conflict
- performed no main mutation while checks were unobserved
- performed no force-merge while checks were unobserved
- assigned no fake green

This matches `EXTERNAL_RUNNER_DEGRADATION`, not JOY failure.

## Governance Interpretation

Queued state is classified as:

`EXTERNAL_RUNNER_DEGRADATION`

Not:

- `JOY_CORE_FAILURE`
- `SCHEMA_FAILURE`
- `RECEIPT_FAILURE`
- `CONSENT_FAILURE`
- `AUTHORITY_FAILURE`
- `NO_FAKE_GREEN_FAILURE`

## Adapter Boundary

GitHub Actions is an execution adapter, not a JOY authority.

Under `JOY_EXTERNAL_ADAPTERS_ARE_NOT_SOURCES_OF_TRUTH`:

- GitHub may report queued, success, failure, or degraded states.
- JOY may use those states as evidence, not truth.
- GitHub does not define JOY correctness.
- GitHub success is not sufficient for semantic approval.
- GitHub queue delay is not evidence of JOY failure.

## JOY Response

Correct JOY response during this incident:

- hold merge
- do not push queue-poking commits
- do not force-merge
- do not assume pass
- do not declare green without observed successful checks
- wait for adapter recovery
- rerun failed jobs only if a timeout or start-delay failure appears

## Runner Strategy Note

A future governed PR may introduce a self-hosted runner lane:

`JOY_SELF_HOSTED_GOVERNANCE_RUNNER`

Such a runner would remain non-authoritative and must be treated as a monitored execution adapter.

Potential future runner label:

```yaml
runs-on: [self-hosted, joy-governance]
```

This must not be introduced as an emergency bypass. It requires:

- governance review
- receipt trail
- replay evidence

## Invariants Held

- `JOY_AUTHORITY_FALSE`: held
- `JOY_NO_FAKE_GREEN`: held
- `JOY_EXTERNAL_ADAPTERS_ARE_NOT_SOURCES_OF_TRUTH`: held
- `JOY_RECEIPT_REQUIRED_FOR_GOVERNED_MERGE`: held
- `JOY_REPLAY_REQUIRED_FOR_PUBLIC_RENDER`: unaffected
- `JOY_CONSENT_REQUIRED_FOR_FAMILY_ARTIFACTS`: unaffected

## Outcome

The incident delayed governance execution but did not compromise JOY governance state.

Final classification:

`EXTERNAL_RUNNER_DEGRADATION_LOGGED_AUTHORITY_FALSE`
