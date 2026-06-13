# ALMS Machine Speed — Open Meme Court

## COURT_RULE_00 — Receipts Are Documentary, Not Performative

A receipt records a state. A receipt does not create a state.

Writing "VERIFIED" in a receipt field does not verify anything. The receipt documents that verification occurred elsewhere and identifies the supporting evidence by hash, witness, or replay path.

The court is a ledger, not an oracle. It witnesses; it does not sanctify.

## Court Rules

- No verdict without a receipt.
- No receipt without evidence_state and content_hash when preservation is claimed.
- promotion_granted defaults to false.
- authority is always false.
- no_fake_green is immutable.
- A hash proves artifact integrity, not truth of the claim.

## Evidence Ladder v1.1

UNKNOWN
→ CLAIM_FILED
→ OBSERVED
→ PRESERVED
→ EXTERNAL_WITNESS
→ VERIFIED
→ REPLAYABLE

## Ladder Definitions

- UNKNOWN: no usable surface.
- CLAIM_FILED: receipt exists and claim is recorded.
- OBSERVED: surface seen and source confirmed reachable.
- PRESERVED: content hash, commit hash, tree hash, or signed identifier recorded.
- EXTERNAL_WITNESS: independent observation exists.
- VERIFIED: evidence supports the specific claim.
- REPLAYABLE: third party can independently reproduce the result.

## Judgment Engine

- The engine never auto-grants promotion.
- Promotion requires a separate court entry.
- Receipts are documentary, not performative.
- Later conflicting receipts may downgrade evidence_state.

## Receipt Format

```json
{
  "receipt_id": "MEME_COURT_RECEIPT_000X",
  "case_name": "",
  "input_type": "meme | screenshot | claim | link | hash | artifact",
  "evidence_state": "UNKNOWN",
  "claim_text": "",
  "source_url": null,
  "observed_at": null,
  "content_hash": null,
  "external_witness": null,
  "promotion_requested": false,
  "promotion_granted": false,
  "reason": "No promotion without receipt.",
  "authority": false,
  "no_fake_green": true
}
