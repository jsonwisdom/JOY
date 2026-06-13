# MNDOR_NONLIABLE_SPOUSE_JOINT_REFUND_MECHANICS_V0_1

```json
{
  "artifact": "MNDOR_NONLIABLE_SPOUSE_JOINT_REFUND_MECHANICS_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MNDOR_NONLIABLE_SPOUSE_JOINT_REFUND_MECHANICS_V0_1.md",
  "parent_artifact": "MNDOR_DEBT_PRIORITY_QUALIFYING_PAYMENTS_V0_1",
  "parent_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "nonliable spouse / joint refund mechanics",
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

MNDOR may apply a married filer’s joint state refund to a debt owed by one spouse. The nonliable spouse is not treated as personally liable for the other spouse’s debt and may request their portion back through the claimant agency after recapture.

This layer answers:

```text
When a joint refund is hit, what protection path exists for the spouse who does not owe the debt?
```

## Source Packet

```json
{
  "public_urls": [
    "https://www.revenue.state.mn.us/revenue-recapture",
    "https://www.revenue.state.mn.us/revenue-recapture-related-information"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MNDOR_NONLIABLE_SPOUSE_JOINT_REFUND_20260613",
  "witness_service_or_replay_surface": "Minnesota Department of Revenue official public website",
  "official_source_type": "MNDOR_PAGE",
  "statutory_cross_reference": "Minnesota Statutes section 519.05"
}
```

## Mechanics Indexed

- A joint state refund may be recaptured for a debt owed by only one spouse.
- The nonliable spouse requests their share directly from the claimant agency, not by treating MNDOR as the debt-origin authority.
- The claimant agency name, address, and contact information appear on the revenue recapture notice.
- The nonliable spouse request window is indexed as 18 months from the recapture notification.
- Allocation may require agency review and supporting calculations, including worksheet-style apportionment.
- MNDOR remits the joint refund to the claimant agency; the claimant agency handles valid nonliable spouse claims.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | Joint-refund model is tied to official guidance and statutory cross-reference. |
| ERS-002 Wrong Vault | PASS | MNDOR recapture and claimant-agency allocation responsibility remain separated. |
| ERS-003 Wrong Certificate | PASS | Nonliable spouse worksheet/guidance belongs to the joint-refund protection mechanism. |
| ERS-004 Unknown Waters | DOWNGRADED | Public path is clear; actual allocation requires person-level claim and supporting records. |

## Strict Scope

This artifact verifies the public program-level protection mechanism.

It does not verify:

- any specific joint refund;
- any specific spouse’s nonliable share;
- any specific debt belongs to one spouse only;
- any specific claimant agency calculation;
- any specific timely request within 18 months;
- any agency error;
- any legal conclusion.

## Remaining Person-Level Unknowns

```json
{
  "specific_joint_return": "NOT_PROVIDED",
  "specific_recapture_notice": "NOT_PROVIDED",
  "claimant_agency": "NOT_SELECTED",
  "liable_spouse": "NOT_IDENTIFIED",
  "nonliable_spouse_request_date": "NOT_PROVIDED",
  "income_or_refund_allocation_records": "NOT_PROVIDED",
  "agency_determination": "NOT_PROVIDED",
  "refund_return_amount": "NOT_PROVIDED"
}
```

## Classification Update

```json
{
  "vector": "nonliable spouse / joint refund mechanics",
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

1. Medical debt exemption mechanics.
2. Specific agency implementation details: DCYF, DEED, courts, county, hospital.
3. Bankruptcy interplay or federal offset boundaries.
4. Person-level joint-refund notice packet, if a specific case lane is selected.

## Closing Receipt

Nonliable spouse layer indexed with official source packet.  
Program protection path holds.  
Person-level allocation remains unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
