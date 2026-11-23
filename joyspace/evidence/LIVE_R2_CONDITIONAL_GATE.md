# JoySpace live conditional-write gate — operator test

**State: NOT RUN.** Companion script `live_r2_conditional_test.ps1` is a machine-side test. The Cloudflare connector's REST upload operation does not offer `If-None-Match`; the S3-compatible API does.

## Machine execution (operator controlled)
On Windows with an authenticated AWS CLI v2 configured for the **Cloudflare R2** S3 endpoint (not AWS S3), provide `CF_ACCOUNT_ID` in the local shell; configure S3 access key and secret through AWS CLI locally, never GitHub or this chat:

```powershell
$env:CF_ACCOUNT_ID = "<your Cloudflare account ID>"
powershell -NoProfile -File .\joyspace\evidence\live_r2_conditional_test.ps1
```

Test procedure:
1. Create a unique public-safe synthetic ASCII/UTF-8 payload and SHA-256-derived key.
2. S3 `PutObject` with `If-None-Match: *` must succeed.
3. Repeating precisely the same request must fail with HTTP 412 `PreconditionFailed`. Any other error is HOLD, not PASS.
4. S3 `GetObject` and independent SHA-256 must equal the original digest.
5. Emit public-safe structured verdict; never output credentials or child data.

No live test result can be claimed before observed command output exists. No bucket versioning or Object Lock required. A successful single-run test does not prove concurrency behavior or immutability. Child publication, guardian approval, production ledger, PR merge and Worker changes remain HOLD / not authorized.

Reference: https://developers.cloudflare.com/r2/api/s3/conditional-operations/
