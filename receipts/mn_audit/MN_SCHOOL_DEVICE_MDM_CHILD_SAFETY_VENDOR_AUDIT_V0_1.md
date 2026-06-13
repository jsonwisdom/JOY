# MN_SCHOOL_DEVICE_MDM_CHILD_SAFETY_VENDOR_AUDIT_V0_1

```json
{
  "artifact": "MN_SCHOOL_DEVICE_MDM_CHILD_SAFETY_VENDOR_AUDIT_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/MN_SCHOOL_DEVICE_MDM_CHILD_SAFETY_VENDOR_AUDIT_V0_1.md",
  "lane": "MN_AUDIT",
  "vector": "school device MDM / Apple / Jamf / child safety vendor audit",
  "classification": "EDUCATION_TECH_VENDOR_PRIVACY_AND_CHILD_SAFETY_AUDIT",
  "state": "CLAIM_INDEXED_SOURCE_PACKET_PENDING",
  "abuse_claim_verified": false,
  "vendor_misconduct_verified": false,
  "foreign_exposure_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Claim Surface

The audit question is whether Minnesota school-device management systems, including Apple devices and Jamf-style mobile device management, create privacy, safety, procurement, monitoring, access-control, or vendor-chain risks for students.

This artifact does not assert that any specific school, vendor, employee, or agency committed abuse or misconduct.

## Serious Allegation Boundary

Allegations involving child sexual abuse, exploitation, grooming, or predatory conduct require specific evidence and immediate routing to proper reporting channels.

This repo artifact only indexes an audit vector. It does not verify:

- any specific abuse event;
- any specific offender;
- any specific school failure;
- any specific Jamf or Apple misconduct;
- any specific device compromise;
- any legal conclusion.

## ERS Update

| ERS Check | Result | Notes |
|---|---:|---|
| ERS-001 Wrong Fridge | HOLD | MDM concern does not prove abuse or vendor misconduct. |
| ERS-002 Wrong Vault | HOLD | Device management, school policy, vendor contract, and criminal abuse reports are separate lanes. |
| ERS-003 Wrong Certificate | ACTIVE | Need contract, policy, device profile, incident report, audit log, or official source packet. |
| ERS-004 Unknown Waters | ACTIVE | District, vendor, device scope, admin access, logs, reporting path, and evidence remain unknown. |

## Vendor / System Chain to Map

```json
{
  "school_district_or_agency": "UNKNOWN",
  "device_type": "UNKNOWN",
  "MDM_vendor": "Jamf_or_other_UNKNOWN",
  "Apple_school_manager_scope": "UNKNOWN",
  "admin_roles": "UNKNOWN",
  "student_monitoring_tools": "UNKNOWN",
  "content_filtering_vendor": "UNKNOWN",
  "network_filtering_vendor": "UNKNOWN",
  "logging_and_audit_retention": "UNKNOWN",
  "data_sharing_or_subprocessors": "UNKNOWN",
  "incident_reporting_policy": "UNKNOWN",
  "law_enforcement_or_mandated_reporter_path": "UNKNOWN"
}
```

## Required Source Packet

```json
{
  "district_device_policy": "REQUIRED",
  "student_privacy_policy": "REQUIRED",
  "MDM_contract_or_procurement_record": "REQUIRED",
  "Apple_School_Manager_or_device_management_scope": "REQUIRED_IF_APPLE_LANE",
  "Jamf_contract_or_admin_scope": "REQUIRED_IF_JAMF_LANE",
  "content_filtering_or_monitoring_vendor_contracts": "REQUIRED_IF_MONITORING_CLAIM",
  "audit_log_policy_or_retention_schedule": "REQUIRED",
  "incident_response_policy": "REQUIRED",
  "child_safety_reporting_policy": "REQUIRED",
  "fetched_at": "REQUIRED_PER_SOURCE",
  "content_hash": "REQUIRED_PER_SOURCE",
  "witness_service_or_replay_surface": "REQUIRED_PER_SOURCE"
}
```

## Records Request Targets

1. MDM contract, vendor order, renewal, and amendments.
2. Apple School Manager configuration policy and role matrix.
3. Jamf admin-role matrix, access-control policy, and audit-log retention policy.
4. Content filtering, classroom monitoring, and web-filtering vendor contracts.
5. Student device privacy policy and parent/student notices.
6. Incident response policy for inappropriate access, device misuse, missing devices, or student-safety reports.
7. Child safety and mandated-reporting policy for digital evidence or online contact.
8. Procurement documents, subprocessors, data-sharing agreements, and security addenda.
9. Any completed security/privacy audit reports or board presentations regarding student devices.

## Immediate Safety Rule

If there is a specific child currently at risk or a specific abuse allegation, route to emergency services, local child protection, school mandated-reporting channels, or law enforcement. Do not wait for a repo audit.

## Classification Update

```json
{
  "vector": "school device MDM / Apple / Jamf / child safety vendor audit",
  "classification": "EDUCATION_TECH_VENDOR_PRIVACY_AND_CHILD_SAFETY_AUDIT",
  "state": "CLAIM_INDEXED_SOURCE_PACKET_PENDING",
  "promotion_allowed": false,
  "abuse_claim_verified": false,
  "vendor_misconduct_verified": false,
  "foreign_exposure_verified": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true
}
```

## Closing Receipt

School-device MDM / child-safety vendor audit indexed.  
No abuse claim verified.  
No vendor misconduct verified.  
No foreign exposure verified.  
Specific source packets and safety reports control the next gate.

Protect kids first.  
Preserve evidence second.  
Do not accuse without receipts.
