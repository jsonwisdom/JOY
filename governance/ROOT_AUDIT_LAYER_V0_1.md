# ROOT_AUDIT_LAYER_V0_1

## Purpose

Establish a zero-state audit gate for the JOY repository.

Every run begins by checking that required directories, files, and workflow definitions are present.

## Build Order

1. Directories
2. Files
3. YAML
4. Actions
5. Receipts
6. Witness
7. Activation

## Promotion States

- ZERO_STATE
- STRUCTURE_EXISTS
- FILES_EXIST
- YAML_DECLARED
- ACTIONS_EXECUTABLE
- WORKFLOW_OBSERVED
- WORKFLOW_GREEN
- WITNESS_READY
- ACTIVE_DRY
- ACTIVE_WITNESS

## Demotion Rules

- Missing required directory: ZERO_STATE
- Missing required file: STRUCTURE_EXISTS
- Empty workflow YAML: FILES_EXIST
- Failed audit script: WORKFLOW_OBSERVED
- Missing receipt: WORKFLOW_GREEN

## Boundary

This layer only checks repository structure. It does not approve any higher-level claim.

## Forward Declaration

Receipt emission, witness placeholders, executable-bit checks, and script hashing are reserved for later versions.
