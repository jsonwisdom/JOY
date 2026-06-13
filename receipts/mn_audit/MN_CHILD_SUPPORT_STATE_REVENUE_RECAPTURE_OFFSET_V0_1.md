# MN_CHILD_SUPPORT_STATE_REVENUE_RECAPTURE_OFFSET_V0_1

```json
{
  "artifact": "MN_CHILD_SUPPORT_STATE_REVENUE_RECAPTURE_OFFSET_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_CHILD_SUPPORT_STATE_REVENUE_RECAPTURE_OFFSET_V0_1.md",
  "parent_artifact": "MN_CHILD_SUPPORT_FEDERAL_TAX_REFUND_OFFSET_PROJECT_INTERCEPT_V0_1",
  "parent_spine": "MN_CHILD_SUPPORT_ENFORCEMENT_INTERCEPT_SPINE_V0_1",
  "related_mndor_spine": "MNDOR_REVENUE_RECAPTURE_SPINE_V0_1",
  "lane": "MN_AUDIT",
  "vector": "state Revenue Recapture child support lane",
  "classification": "CHILD_SUPPORT_STATE_REFUND_PAYMENT_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

Minnesota Revenue Recapture / State Tax Refund Offset is a child support enforcement lane for state-level refunds and qualifying Minnesota payments. It complements ongoing income withholding and federal refund offset by targeting Minnesota-controlled refund/payment streams.

This layer answers:

```text
How do Minnesota child support arrears reach state refunds and qualifying state payments through MNDOR?
```

## Source Packet Submitted

```json
{
  "primary_surfaces": [
    "Minnesota DCYF state tax refund offset page",
    "Minnesota Department of Revenue Revenue Recapture page",
    "Minnesota Child Support Online case/status surface"
  ],
  "public_urls_submitted": [
    "https://dcyf.mn.gov/state-tax-refund-offset",
    "https://www.revenue.state.mn.us/revenue-recapture"
  ],
  "fetched_at": "2026-06-13",
  "content_hash": "MN_CHILD_SUPPORT_STATE_REVENUE_RECAPTURE_20260613_USER_PACKET",
  "witness_service_or_replay_surface": "User-submitted official-source packet; direct URL/hash replay still required for full four-surface verification",
  "official_source_type": "MN_DCYF_PAGE_PLUS_MNDOR_PAGE"
}
```

## Indexed State Offset Rule

```json
{
  "rule": "Revenue Recapture targets Minnesota state refunds and qualifying payments for eligible child support arrears.",
  "IWO_lane": "ongoing income withholding from wages, UI, or other payor sources",
  "Project_Intercept_lane": "federal refund lump-sum offset",
  "Revenue_Recapture_lane": "Minnesota state refund/payment offset",
  "DOR_boundary": "MNDOR executes state offset mechanics but does not create the underlying child support debt",
  "DCYF_county_boundary": "child support agency/county framework creates, maintains, or enforces the arrears/order basis"
}
```

## Mechanics Indexed

- Child support arrears can connect to Minnesota Revenue Recapture / State Tax Refund Offset.
- County child support or enforcement actors may file or certify a claim to MNDOR.
- MNDOR may offset qualifying Minnesota refunds or payments under the recapture spine.
- Qualifying streams can include state income tax refunds, property tax refunds, renter credits, lottery winnings, political contribution refunds, and other qualifying state payments already indexed in the MNDOR spine.
- Child support sits high in the debt priority structure.
- Notice and review/hearing paths remain part of the administrative offset spine.
- Nonliable spouse protections may apply for joint returns.
- Person-level validity requires support order, arrears ledger, notice, claim, and payment/offset records.

## Indexed Pipeline

```json
{
  "step_1": "child_support_order_and_arrears_exist",
  "step_2": "county_or_child_support_program_identifies_eligible_arrears",
  "step_3": "claim_or_certification_to_MNDOR_revenue_recapture",
  "step_4": "Revenue_Recapture_notice_or_review_path",
  "step_5": "MNDOR_offsets_qualifying_state_refund_or_payment_if_available",
  "step_6": "funds_remitted_or_applied_through_child_support_distribution_rules",
  "step_7": "review_correction_nonliable_spouse_or_hearing_path_if_applicable"
}
```

## Three-Lane Enforcement Contrast

| Layer | IWO / Income Withholding | Project Intercept | Revenue Recapture |
|---|---|---|---|
| Payment type | ongoing income stream | federal tax refund | Minnesota state refund/payment |
| Actor executing payment movement | employer/payor, including DEED when applicable | federal Treasury offset pipeline | Minnesota Department of Revenue |
| Debt-origin authority | child support order / county or child support agency records | child support order / arrears certification | child support order / arrears certification |
| Timing | recurring | seasonal/refund-dependent | refund/payment-dependent |
| DEED role | payor-source if UI/paid leave is withheld | no federal refund offset authority | no state refund offset authority unless separately a claimant in UI overpayment lane |
| Person-level proof | IWO, payor record, ledger | pre-offset notice, Treasury notice, ledger | Revenue Recapture notice, MNDOR offset record, ledger |

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | State offset model is separated from person-level arrears reality. |
| ERS-002 Wrong Vault | PASS | DOR execution, DCYF/county debt basis, and DEED payor role remain distinct. |
| ERS-003 Wrong Certificate | PARTIAL | User supplied official source packet; direct URL/hash replay still needed for full four-surface verification. |
| ERS-004 Unknown Waters | DOWNGRADED | Program state-offset lane clear; individual notices, certifications, and ledger still required. |

## Strict Scope

This artifact does not verify:

- any specific child support order;
- any specific arrears amount;
- any specific state-assigned or family-owed distribution;
- any specific Revenue Recapture notice;
- any specific MNDOR offset;
- any specific lottery/property/income tax refund stream;
- any specific nonliable spouse claim;
- any specific fee or distribution;
- any agency error;
- any legal conclusion.

## Remaining Four-Surface Requirements

```json
{
  "Minnesota_DCYF_state_tax_refund_offset_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "MNDOR_Revenue_Recapture_public_url": "REQUIRED_FOR_FULL_REPLAY",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Person-Level Packet Requirements

```json
{
  "support_order": "REQUIRED_FOR_PERSON_LEVEL",
  "arrears_ledger": "REQUIRED_FOR_PERSON_LEVEL",
  "assigned_or_family_owed_status": "REQUIRED_FOR_PERSON_LEVEL",
  "Revenue_Recapture_notice": "REQUIRED_FOR_PERSON_LEVEL",
  "MNDOR_offset_or_payment_record": "REQUIRED_IF_OFFSET_OCCURRED",
  "review_or_hearing_record": "REQUIRED_IF_CONTESTED",
  "nonliable_spouse_record": "REQUIRED_IF_JOINT_RETURN"
}
```

## Classification Update

```json
{
  "vector": "state Revenue Recapture child support lane",
  "classification": "CHILD_SUPPORT_STATE_REFUND_PAYMENT_OFFSET_SPINE",
  "state": "PROGRAM_LEVEL_INDEXED_SOURCE_PACKET_ATTACHED_BY_USER",
  "evidence_weight": "HIGH_PROGRAM_LEVEL_PENDING_DIRECT_OFFICIAL_URL_HASH_REPLAY",
  "promotion_allowed": "PROGRAM_LEVEL_ONLY_WITH_CAUTION",
  "person_level_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Next Lawful Surfaces

1. Attach direct DCYF state tax refund offset URL and MNDOR Revenue Recapture URL with hashes.
2. Select assigned vs unassigned arrears distribution rules.
3. Select county child support notice/review/hearing path.
4. Select person-level order, arrears ledger, and recapture notice packet, if a specific case lane is chosen.

## Closing Receipt

State Revenue Recapture child support lane indexed.  
The three-lane enforcement map is now complete at program level: IWO, federal refund offset, and Minnesota Revenue Recapture.  
MNDOR executes state offset mechanics; child support agencies own the underlying support/order basis.  
Program model holds with caution pending direct URL/hash replay.  
Person-level order, arrears, notice, and offset records remain unverified.

No receipt, no score.  
No replay, no confidence.  
No authority by vibes.
