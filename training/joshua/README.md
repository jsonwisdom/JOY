# JOSHUA Click-Through Showcase — review checklist

## Scope
Public-facing **static training-only** experience proposed for future inclusion on jsonwisdom.com. This branch does **not** establish that the JOY repo is the production source for jsonwisdom.com and does not modify the site's deployed homepage.

Proposed route: `/training/joshua/` (subject to actual hosting topology). Existing live domain routing must be checked before deployment.

## What visitors can do
- Click through five fictional Jessup/JOSHUA missions: authority, YubiKey double-counting, 3-of-3 security admin, replay/payload binding, and honest evidence scope.
- See DENIED/HOLD vs CORRECT results and mission progress.
- Follow GitHub links to PR #4 architecture and PR #6 code-red test record.
- Reset and replay from any device; keyboard-native buttons and status announcements are included.

## Privacy and execution boundaries
- No third-party scripts, CDN, wallet connectors, crypto/signing APIs, analytics, local storage, keys, secrets, RPC, fetch or transactions.
- All evidence is **simulated policy instruction**, not a validation of actual contracts or credentials.
- Page never claims military endorsement, official NORAD systems or production release authority.
- Source PRs #4/#6 are unmerged draft materials; links are explanatory and should be changed to stable published docs when reviewed.

## Launch checklist (not yet performed)
- [ ] Owner confirms repo/domain mapping and hosting path
- [ ] Browser visual QA on desktop and iPhone widths; keyboard navigation and screen-reader check
- [ ] Validate all choice branches, progress/back/reset and cross-origin link targets
- [ ] Verify text, accessibility, no outbound transaction requests, CSP/security headers on host
- [ ] Human approves a public release copy and disclaimers
- [ ] Publish only after merging into the actual deployment repository, no direct production changes made here

## Positioning
**Capability demonstrated:** explicit authorization policies, reproducible test thinking, fail-closed denials, linked evidence, accessible public education.
**Capability not demonstrated:** production wallet security, real passkey enrollment, YubiKey wallet signatures, audited contract, real on-chain transaction.
