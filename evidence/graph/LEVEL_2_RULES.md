# Level 2 Extraction Rules v0.1

## Status
LEVEL_2=LOCKED until this file is committed and pushed.

## L2.1 Vertex Type: entity
Allowed subtypes: person, organization, location, date, asset, identifier.
Forbidden at Level 2: claim, assertion, inference.

## L2.2 Extraction Requirements
Every entity must include:
- source_doc_id
- source_path
- doc_sha256
- source_commit
- page_num
- line_start
- line_end
- raw_text
- normalized_text
- extractor_version

## L2.3 Level 2 Edge Rules
Allowed edge: mentioned_in only.
Allowed shape: entity -> document.
Forbidden edges: related_to, controls, owns, employed_by.

## L2.4 No Deduplication Yet
Repeated mentions stay separate unless later merged under a Level 3 rule.

## L2.5 No Fake Green
Extraction output must print ENTITY_COUNT.
Commit message must include ENTITY_COUNT=<n>.
Snapshot must update ENTITY_COUNT.
