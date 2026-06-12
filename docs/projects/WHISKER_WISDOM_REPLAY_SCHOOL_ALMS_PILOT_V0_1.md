# Whisker Wisdom — Replay School ALMS Pilot V0.1

Timestamp: 2026-06-12 America/Chicago
Repository: jsonwisdom/JOY
Operator: Jay Wisdom
Public Names: jaywisdom.eth / jaywisdom.base.eth
Project Lane: WHISKER_WISDOM
Mode: REPLAY_SCHOOL_WITH_PAY
Authority: false
No Fake Green: true

## Purpose

Build a joyful, simple, replayable pilot for elder engagement using friendly kitten content, family photos, easy video calls, and ALMS-style activity logging.

This project is about daily joy, familiar faces, and gentle engagement. It is not a medical device, not a cure, and not a substitute for clinicians, caregivers, family, or professional care.

## Explain It Like Someone Is Six

Some grandmas and grandpas feel lonely or confused sometimes.

A helper computer can show them a kitten, a family face, a song, or a simple button that says: Tap for purr.

The computer does not replace people.
It just helps make one small happy moment easier to find.

GitHub is the project notebook.
Metadata is the label on each page.
Replay School teaches helpers how to build, check, and improve the notebook.

## Project Frame

```text
Massive Audience — families, caregivers, senior centers, Facebook groups
Massive Meta — video calls, reels, Quest pass-through, simple wake screens
Massive Purpose — daily joy and familiar faces for elders
Massive Relief — engagement, reminiscence, calm routines, not treatment
```

## Product Name

Working name: Whisker Wisdom

Alternate names:

- Kitty Krew MN
- Purr Purpose Collective
- Meow Memory Mob
- 9 Lives Ops
- Grandma Mode

## Dell Computers For Boomers

Pilot bundle:

- Dell desktop or all-in-one computer
- Large display
- Webcam with privacy shutter
- Loud, clear speakers
- One-click desktop launcher
- Giant Call Kitty icon
- High contrast interface
- 48pt text mode
- Auto-updates during overnight quiet hours
- No password prompts for the daily experience
- Staff-controlled admin settings

## Grandma Mode

```json
{
  "mode": "GRANDMA_MODE",
  "font_size": "48pt",
  "contrast": "high",
  "buttons": "large",
  "daily_prompt": "Tap for purr",
  "video_call": "one_click",
  "admin_controlled": true,
  "medical_claims": false
}
```

## ALMS Integration

ALMS is treated here as an Assisted Living Management System layer.

Integration ideas:

- Scheduled kitty visits as resident activities
- Staff-approved reminder copy
- Engagement pings with no PHI
- Calendar activity logging
- Family content queue
- Simple dashboard: tapped, watched, called, skipped
- Optional staff review before content appears

## Privacy Boundary

Do not collect health diagnoses, medical notes, or private clinical details in the engagement dashboard.

Use low-risk engagement metadata only:

```json
{
  "resident_id": "local_internal_id_only",
  "activity": "kitty_visit",
  "timestamp": "YYYY-MM-DDTHH:MM:SS",
  "duration_seconds": 0,
  "button_pressed": "tap_for_purr | call_family | skip",
  "mood_claim": null,
  "phi_collected": false
}
```

## Replay With Pay Worker Model

Workers make the system better by producing clean tasks.

```text
Scout — finds senior centers, family groups, and pilot partners
Designer — makes big-button screens
Builder — creates the desktop launcher
Content Helper — prepares kitten and family-safe content
ALMS Connector — maps activities into schedule/log format
Privacy Checker — removes PHI risk
Tester — watches whether a six-year-old and a boomer can use it
Explainer — writes simple instructions
Verifier — checks that another worker can replay the setup
```

## Worker Metadata

Every task should produce metadata.

```json
{
  "task_id": "WW_###",
  "worker_role": "",
  "artifact_path": "",
  "source_or_input": "",
  "observed_date": "YYYY-MM-DD",
  "claim_made": false,
  "medical_claim": false,
  "phi_collected": false,
  "state": "DRAFT | BUILT | TESTED | PRESERVED | REPLAYED",
  "authority": false
}
```

## Pilot Scope

Initial fixed-price pilot concept:

```json
{
  "pilot_name": "Whisker Wisdom 50-Unit Minnesota Pilot",
  "unit_count": 50,
  "target_sites": "Minnesota senior centers or assisted living partners",
  "hardware": "Dell computer bundle",
  "software": "Grandma Mode launcher",
  "content": "daily kitten and family-safe engagement loops",
  "integration": "ALMS-style activity scheduling and engagement logging",
  "medical_device": false,
  "clinical_claims": false
}
```

## OODA Loop

### Observe

Elders need simple, familiar, low-friction engagement.
Families already share photos and videos.
Caregivers need lightweight activity tools.
Computers are often too confusing.

### Orient

The product should not be a complex app. It should be a calm daily button.

### Decide

Build Whisker Wisdom as a joyful engagement layer first.

### Act

Create prototype screens, launcher spec, ALMS metadata schema, and pilot one-pager.

### Preserve

Commit docs, screenshots, specs, test notes, and worker task logs.

### Replay

A new worker should be able to recreate the pilot setup from the repo.

## Legal and Safety Guardrails

```text
Engagement support, not treatment.
Caregiver aid, not clinician replacement.
Reminder copy must be staff-approved.
No PHI in simple engagement logs.
No unsupported medical claims.
No dark patterns.
No confusing buttons.
No forced recording.
```

## Initial Build Tasks

```json
[
  {
    "task_id": "WW_001",
    "title": "Create Grandma Mode screen spec",
    "state": "DRAFT"
  },
  {
    "task_id": "WW_002",
    "title": "Create Dell hardware bundle checklist",
    "state": "DRAFT"
  },
  {
    "task_id": "WW_003",
    "title": "Create ALMS engagement metadata schema",
    "state": "DRAFT"
  },
  {
    "task_id": "WW_004",
    "title": "Create pilot one-pager for partners",
    "state": "DRAFT"
  },
  {
    "task_id": "WW_005",
    "title": "Create worker task board labels",
    "state": "DRAFT"
  }
]
```

## Closing State

```json
{
  "artifact": "WHISKER_WISDOM_REPLAY_SCHOOL_ALMS_PILOT_V0_1",
  "project": "Whisker Wisdom",
  "state": "CREATED",
  "mode": "REPLAY_SCHOOL_WITH_PAY",
  "operator": "Jay Wisdom",
  "authority": false,
  "medical_claims": false,
  "phi_collected": false,
  "no_fake_green": true
}
```

Make work fun again. Build small. Test gently. Replay clean.
