# JAY'S BOX D / GARBAGE PAIL STICKER GRAMMAR V0.1

OPERATOR: JAY
ARTIST: JAY
CREATIVE_DIRECTOR: JAY
CHATGPT_ROLE: RENDER_ASSIST_AUDIT
IMAGE_MODEL_ROLE: EXECUTION_SURFACE
AUTHORITY_CREATED: false
LICENSE_CLAIM: false
OWNERSHIP_CLAIM_OVER_GPK_OR_TOPPS: false
STYLE_REFERENCE_ONLY: true

## Root Object Rule

When JAY asks for a Garbage Pail / GPK-style / Box D card or sticker, the default object is a SINGLE PEELABLE STICKER FRONT.

STICKER_CARD != POSTER
STICKER_CARD != MAGAZINE_COVER
STICKER_CARD != DASHBOARD
STICKER_CARD != CHART
STICKER_CARD != MULTI_PANEL

A poster, cover, dashboard, or other editorial object requires an explicit separate request.

## Front Grammar

- Off-white or white card stock wider than the peelable sticker area.
- A visible die-cut line surrounds the sticker art.
- Use an original JAY/Box D house banner such as BOX D PRESS. Do not use the Garbage Pail Kids or Topps logo.
- One card number in a fixed corner position.
- One PEEL HERE diamond in a fixed position.
- One focal character.
- Exaggerated head / caricature scale.
- One predicament.
- One primary prop.
- The art carries the gag. Extra props may not explain the joke.
- One bottom name pill is the only caption.
- The name pill is yellow unless JAY explicitly changes the house grammar.
- Painted cartoon treatment, black contour, soft airbrushed color.
- Not photorealistic.
- No charts, audit dashboards, explainer panels, headline stacks, subheads, or slogan bars on the sticker front.

ONE_CHARACTER + ONE_PREDICAMENT + ONE_PROP + ONE_NAME = FRONT

## Twin Rule

BOX_D_TWIN_RULE:
  painting_same: TRUE
  crop_same: TRUE
  costume_same: TRUE
  prop_same: TRUE
  background_same: TRUE
  die_cut_same: TRUE
  banner_same: TRUE
  number_position_same: TRUE
  changes_allowed:
    - name_pill_text
    - number
  changes_forbidden:
    - painting
    - crop
    - costume
    - prop
    - background
    - die_cut
    - banner
    - number_position
  authority_created: FALSE

A legal a/b twin changes only:
1. name_pill_text
2. number

Same painting means same painting. A visually similar redraw is not proof of twin identity.

## Current Twin Fixture

freeze_painting: pQhn3
candidate_edit: UD543
emfg4: NOT_A_TWIN
UD543: CANDIDATE_EDIT
UD543_PIXEL_IDENTITY_PROOF: NOT_ESTABLISHED

## Backs

The back is a second object.

FRONT_APPROVED != BACK_APPROVED
FRONT_GRAMMAR != BACK_GRAMMAR

Do not invent a puzzle, certificate, award, stats panel, or other back until JAY requests the back object.

## Satire / Public-Figure Boundary

Satire may caricature a public figure, but the card may not silently turn a joke into a factual claim.

SATIRE != CANDIDACY
SATIRE != ENDORSEMENT
SATIRE != ELECTION_STATUS
SATIRE != FINDING

If the subject is a real public figure, keep the joke visibly satirical and do not add official seals or branding that imply government authorship.

## Attribution

JAY is the artist and creative director.

ChatGPT and image-generation systems are tools used to render, inspect, compare, and audit JAY's requested object.

TOOL_ASSISTANCE != ARTIST_AUTHORSHIP

## Mandatory Preflight

Before rendering:
1. Load this grammar.
2. Parse JAY's requested subject.
3. Set the requested object class.
4. Reduce the front to one focal character, one predicament, one primary prop, and one name.
5. Confirm house branding and prohibit GPK/Topps marks.
6. Render only after the object boundary passes.

If this grammar cannot be loaded, HOLD. Do not substitute a generic "GPK aesthetic."

## Mandatory Postflight

After rendering, ask first:

DID_THE_OUTPUT_PRESERVE_THE_REQUESTED_UNIT?

Then test:
- subject_match
- sticker_card_object_match
- one_character
- one_predicament
- one_primary_prop
- one_name_pill
- die_cut_present
- house_banner_present
- number_position_valid
- peel_here_present
- no_forbidden_brand_transfer
- no_explainer_clutter

If any required gate fails:

DISPOSITION = REJECT_AS_FACTORY_OUTPUT

The image may still be preserved as a useful art artifact, but it is not counted as a successful sticker card.

If all required gates pass:

DISPOSITION = READY_FOR_HUMAN_REVIEW

No automatic publication, mint, promotion, or canonization follows.

## Anti-Fake-Green Rules

GOOD_IMAGE != CORRECT_OBJECT
SATIRE_MATCH != FORMAT_MATCH
SUBJECT_MATCH != FACTORY_MATCH
VISUAL_SUCCESS != REQUEST_SUCCESS
SIMILAR_PAINTING != TWIN_IDENTITY
CANDIDATE_EDIT != PIXEL_IDENTITY_PROOF
READY_FOR_HUMAN_REVIEW != PUBLICATION_APPROVED
