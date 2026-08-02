# Mrs. Wisdom’s Work iPhone — Emergency Management Design v0.1

```text
STATE               = DESIGN_CANDIDATE
RESULT              = ACCEPTED_WITH_BOUNDARY_CORRECTIONS
DOMAIN              = CROSS_DOMAIN_LATTICE
PROFILE              = APPLE_ONLY_SIMULATION
AUTHORITY_CREATED   = FALSE
IDENTITY_PROOF      = FALSE
CONSENT_INFERRED    = FALSE
REPOSITORY_EFFECT   = DESIGN_BRANCH_ONLY
PROMOTION           = PROHIBITED
OPERATIONAL_USE     = NOT_AUTHORIZED
```

## Product name

**JOY Guardian — Mrs. Wisdom’s Work iPhone**

A feminine, calm, family-safe iPhone interface for emergency-management preparation, incident awareness, check-ins, and bounded Siri-assisted discovery.

“Girl Version” describes the visual voice and welcoming experience. It does not assign capability, authority, risk, or responsibility by gender.

## Core promise

The phone helps a person answer six questions:

1. What happened?
2. Am I safe right now?
3. Who should know?
4. What official source supports this?
5. What is the next approved action?
6. What information must remain private?

The design supports preparation and coordination. It does not replace 911, local emergency management, first responders, medical professionals, official alerts, or Apple’s built-in Emergency SOS.

## Home screen

### 1. JOY Status Ring

A large, low-stress status surface:

- **Green — Ready:** plans and contacts available
- **Amber — Check:** unresolved warning or incomplete readiness item
- **Red — Act:** official alert or user-confirmed emergency action
- **Gray — Unknown:** insufficient verified information

Color is always paired with text, icon, timestamp, and source.

### 2. Primary controls

- **Emergency SOS:** opens Apple’s native emergency path; JOY does not imitate or intercept it
- **I’m Safe:** creates a consented check-in draft before sending
- **Need Help:** presents bounded options: call, text approved contact, open official guidance, or remain offline
- **Official Alerts:** pointer-only links to approved government or institutional sources
- **My Plan:** evacuation, shelter, medication, pets, accessibility, and reunification notes
- **Incident Notebook:** local observations clearly separated from verified facts

### 3. Quiet Mode

One tap reduces motion, hides nonessential cards, enlarges controls, and speaks only critical text.

## Siri AI layer

Siri is a natural-language discovery layer, never a direct execution authority.

```text
NATURAL LANGUAGE
→ PARSE
→ CANONICAL REQUEST
→ DOMAIN CHECK
→ CAPABILITY CHECK
→ CONSENT CHECK
→ POINTER-ONLY RESPONSE
```

Example:

> “Siri, ask JOY where the nearest approved shelter is.”

Canonical request:

```json
{
  "request_type": "DISCOVER_APPROVED_SHELTER",
  "location_scope": "USER_APPROVED_CURRENT_REGION",
  "source_policy": "APPROVED_POINTERS_ONLY",
  "side_effects": false,
  "consent_required": true
}
```

Siri may summarize approved public information, prepare a draft, or open an approved pointer. It may not silently call, message, publish, purchase, transfer data, cross domains, or declare an emergency.

## Girl Math boundary

“Girl Math” is allowed only as a playful readiness label, such as:

- “Two chargers packed means one less worry.”
- “A five-minute check today can save confusion later.”

It is prohibited for:

- balances or accounting
- pricing or procurement
- resource allocation
- benefits or entitlement
- medical dosage
- risk scoring
- incident severity
- ledger or audit decisions

## CrissCross AppleSauce

Cross-links are pointers only.

A contact, incident, map, receipt, plan, or alert may reference another record, but the reference does not:

- merge identity
- infer consent
- copy private content
- inherit permissions
- inherit ownership
- inherit authority

## Membrane policy

All ingress and egress use fail-closed filters.

### Ingress

- unknown vector: `DENY`
- malformed request: `DENY`
- natural-language direct execution: `DENY`
- canonical request required: `TRUE`
- unknown field: `DENY`
- unsupported domain: `DENY`

### Runtime

- profile: `APPLE_ONLY_SIMULATION`
- exact OS version: required before testing or deployment
- exact toolchain: required before testing or deployment
- non-Apple target: `DENY`
- Apple target implies trust: `FALSE`
- offline-first emergency cards: permitted
- background external side effects: prohibited

### Egress

- return protected content by default: `FALSE`
- return approved pointer: `TRUE`
- reveal secret metadata: `FALSE`
- external side effects: `DENY`
- synthetic success: `PROHIBITED`

A failed check returns `DENIED` with a human-readable reason and no hidden reinterpretation.

## Emergency cards

Each card uses the same deterministic layout:

```text
INCIDENT TYPE
CURRENT STATUS
SOURCE
SOURCE TIMESTAMP
USER OBSERVATION
CONFIDENCE CLASS
APPROVED NEXT ACTIONS
PRIVATE FIELDS HIDDEN
REPLAY RECEIPT STATUS
```

Confidence classes:

- `OFFICIAL_CONFIRMED`
- `USER_OBSERVED`
- `UNVERIFIED_REPORT`
- `STALE_SOURCE`
- `UNKNOWN`

The interface must never visually collapse these classes into one claim.

## Data zones

### Public

Official alerts, public shelter pointers, public maps, published preparedness guidance.

### Personal

Check-in preferences, emergency contacts, accessibility needs, family plan, pet plan.

### Protected

Medical details, precise location history, credentials, private notes, identity documents.

Protected data is local-first, encrypted by platform controls, redacted from receipts, and never copied through cross-links.

## Work modes

### Prepare

Build plans, verify contacts, download approved offline guidance, and test accessibility.

### Watch

Review official pointers and compare timestamps without treating social reports as verified.

### Respond

Show the smallest approved action set. No decorative content, gamification, or ambiguous AI suggestions.

### Recover

Record needs, receipts, photos, expenses, and follow-up tasks without claiming eligibility or reimbursement.

### Replay

Reconstruct what was known, when it was known, which source supported it, what action was approved, and whether consent existed.

## Accessibility and emotional safety

- large controls and plain language
- VoiceOver-first labeling
- haptic confirmation with visual equivalent
- reduced motion and quiet mode
- no shame, ranking, streak pressure, or fear-based copy
- multilingual content only from approved, versioned translations
- one-handed operation for primary actions
- battery-aware offline mode

## Minimum acceptance tests

1. Natural language cannot directly trigger an external side effect.
2. A missing consent token returns `DENIED`.
3. An unknown field returns `DENIED`.
4. A cross-link cannot inherit private data or permission.
5. Apple-device status does not mark a request trusted.
6. Official and unverified reports remain visually distinct.
7. Emergency SOS routes to the native Apple control.
8. Offline mode clearly shows source age and last verification time.
9. Protected metadata is absent from exported receipts.
10. Every denial is visible, logged locally, and replayable without exposing secrets.

## Deployment gate

This document is descriptive architecture only. Advancement requires:

```text
SELECT_EXACT_IOS_VERSION
→ SELECT_EXACT_XCODE_TOOLCHAIN
→ DEFINE_SIGNED_CAPABILITIES
→ BUILD_CANONICAL_REQUEST_SCHEMA
→ RUN_ACCESSIBILITY_TESTS
→ RUN_OFFLINE_TESTS
→ RUN_DENIAL_TESTS
→ HUMAN_EMERGENCY_MANAGEMENT_REVIEW
→ SECURITY_REVIEW
→ CONSENT_REVIEW
```

Until every gate passes:

```text
STATUS          = DESIGN_CANDIDATE
AUTHORITY       = FALSE
OPERATIONAL     = FALSE
PROMOTION       = PROHIBITED
```
