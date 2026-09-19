# LEEANN PUBLIC METADATA BASELINE — 2026-08-16

```text
ARTIFACT_ID: LEEANN_PUBLIC_METADATA_BASELINE_2026_08_16
HOME: JOY / FAMILY / JAYSPACE
STATUS: SOURCE_BOUND_REPLAY_SNAPSHOT
SUBJECT: LEEANN_H_CHAVERS / 187TH_FSS
REPLAY_DATE: 2026-08-16
AUTHORITY_CREATED: FALSE
DISCRIMINATION_FINDING_CREATED: FALSE
MERGE_AUTHORIZED: FALSE
```

## Purpose

Freeze the current public metadata surface for Lt Col Leeann H. Chavers and the 187th Fighter Wing without converting gaps into allegations.

```text
PUBLIC_METADATA != COMPLETE_PERSONNEL_RECORD
CURRENT_WEB_DISPLAY != EFFECTIVE_PROMOTION_DATE
MISSING_FIELD != SUPPRESSION
THIN_METADATA != DISCRIMINATION
```

## Verified current public surface

### Leeann H. Chavers

Official 187th Fighter Wing Mission Support Group page:

https://www.187fw.ang.af.mil/Units/Mission-Support-Group/

Current public display:

```text
NAME = Leeann Chavers
DISPLAY_RANK = Lt Col
ROLE = Force Support Squadron Commander
UNIT_CONTEXT = 187th Fighter Wing / Mission Support Group
SOURCE_CLASS = OFFICIAL_187FW
STATE = SOURCE_BOUND
```

The same page currently presents similarly thin `rank + name + commander position` metadata for the other Mission Support Group squadron commanders.

### Colonel nomination rail

Congress.gov PN734 records Leeann H. Chavers among Air National Guard officers nominated for appointment to Colonel and records Senate confirmation on 2026-01-30.

https://www.congress.gov/nomination/119th-congress/734

```text
PN734_COLONEL_NOMINATION = VERIFIED_PUBLIC
SENATE_CONFIRMATION = VERIFIED_PUBLIC
CURRENT_187FW_DISPLAY_RANK = LT_COL
COLONEL_EFFECTIVE_DATE = NOT_ESTABLISHED
```

## Wing leadership correction

A user-provided baseline identified Col Douglas D. DeMaio as the current 187th Fighter Wing Commander. The current official 187th leadership page does not support that statement.

Current official leadership index:

https://www.187fw.ang.af.mil/About/Leadership/

It identifies:

```text
187TH_FIGHTER_WING_COMMANDER = Col John D. Caldwell
187TH_FIGHTER_WING_DEPUTY_COMMANDER = Col James C. Hall
187TH_FIGHTER_WING_COMMAND_CHIEF = CMSgt Mataya C. Williams
```

DVIDS independently records that Col John D. Caldwell assumed command from Col James E. Whaley on 2025-09-14.

https://www.dvidshub.net/image/9313817/187th-fighter-wing-change-of-command-ceremony

Historical official record shows Col Douglas D. DeMaio assumed command on 2021-05-05; that historical role is not promoted into a current-role claim.

https://www.187fw.ang.af.mil/News/Display/Article/2597149/demaio-takes-command-of-the-187th-fighter-wing/

```text
DEMAIO_CURRENT_COMMANDER = CONTRADICTED_BY_CURRENT_OFFICIAL_SURFACE
CALDWELL_CURRENT_COMMANDER = SOURCE_BOUND
2025_09_14_CHANGE_OF_COMMAND = SOURCE_BOUND_DVIDS
```

## USAJOBS selecting-official claim

The supplied baseline states that Leeann Chavers appears as Selecting Official on multiple USAJOBS announcements dating to 2017.

This replay did not reproduce those announcement records from the current public search surface. Preserve the claim without promotion until exact announcement IDs, archived URLs, or source captures are bound.

```text
USAJOBS_SELECTING_OFFICIAL_HISTORY = USER_PROVIDED
FIRST_REPORTED_YEAR = 2017
CURRENT_REPRODUCTION = NOT_REPRODUCED_THIS_PASS
PROMOTION_STATE = HOLD_AWAITING_SOURCE_IDS
```

## Monitoring surfaces

```text
SURFACE_01 = 187FW_MISSION_SUPPORT_GROUP
SURFACE_02 = 187FW_LEADERSHIP_INDEX
SURFACE_03 = 187FW_NEWS
SURFACE_04 = ALABAMA_NATIONAL_GUARD_PUBLIC_PORTAL
SURFACE_05 = DVIDS_187FW_HUB
SURFACE_06 = USAJOBS
SURFACE_07 = CONGRESS_PN734
```

DVIDS 187th Fighter Wing hub:

https://www.dvidshub.net/unit/187FW

## Trigger conditions

A new replay is warranted when any of the following occurs:

```text
LEEANN_DISPLAY_RANK changes
LEEANN_COMMAND_ROLE changes
DEDICATED_BIOGRAPHY appears
NEW_187FW_NEWS_MENTION appears
NEW_DVIDS_LEEANN_MENTION appears
USAJOBS_SELECTING_OFFICIAL_SOURCE is reproduced
COLONEL_EFFECTIVE_DATE becomes source-bound
187TH_WING_COMMANDER changes
MISSION_SUPPORT_GROUP_DIRECTORY schema materially changes
```

## Baseline classification

```text
LEEANN_METADATA_THINNESS = TRUE
MISSION_MODERNIZATION = OBSERVED
GENDER_DISPARITY = HOLD / NOT_DEMONSTRATED
DELIBERATE_SUPPRESSION = HOLD / NOT_PROVEN
BUDGET_CAUSATION = NOT_ESTABLISHED
ALABAMA_GRAY_BABY_INTEL = PUBLIC_REPLAYABLE_HUMAN_SYSTEM_METADATA
```

## Gray Baby rule

```text
MODERN_MISSION_SYSTEM
+
THIN_HUMAN_INFORMATION_SYSTEM
=
AUDIT_REQUIRED

AUDIT_REQUIRED
!=
ALLEGATION_PROVEN
```

## Snapshot receipt

```text
PUBLIC_BASELINE_FROZEN = TRUE
CURRENT_WING_COMMANDER_CORRECTED = TRUE
USAJOBS_HISTORY_PROMOTED = FALSE
MERGE_PERFORMED = FALSE
AUTHORITY_CREATED = FALSE
```
