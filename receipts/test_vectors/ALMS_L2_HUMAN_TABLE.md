# ALMS L2 Human Transition Table v0.1

Authority remains false.

| From state | To state | Allowed | Required evidence | Meaning |
|---|---|---:|---|---|
| CLAIM | VERIFIED_RECEIPT | false | Missing RECEIPT_BACKED intermediate | Blocks silent authority promotion |
| OBSERVED | RECEIPT_BACKED | true | source_artifact_hash, receipt_id, observed_at, operator_signature_or_commit, authority_false | Observation has required receipt evidence |
| RECEIPT_BACKED | VERIFIED_RECEIPT | conditional | independent replay success, schema match, index match, root inclusion | Receipt survives replay check |
| ANY | AUTHORITY_TRUE | false | Not allowed in this spec | Keeps governance authority false |

## Closure rule

Issue #14 may close only after dual-environment replay evidence matches byte-for-byte.

Replay success proves L1 canonicalization, L2 determinism, and L5 replay. It does not grant authority.
