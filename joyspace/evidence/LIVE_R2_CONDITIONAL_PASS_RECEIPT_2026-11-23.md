# JoySpace — live R2 conditional-write evidence receipt (synthetic only)

Date: 2026-11-23 UTC  
Scope: CI-FIRST Windows operator test + independent connected Cloudflare R2 GET.  
Status: **LIVE SYNTHETIC GATE PASS; PRODUCTION LEDGER HOLD.**

## Local operator evidence

After replacing the stale local script with GitHub commit `3189aecfcbae1d07e2dcfae79b5873bd53130306`, the operator ran `joyspace/evidence/live_r2_conditional_test.ps1` under the `joyspace-r2` profile.

The operator-provided terminal JSON reported:

```json
{
  "scope": "LIVE_R2_SYNTHETIC_ONLY",
  "conditional_put": "PASS",
  "duplicate_put": "HTTP_412_PRECONDITION_FAILED",
  "readback_sha256": "PASS",
  "bucket": "joyspace-evidence-v1",
  "key": "ci-first/conditional/sha256-42cb8b42e175767250055f4647aabeae1d0e3985e00dc4132420574eb49d14cb.txt",
  "sha256": "42cb8b42e175767250055f4647aabeae1d0e3985e00dc4132420574eb49d14cb",
  "production_ledger": "HOLD",
  "guardian_approval": "NOT_ESTABLISHED",
  "child_publication": false
}
```

The script's success path requires that its first `PutObject --if-none-match *` exits 0, a duplicate conditional write exits nonzero and emits `412` or `PreconditionFailed`, then S3 `GetObject` returns bytes with the expected SHA-256. The actual AWS CLI duplicate response was **not separately preserved** as an independently inspectable server log. Treat the terminal output as operator test evidence, not an independently executable public proof of HTTP 412.

A prior exploratory attempt with `$duplicateExit=252` emitted `ParamValidation: following arguments are required: command`. That prior command was *not* evidence of an R2 412 and is explicitly excluded.

## Independent read-back

Via a separate connected Cloudflare REST R2 `GET` of the exact bucket and object key, the following **synthetic-only** object body was retrieved:

```text
COMPUTER WISDOM JOYSPACE synthetic-only
run_id=75f64fd592c544258c0a24200575dc3e
contains_child_data=false
```

The payload contains **106 UTF-8/ASCII bytes**, including LF line endings and a final LF. Independent SHA-256 computed over these bytes:

`42cb8b42e175767250055f4647aabeae1d0e3985e00dc4132420574eb49d14cb`

Matches operator output, content-addressed object key, and independent R2 retrieval.

## Strict boundaries

- Bucket stays private; object cannot be fetched from unauthenticated public HTTP.
- This GitHub receipt publicly witnesses a synthetic payload and test claims; it **does not** expose R2 credentials or private child data.
- Conditional write proof is operator-tested; independent REST GET corroborates existence and hash, **not HTTP 412 itself**.
- R2 versioning and S3 Object Lock are unsupported. Tamper detection is **not immutable storage**.
- The deployed JoySpace evidence desk may still show historical `BLOCKED_10042`; **this receipt does not update the Worker**.
- JOY PR #129 remains a draft; no merge, guardian consent, child-facing deployment, or production ledger authority is conferred.

```ini
LIVE_SYNTHETIC_CONDITIONAL_PUT=PASS_OPERATOR_TEST
LIVE_DUPLICATE_412=PASS_OPERATOR_TEST
INDEPENDENT_R2_GET=PASS
INDEPENDENT_SHA256=PASS
PUBLIC_WORKER_SYNC=PENDING
PRODUCTION_EVIDENCE_LEDGER=HOLD
GUARDIAN_APPROVAL=NOT_ESTABLISHED
CHILD_PUBLICATION=false
```
