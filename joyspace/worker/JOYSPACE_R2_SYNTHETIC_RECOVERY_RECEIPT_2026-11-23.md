# JoySpace R2 entitlement recovery — synthetic verification receipt

**Date:** 2026-11-23 UTC
**Scope:** Read-only public documentation of private account API observations plus a deliberately authorized synthetic infrastructure test. Not a child-facing release.

## Historical failure (preserved, not overwritten)

- Earlier `GET /accounts/{account_id}/r2/buckets` returned HTTP 403, Cloudflare error `10042 NotEntitled`, message `Please enable R2 through the Cloudflare Dashboard.`
- The static public evidence desk still reported `BLOCKED_10042` at the time of the user-supplied independent re-check. The historical failure was real and is not retroactively invalidated.

## New independent connected-account observations

- `GET /accounts/{account_id}/r2/buckets`: API success, listed `joyspace-evidence-v1`.
- `GET /accounts/{account_id}/r2/buckets/joyspace-evidence-v1`: API success.
- Bucket creation time reported by Cloudflare: `2026-11-23T04:53:33.833Z`.
- Storage class: `Standard`; location: `ENAM`; jurisdiction: `default`.
- Public access disabled according to the operator's Cloudflare dashboard screenshot. No public bucket URL is claimed.
- Billing subscription state was NOT independently inspected, due to API permission limits.

## Synthetic write/read test

- Bucket: `joyspace-evidence-v1`
- Object key: `ci-first/synthetic/r2-entitlement-retest-2026-11-23.txt`
- PUT response: `success=true`, `errors=[]`, uploaded `2026-11-23T04:55:36.517Z`.
- Returned size: `122` bytes; returned ETag `d3a8113b2504f6aa70b198a6fa148d81`.
- GET returned exact UTF-8 payload; byte-for-byte equality with expected ASCII text confirmed. SHA-256 for 122-byte exact payload: `2cdba5ad84d32cf5cad0688cf402a6694e44980b21e205d4a2d21a8f99111bb7`.

Exact payload (LF line endings, terminal LF):
```text
COMPUTER WISDOM JOYSPACE CI-FIRST
synthetic=true
contains_child_data=false
purpose=R2 private write-read byte-parity test
```

SHA-256 above is reproducible from the exact 122-byte payload. This publicly documented receipt allows third parties to reproduce the hash of the stated test bytes; it does NOT let an unauthenticated third party independently read the private R2 object or prove its contents from public HTTP alone.

## Status boundaries

```ini
R2_ERROR_10042_HISTORICAL=OBSERVED
R2_ERROR_10042_CURRENT=NOT_REPRODUCED
R2_BUCKET_API_LIST_GET=PASS
R2_SYNTHETIC_PUT_GET=PASS
R2_SYNTHETIC_BYTE_PARITY=PASS
R2_SYNTHETIC_SHA256=2cdba5ad84d32cf5cad0688cf402a6694e44980b21e205d4a2d21a8f99111bb7
PUBLIC_EVIDENCE_DESK_STATUS=STALE_BLOCKED_10042
PUBLIC_WORKER_UPDATE=NOT_PERFORMED
GUARDIAN_APPROVAL=NOT_ESTABLISHED
REAL_DEVICE_VALIDATION=NOT_RUN
CHILD_FACING_PUBLICATION=false
PRODUCTION_EVIDENCE_LEDGER=HOLD
PRODUCTION_WRITE=false
EXTERNAL_ANCHOR=false
```

No merge, child-facing deployment, private child material, or production ledger operation was performed. This receipt resides on the existing draft JOY PR branch until reviewed.
