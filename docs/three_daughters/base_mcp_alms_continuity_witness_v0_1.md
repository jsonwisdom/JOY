# Three-Daughters Base MCP ALMS Continuity Witness V0.1

## Doctrine Preamble V0.1

Binary systems decide too soon.  
Trinity systems preserve replay.

A claim must be allowed to stand.  
A challenge must be allowed to answer.  
A witness must be allowed to preserve context.

Memory precedes verdict.  
Continuity precedes closure.  
Authority remains false.

Installation semantics: non-binding, non-authoritative, non-executing, non-promotional, non-merging, non-review-advancing.

Status: DRAFT_CONTINUITY_EXTENSION
Authority: false
Mutation model: append-only
Membrane: HOLDS

## Purpose

This document binds `JOY_ALMS_BASE_MCP_PLUGIN_V0_1` to the JOY family-continuity witness layer. It is a continuity extension only. It does not create a new witness doctrine and does not override existing JOY witness, receipt, or verification surfaces.

## Parent references

This extension must be read as a child of:

- `JOY Witness Protocol V0.1` / PR #5
- `JOY Receipt Schema V0.1` / PR #7
- `JOY Verification Record V0.1` / PR #9
- `JOY Repository Spec V0.1` / PR #10

## Three-daughters priority

```json
{
  "priority_1": "protect_daughters_first",
  "priority_2": "preserve_continuity_second",
  "priority_3": "expand_systems_third",
  "authority": false
}
```

The Base MCP ALMS plugin must preserve family-safe barriers before any technical expansion. No wallet, agent, plugin, or receipt surface may silently promote continuity records into truth claims or family authority.

## Plugin boundary

The plugin may prepare unsigned calldata for append-only receipts. It may not:

- hold custody
- sign for a daughter or family member
- execute without wallet approval
- require reputation stake for family witness records
- adjudicate family meaning
- decide truth
- rewrite prior records

## Allowed continuity use

The plugin may support:

- anchoring a continuity claim
- disputing a continuity claim
- witnessing a claim or dispute
- reading a receipt DAG for review

Every action remains receipt-level only.

## Truth boundary

```json
{
  "anchor_means": "a continuity claim was recorded by an address",
  "dispute_means": "a prior record was challenged by an address",
  "witness_means": "an address attached testimony or context",
  "does_not_mean": "truth, custody, family authority, adjudication, or universal verification",
  "authority": false
}
```

## Continuity invariant

```json
{
  "family_barriers": "PROTECTED_FIRST",
  "continuity": "PRESERVED_SECOND",
  "expansion": "THIRD_ONLY_AFTER_RECEIPTS",
  "mutation_model": "append_only",
  "wallet_role": "approval_boundary",
  "plugin_role": "untrusted_compiler",
  "truth_status": "NOT_ADJUDICATED_BY_PLUGIN",
  "authority": false,
  "membrane": "HOLDS"
}
```
