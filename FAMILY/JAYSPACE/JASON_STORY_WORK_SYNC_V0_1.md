# JASON STORY + WORK SYNC V0.1

STATUS = STRUCTURAL_SYNC_INDEX
AUTHORITY_CREATED = false
MERGE_STATUS = 0
CROSS_PROVIDER_ATOMICITY = false
NO_FAKE_GREEN = true

## Purpose

Synchronize Jason's observable work history across separate rails without collapsing them:

- JaySpace in jsonwisdom/JOY
- JoySpace in jsonwisdom/JOY
- Zora creator/publication surface in jsonwisdom/jay-zora-portal
- Coinbase read-only / receipt surfaces in jsonwisdom/COMPUTERWISDOM
- GitHub commits as repository revision timestamps

This is a reconciliation index, not a claim that all systems share one clock or one identity object.

## Sovereign surfaces

JAYSPACE
- canonical family/operator home: /JOY/joyspace/jayspace.html
- role: technical work, receipts, replay, drill-down
- merge with Zora portal: forbidden by default

JOYSPACE
- role: family-safe reader/demonstrator surface
- relationship to JaySpace: linked but separate

ZORA
- repo: jsonwisdom/jay-zora-portal
- branch: live-zora-ingestion
- role: creator/post/publication inventory and public proof mirror
- wallet/signer identity joins: separate proof gates

COINBASE
- repo receipt surface: jsonwisdom/COMPUTERWISDOM/receipts/coinbase-agent
- role: read-only/account/connectivity observations unless a separate execution receipt exists
- connector access != human identity
- account data != wallet control

## Timestamp model

Every event must preserve its timestamp type.

- HUMAN_OBSERVED_AT
- HUMAN_REFLECTED_AT
- HUMAN_AUTHORED_AT
- SOURCE_CREATED_AT
- SOURCE_PUBLISHED_AT
- GITHUB_AUTHOR_AT
- GITHUB_COMMITTER_AT
- SYSTEM_RECORDED_AT

Rules:

1. A GitHub commit timestamp does not rewrite a Zora post timestamp.
2. A Zora created_at does not prove when Jason authored the underlying idea.
3. Coinbase receipt time records the observation/receipt event, not the origin of every underlying transaction.
4. Human story timestamps remain first-class and may remain unresolved.
5. If clocks conflict, preserve all clocks and emit HOLD_CLOCK_CONFLICT.
6. MISSING_TIMESTAMP != ZERO_TIMESTAMP.
7. SAME_DAY != SAME_EVENT.
8. ORDERED_BY_TIME != CAUSAL_RELATIONSHIP.

## Current replay anchors

### JaySpace
- 2026-06-15T02:43:51Z
- commit 3f7f661806c9aa471b82d15d9c5bc480430e41f7
- message: feat(jayspace): add JaySpace homepage

### JaySpace Needs You extension
- 2026-09-17T00:12:36Z
- commit 392b0f4c2ba6f1ab350e19f435d9300cad01226e
- message: Add JaySpace Needs You door and card schema

### JoySpace reader index
- 2026-06-11T02:38:12Z
- commit 3bc99c9840f6f96e3e906c7bb2d15e564703f9a0
- message: docs: update JoySpace index for Ms Wisdom

### JoySpace front-door update
- 2026-09-05T10:47:09Z
- commit 5c1adb69563b9b3a6296d5da01016f68c74948ab
- message: docs(joyspace): add Sister Sidcars front door (YELLOW, unbound, no fake green)

### Zora inventory checkpoints
- 2026-05-18T07:25:50Z — a7356429815373e0b7a8a0f46a7da3d2ecfb9036 — Add normalized 857 Zora coin corpus
- 2026-09-01T18:36:26Z — 390fc8f6189bbe4fd81fa81e94aa86b4cab803d5 — Refresh live Zora inventory
- 2026-09-02T13:11:03Z — e53beae2cf1246c85b46307f38cf8f31bdc4de32 — Refresh live Zora inventory
- 2026-09-12T00:37:04Z — d089c88f9fbc40c9cb093f500bf562753b32d5c4 — Refresh live Zora inventory
- 2026-10-04T07:25:35Z — 5962509e6f75f6e4b98100a42ae7b40d8d3031ae — Refresh live Zora inventory

### Coinbase receipt anchors
- 2026-06-19T20:14:44Z author / 2026-06-19T20:19:30Z committer
- commit 6d89e9a3e7f782a3017447ee73f94a1da20b840a
- first live Coinbase connectivity receipt; execution=false

- 2026-06-19T20:32:34Z
- commit 15ab4adebd307cc66277d6822449b2f4bb11bb7f
- Coinbase portfolio read attestation; trade=false, transfer=false

## Story reconciliation rule

The timeline is constructed by joining only through explicit evidence keys:

EVENT_ID
SOURCE_SYSTEM
SOURCE_OBJECT_ID
SOURCE_CREATED_AT
GITHUB_COMMIT
GITHUB_COMMITTER_AT
HUMAN_STORY_REF
RECEIPT_REF
AUTHORITY
STATUS

No event is promoted into "Jason's Story" merely because timestamps are close.

Allowed states:

- SOURCE_BOUND
- STORY_BOUND
- RECEIPT_BOUND
- CROSS_RAIL_CORRELATED
- HOLD
- UNRESOLVED

## Report-back rule

Each external rail reports back to JaySpace as a pointer + timestamp tuple.

ZORA -> JAYSPACE
COINBASE -> JAYSPACE
GITHUB -> JAYSPACE
JOYSPACE -> JAYSPACE

JaySpace records the relationship; it does not absorb or rewrite the source.

REPORT_BACK != MERGE
REPORT_BACK != IDENTITY_JOIN
REPORT_BACK != AUTHORITY

## Next machine pass

Generate append-only rows from:

1. Zora post created_at + contract/zora_url
2. Coinbase receipt timestamps + receipt IDs
3. GitHub commit author/committer timestamps
4. JaySpace/JoySpace story references
5. explicit human-authored story timestamps where present

Then classify each row as:
- EXACT_ALIGNMENT
- ORDER_ONLY
- CLOCK_CONFLICT
- MISSING_LINK
- HOLD

