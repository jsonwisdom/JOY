# Receipt Noise Suppression Layer V0.1

**Status:** DRAFT  
**Authority:** false (pattern only)  
**Inspiration:** DSF-DETR (End-to-End SAR Ship Detection via Spatial-Frequency State Space Modeling and Dynamic Attention)  
**Purpose:** Separate evidence-bearing signals from background narrative clutter before classification in audit and verification systems.

---

## Core Problem

Most verification systems classify first (e.g., "claim is true/false") and only then look for supporting evidence. This reverses the correct order and allows narrative noise to consume verification budget.

Institutional responses often contain:
- Speckle (minor inconsistencies, irrelevant detail)
- Clutter (background narrative, press releases)
- False targets (claims without receipts)

**A noise-resistant verification system must separate signal from noise before any authority decision.**

---

## Architectural Pattern (from DSF-DETR)

DSF-DETR for SAR ship detection uses:

1. **Dual-branch feature extraction** (spatial + frequency)
2. **State space modeling** for long-range dependencies
3. **Dynamic attention** to focus compute on likely targets
4. **Reparameterization** for efficient deployment

Mapping to audit / readiness verification:

| DSF-DETR concept | ALMS / JOY mapping |
|-----------------|--------------------|
| Speckle / clutter | Narrative noise, false claims, weak signals |
| Ship target | Verifiable event / receipt |
| Spatial branch | Direct observable evidence (commit hashes, timestamps, delivery receipts) |
| Frequency branch | Pattern-level anomaly detection (recurring institutional behavior) |
| SSM / Mamba | Long-range replay memory of past audit interactions |
| CADA (dynamic attention) | Spend verification budget only on high-anomaly or high-dispute claims |
| ERFP (reparameterization) | Train rich, multi-source audit model -> collapse to lightweight public validator |
| NMS-free DETR | No manual post-hoc authority override |

---

## Proposed Layer: Receipt Noise Suppression Layer V0.1

```json
{
  "artifact": "RECEIPT_NOISE_SUPPRESSION_LAYER_V0_1",
  "modules": {
    "spatial_receipt_branch": {
      "function": "Checks direct observable facts",
      "inputs": ["commit hash", "timestamp", "delivery receipt", "screenshot", "submission ID"],
      "output": "PRIMARY_EVIDENCE_PRESENT / ABSENT"
    },
    "frequency_pattern_branch": {
      "function": "Checks recurring anomaly patterns from institutional memory",
      "inputs": ["past response history", "known evasion signatures", "referral loops", "press_release_only patterns"],
      "output": "PATTERN_MATCH_CONFIDENCE (0.0-1.0)"
    },
    "state_space_memory": {
      "function": "Models long-range institutional behavior across multiple audit attempts",
      "implementation": "Key-value store of (institution, domain) -> response signature",
      "update_rule": "Append on each interaction"
    },
    "dynamic_attention_gate": {
      "function": "Prioritizes records with high dispute density or anomaly score",
      "formula": "attention_budget proportional_to (1 - pattern_confidence) * (dispute_flag + 1)",
      "effect": "Reduce compute on routine, low-anomaly responses"
    },
    "deployment_compression": {
      "function": "Turns rich review model into lightweight public validator",
      "method": "Pre-compute frequency branch weights; deploy only spatial branch + threshold",
      "example": "GitHub receipt + issue tracker as public lightweight checker"
    }
  },
  "decision_order": [
    "observe",
    "separate_signal_from_noise",
    "allocate_attention",
    "classify"
  ],
  "authority": false
}
```

---

## Invariant

No classification before separation. No authority before receipt.

Tertiary evidence (press releases, narratives, claims) cannot bypass the noise suppression layer. They enter only the frequency branch for pattern matching, never the spatial branch for direct evidence.

---

## Deployment Example: TX DIR Quantum Readiness Audit

The TX DIR audit packet (`docs/audits/TX_DIR_QUANTUM_READINESS_AUDIT_REQUEST_PACKET_V0_1.md`) will be extended with a frequency branch memory:

```json
{
  "frequency_branch_memory": {
    "source": "public PIA response history (Texas DIR)",
    "pattern_signatures": [
      "delayed_response_gt_60d",
      "referral_loop",
      "press_release_only",
      "no_primary_evidence_produced"
    ],
    "attention_multiplier": 2.0,
    "authority": false
  }
}
```

This ensures that if DIR has a known pattern of non-response or narrative-only replies, the audit system allocates more verification attention to the request, not less.

---

## Future Leaves

- ALMS (Accountable Large Model System)
- Computer Wisdom / JOY core
- Minnesota MMB audits
- Quantum-readiness institutional assessments
- Any noisy verification environment

---

## Reference

Inspired by:
DSF-DETR: End-to-End SAR Ship Detection via Spatial-Frequency State Space Modeling and Dynamic Attention
(Paper title; original domain: Synthetic Aperture Radar ship detection)

---

This pattern is authority-false. It does not assert truth. It asserts an architectural ordering for noise-resistant verification.
