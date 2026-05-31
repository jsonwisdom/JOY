# Operator Hash Trigger v0.1

Purpose: define when the operator must supply a real commit SHA for replay hash generation.

Authority remains false.

## Rule

Ask the operator for a SHA only when a shell command is about to compute or lock a hash.

Do not ask for a SHA during planning, drafting, discussion, or issue triage.

## When SHA is needed

A SHA is needed when running a command that produces one of these values:

- `index_entry_hash`
- `canonical_json_sha256`
- `known_good_output_hash`
- any L3 root hash derived from committed files

## Operator prompt

When the SHA is needed, prompt the operator with this exact command surface:

```text
SHA needed by operator.

Run:

git rev-parse HEAD

Then run:

python lock_replay_proof.py <REAL_JOY_COMMIT_SHA>
```

## Shell trigger

```bash
JOY_SHA=$(git rev-parse HEAD)
python lock_replay_proof.py "$JOY_SHA"
```

## Environment A/B rule

Run the same shell trigger in Environment A and Environment B.

Environment B must be a fresh clone or independent runtime.

Do not copy hashes from Environment A into Environment B.

## PASS condition

Replay is proven only if Environment A and Environment B independently produce matching values for:

```json
{
  "index_entry_hash": "sha256:...",
  "canonical_json_sha256": "sha256:...",
  "known_good_output_hash": "sha256:..."
}
```

## Boundary

A matching replay makes Issue #14 closable.

It does not grant authority.

```json
{
  "replay_proven": true,
  "issue_closable": true,
  "authority": false
}
```
