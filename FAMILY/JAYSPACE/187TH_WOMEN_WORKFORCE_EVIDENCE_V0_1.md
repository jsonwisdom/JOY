# 187TH WOMEN WORKFORCE EVIDENCE v0.1

```text
ARTIFACT_ID: 187TH_WOMEN_WORKFORCE_EVIDENCE_V0_1
HOME: JOY / FAMILY / JAYSPACE
REPLAY_DATE: 2026-08-16
METHOD: PUBLIC_SOURCE_BOUND_COHORT_SEED
STATUS: INVESTIGATION_OPEN
AUTHORITY_CREATED: FALSE
DISCRIMINATION_FINDING_CREATED: FALSE
```

## Purpose

Move the 187th investigation from one-person narrative to a cohort method.

```text
LEEANN_CASE != POPULATION
PUBLICLY_DOCUMENTED_WOMEN != ALL_187TH_WOMEN
NAMED_PUBLIC_CASES != CURRENT_FEMALE_HEADCOUNT
PUBLIC_WEBSITE_STALENESS != INTERNAL_PERSONNEL_RECORD_FAILURE
SHARED_BAD_SYSTEM != SEX_DISCRIMINATION
```

The goal is to determine whether measurable administrative or information-system friction produces different career outcomes for women after controlling for rank, AFSC/occupation, status, and era.

## Current denominator state

No public source located in this pass provides a current 187th Fighter Wing workforce headcount broken out by sex together with rank, AFSC, status, record completeness, correction delays, promotion, PME, awards, assignment, or retention outcomes.

A historical 2015 official 187th article said the wing consisted of more than 1,500 Airmen. That is not a current denominator and contains no sex breakout.

Source:
https://www.187fw.ang.af.mil/News/Display/Article/870016/alabama-air-national-guard-col-randal-efferson-assumes-command-of-187th-fighter/

```text
CURRENT_187TH_TOTAL_HEADCOUNT = NOT_SOURCE_BOUND_THIS_PASS
CURRENT_187TH_FEMALE_HEADCOUNT = UNKNOWN
CURRENT_187TH_FEMALE_PERCENTAGE = UNKNOWN
CURRENT_OUTCOME_DATA_BY_SEX = NOT_LOCATED
```

## Publicly documented women — cohort seed

These are examples demonstrating role breadth. They are not a complete roster and must not be used as the denominator.

### Leeann H. Chavers

- Current public role: Lt Col, Commander, 187th Force Support Squadron.
- Woman classification: project/user-declared; not inferred from name.
- Public career metadata remains thin relative to wing-level biography pages.

Source:
https://www.187fw.ang.af.mil/Units/Mission-Support-Group/

### CMSgt Mataya C. Williams

- Current 187th leadership page lists Williams as Wing Command Chief.
- Her official biography uses she/her and documents service at the 187th since 2004 across logistics, information management, civil engineering, and senior enlisted leadership.
- Biography includes education, assignments, awards, and effective promotion dates.

Sources:
https://www.187fw.ang.af.mil/About/Leadership/
https://www.187fw.ang.af.mil/About/Biographies/Display/Article/2771873/mataya-c-williams/

### CMSgt Bernadette Hollinger

- Official Air Force article identifies Hollinger as the first female Command Chief of the 187th Fighter Wing in 2019.
- Alabama National Guard biography states she joined the 187th in 1990, served in information management, first sergeant and personnel roles, and later served as 187th Command Chief before State Command Chief duties.

Sources:
https://www.wpafb.af.mil/News/Article-Display/Article/1791171/trailblazer-arrives-at-air-national-guard/
https://al.ng.mil/About-Us/Leadership/Bio-Article-View/article/2706425/command-chief-master-sergeant-bernadette-hollinger/

### Jessica Wilkes

- DVIDS identifies Wilkes as a 187th Aircraft Maintenance Squadron crew chief and explicitly states she was one of two female crew chiefs participating in Red Flag 17-2 in 2017.

Source:
https://www.dvidshub.net/image/3200138/187th-fighter-wing-aircrew-and-maintainers-prepare-night-flight-during-red-flag-17-2

### TSgt Ivey Sweeney

- Official 187th article identifies Sweeney as the 187th Communications Flight knowledge operations manager and recipient of the 2018 Alabama National Guard Woman of the Year award.

Source:
https://www.187fw.ang.af.mil/News/Article/1855800/sweeney-named-2018-al-national-guard-woman-of-the-year/

### Lt Col Amy Z. Mundell / Col Tara D. McKennie

- Official 187th article states Mundell assumed command of the 187th Medical Group from McKennie on 2021-05-15.
- The article uses she/her for Mundell and records McKennie's transition to Alabama National Guard Joint Force Headquarters.

Source:
https://www.187fw.ang.af.mil/News/Article/2650774/mundell-assumes-command-of-187th-medical-group/

## Demonstrated public record freshness defect

The current public 187th Medical Group page still displays:

```text
Col Tara D. Mckennie, Medical Group Commander
```

Source:
https://www.187fw.ang.af.mil/Units/Medical-Group/

This conflicts with the official 2021 187th article stating Amy Z. Mundell assumed command from Tara D. McKennie. It is further inconsistent with the National Guard biography that records Brig. Gen. Tara D. McKennie as retired effective 2025-06-01.

Source:
https://www.nationalguard.mil/portals/31/Features/ngbgomo/bio/3/3887.html

Classification:

```text
187TH_PUBLIC_WORKFORCE_PAGE_STALENESS = DEMONSTRATED
MEDICAL_GROUP_COMMANDER_PUBLIC_CONFLICT = DEMONSTRATED
INTERNAL_PERSONNEL_RECORD_INACCURACY = NOT_ESTABLISHED
CAUSE = UNKNOWN
SEX_CAUSATION = NOT_ESTABLISHED
CAREER_HARM = NOT_ESTABLISHED
```

This is a measurable Gray Baby target because an official unit page and official personnel-transition records disagree about a command role.

## Human HR technology context

The Air Force has publicly described ongoing HR-IT modernization rather than a static legacy-only environment. In 2024 it described eWAPS and myFSS as HR transformation efforts and stated that transforming HR information technology underpins the HR enterprise. Air Reserve Personnel Center materials describe migration from myPers/vPC capabilities toward myFSS and MyVector.

Sources:
https://www.af.mil/News/Article-Display/Article/3660220/waps-testing-going-digital-in-february-2024/
https://www.arpc.afrc.af.mil/Services/Digital-Transformation/

Therefore:

```text
AIR_FORCE_HR_IT_MODERNIZATION = OBSERVED
187TH_LOCAL_SYSTEM_AGE_2002 = NOT_ESTABLISHED
187TH_INTERNAL_HR_SYSTEM_FAILURE = NOT_ESTABLISHED
PUBLIC_WEBSITE_STALENESS = DEMONSTRATED
```

## National women-workforce context

GAO-20-61 Recommendation 5 remains open. GAO states that the Department of the Air Force still needs a plan with clearly defined goals, performance measures, and timeframes for female active-duty recruitment and retention, and that GAO requested another update in February 2026.

Source:
https://www.gao.gov/products/gao-20-61

This is national active-duty context, not a direct statistical comparator for one Air National Guard wing.

```text
GAO_NATIONAL_CONTEXT != 187TH_LOCAL_FINDING
ACTIVE_DUTY_DATA != ANG_UNIT_DATA
```

## Cohort protocol v0.1

For every public case, capture independently:

```text
PERSON_ID
SEX_EVIDENCE_CLASS
CURRENT_OR_HISTORICAL
RANK
AFSC_OR_OCCUPATION
UNIT
STATUS_IF_PUBLIC
ROLE_START
ROLE_END
DIRECTORY_ENTRY
DEDICATED_BIOGRAPHY
NEWS_FEATURES
EDUCATION
PME
ASSIGNMENTS
AWARDS
PROMOTION_HISTORY
EFFECTIVE_PROMOTION_DATES
NAME_VARIANTS
SOURCE_DATE
SOURCE_FRESHNESS
PUBLIC_RECORD_CONFLICTS
CORRECTION_REQUEST_VISIBLE
CORRECTION_DELAY_VISIBLE
PERSONNEL_SYSTEM_NAMED
TECH_FRICTION_SOURCE
OUTCOME_ASSERTED
OUTCOME_VERIFIED
```

Comparison gate:

```text
WOMAN_CASE
↓
MATCH MAN — SAME RANK / AFSC OR OCCUPATION / STATUS / ERA
↓
COMPARE RECORD COMPLETENESS
↓
COMPARE CORRECTION DELAY
↓
COMPARE PME / AWARDS / PROMOTION / ASSIGNMENT / RETENTION OUTCOMES
↓
TEST WHETHER DELTA PERSISTS
```

## Current investigation state

```text
PUBLIC_WOMEN_ROLE_BREADTH = DEMONSTRATED
CURRENT_FEMALE_DENOMINATOR = UNKNOWN
CURRENT_MALE_DENOMINATOR = UNKNOWN
PUBLIC_RECORD_STALENESS = DEMONSTRATED
LEEANN_ONLY_ANOMALY = NOT_DEMONSTRATED
GENDER_OUTCOME_DELTA = NOT_MEASURED
DISPARATE_EFFECT = NOT_ESTABLISHED
DELIBERATE_SUPPRESSION = NOT_PROVEN
SHOCK_GLOVES = STORY / SATIRE / NO EVIDENCE
AUTHORITY_CREATED = FALSE
```

Maximum supported claim:

> Public records establish that women have served across multiple 187th career and leadership lanes and that at least one current 187th workforce webpage contains a demonstrably stale command assignment. Public sources located in this pass do not provide the current sex-disaggregated denominator or matched career-outcome data required to determine whether women experience systematically greater administrative or technology-related career friction.
