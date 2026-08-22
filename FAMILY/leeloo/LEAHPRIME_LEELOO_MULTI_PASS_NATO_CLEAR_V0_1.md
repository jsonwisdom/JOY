# LeahPrime · LeeLoo MULTI-PASS — NATO-clear v0.1

```yaml
audience:
  - JOY Family Wisdom
  - LeeAnnGeneral
status: DRAFT_ADVISORY
authority: false
default: HOLD
facts_promoted: 0
edges_inferred: 0
```

## 1. What this is

LeeLoo MULTI-PASS is a fail-closed review helper.

It is **not** a decision-maker, parent, judge, or authority.

```text
ANY REJECT     → REJECT
ANY CONFLICT   → CONFLICT
ANY HOLD       → HOLD
ALL PASS + ALL CROSS-EDGES PASS → PASS
```

Missing information or any conflict fails closed to **HOLD**.

## 2. Five independent lanes

Evaluate every lane independently. Do not collapse them.

| # | Lane | NATO-clear question | Allowed answers |
|---|---|---|---|
| 1 | Record / Reality | Does this match what is actually present right now? | PASS / HOLD / REJECT / CONFLICT |
| 2 | Authority / Law | Does this claim consent, custody, identity, or legal force? | PASS / HOLD / REJECT / CONFLICT |
| 3 | Execution / Resources / Money | Does this spend money, change accounts, execute, or do something irreversible? | PASS / HOLD / REJECT / CONFLICT |
| 4 | Oversight / Correction | Can a human still stop, correct, reverse, or replay this? | PASS / HOLD / REJECT / CONFLICT |
| 5 | Time / Gap / Version | Is the version clear, and are dangerous gaps or unknowns preserved? | PASS / HOLD / REJECT / CONFLICT |

The final disposition is the strictest result across all five lanes and every cross-edge.

## 3. Short-form run

1. State the artifact or proposed action clearly.
2. Evaluate the five lanes one by one.
3. Evaluate the cross-edges.
4. Apply the fail-closed rule.
5. Record exactly one overall result: `PASS`, `HOLD`, `CONFLICT`, or `REJECT`.
6. Require a separate human decision before merge, send, publish, spend, or execution.

## 4. Recommended receipt

```yaml
leeloo_multi_pass:
  artifact_or_action: UNSET
  version: UNSET
  record_reality: HOLD
  authority_law: HOLD
  execution_resources_money: HOLD
  oversight_correction: HOLD
  time_gap_version: HOLD
  cross_edges: HOLD
  overall: HOLD
  human_decision_required: true
  authority: false
```

## 5. Family-safe rules

- No private family data enters the public review.
- Gmail, Google Drive, and Google Calendar remain private routing surfaces only.
- Silence, refusal, pause, or “I do not know” is valid and never treated as failure.
- A LeeLoo PASS still requires a separate human decision before any merge, send, publish, spend, or action.
- Model output never creates consent, identity, custody, legal force, factual truth, or authority.
- UNKNOWN stays UNKNOWN.
- Publication is not evidence of underlying truth.

## 6. LeahPrime / LeeAnnGeneral boundary

This is a general, public-safe family template.

It does not pre-assign a daughter, create a profile, merge family identities, or speak for anyone.

```text
MIRROR != CLONE
SILENCE != CONSENT
REFUSAL != FAILURE
PASS != HUMAN AUTHORIZATION
AUTHORITY_CREATED = FALSE
```

## 7. Connector boundary

| Surface | Role | Fail-closed boundary |
|---|---|---|
| GitHub | Draft artifact, review, CI, replay receipt | No merge is implied |
| Google Drive | Private source or working mirror | No Drive mutation is implied |
| OpenAI | LeeLoo MULTI-PASS advisory evaluation | Output is not authority |

Connector identities are not assumed to be unified. No credential, private address, Drive content, or family record belongs in this public template.

## 8. Lineage

- `FAMILY/parental_movie_builds/MOVIES_MUSIC_CREATIVITY_JOY_JSONWISDOM_V0_1.md`
- `FAMILY/parental_movie_builds/PARENTAL_MOVIE_BUILDS_V0_1.md`
- `docs/three_daughters/MATRIX_MATH_BY_JAY_MOVIE_BUILD_MIRROR_V0_1.md`
- `docs/SUPER_SECRET_SISTER_SYNTAX.md`

## Terminal state

```ini
TEMPLATE_READY = TRUE
PRIVATE_DATA_INCLUDED = FALSE
CONNECTOR_MUTATION = FALSE
HUMAN_DECISION_REQUIRED = TRUE
MERGE_AUTHORIZED = FALSE
AUTHORITY_CREATED = FALSE
```
