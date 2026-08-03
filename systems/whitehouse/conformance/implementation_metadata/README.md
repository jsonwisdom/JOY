# Independent Implementation Metadata

`CMP-CT-0034` requires metadata for each independent implementation.

Required fields:

```text
implementation_name
implementation_version
codebase_digest
runtime_platform
operating_system
canonicalization_library_name
canonicalization_library_version
dependency_lockfile_digest
```

Missing metadata does not change digest-comparison semantics, but it sets:

```text
metadata_complete          = false
eligible_for_human_freeze  = false
```

The two implementations must use different codebases and may not share a redaction engine or rule evaluator. Shared fixtures are permitted.
