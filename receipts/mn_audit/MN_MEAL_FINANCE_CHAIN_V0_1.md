# MN_MEAL_FINANCE_CHAIN_V0_1

```json
{
  "artifact": "MN_MEAL_FINANCE_CHAIN_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_MEAL_FINANCE_CHAIN_V0_1.md",
  "parent_artifact": "MN_DISTRICT_PACKET_ISD_742_V0_1",
  "gate": "PROTECT_CHILDREN_FROM_AI_SYSTEMS_JAYWISDOM_GATE_V0_1",
  "lane": "MN_AUDIT",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "classification": "SCHOOL_MEAL_FINANCE_CHAIN_OF_CUSTODY_MAP",
  "state": "CHAIN_MAP_INDEXED_SOURCE_PACKET_PENDING",
  "kid_readable": true,
  "kid_protective": true,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "vendor_chain_verified": false,
  "processor_chain_verified": false,
  "data_retention_verified": false,
  "fraud_claim": false,
  "foreign_exposure_verified": false
}
```

## Core Rule

```text
Every hop is separate.
No hop inherits authority.
No hop can deny meals.
Receipts decide.
```

A six-year-old version:

```text
School gives lunch.
Payment app moves money.
Card company checks card.
Bank settles money.
Vendors may store data.
None of them get to take lunch away.
Adults must show receipts.
```

## Chain Summary

```text
District
  -> Portal
    -> POS
      -> Processor
        -> Gateway
          -> Acquirer
            -> Subprocessors
              -> Data Retention
```

## 0. District

Lane: Meal Rights + Vendor Chains

The district is the public governance surface for school meal access, procurement, policy, compliance, and student-data obligations.

The district does not automatically own or control every downstream vendor system.

Artifacts to request:

- payment platform contract;
- fee split schedule;
- third-party vendor list;
- data-sharing agreements;
- meal access policy;
- procurement and board approval records.

## 1. Portal

Lane: Payment Systems + Data & Privacy

The portal may support:

- parent login;
- student lookup;
- balance view;
- meal or a la carte deposits;
- activity fees;
- recurring payments.

The portal may collect:

- parent email;
- student ID;
- device/browser metadata;
- transaction logs;
- optional allergy or meal preference data if entered.

Portal does not equal meal authority.  
Portal does not equal debt creator.  
Portal does not equal child-safety certification.

Artifacts to request:

- portal privacy notice;
- terms of service;
- subprocessor list;
- PCI or payment security attestation;
- data processing addendum.

## 2. POS

Lane: Vendor Chains + Food Quality

The POS is the cafeteria point-of-sale or meal-service system used by staff.

It may log:

- student ID/PIN/scan;
- meal served;
- a la carte item;
- timestamp;
- cashier or terminal ID.

POS does not equal payment processor.  
POS does not equal retention authority.  
POS does not equal meal-rights authority.

Artifacts to request:

- POS hardware model;
- POS software/version;
- local network or system diagram;
- food service system contract;
- meal transaction retention policy.

## 3. Processor

Lane: Vendor Chains

The processor is the entity that processes card or electronic payment activity.

Processor responsibilities may include:

- card authorization;
- risk/fraud screening for transactions;
- settlement batching;
- PCI compliance obligations.

Processor does not equal district.  
Processor does not equal meal authority.  
Processor does not equal portal.

Artifacts to request:

- processor name and contract chain;
- PCI-DSS certificate or validation summary;
- data-flow diagram;
- processor privacy/security terms.

## 4. Gateway

Lane: Vendor Chains

The gateway routes payment messages between portal, processor, and response systems.

Gateway logs may include:

- transaction metadata;
- routing events;
- approval/decline response;
- error codes;
- timestamps.

Gateway does not equal processor.  
Gateway does not equal acquirer.  
Gateway does not equal district.

Artifacts to request:

- gateway documentation;
- routing disclosures;
- error code or event log policy;
- subprocessor or platform relationship.

## 5. Acquirer

Lane: Vendor Chains

The acquirer is the bank or merchant-acquiring institution that receives card-settlement funds and connects the merchant to the card-network settlement flow.

The acquirer does not equal district.  
The acquirer does not equal processor.  
The acquirer does not equal portal.  
The acquirer does not control student meal rights.

Artifacts to request:

- acquiring bank disclosure;
- settlement schedule;
- merchant category code;
- merchant-of-record disclosure;
- settlement account relationship.

## 6. Subprocessors

Lane: Data & Privacy

Subprocessors may include:

- cloud hosting;
- analytics tools;
- email delivery services;
- logging and monitoring vendors;
- identity providers;
- CDN providers;
- support or ticketing vendors.

Subprocessors do not equal district.  
Subprocessors do not equal meal authority.  
Subprocessors do not equal payment authority.

Artifacts to request:

- vendor subprocessor list;
- data-sharing agreements;
- cross-border transfer statements;
- security addenda;
- ownership/control disclosures.

## 7. Data Retention

Lane: Data & Privacy

Each entity may have its own retention obligations and deletion policies.

District retention may include:

- student records;
- meal-service logs;
- financial records;
- public-records schedules.

Portal retention may include:

- account data;
- transaction logs;
- device metadata;
- user activity records.

Processor/gateway retention may include:

- PCI-related logs;
- transaction/risk logs;
- settlement records.

Acquirer retention may include:

- banking records;
- settlement history;
- merchant account records.

Retention does not equal authority.  
Retention does not equal consent.  
Retention does not equal compliance.

Artifacts to request:

- retention schedules;
- deletion policies;
- FERPA/MGDPA/USDA confidentiality statements;
- PCI retention requirements;
- breach/incident retention policy.

## ERS Replay

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | PASS | The chain separates each role instead of collapsing them into one claim. |
| ERS-002 Wrong Vault | PASS | District, portal, POS, processor, gateway, acquirer, subprocessors, and retention are separate vaults. |
| ERS-003 Wrong Certificate | ACTIVE | Need contracts, receipts, privacy notices, data-flow maps, PCI artifacts, and retention schedules. |
| ERS-004 Unknown Waters | ACTIVE | Actual ISD 742 vendor chain remains unmapped until public source packet arrives. |

## Strict Scope

This artifact does not verify:

- which portal ISD 742 currently uses;
- which POS hardware or software is deployed;
- which processor, gateway, or acquirer is active;
- any subprocessor list;
- any retention period;
- any data misuse;
- any foreign exposure;
- any fraud;
- any legal violation.

## Required Source Packet for Promotion

```json
{
  "district_payment_or_meal_page": "REQUIRED",
  "portal_or_vendor_page": "REQUIRED",
  "contract_or_procurement_record": "REQUIRED",
  "receipt_or_portal_observation": "REQUIRED_FOR_TRANSACTION_TRACE",
  "fee_schedule": "REQUIRED_FOR_FEE_CLAIM",
  "processor_gateway_acquirer_disclosure": "REQUIRED_FOR_VENDOR_CHAIN_CLAIM",
  "subprocessor_list": "REQUIRED_FOR_DATA_EXPOSURE_CLAIM",
  "data_retention_policy": "REQUIRED_FOR_RETENTION_CLAIM",
  "PCI_or_security_attestation": "REQUIRED_FOR_PAYMENT_SECURITY_CLAIM",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Closing Receipt

MN Meal Finance Chain indexed.  
District -> Portal -> POS -> Processor -> Gateway -> Acquirer -> Subprocessors -> Data Retention.  
Each hop is a separate governance surface.  
No hop inherits authority from the previous hop.  
No hop can deny meals.  
Only receipts, contracts, and data-flow maps promote claims.

Children protected.  
Evidence preserved.  
Audit cold.  
JAYWISDOM Gate holds.  
Receipts decide.
