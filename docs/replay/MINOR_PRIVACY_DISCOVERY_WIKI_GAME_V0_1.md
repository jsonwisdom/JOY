# MINOR_PRIVACY_DISCOVERY_WIKI_GAME_V0_1

Status: GAME_SPEC
Authority: false
No Fake Green: true
Finding Posture: NO_FINDINGS_ASSERTED

## Purpose

Turn public-records discovery into a Wikipedia-style replay game.

The game rewards players for finding public policy surfaces, contracts, notices, retention schedules, vendor agreements, board materials, and privacy documents — not for making accusations.

## Core Loop

```text
Pick a page -> follow a source -> capture a public record -> classify it -> preserve it -> ask the next question
```

## Player Fantasy

You are not a prosecutor.
You are not a judge.
You are not a spy.

You are a civic librarian trying to map where student-authored content can travel.

## Game Board

Each district, vendor, policy, contract, board packet, handbook, or privacy notice is a node.

Each link between nodes is an edge.

Examples:

```text
ISD 742 Acceptable Use Policy -> Google Workspace for Education Notice
Technology Handbook -> Device Monitoring Software
Board Packet -> Vendor Contract
Vendor Contract -> Data Processing Addendum
Privacy Notice -> Retention Schedule
```

## Node Types

```json
{
  "district_policy": "official district policy or procedure",
  "student_handbook": "student-facing or parent-facing rules",
  "technology_notice": "device, account, filtering, or monitoring notice",
  "vendor_contract": "contract or service agreement",
  "dpa": "data processing agreement or privacy addendum",
  "retention_schedule": "record retention or deletion rule",
  "board_record": "agenda, minutes, packet, or approval record",
  "public_records_response": "records produced by a custodian",
  "external_law_or_guidance": "statute, agency guidance, FERPA, state law, or official FAQ"
}
```

## Scoring

Players earn points only for replayable public surfaces.

```json
{
  "public_url_found": 1,
  "official_source": 2,
  "downloaded_or_preserved_copy": 2,
  "sha256_recorded": 2,
  "node_classified": 1,
  "edge_to_another_record": 2,
  "custodian_contact_identified": 1,
  "public_records_request_drafted": 3,
  "external_response_received": 5,
  "independent_replay_pass": 10
}
```

No points for rumors, insults, private student information, doxxing, or unsupported claims.

## Red Cards

Immediate zero-score actions:

```json
[
  "requesting student names or private diaries",
  "publishing student-specific information",
  "calling a finding without records",
  "confusing vendor access possibility with proven misuse",
  "harassing staff, students, parents, or vendors",
  "claiming authority beyond public-records requester"
]
```

## Level Structure

### Level 1: Find the Public Door

Goal: locate official district pages.

Targets:

- district website
- board policy page
- technology department page
- student handbook
- acceptable use policy
- privacy notices
- records custodian contact

Promotion condition:

```text
At least 3 official district URLs preserved.
```

### Level 2: Find the Platform Layer

Goal: identify school technology systems that may store student-authored content.

Targets:

- learning management systems
- school-issued account platforms
- journaling or writing tools
- counseling or wellness platforms
- filtering or monitoring tools
- productivity suites

Promotion condition:

```text
At least 1 platform surface linked to an official district source.
```

### Level 3: Find the Contract Trail

Goal: locate contracts, DPAs, privacy notices, or vendor terms.

Promotion condition:

```text
At least 1 vendor record or privacy addendum preserved.
```

### Level 4: Ask the Custodian

Goal: send a neutral public-records request.

Promotion condition:

```text
External delivery receipt required.
```

No delivery receipt means no REQUESTED state.

### Level 5: Replay the Map

Goal: another person follows the game map and reaches the same nodes.

Promotion condition:

```text
Independent replay pass from public entrypoint without author guidance.
```

## Card Template

```json
{
  "card_id": "",
  "title": "",
  "node_type": "",
  "public_url": "",
  "source_owner": "",
  "captured_at_utc": "",
  "sha256": "",
  "excerpt": "",
  "summary": "",
  "summary_role": "analysis_only_not_replay_source",
  "mentions_student_authored_content": false,
  "mentions_monitoring_or_access": false,
  "mentions_vendor_storage": false,
  "mentions_retention_or_deletion": false,
  "linked_nodes": [],
  "risk_language": "none | low | medium | high",
  "finding_asserted": false,
  "authority": false,
  "evidence_fields_locked": true,
  "ui_label": "",
  "ui_feedback": "",
  "ui_red_card_message": ""
}
```

## Evidence / UI Separation Rules

Evidence fields are boring record fields. UI fields are game feedback fields.

```json
{
  "evidence_fields": [
    "excerpt",
    "summary",
    "public_url",
    "source_owner",
    "sha256",
    "linked_nodes"
  ],
  "ui_fields": [
    "ui_label",
    "ui_feedback",
    "ui_red_card_message"
  ],
  "write_rule": "Only the capture step may write evidence fields. UI steps may write ui_fields only.",
  "reject_if": [
    "ui_step_writes_excerpt",
    "ui_step_writes_summary",
    "ui_step_writes_public_url",
    "ui_step_writes_source_owner",
    "ui_step_writes_sha256",
    "ui_step_writes_linked_nodes",
    "ui_text_embedded_in_excerpt",
    "ui_text_embedded_in_public_url"
  ]
}
```

`excerpt` is the verbatim public-record field and the replay source of truth.

`summary` is analysis-only. It may help a reader understand a card, but it is not used for reproducibility.

Brenda commentary, jokes, red-card messages, and scoring flavor live only in `ui_label`, `ui_feedback`, and `ui_red_card_message`.

## Brenda UI Examples

```json
{
  "pick": "Great, you clicked a link. Let's see if it still exists tomorrow.",
  "red_card_404": "Cease and Desist (from yourself): this link expired faster than milk in July.",
  "pass": "Boring, reproducible, beautiful. +5 clerk time returned.",
  "fail": "You saved a screenshot of a tweet. I cannot replay a vibe. Try the actual PDF."
}
```

These examples are UI-only. They must never be written into `excerpt`, `public_url`, `source_owner`, `sha256`, or `linked_nodes`.

## Replay Test Template

```json
{
  "test_id": "",
  "starting_url": "",
  "steps": [],
  "expected_nodes": [],
  "observed_nodes": [],
  "missing_nodes": [],
  "unexpected_nodes": [],
  "result": "PASS | FAIL | PARTIAL",
  "replayer": "self | external",
  "authority": false,
  "no_fake_green": true
}
```

## District-Facing Boundary

The game is internal/public-interest mapping only.

The district-facing packet must stay neutral:

- no game language
- no accusations
- no memes
- no student data
- no private diary request
- no rights conclusion
- no finding

## Final Rule

```text
Make discovery addictive, but keep the evidence boring.
```
