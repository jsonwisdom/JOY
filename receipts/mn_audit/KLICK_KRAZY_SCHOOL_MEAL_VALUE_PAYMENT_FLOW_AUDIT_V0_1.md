# KLICK_KRAZY_SCHOOL_MEAL_VALUE_PAYMENT_FLOW_AUDIT_V0_1

```json
{
  "artifact": "KLICK_KRAZY_SCHOOL_MEAL_VALUE_PAYMENT_FLOW_AUDIT_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/KLICK_KRAZY_SCHOOL_MEAL_VALUE_PAYMENT_FLOW_AUDIT_V0_1.md",
  "parent_artifact": "KLICK_KRAZY_KID_EDITION_PAYMENT_AUDIT_V0_1",
  "lane": "MN_AUDIT",
  "edition": "KLICK_KRAZY_KID",
  "vector": "school meal money flow / monthly payments / lunch quality / delivery alternative pressure",
  "classification": "SCHOOL_MEAL_PAYMENT_VALUE_AND_VENDOR_FLOW_AUDIT",
  "state": "QUESTION_INDEXED_SOURCE_PACKET_PENDING",
  "kid_protective": true,
  "fraud_claim": false,
  "misuse_claim_verified": false,
  "food_quality_claim_verified": false,
  "DoorDash_solution_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Trigger Question

```text
School gets a check every month for what?
My lunch is this?
DoorDash to schools now?
67-67
```

## Clean Translation

This audit asks:

```text
What money does the school receive for meals, what does it spend, what food reaches students, what payment vendors take fees, and what alternatives exist without disrupting student meal access?
```

This is not a fraud claim.  
This is not a food-safety claim.  
This is not a DoorDash procurement recommendation.  
This is a value-for-money and meal-access audit.

## Money Flow to Separate

```json
{
  "federal_or_state_meal_reimbursement": "UNKNOWN_UNTIL_MDE_OR_DISTRICT_PACKET",
  "family_paid_meal_accounts": "UNKNOWN_UNTIL_DISTRICT_PACKET",
  "school_lunch_debt_or_negative_balances": "UNKNOWN_UNTIL_DISTRICT_PACKET",
  "vendor_payment_fees": "UNKNOWN_UNTIL_PORTAL_OR_CONTRACT_PACKET",
  "food_service_contract": "UNKNOWN_UNTIL_DISTRICT_PACKET",
  "food_quality_or_menu_claim": "UNKNOWN_UNTIL_MENU_PHOTO_SURVEY_OR_INSPECTION_PACKET",
  "delivery_platform_option": "UNVERIFIED_POLICY_AND_COST_RISK"
}
```

## ERS Replay

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | A bad lunch experience does not prove misuse of funds. |
| ERS-002 Wrong Vault | HOLD | Meal reimbursement, family payments, vendor fees, and food quality are separate lanes. |
| ERS-003 Wrong Certificate | ACTIVE | Need menu, meal reimbursement data, food-service contract, payment portal fees, receipts, or district budget documents. |
| ERS-004 Unknown Waters | ACTIVE | Monthly payment source, food costs, vendor fees, nutrition rules, and alternatives remain unmapped. |

## Required Source Packet

```json
{
  "district_name": "REQUIRED",
  "school_name": "REQUIRED",
  "meal_program_type": "REQUIRED",
  "menu_or_meal_photo": "OPTIONAL_BUT_USEFUL_IF_LAWFUL",
  "meal_reimbursement_or_claim_summary": "REQUIRED",
  "food_service_budget_or_contract": "REQUIRED",
  "payment_portal_vendor_contract": "REQUIRED_IF_ONLINE_PAYMENTS",
  "fee_schedule": "REQUIRED_IF_FEES_CLAIMED",
  "student_meal_access_policy": "REQUIRED",
  "free_reduced_or_universal_meal_policy": "REQUIRED_IF_APPLICABLE",
  "food_quality_or_complaint_process": "REQUIRED_IF_QUALITY_CLAIM",
  "delivery_platform_policy_or_procurement_analysis": "REQUIRED_IF_DOORDASH_CLAIM",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Records Request Targets

1. Monthly meal reimbursement claims or summaries submitted to Minnesota Department of Education.
2. Food service budget, invoices, vendor contracts, and procurement records.
3. Meal price schedule, unpaid meal debt policy, and student meal access policy.
4. Online lunch payment vendor contract, merchant fees, convenience fees, and district subsidy policy.
5. Menus, nutrition compliance records, and complaint process for meal quality.
6. Any board reports about meal program finances or vendor changes.
7. Any analysis of third-party delivery, outside food policy, or meal delivery restrictions.

## DoorDash Boundary

DoorDash or delivery platforms are not promoted here.

Before any delivery-platform idea receives a green light, the district would need to prove:

- student safety procedures;
- nutrition compliance;
- cost comparison;
- equity and access for low-income students;
- allergy and food-handling controls;
- delivery security at school buildings;
- data privacy and payment-vendor terms;
- procurement authority and board approval.

## Kid-Protective Rule

Do not block meals.  
Do not shame students.  
Do not turn lunch quality complaints into unsupported fraud claims.  
Follow the money, the menu, the contract, and the receipts.

## Classification Update

```json
{
  "vector": "school meal money flow / monthly payments / lunch quality / delivery alternative pressure",
  "classification": "SCHOOL_MEAL_PAYMENT_VALUE_AND_VENDOR_FLOW_AUDIT",
  "state": "QUESTION_INDEXED_SOURCE_PACKET_PENDING",
  "promotion_allowed": false,
  "fraud_claim": false,
  "misuse_claim_verified": false,
  "food_quality_claim_verified": false,
  "DoorDash_solution_verified": false,
  "kid_protective": true,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Closing Receipt

School meal value question indexed.  
Money flow, meal quality, and vendor fees must be separated.  
DoorDash is not a verified solution.  
Children must keep meal access while adults produce receipts.

Kids eat first.  
Adults audit the money.  
No fake green.
