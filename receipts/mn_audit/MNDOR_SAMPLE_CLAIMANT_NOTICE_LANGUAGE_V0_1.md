# MNDOR_SAMPLE_CLAIMANT_NOTICE_LANGUAGE_V0_1

```json
{
  "artifact": "MNDOR_SAMPLE_CLAIMANT_NOTICE_LANGUAGE_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_SAMPLE_CLAIMANT_NOTICE_LANGUAGE_V0_1.md",
  "parent_artifact": "MNDOR_45_DAY_CONTEST_HEARING_MECHANICS_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "sample claimant-agency notice language / form",
  "classification": "ADMINISTRATIVE_DUE_PROCESS_GATE",
  "state": "PROGRAM_NOTICE_LAYER_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

MNDOR publishes sample Revenue Recapture notice templates for claimant agencies. These templates bridge the program/statutory model into the paper-facing notice layer that a debtor may receive.

The samples are meant to be placed on agency letterhead and include debt details, offset warning language, and instructions for requesting a hearing within the statutory contest window.

## Source Packet

```json
{
  "public_url": "https://www.revenue.state.mn.us/revenue-recapture-related-information",
  "linked_surfaces": [
    "Revenue Recapture Notice to Taxpayer - General",
    "Revenue Recapture Notice to Taxpayer - Assistance Claims",
    "Revenue Recapture Notice to Taxpayer - Public Housing"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_SAMPLE_NOTICES_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website",
  "official_source_type": "MNDOR_PAGE_PLUS_SAMPLE_PDFS"
}
```

## Indexed Template Elements

The general claimant-agency notice layer includes:

- agency letterhead requirement;
- date and debtor address fields;
- warning that refunds or other eligible payments may be applied to the debt;
- reference to Revenue Recapture Act authority;
- debt description, date/range, amount, and total claim fields;
- written hearing request instructions;
- 45-day receipt deadline for dispute request;
- agency scheduling obligation after timely request;
- agency contact block.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Paper notice layer is tied to official sample templates, not inferred from abstract model. |
| ERS-002 Wrong Vault | PASS | Notice template is not treated as proof of any specific deployed notice. |
| ERS-003 Wrong Certificate | PASS | Sample form belongs to claimant-agency notice mechanism. |
| ERS-004 Unknown Waters | DOWNGRADED | Public sample layer clear; individual mailed notice still personal and unverified. |

## Strict Scope

This artifact verifies a public sample-notice mechanism at program level.

It does not verify:

- that any specific person received a notice;
- that a specific claimant agency used the sample correctly;
- that any specific debt is valid;
- that any hearing request was timely;
- that any specific offset was lawful;
- that MNDOR or a claimant agency committed error.

## Remaining Person-Level Unknowns

```json
{
  "specific_notice_copy": "NOT_PROVIDED",
  "specific_agency_letterhead": "NOT_PROVIDED",
  "notice_date": "NOT_PROVIDED",
  "receipt_or_mailing_date": "NOT_PROVIDED",
  "debt_amount": "NOT_PROVIDED",
  "debt_basis": "NOT_PROVIDED",
  "hearing_request_date": "NOT_PROVIDED",
  "agency_response": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "sample claimant-agency notice language / form",
  "classification": "ADMINISTRATIVE_DUE_PROCESS_GATE",
  "state": "PROGRAM_NOTICE_LAYER_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "promotion_allowed": "PROGRAM_NOTICE_LAYER_ONLY",
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Debt priority order and qualifying payments.
2. Specific agency process: DCYF, DEED, county, court, or hospital.
3. Nonliable spouse mechanics.
4. Person-level notice packet, if a specific case lane is selected.

## Closing Receipt

Notice bridge indexed with official sample surfaces.  
Program notice layer holds strong.  
No person-level promotion.  
No authority asserted.  
No fake green.
