# Goblin Court MN Edition v0.1

**Author:** Jay Wisdom  
**Project lineage:** JOY → Jay → Computer Wisdom → Goblin Court MN Edition  
**Repository:** jsonwisdom/JOY  
**Status:** REBOOT_DRAFT  
**Authority:** false  
**Fraud status:** UNKNOWN  
**Crawler:** DISABLED  
**Polling:** DISABLED  
**Membrane:** HOLDS

---

## Purpose

Goblin Court MN Edition is a civic-replay surface for Minnesota public-record artifacts.

It exists to make records measurable before they become stories.

The court does not accuse.  
The court does not infer.  
The court does not promote anomaly into fraud.  
The court asks for receipts.

---

## Current Active Leaf

```json
{
  "leaf": "Leaf 005",
  "target": "Saint Cloud City Council June 2026 agenda PDF",
  "eid": "6508",
  "status": "WATCH",
  "mode": "DORMANT_HIGH_FIDELITY",
  "manual_trigger_required": true,
  "authority": false,
  "fraud_status": "UNKNOWN"
}
```

---

## Birth-Certificate Fields

Every public artifact must begin with five real values:

```json
{
  "source_url": null,
  "observed_at": null,
  "sha256": null,
  "file_name": null,
  "byte_size": null
}
```

Rules:

- No invented URL.
- No invented timestamp.
- No invented hash.
- No invented file name.
- No invented byte size.
- No crawler.
- No polling.
- No accusation.
- No ghost authority.

---

## Versioning Universe

| Event | Version move |
|---|---|
| No artifact observed | `v0.null` |
| Artifact first appears | `v1.birth` |
| Same URL, same hash | `v1.confirmed` |
| Same URL, changed hash | `v2.drift_detected` |
| Artifact disappears | `vX.absence_observed` |
| Independent verification | `verified_receipt` |

---

## MN Edition Player Rules

1. Observe only.
2. Measure before meaning.
3. Hash before narrative.
4. Preserve the receipt.
5. Keep authority false until verification.
6. Never convert association into guilt.
7. Never convert anomaly into fraud without adjudicated proof.

---

## Reboot Phrase

> Grab your joysticks, Minnesota.  
> Goblin Court MN Edition is awake, but Leaf 005 remains dormant.  
> No crawl. No claim. No drift.  
> Await the public artifact, then measure reality.

---

## Standing Operator Command

```text
Trigger Leaf 005 manual observation.
```

Until then:

```json
{
  "server": "LOCKED",
  "membrane": "HOLDS",
  "authority": false,
  "fraud_status": "UNKNOWN"
}
```
