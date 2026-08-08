# RootReplay Binding Protocol v1

## Purpose

Bind the Purpose Portal manifest to a reproducible family replay receipt without treating identity, repository presence, workflow status, or a placeholder value as authority.

`authority = false`

## Family root

Every audit MUST begin and end at the same explicit family workspace root.

```bash
ROOT_REPLAY_HOME="$GITHUB_WORKSPACE/root-replay"
cd "$ROOT_REPLAY_HOME"
```

Repository-specific work MUST execute in subshells or equivalent isolated contexts. No operation may rely on the prior operation's working directory.

At completion:

```bash
cd "$ROOT_REPLAY_HOME"
test "$PWD" = "$ROOT_REPLAY_HOME"
```

## Binding inputs

A binding receipt MUST record:

- exact repository set
- default branch or explicit ref for each repository
- resolved commit SHA for each repository
- deterministic file manifest hash for each repository
- family manifest hash computed from the ordered repository receipts
- workflow run ID
- workflow commit SHA
- anomaly count and anomaly pointers
- portal manifest SHA-256 before binding
- authority state `false`

## Canonical repository order

1. `jsonwisdom/JOY`
2. `jsonwisdom/AL`
3. `jsonwisdom/COMPUTERWISDOM`
4. `jsonwisdom/receiptos-base`

The family binding hash MUST be computed over deterministic JSON using that order. Repository names, resolved commit SHAs, and repository manifest SHA-256 values are required fields.

## Promotion ladder

```text
UNBOUND_PENDING_REPLAY_RECEIPT
  -> FAMILY_WORKSPACE_CREATED
  -> REPOSITORY_REFS_RESOLVED
  -> REPOSITORY_MANIFESTS_EMITTED
  -> ANOMALIES_RECORDED
  -> FAMILY_MANIFEST_EMITTED
  -> FAMILY_BINDING_HASH_COMPUTED
  -> INDEPENDENT_REPLAY_MATCHED
  -> PURPOSE_PORTAL_BOUND
```

No state may be skipped.

## No-fake-green rules

The following do NOT establish a valid binding:

- a shortened Git SHA
- a placeholder hash
- a successful workflow conclusion without downloaded receipt inspection
- repository presence alone
- a public URL alone
- an identity name alone
- absence of reported anomalies

A valid binding requires an observed family replay receipt and an independently recomputed matching family hash.

## Binding receipt shape

```json
{
  "receipt_type": "PURPOSE_PORTAL_ROOT_BINDING_V1",
  "identity_anchor": "jaywisdom.base.eth",
  "authority": false,
  "workflow_run_id": null,
  "workflow_commit_sha": null,
  "repositories": [],
  "family_manifest_sha256": null,
  "portal_manifest_sha256_before_binding": null,
  "independent_replay": {
    "performed": false,
    "recomputed_family_manifest_sha256": null,
    "match": null
  },
  "binding_status": "PENDING"
}
```

## Portal update rule

Only after an independently replayed family hash matches may `family/PURPOSE_PORTAL_ROOT.json` be updated from:

```json
"status": "UNBOUND_PENDING_REPLAY_RECEIPT"
```

to:

```json
"status": "BOUND_VERIFIED"
```

The final manifest MUST include the full 64-character SHA-256 family binding hash and a pointer to the inspected receipt artifact.

## Timer boundary

No schedule is authorized by this protocol. Timer promotion requires repeated manual runs with deterministic outputs, acceptable anomaly noise, and inspected receipts.
