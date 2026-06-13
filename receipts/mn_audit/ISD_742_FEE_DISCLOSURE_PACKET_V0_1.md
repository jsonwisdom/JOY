# ISD_742_FEE_DISCLOSURE_PACKET_V0_1

```json
{
  "artifact": "ISD_742_FEE_DISCLOSURE_PACKET_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/ISD_742_FEE_DISCLOSURE_PACKET_V0_1.md",
  "parent_artifact": "ISD_742_RECEIPT_PACKET_V0_1",
  "data_flow_diagram": "ISD_742_DATA_FLOW_DIAGRAM_V0_1",
  "vendor_chain_map": "ISD_742_VENDOR_CHAIN_MAP_V0_1",
  "district_packet": "MN_DISTRICT_PACKET_ISD_742_V0_1",
  "gate": "PROTECT_CHILDREN_FROM_AI_SYSTEMS_JAYWISDOM_GATE_V0_1",
  "lane": "MN_AUDIT",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "district": "St. Cloud Area Schools / ISD 742",
  "classification": "MINNESOTA_SCHOOL_MEAL_FEE_EVIDENCE_PACKET",
  "state": "FEE_TEMPLATE_INDEXED_NO_OBSERVATION_ADMITTED",
  "kid_protective": true,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "fee_observation_admitted": false,
  "receipt_attached": false,
  "fee_verified": false,
  "fee_free_option_verified": false,
  "meal_access_denial_verified": false,
  "vendor_chain_verified": false,
  "privacy_notice_verified": false,
  "fraud_claim": false,
  "foreign_exposure_verified": false
}
```

## Purpose

This packet captures one real fee observation in ISD 742 and enforces separation between:

- convenience fee;
- merchant fee;
- surcharge;
- cash/check option;
- meal-access rights.

Fees belong to the Payment Systems lane.  
Meal access belongs to the Meal Rights lane.

Fees do not create meal denial.  
Fees do not prove misuse.  
Fees do not prove fraud.

## Fee Type Definitions

```json
{
  "convenience_fee": "Fee disclosed for optional online/card/payment-portal convenience.",
  "merchant_fee": "Processor/acquirer cost, if disclosed or passed through.",
  "surcharge": "Card-brand or card-use add-on, if separately disclosed.",
  "cash_check_option": "Fee-free payment method or non-card alternative, if available and documented.",
  "meal_access_rights": "Student meal access lane; cannot be conditioned on optional portal fee."
}
```

Each fee type is mutually separated until receipts or fee schedules prove otherwise.

## Canonical Fee Observation Template

```json
{
  "district": "St. Cloud Area Schools ISD 742",
  "school_building": "",
  "observation_timestamp": "ISO8601",
  "payment_channel": "PaySchools Central | Cash | Check | POS | Other | Unknown",
  "portal_url": "",
  "fee_disclosure": {
    "convenience_fee": {
      "amount": "",
      "visible": false,
      "notes": ""
    },
    "merchant_fee": {
      "amount": "",
      "visible": false,
      "notes": ""
    },
    "surcharge": {
      "amount": "",
      "visible": false,
      "notes": ""
    },
    "cash_check_option": {
      "available": true,
      "signage_visible": false,
      "notes": ""
    }
  },
  "meal_access_rights": {
    "free_meal_access_visible": true,
    "denial_observed": false,
    "notes": ""
  },
  "receipt_details": {
    "receipt_available": true,
    "merchant_dba": "",
    "transaction_amount": "",
    "transaction_id": "",
    "payment_method": "card | ACH | cash | check | unknown",
    "screenshot_or_photo": "yes/no"
  },
  "vendor_chain_alignment": {
    "portal": "",
    "processor": "",
    "gateway": "",
    "acquirer": "",
    "notes": ""
  },
  "data_privacy": {
    "fee_related_data_collected": [],
    "privacy_notice_link_visible": false,
    "notes": ""
  },
  "ers_flags": {
    "ers_001_wrong_fridge": "hold",
    "ers_002_wrong_vault": "hold",
    "ers_003_wrong_certificate": "active_if_missing_receipt_or_contract",
    "ers_004_unknown_waters": "active_if_fee_split_unmapped"
  },
  "observer_notes": ""
}
```

## Field-by-Field Constitutional Logic

### 1. Payment Channel

Identifies whether the fee is tied to:

- online portal;
- POS/card terminal;
- cash;
- check;
- other channel.

Payment channel does not equal meal authority.

### 2. Fee Disclosure Block

Separates:

- convenience fee;
- merchant fee;
- surcharge;
- cash/check or fee-free option.

No mixing.  
No inference.  
No claim promotion without receipt, screenshot, fee schedule, or contract.

### 3. Meal-Access Rights Block

Captures whether free meal access was visible and whether denial was observed.

Fees cannot affect this lane without direct evidence of denial or policy violation.

### 4. Receipt Details Block

Merchant DBA anchors the vendor chain. Transaction amount and ID anchor replay.

### 5. Vendor Chain Alignment Block

Confirms whether the fee aligns to:

- portal;
- processor;
- gateway;
- acquirer.

Vendor chain is not verified without contract, receipt, privacy notice, or processor disclosure.

### 6. Data Privacy Block

Captures fee-related data collection, such as:

- transaction amount;
- payment method;
- timestamp;
- device metadata;
- account identifiers.

Data does not equal meal rights.  
Data does not equal payment authority.  
Data does not equal consent to unrelated use.

## Fictional Shape Example

The following example is fictional and only demonstrates packet shape. It is not admitted evidence.

```json
{
  "district": "St. Cloud Area Schools ISD 742",
  "school_building": "Example School",
  "observation_timestamp": "2026-06-12T22:01:00-05:00",
  "payment_channel": "Example Portal",
  "portal_url": "https://example.invalid",
  "fee_disclosure": {
    "convenience_fee": {
      "amount": "$0.00",
      "visible": false,
      "notes": "Example only."
    },
    "merchant_fee": {
      "amount": "",
      "visible": false,
      "notes": ""
    },
    "surcharge": {
      "amount": "",
      "visible": false,
      "notes": ""
    },
    "cash_check_option": {
      "available": true,
      "signage_visible": false,
      "notes": "Example only."
    }
  },
  "meal_access_rights": {
    "free_meal_access_visible": true,
    "denial_observed": false,
    "notes": "Example only; no real observation admitted."
  },
  "receipt_details": {
    "receipt_available": false,
    "merchant_dba": "EXAMPLE DBA",
    "transaction_amount": "$0.00",
    "transaction_id": "EXAMPLE",
    "payment_method": "unknown",
    "screenshot_or_photo": "no"
  },
  "vendor_chain_alignment": {
    "portal": "Example Portal",
    "processor": "Unknown",
    "gateway": "Unknown",
    "acquirer": "Unknown",
    "notes": "Example only; no vendor claim promoted."
  },
  "data_privacy": {
    "fee_related_data_collected": ["example_field"],
    "privacy_notice_link_visible": false,
    "notes": "Example only."
  },
  "ers_flags": {
    "ers_001_wrong_fridge": "hold",
    "ers_002_wrong_vault": "hold",
    "ers_003_wrong_certificate": "active_if_missing_receipt_or_contract",
    "ers_004_unknown_waters": "active_if_fee_split_unmapped"
  },
  "observer_notes": "Fictional shape demonstration only."
}
```

## ERS Replay

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | Fee observation does not prove denial, misuse, fraud, or foreign exposure. |
| ERS-002 Wrong Vault | PASS | Payment fees and meal-access rights remain separate vaults. |
| ERS-003 Wrong Certificate | ACTIVE | Receipt, fee schedule, merchant DBA, contract, privacy notice, or processor disclosure required. |
| ERS-004 Unknown Waters | ACTIVE | Fee split, processor, gateway, acquirer, and data collection remain unmapped until sourced. |

## Admission Requirements

A completed fee packet may be admitted only if it includes:

```json
{
  "school_building": "REQUIRED",
  "observation_timestamp": "REQUIRED",
  "payment_channel": "REQUIRED",
  "fee_disclosure": "REQUIRED",
  "meal_access_rights": "REQUIRED",
  "observer_notes": "REQUIRED",
  "ers_flags": "REQUIRED"
}
```

Promotion still requires source-specific evidence:

```json
{
  "fee_amount": "REQUIRED_FOR_FEE_CLAIM",
  "fee_type": "REQUIRED_FOR_FEE_CLASSIFICATION",
  "merchant_DBA": "REQUIRED_FOR_VENDOR_CHAIN_PROMOTION",
  "receipt_or_screenshot": "REQUIRED_FOR_TRANSACTION_CLAIM",
  "fee_schedule_or_contract": "REQUIRED_FOR_FEE_SPLIT_CLAIM",
  "cash_check_policy": "REQUIRED_FOR_FEE_FREE_OPTION_CLAIM",
  "privacy_notice_or_DPA": "REQUIRED_FOR_FEE_DATA_CLAIM",
  "processor_acquirer_disclosure": "REQUIRED_FOR_VENDOR_CHAIN_CLAIM",
  "meal_denial_record": "REQUIRED_FOR_MEAL_ACCESS_DENIAL_CLAIM"
}
```

## Strict Scope

This artifact does not admit any real fee observation.

It does not verify:

- actual ISD 742 portal provider;
- actual fee amount;
- actual fee type;
- actual merchant DBA;
- actual fee-free option;
- actual processor, gateway, or acquirer;
- actual privacy notice;
- actual meal denial;
- actual data misuse;
- actual foreign exposure;
- fraud;
- legal violation.

## Closing Receipt

ISD 742 Fee Disclosure Packet indexed.  
This is the fee-lane evidence-class object.  
It isolates the payment lane from the rights lane.  
Convenience fees, merchant fees, and surcharges belong to payment systems.  
Cash/check or other fee-free options must be mapped separately.  
Meal access remains a rights lane and cannot be inferred from payment fees.

Only receipts, fee schedules, processor contracts, privacy notices, and meal-access records promote a claim.

Children protected.  
Evidence preserved.  
Audit cold.  
JAYWISDOM Gate holds.  
Receipts decide.
