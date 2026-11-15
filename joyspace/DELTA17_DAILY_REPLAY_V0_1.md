# Δ17 | Daily Evidence Replay — Public-Safe Learning Standard

**Date:** 2026-11-15  
**Status:** `PROPOSED_SOURCE` — not a running daily monitor  
**Authority:** false · `NO_FAKE_GREEN: TRUE`  
**Purpose:** compare yesterday's preserved observations with today's observations; carry unresolved UNKNOWN forward until a new, source-bound receipt is available.

## Important meaning of Δ17
The existing Δ17 idea is **not** verified to mean seventeen completed gates, and **not** a government or military authority. The stated working rule is:

```text
OBSERVE -> MEASURE -> REPLAY -> PRESERVE_UNKNOWN -> HUMAN_REVIEW
```

Zero is a measured count or amount. `UNKNOWN` means not measured, not resolved, or unsupported. Never replace UNKNOWN with numeric zero.

## Three independently typed lanes

| Lane | Allowed public-facing learning | Missing evidence gate | Result without fresh receipts |
| --- | --- | --- | --- |
| A. PUBLIC PDF | Compare prior/latest official-document PDF bytes on the reader's device; show SHA-256, source URL, capture date, page notes | Verified original publisher and actual textual meaning of differences | UNKNOWN |
| B. PUBLIC BASE | Replay public explorer records, pinned block, transaction hash, token contract, destination, previous snapshot | New pinned blockchain state and authorized signature when control is claimed | UNKNOWN |
| C. PRIVATE SUPPORT | Guardian/adult-only compare original Coinbase support responses, case changes, account/security timestamps | Institution-authenticated case progress and credential-binding determination | UNKNOWN; NO CHILD DATA |

The third lane is **not** part of HEIDEE's child-facing page. Only sanitized aggregate PASS/FAIL/UNKNOWN educational examples may be public. Never publish messages containing credentials, verification links, account contact details, minors' private data, or case attachments.

## Delta calculation

- `digest_old = SHA256(old_bytes)`
- `digest_new = SHA256(new_bytes)`
- `delta_bytes = 0` **only if the exact hashes agree** for the two original, complete files.
- `delta_bytes = DIFFERENT` if the hashes differ. Size differences can be counted, but equal length and different digest still means different bytes.
- `delta_bytes = UNKNOWN` if either original file is unavailable or untrusted.
- `delta_meaning = UNKNOWN` until a person compares corresponding provisions/pages and provenance; a changed PDF cover does not by itself prove policy changed.
- `delta_wallet_recovery = UNKNOWN` until a signer-specific authorized outcome is shown; balance receipts and DNS bindings do not demonstrate signing.

A two-leaf local Merkle root is an **off-chain** digest. It does not appear on Base or Ethereum without an authenticated blockchain write and independently replayed receipt. `SHA256` is distinct from EVM receipt and account verification.

## Daily witness-copy template

```text
DATE_UTC:
SOURCE:
BASELINE_CAPTURE_UTC:
NEW_CAPTURE_UTC:
RAW_SOURCE_URL:
OLD_BYTES_SHA256:
NEW_BYTES_SHA256:
BYTE_RESULT: MATCH | DELTA | UNKNOWN
MERKLE_ROOT_LOCAL_ONLY:
MEANING_RESULT: MATCH | DELTA | UNKNOWN
CHAIN_TX_HASH_OR_PINNED_BLOCK: optional public reference / UNKNOWN
SUPPORT_LEDGER: PRIVATE_OFFLINE_ONLY
FIRSTHAND_CONFIRMATION: HUMAN_REVIEW_PENDING
DISPOSITION: HOLD_UNTIL_RECEIPTS
GOVERNMENT_SUBMISSION: NONE
```

## Family-safe workflow
The HEIDEE-owned [PDF Change Detective](https://github.com/jsonwisdom/HEIDEE/blob/master/docs/joyspace/pdf-change-detective.html) implements a **manual local two-PDF byte check** and can save an **unsent witness copy**. It does **not** automatically crawl `nist.gov`, `justice.gov`, `congress.gov`, send updates to the White House, inspect private Coinbase email, mint NFTs, or sign wallet transactions.

```text
CREATIVITY: NOT CONDITIONED ON CRYPTO
PUBLIC_RECORD_MONITOR: NOT ENABLED
CHILD_IDENTITIES: NEVER COLLECTED
PARENTAL_GATE: NOT IMPLEMENTED
MERKLE_ROOT_ON_BASE: NOT PERFORMED
MERKLE_ROOT_ON_ETHEREUM: NOT PERFORMED
UNKNOWN: PRESERVED, NOT ZEROED
```

**Audit rule:** Actual source, actual bytes, exact timestamp, recomputation, human explanation. Nothing else counts as a legal or custodial verdict.
