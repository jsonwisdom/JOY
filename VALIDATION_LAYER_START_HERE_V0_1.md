# Validation Layer Start Here V0.1

Project: `jaywisdom.base.eth`  
Root repo: `jsonwisdom/JOY`  
Mode: public repo validation  
Authority: false  
No fake green: true

The discovery layer is no longer the main work. The next layer is validation.

## Run the verifier

From the repo root:

```bash
python3 tools/verify-this-repo.py --json
```

Expected result:

- JSON report is printed.
- `status` is `PASS` when required files exist and JSON parses.
- Any missing file or invalid JSON returns `FAIL`.

## GitHub Actions drill

Workflow path:

```text
.github/workflows/zero-trust-audit.yml
```

The workflow runs the verifier on push, pull request, and manual dispatch.

## Public audit game

Drill map:

```text
drills/ZERO_TRUST_PUBLIC_AUDIT_DRILLS_V0_1.json
```

Scoring:

- RED: visitor cannot verify.
- YELLOW: partial audit.
- GREEN: audit path works.
- DEEP GREEN: verifier run plus public feedback receipt.

## Audit memory

Audit log:

```text
AUDIT_LOG.md
```

Use it to record workflow passes, public comments, and commit receipts.

## Rule

Do not call anything green unless a stranger can find it, run it, or verify it from public receipts.
