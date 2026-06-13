# MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_V0_1

```json
{
  "artifact": "MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_V0_1.md",
  "parent_artifact": "MNDOR_SAMPLE_CLAIMANT_NOTICE_LANGUAGE_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "debt priority order / qualifying payments list",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

MNDOR applies recaptured funds according to a statutory or program priority structure. The available payment streams are limited to qualifying state refunds or payments; revenue recapture is not a blanket seizure mechanism for every income stream.

This layer answers:

```text
What can be touched?
In what order?
What remains unverified at person level?
```

## Source Packet

```json
{
  "public_urls": [
    "https://www.revenue.state.mn.us/debt-priority",
    "https://www.revenue.state.mn.us/qualifying-refunds-and-payments"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website",
  "official_source_type": "MNDOR_PAGE",
  "statutory_cross_reference": "Minnesota Statutes Chapter 270A / priority mechanics"
}
```

## Qualifying Refunds and Payments Indexed

The listed qualifying streams include:

- Minnesota income tax refunds and payments;
- Political Contribution Refunds;
- Property Tax Refunds, including homestead credit or renter’s refunds;
- lottery winnings of $600 or more;
- Sustainable Forest Incentive Act payments;
- awards from the Joint House-Senate Subcommittee on Claims.

## Debt Priority Order Indexed

```json
{
  "priority_1": "State taxes owed to the Department of Revenue",
  "priority_2": "Child support",
  "priority_3": "Court-ordered criminal restitution",
  "priority_4": "Debts owed to hospital or ambulance services",
  "priority_5": "Debts to other Minnesota agencies",
  "priority_6": "Debts to government agencies from other states",
  "priority_7": "Federal taxes",
  "tie_breaker": "If multiple claims share the same priority, oldest claim date first, then oldest document number if needed"
}
```

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Payment mechanics are tied to official source packet, not inferred from grievance. |
| ERS-002 Wrong Vault | PASS | Priority order is not treated as proof that any specific offset was valid. |
| ERS-003 Wrong Certificate | PASS | The source packet belongs to the administrative offset mechanics layer. |
| ERS-004 Unknown Waters | DOWNGRADED | Public priority and payment streams are clear; individual application still requires personal notice/claim packet. |

## Strict Scope

This artifact verifies program-level mechanics only.

It does not verify:

- any specific person's refund was eligible;
- any specific debt priority was applied correctly;
- any specific $15 fee application;
- any specific child support, DEED, court, county, hospital, or federal claim;
- any specific agency error;
- any legal conclusion.

## Remaining Person-Level Unknowns

```json
{
  "specific_payment_stream": "NOT_PROVIDED",
  "specific_claimant_agency": "NOT_SELECTED",
  "specific_claim_date": "NOT_PROVIDED",
  "specific_document_number": "NOT_PROVIDED",
  "specific_priority_position": "NOT_PROVIDED",
  "specific_fee_application": "NOT_PROVIDED",
  "specific_offset_amount": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "debt priority order / qualifying payments list",
  "classification": "ADMINISTRATIVE_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED",
  "evidence_weight": "HIGH_STATUTORY_PROGRAM_LEVEL",
  "promotion_allowed": "PROGRAM_LEVEL_ONLY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Nonliable spouse / joint refund mechanics.
2. Medical debt exemption or hospital/ambulance debt mechanics.
3. Specific agency implementation details: DCYF, DEED, courts, county, hospital.
4. Person-level notice and offset packet, if a specific case lane is selected.

## Closing Receipt

Priority and qualifying payment mechanics indexed with official source packet.  
Program-level model holds.  
Person-level application remains unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
