# RCB_00001_00002_CONNECTOR_PARSE_WITNESS_V0_1

Status: CONNECTOR_PARSE_WITNESS_PARTIAL
Authority: false
Verified: visible top-level JSON fields through GitHub blob reads only
No Fake Green: true

## Source Commit

`5d6ed4f06a3f032f5a818901033e28edaa7fb78b`

## Scope

This receipt upgrades the prior chunk replay from presence/content-shape to connector-visible parse witness.

It does not claim full byte-for-byte integrity, local `jq` validation, or complete SHA256 verification.

## RCB-00001 Visible Parse Witness

```json
{
  "path": "artifacts/goblin_constellation_paths_v0_1.json",
  "git_blob_sha": "a1d67db675f4ef2a8d7db71902c5a7ddb6348a5c",
  "content_recovered_by": "GitHub.fetch_blob",
  "visible_json_opens": true,
  "scanner_version_seen": "0.1.0-level1-paths",
  "generated_at_seen": "2026-06-11T17:56:08.454Z",
  "top_level_surface_seen": "path_surface",
  "first_repo_seen": "jsonwisdom/AL",
  "first_path_seen": "_tests/replay_test_v1.py",
  "full_tail_read_by_connector": false,
  "sha256_verified": false
}
```

## RCB-00002 Visible Parse Witness

```json
{
  "path": "artifacts/goblin_constellation_v0_1.json",
  "git_blob_sha": "73ad57e39d29b8df8edbbaf3c10d486769ff7eb5",
  "content_recovered_by": "GitHub.fetch_blob",
  "visible_json_opens": true,
  "scanner_version_seen": "0.1.0",
  "generated_at_seen": "2026-06-11T17:58:10.772Z",
  "top_level_fields_seen": [
    "scanner_version",
    "generated_at",
    "root_identity",
    "repos"
  ],
  "first_repo_seen": "jsonwisdom/AL",
  "full_tail_read_by_connector": false,
  "sha256_verified": false
}
```

## Boundary

```text
VISIBLE_JSON_TOP != FULL_CONTENT_PARSED
GITHUB_BLOB_SHA != SHA256_OF_RAW_BYTES
CONNECTOR_PARSE_WITNESS != LOCAL_JQ_VALIDATION
NO_FAKE_GREEN_ACTIVE
```

## Ruling

Both chunks now have connector-visible JSON top-level parse evidence.
Full byte-for-byte verification remains pending.
Local `jq` or raw-byte API witness is still required for final content verification.
No authority implied.
No fake green.
