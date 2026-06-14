# BOSS BYTE SCORECARD V0.1

```text
STATUS: SCORECARD_DRAFT
TRUTH_STATE: YELLOW_PROTECTED
NO_FAKE_GREEN: TRUE
```

## Scorecard

| Check | Points | Required For Green |
| --- | ---: | --- |
| Boss selected from protected lane | 1 | Yes |
| Approved payload exists | 1 | Yes |
| Stable birthday frame used | 1 | Yes |
| Repo read-back passed | 1 | Yes |
| Public route returns HTTP 200 | 1 | Yes |
| Repo/public SHA256 byte-match | 2 | Yes |
| Human visual approval passed | 2 | Yes |
| Privacy check passed | 2 | Yes |

## Max Score

```text
11 / 11 = BIRTHDAY_GREEN
Anything less = YELLOW_PENDING
```

## Operator Rule

```text
Operator A builds and reads repo bytes.
Operator B checks public bytes and visual approval.
AI Builder may draft.
AI Verifier must refuse fake green.
```

## Replay Line

```text
No byte match, no birthday green. No approval, no public boss claim.
```
