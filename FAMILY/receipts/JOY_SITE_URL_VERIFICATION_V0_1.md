# JOY_SITE_URL_VERIFICATION_V0_1

```yaml
artifact: JOY_SITE_URL_VERIFICATION_V0_1
authority: false
fake_green: forbidden
status: PENDING_FETCH
site_status_before: DOCS_READY_PENDING_PAGES_ENABLEMENT
site_status_after: "<pending>"
url_fetched: "<pending>"
fetch_method: "<pending>"
fetch_result: "<pending>"
fetched_at: "<pending>"
content_hash: "<pending>"
language_layer: "MRS_WISDOM_APPROVED_JOYSPACE"
notes: "<pending>"
```

## Verification Rule

`PAGES_ENABLED && FETCH_SUCCESS && URL_PRESENT -> LIVE_URL_VERIFIED`

## Invalid States

- `PAGES_DISABLED + LIVE_URL_VERIFIED`
- `URL_UNFETCHED + SUCCESS`
- `CEREMONY_ONLY + DEPLOYMENT_CONFIRMED`

## Completion Condition

This receipt becomes valid only when:

- Pages URL exists
- URL is fetched manually
- Successful fetch is timestamped

No fake green. No implied verification before a real fetch.
