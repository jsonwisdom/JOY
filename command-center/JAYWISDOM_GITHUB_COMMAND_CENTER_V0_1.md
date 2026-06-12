# JayWisdom GitHub Command Center V0.1

Purpose: give `jaywisdom.eth` / `jaywisdom.base.eth` one repo-native control room for public metadata, validation, feedback, and receipt-gated anchors.

Canonical root: `jsonwisdom/JOY`

Project identity:

- ENS: `jaywisdom.eth`
- Basename: `jaywisdom.base.eth`
- GitHub root: `jsonwisdom/JOY`
- Authority: `false`
- No fake green: `true`

## Command Center Panels

| Panel | Role | First action |
|---|---|---|
| Public Door | Show outsiders where to start | `PUBLIC_AUDIT_LOCATOR_INDEX_V0_1.md` |
| Validation | Run local and GitHub checks | `VALIDATION_LAYER_START_HERE_V0_1.md` |
| ALMS | Keep metadata aligned | `metadata/operation-vcr/OPERATION_VCR_ALMS_KEEPUP_V0_1.json` |
| State Lanes | Route public metadata lanes | `metadata/mn/`, `metadata/alms/` |
| Schemas | Define machine-readable packages | `schemas/` |
| Drills | Gamify public auditing | `drills/ZERO_TRUST_CIVIC_AUDIT_DRILLS_V0_1.md` |
| Issues | Collect public feedback | `.github/ISSUE_TEMPLATE/public-audit.yml` |

## Operating Loop

1. Intake a public artifact or claim.
2. Classify it as GREEN, YELLOW, or RED.
3. Record the repo path and commit SHA.
4. Validate JSON and required files.
5. Create or update the audit log.
6. Only then prepare optional EAS, IPFS, Zora, or Base anchors.

## Command Rules

- No receipt = no authority.
- GitHub commit first; external anchor second.
- Public metadata only by default.
- No private targeting, no secret collection, no fake attestation.
- Every outside claim must point to a visible file, issue, workflow, commit, or receipt.

## Starter Command

Use this command center before touching external anchors:

```bash
python3 tools/verify-this-repo.py --json
```

If it does not pass locally or in GitHub Actions, the system is not green.
