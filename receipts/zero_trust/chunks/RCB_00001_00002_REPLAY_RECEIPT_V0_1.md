# RCB_00001_00002_REPLAY_RECEIPT_V0_1

Status: CHUNK_REPLAY_DRAFT
Authority: false
Verified: connector blob/content-shape only
No Fake Green: true

## Source Commit

`5d6ed4f06a3f032f5a818901033e28edaa7fb78b`

## Cases

- RCB-00001: `artifacts/goblin_constellation_paths_v0_1.json`
- RCB-00002: `artifacts/goblin_constellation_v0_1.json`

## Connector Replay Read-Back

### RCB-00001

```json
{
  "path": "artifacts/goblin_constellation_paths_v0_1.json",
  "source_commit": "5d6ed4f06a3f032f5a818901033e28edaa7fb78b",
  "git_blob_sha": "a1d67db675f4ef2a8d7db71902c5a7ddb6348a5c",
  "content_recovered_by": "GitHub.fetch_blob",
  "content_shape": "json_object_with_scanner_version_generated_at_path_surface",
  "scanner_version_seen": "0.1.0-level1-paths",
  "generated_at_seen": "2026-06-11T17:56:08.454Z",
  "first_repo_seen": "jsonwisdom/AL",
  "first_path_seen": "_tests/replay_test_v1.py"
}
```

### RCB-00002

```json
{
  "path": "artifacts/goblin_constellation_v0_1.json",
  "source_commit": "5d6ed4f06a3f032f5a818901033e28edaa7fb78b",
  "git_blob_sha": "73ad57e39d29b8df8edbbaf3c10d486769ff7eb5",
  "content_shape": "json_object_with_scanner_version_generated_at_root_identity_repos",
  "scanner_version_seen": "0.1.0",
  "generated_at_seen": "2026-06-11T17:58:10.772Z",
  "first_repo_seen": "jsonwisdom/AL"
}
```

## Correction

Earlier connector line-read returned no visible payload for RCB-00001.
Direct blob fetch recovered visible JSON content.
The anomaly is corrected without using a terminal.

## Ruling

Small chunk replay only.
No final truth ruling.
No authority implied.
RCB-00001 and RCB-00002 both have connector-visible JSON content-shape evidence.
No fake green.
