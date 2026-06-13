# CATEGORIES_MATRIX_INDEXING_ENGINE_V0_1

```json
{
  "artifact": "CATEGORIES_MATRIX_INDEXING_ENGINE_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/pattern/CATEGORIES_MATRIX_INDEXING_ENGINE_V0_1.md",
  "parent_artifact": "PATTERN_REINFORCEMENT_V0_1",
  "parent_commit": "e24273f42e1aa467ce9f204d6c618e764659f8d8",
  "live_cursor": "https://github.com/jsonwisdom/JOY/issues/35",
  "lane": "MN_AUDIT",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "state": "SMALL_SCALE_RETEST_PREPARED",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Purpose

This artifact turns the Arena into an indexing engine.

Every new claim, loss, receipt, agency surface, public record, on-chain surface, screenshot, commit, or replay gets sorted before it gets promoted.

The engine prevents scoreboard emotion from outrunning evidence.

## Core Rule

```text
Classify first.
Index second.
Gate third.
Promote never without receipts.
```

## Category Matrix

| Category | Input Type | Minimum Surface | Default State | Promotion Gate | Downgrade Trigger |
|---|---|---|---|---|---|
| CLAIM | Statement, allegation, thesis, hypothesis | Text claim with source or author | CLAIMED | observation surface found | no source, contradiction, unsupported leap |
| OBSERVATION | screenshot, public page view, repo file view, visible artifact | public_url + fetched_at | OBSERVED | content_hash + witness/replay | page unavailable, mismatch, stale capture |
| REQUEST | public-record request, agency intake, formal demand | submitted request copy + date | REQUESTED | agency acknowledgement or receipt | no submission proof, wrong agency, wrong scope |
| RECEIPT | response, confirmation, tx, commit, UID, CID, hash | stable identifier | RECEIVED | preservation hash + replay path | identifier does not resolve or match |
| PRESERVATION | archived copy, local hash, repo commit, IPFS, release | content_hash + storage path | PRESERVED | independent replay confirms identity | hash mismatch, missing bytes, broken path |
| VERIFICATION | external witness, reproduced fetch, independent replay | all four surfaces | VERIFIED | repeated replay or immutable anchor | witness contradiction, partial reproduction |
| IMMUTABILITY | signed release, tag, EAS, on-chain tx, timestamped archive | immutable reference + content identity | IMMUTABLE_CANDIDATE | later recovery proves same record | anchor points to wrong artifact |
| WHAMMY | failed claim, failed hype, false green, busted assumption | autopsy surface | WHAMMY_CANDIDATE | pattern extraction | refusal to autopsy, repeated drift |
| PROTOCOL_ASSET | failure converted into reusable rule | pattern + gate + retest plan | PROTOCOL_ASSET | successful small retest | no retest, vague rule, no enforcement |
| LIVE_CURSOR | issue, PR, checklist, task, next gate | open execution surface | OPEN | checklist completion | abandoned cursor, missing owner, stale state |

## Index Fields

Every indexed item should use this shape:

```json
{
  "index_id": "IDX_0000",
  "category": "CLAIM | OBSERVATION | REQUEST | RECEIPT | PRESERVATION | VERIFICATION | IMMUTABILITY | WHAMMY | PROTOCOL_ASSET | LIVE_CURSOR",
  "title": "Short human-readable title",
  "source": "Where this came from",
  "public_url": null,
  "fetched_at": null,
  "content_hash": null,
  "witness_service_or_replay_surface": null,
  "current_state": "CLAIMED",
  "promotion_allowed": false,
  "downgrade_rule": "What sends this backward",
  "next_gate": "What must happen next",
  "authority": false,
  "green_implied": false
}
```

## Evidence Weighting

| Weight | Meaning | Examples |
|---|---|---|
| 0 | unsupported | memory, vibe, unsourced claim |
| 1 | visible | screenshot, page view, chat statement |
| 2 | received | response, commit, tx, UID, CID |
| 3 | preserved | hash, repo commit, archived copy |
| 4 | verified | independent replay or external witness |
| 5 | replayable | repeatable path with stable recovery |
| 6 | immutable candidate | tag, chain anchor, timestamped release |

Weight does not equal truth.  
Weight only describes evidence strength.

## MN Audit Lanes

| Lane | Category Bias | First Gate | Notes |
|---|---|---|---|
| DEED / UI TOP | REQUEST, RECEIPT, PRESERVATION | agency acknowledgement | no violation presumed before response or deadline evidence |
| MNDOR / Revenue Recapture | REQUEST, RECEIPT | statute + record request surface | separate debt claim from process claim |
| DCYF / Child Support TOP | REQUEST, RECEIPT | certification and correction records | track federal vs state handoff |
| Courts / FTA / DMV | OBSERVATION, REQUEST | docket or agency record | do not infer intent from automated status |
| Housing / Benefits | CLAIM, REQUEST, RECEIPT | notice + agency source | preserve notices before narrative |
| On-chain Identity | RECEIPT, PRESERVATION, IMMUTABILITY | tx/UID/CID/ENS record | address control is not claim truth |
| Repo Governance | PRESERVATION, LIVE_CURSOR | commit + issue/PR | commit exists; claim still separately tested |

## Routing Rules

```json
{
  "if_input_is_text_only": "CLAIMED",
  "if_public_surface_visible": "OBSERVED",
  "if_request_submitted": "REQUESTED",
  "if_response_or_identifier_received": "RECEIVED",
  "if_hash_or_commit_preserves_bytes": "PRESERVED",
  "if_independent_replay_matches": "VERIFIED",
  "if_anchor_is_durable_but_not_replayed_later": "IMMUTABLE_CANDIDATE",
  "if_claim_fails": "WHAMMY_CANDIDATE",
  "if_failure_becomes_rule": "PROTOCOL_ASSET"
}
```

## Small-Scale Retest Candidate

The first retest should be narrow:

```json
{
  "candidate": "ISSUE_35_SMALL_SCALE_RETEST",
  "target": "one public repo artifact",
  "required_surfaces": [
    "public_url",
    "fetched_at",
    "content_hash",
    "witness_service_or_replay_surface"
  ],
  "promotion_rule": "All four surfaces present and matching",
  "downgrade_rule": "Any missing or mismatched surface keeps state below VERIFIED"
}
```

## Closing Receipt

```json
{
  "event": "CATEGORIES_MATRIX_INDEXING_ENGINE_LOCKED",
  "state": "SMALL_SCALE_RETEST_PREPARED",
  "engine": "CLASSIFY_INDEX_GATE",
  "live_cursor": "ISSUE_35",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "closing_line": "The Arena now has a sorting engine. Every beast gets indexed before it gets chased."
}
```
