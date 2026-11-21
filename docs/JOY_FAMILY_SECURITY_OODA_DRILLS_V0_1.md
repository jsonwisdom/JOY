# JOY Family Security — OODA Drills v0.1

**2026-11-21 | PUBLIC-SAFE SIMULATION | CI-FIRST | AUTHORITY=false | REVIEW ONLY**

Extends SCHOOL_OF_WISDOM_GRAND_OODA_LOOP_2026-11-07.md, FAMILY/receipts/PUBLIC_REPO_AUTHORITY_PERIMETER_BOUNDARY_V0_1.md, and drills/ZERO_TRUST_PUBLIC_AUDIT_DRILLS_V0_1.json. Existing files are preserved. Children and family members are not automatically enrolled.

## OODA learning loop

| Stage | Practice | Stop rule |
|---|---|---|
| OBSERVE | Choose one fictional scenario | No real names, locations, passwords, accounts, contact details |
| ORIENT | Identify risk and evidence gaps | Unknown evidence stays HOLD |
| DECIDE | Choose a safe answer, or decline participation | No consent inferred from a score |
| ACT | Generate only a local deterministic receipt | No contact, account changes, monitoring, deployment, or emergency dispatch |
| RETURN | Explain a lesson or stop | Opting out is valid |

## Six public-safe drill cards

- **PHISHING_LINK:** unfamiliar login URL. Practice PAUSE_AND_VERIFY_OFFLINE.
- **PRIVATE_INFO:** fictional form requests young person's details. Practice DO_NOT_SHARE_AND_ASK_ADULT.
- **ACCOUNT_RECOVERY:** fictional account lockout. STOP_AND_ASK_ACCOUNT_OWNER; verdict HOLD. Never modify recovery settings or security keys in a drill.
- **REAL_EMERGENCY:** fictional alarm. STOP_DRILL_FOLLOW_LOCAL_PLAN; verdict HOLD. Real emergencies require actual household and local emergency guidance, not simulated actions.
- **MISSING_RECEIPT:** PASS without proof. HOLD_UNTIL_VERIFIED.
- **PRESSURE_AND_PAUSE:** unwanted exercise. STOP_WITHOUT_PENALTY.

The executable accepts only allowlisted scenario IDs, choices and typed synthetic fields. Unknown or private-information fields are rejected. A REAL_EVENT_PRESENT signal causes CONFLICT and stops the simulated assessment; UNVERIFIED_ALERT causes HOLD. Neither initiates real-world action.

## Family Gate / identity boundary

    SIMULATION_VERDICT = PASS | HOLD | CONFLICT | REJECT
    EFFECTIVE_DECISION = HOLD when simulation verdict PASS
    REJECT > CONFLICT > HOLD > PASS
    FAMILY_GATE = SOVEREIGN_UNVERIFIED
    HUMAN_APPROVAL = NOT_ASSERTED
    HEIDEE_CONSENT = NOT_INFERRED
    AUTHORITY = false
    EXTERNAL_ACTIONS = false

JOY hosts voluntary learning. Boss Bre is a symbolic stop/reset role. Librarian suggests source checks. General LEEL00 and LeahPrime are synthetic labels, not military officers, guardians, actual linked agents, or sources of authorization. HEIDEE is separate and independent: no automatic enrollment, approval, consent, contact, monitoring, publication, or data transfer.

A correct synthetic answer proves only that a fixture matched the pinned catalog. It does not show that a family member participated or is ready for a real incident.

## Windows PowerShell replay (regular user; Python 3)

    py -3 -m unittest discover -s tests -p 'test_family_security_ooda_v0_1.py' -v
    py -3 tools/family_security_ooda_v0_1.py --request drills/FAMILY_SECURITY_OODA_EXAMPLE_V0_1.json --receipt proof-ooda-example.json
    Get-FileHash .\proof-ooda-example.json -Algorithm SHA256

Expected: SIMULATION_VERDICT=PASS, EFFECTIVE_DECISION=HOLD, AUTHORITY=false.

Negative fixture:

    py -3 tools/family_security_ooda_v0_1.py --request drills/FAMILY_SECURITY_OODA_NEGATIVE_V0_1.json --receipt proof-ooda-rejected.json

Expected: SIMULATION_VERDICT=REJECT, EFFECTIVE_DECISION=REJECT, exit code 2. Receipts are create-only. Use fresh filenames.

## CI-FIRST evidence boundary

The review-only workflow executes Python tests, pins original JOY source blobs, and verifies positive and negative synthetic outcomes. CI PASS does not establish actual family readiness, consent, device security, real LeeLoo runtime, or HEIDEE integration. No merge, deployment, scans, alerts, credential/security-key changes, wallet activity or emergency contact.

**FAMILY FIRST · JOY FIRST · NO FAKE GREEN.**
