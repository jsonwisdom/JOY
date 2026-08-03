# CMP-WH v0.1 Conformance Runner

This directory implements the execution layer for the conceptual Civic Mirror Protocol schema bundle.

## Boundary

```text
OFFICIAL_AFFILIATION          = NONE
GOVERNMENT_AUTHORITY_CREATED  = FALSE
EXECUTION_AUTHORITY           = FALSE
VALIDATOR_REPORTS_ELIGIBILITY = TRUE
VALIDATOR_GRANTS_AUTHORITY     = FALSE
```

The runner is fail-closed. Missing fixtures, validators, implementation metadata, or independent replay attestations produce `BLOCKED` or `FAIL`, never a synthetic pass.

## Layout

- `runner.py` — reference manifest runner and report generator
- `suite.json` — 60-test conformance manifest
- `fixtures/` — materialized test inputs
- `implementation_metadata/` — reproducibility metadata for independent implementations
- `reports/` — generated reports; no report authorizes schema freeze or OpenAPI generation

## Execution

```bash
python systems/whitehouse/conformance/runner.py \
  --suite systems/whitehouse/conformance/suite.json \
  --fixtures systems/whitehouse/conformance/fixtures \
  --report systems/whitehouse/conformance/reports/CMP-WH-CONFORMANCE-REPORT-000001.json
```

Until all validators and fixtures are implemented, the expected result is fail-closed with `conformance_passed = false`.
