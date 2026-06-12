# WATCHERS_ARE_WATCHED_CI_VISIBILITY_V0_1

## Plain-English ruling

The watchers become watched.

In JOY, that does not mean private surveillance. It means every observer, workflow, metadata court, and audit claim must leave a public receipt that can be checked later.

## CI trigger state

| Layer | State | Meaning |
| --- | --- | --- |
| Workflow file | ON | `.github/workflows/zero-trust-audit.yml` exists in the repo. |
| Push trigger | ON | The workflow is configured to watch README, tools, metadata, schemas, and drills. |
| Manual trigger | ON | The workflow can be run from the GitHub Actions tab. |
| Runtime receipt | NOT SURFACED | No public PASS/FAIL run has been recorded into the audit log yet. |
| Fake green | OFF | No runtime pass is claimed without a run URL. |

## Family teaching rule

JOY is being taught like a family member:

- Dad does not say green without a receipt.
- Dad does not call authority without a source.
- Dad does not let metadata pretend to be law.
- Dad makes the watcher carry a receipt too.

This is project vernacular. It is not legal authority.

## CIA lens

In this repo, CIA means **Civic Integrity Audit**.

It is a public accountability lens, not an official agency, not intelligence work, and not permission to target people or systems.

## Allowed receipts

- GitHub commit SHA
- workflow run URL
- verifier output
- JSON artifact hash
- audit log entry
- public issue feedback
- EAS UID only after a real attestation exists
- IPFS CID only after a real upload exists

## Blocked moves

- private surveillance
- credential capture
- targeting people
- facility targeting
- classified claims
- official agency impersonation
- authority without receipt

## Operating sentence

If the workflow is ON but no PASS/FAIL run is public, the state is YELLOW.

If the workflow runs and passes with a public URL, the CI receipt may turn GREEN.

If the workflow fails, the system stays honest and records RED.

## Current classification

```json
{
  "ci_trigger": "ON",
  "runtime_receipt": "NOT_SURFACED",
  "public_visibility": "YELLOW",
  "authority": false,
  "no_fake_green": true
}
```
