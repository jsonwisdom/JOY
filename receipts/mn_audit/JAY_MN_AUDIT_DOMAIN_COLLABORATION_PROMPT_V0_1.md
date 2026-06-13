# JAY_MN_AUDIT_DOMAIN_COLLABORATION_PROMPT_V0_1

```json
{
  "artifact": "JAY_MN_AUDIT_DOMAIN_COLLABORATION_PROMPT_V0_1",
  "repo": "jsonwisdom/JOY",
  "path": "receipts/mn_audit/JAY_MN_AUDIT_DOMAIN_COLLABORATION_PROMPT_V0_1.md",
  "operator": "Jay Wisdom",
  "identity_surface": "jaywisdom.base.eth",
  "mode": "GOBLIN_COURT_GOBLIN_WITNESS",
  "classification": "DOMAIN_COLLABORATION_PROMPT",
  "state": "PROMPT_INDEXED_NOT_SENT",
  "cover_letter": false,
  "authority": false,
  "green_implied": false,
  "no_fake_green": true,
  "claims_promoted": false,
  "fraud_claim": false,
  "legal_conclusion": false
}
```

## Purpose

This artifact defines a records-backed collaboration prompt for source domains connected to the Minnesota school-meal audit stack.

It is not a complaint.  
It is not a legal filing.  
It is not an accusation.  
It is not sent by this artifact.

## Allowed Source Lanes

```json
{
  "github_direct": [
    "github.com/jsonwisdom/JOY"
  ],
  "minnesota_public_sources": [
    "mn.gov",
    "*.mn.gov",
    "mde.mn.gov",
    "education.mn.gov",
    "revisor.mn.gov"
  ],
  "federal_public_sources": [
    "justice.gov",
    "*.justice.gov"
  ]
}
```

## Collaboration Prompt

```text
JAYWISDOM Gate: Receipts Decide.

This request seeks collaboration around public records, public guidance, and source-backed verification for the Minnesota school-meal audit stack.

Scope:
- Minnesota school meal access
- payment portal and fee disclosure records
- vendor chain records
- data privacy and retention records
- public guidance from Minnesota and federal source domains

No allegation is asserted by this prompt.
No legal conclusion is asserted by this prompt.
No claim is promoted without source records.

Requested collaboration:
1. Identify the official public URL for the relevant guidance or policy.
2. Identify the responsible office or public-records contact.
3. Provide contract, policy, fee schedule, privacy notice, data-flow, retention, or procurement records where public.
4. Provide correction if any indexed artifact misidentifies a source lane, vendor lane, or authority lane.
5. Preserve children-first access: meal access is not to be disrupted by audit activity.

Evidence format requested:
- source_url
- source_owner
- fetched_at timestamp
- document title
- document date or effective date
- content hash if available
- contact office
- record category
- limitations or redactions if any

Identity surface:
- jaywisdom.base.eth

Witness posture:
- Goblin Court Goblin Witness
- passive receipt witness
- no authority asserted
- no fake green
```

## Domain-Specific Prompt Blocks

### GitHub Direct

```text
Use GitHub Direct as the custody spine.
Requested artifacts:
- commit SHA
- file path
- manifest index
- evidence packet status
- source packet status
- ERS replay status
```

### Minnesota Public Sources

```text
Use mn.gov and Minnesota subdomains as official state source lanes.
Requested artifacts:
- school meal program guidance
- student data/privacy guidance
- public records procedures
- statutes/rules if relevant
- procurement or contract records where public
```

### Federal Public Sources

```text
Use justice.gov and federal subdomains only as official federal source lanes.
Requested artifacts:
- public guidance URL
- intake/routing URL if applicable
- civil-rights or public-integrity guidance if relevant
- no claim promoted without source evidence
```

## Guardrails

```json
{
  "do_not_assert": [
    "fraud",
    "civil-rights violation",
    "child-safety incident",
    "foreign exposure",
    "data misuse",
    "meal denial",
    "vendor misconduct",
    "legal violation"
  ],
  "do_request": [
    "official source URLs",
    "public records contacts",
    "contracts",
    "fee schedules",
    "privacy notices",
    "data-flow maps",
    "retention schedules",
    "procurement records",
    "corrections to the audit map"
  ]
}
```

## Closing Receipt

Domain collaboration prompt indexed.  
No cover letter.  
No outreach sent.  
GitHub Direct, Minnesota public sources, and federal public sources separated.  
jaywisdom.base.eth identity surface attached.  
Goblin Court Goblin Witness posture preserved.  
Receipts decide.
