# L4 Verifier Extension V0.1

## Status

DRAFT

## Purpose

Define the Layer 4 verification extension for JOY receipts.

This extension evaluates whether L4 artifacts preserve the JOY verification membrane:

- no authority claimed
- no fake green
- witness over projection
- replay required
- membrane intact

## Depends On

- _truth/verification/VERIFICATION_RECORD_V0_1.md
- artifacts/L4_OPENING_RECEIPT_V0_1.json
- artifacts/L4_SCOPE_V0_1.json

## Scope

This verifier extension applies to:

- L4 opening receipts
- L4 scope receipts
- Zora receipt flywheel candidates
- proof dashboard artifacts
- replay viewer artifacts
- agent delegation artifacts

## Required L4 Checks

Each L4 artifact must satisfy:

- authority: false
- no_fake_green: true
- witness_over_projection: true
- replay_required: true
- membrane_status: INTACT

## Zora Flywheel Gate

A Zora post or coin candidate is not mintable unless:

- opening_receipt_present: true
- scope_receipt_present: true
- verifier_extension_present: true
- replay_pass_present: true
- mint_decision_present: true

## Agent Delegation Gate

Agent delegation may prepare artifacts, drafts, dashboards, and candidate posts.

Agent delegation may not:

- claim authority
- bypass replay
- mint without human approval
- treat projected success as verified success
- mutate prior receipts

## Dashboard Gate

The proof dashboard may display receipt state.

The dashboard may not convert a displayed receipt into canon.

## Forbidden States

- authority_true
- fake_green
- replay_skipped
- membrane_broken
- mint_without_replay_pass
- dashboard_claims_canon
- agent_claims_authority
- zora_post_claims_verification_without_receipt_chain

## Closing Rule

L4 verification extends the JOY receipt chain.

It does not crown artifacts.

It only evaluates whether downstream actions preserve the membrane.
