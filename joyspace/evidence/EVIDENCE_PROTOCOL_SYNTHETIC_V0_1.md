# JoySpace Evidence Protocol v0.1 — synthetic-only CI checkpoint

2026-11-23 UTC. **DRAFT / NOT DEPLOYED / NOT A PRODUCTION LEDGER.**

## Scope and prior work
- Repository: `jsonwisdom/JOY` draft PR #129; HEIDEE PR #9 remains separate and draft.
- Existing read-only R2 receipt: `joyspace/worker/JOYSPACE_R2_SYNTHETIC_RECOVERY_RECEIPT_2026-11-23.md`.
- Existing Google Drive reference: Wisdom Accountability Append-Only Execution Ledger v1. That document says append-only is an operating rule, not Google Drive immutability.
- Public Worker at `joyspace.jsonwisdom.com` remains stale and continues to show historical `BLOCKED_10042`; **not changed** by this commit.

## Synthetic harness
Run `node joyspace/evidence/receipt_protocol_synthetic_v0_1.js` in the repository root. Node.js built-in libraries only; no credentials or network access.

Protocol is **restricted** deterministic JSON, not a full RFC 8785 implementation. It sorts object keys recursively, UTF-8 encodes JSON with one terminal LF, supports null/strings/booleans/safe integers/arrays/plain records, and rejects floats and unsupported types. Production use needs full Unicode and canonicalization specification review.

Receipt key = `receipts/sha256-<SHA256(bytes)>.json`; manifest key = `manifests/sha256-<SHA256(bytes)>.json`. Each manifest includes `sequence`, `previous_manifest_sha256`, `receipt_key`, and `receipt_sha256`. The root is not immutable unless independently witnessed.

## Locally observed result
- A mock in-memory R2 accepts first write, rejects duplicate conditional write (modelled as 412), verifies read-back SHA-256.
- Two hash-linked synthetic manifests pass replay; swapped order fails; floating-point canonicalization fails closed.
- Receipt hash: `2217c7f2d43c1f677be6a9a5ba815638508fb86051d60585b7fe2dca9a5d6670`
- Manifest 1 hash: `ebfef935d21ee5b4f1edb13bc9538cd509a45e02fc2ef33b669bdc1d7719d2a6`
- Manifest 2/root hash: `d1e714e8d06a12a461e9e78346f258717f36a81346293609eaa376fd607520e7`

**The mocked duplicate rejection does not prove that a live Cloudflare conditional PUT works.** A live conditional-write test must use documented `If-None-Match: *`, inspect actual 412, do exact GET/hash validation, and publish independent public-safe witness evidence. Do not expose private R2 credentials or child data.

## CI-FIRST gates
```ini
SYNTHETIC_LOCAL_REPLAY=PASS
LIVE_CONDITIONAL_WRITE_GATE=NOT_TESTED
LIVE_MANIFEST_REPLAY=NOT_TESTED
R2_PRIOR_SYNTHETIC_READ_WRITE=PASS
R2_VERSIONING=UNSUPPORTED
EVIDENCE_IMMUTABILITY=NOT_PROVEN
PUBLIC_DESK_SYNC=PENDING
PRODUCTION_LEDGER=HOLD
GUARDIAN_APPROVAL=NOT_ESTABLISHED
CHILD_PUBLICATION=HOLD
PR_MERGE=NOT_AUTHORIZED
```

No child-facing content, production Worker, Cloudflare bucket settings, or Google Drive source records altered.
