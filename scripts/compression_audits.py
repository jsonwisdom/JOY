#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, sys
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = ROOT / "docs/school-of-wisdom/compression-queries.wiki-atom-bomb-governor.v0.2.json"
CENTER = ROOT / "docs/school-of-wisdom/center-object.v0.2.json"
HOME = ROOT / "index.html"
AUDIT = ROOT / "docs/school-of-wisdom/compression-audit.latest.json"
SCAFFOLD = ROOT / "docs/school-of-wisdom/homepage-scaffold.latest.json"

def sha256(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

cfg = json.loads(CFG.read_text(encoding="utf-8"))
center = json.loads(CENTER.read_text(encoding="utf-8"))
home = HOME.read_text(encoding="utf-8")

checks = []
for q in cfg["critical_queries"]:
    target = q["target"]
    if q["check"] == "marker":
        passed = target in home
        detail = {"marker": target}
    elif q["check"] == "path":
        p = ROOT / target
        passed = p.exists()
        detail = {"path": target, "sha256": sha256(p) if passed and p.is_file() else None}
    else:
        passed = False
        detail = {"error": "unsupported query check"}
    checks.append({
        "id": q["id"],
        "question": q["question"],
        "check": q["check"],
        "target": target,
        "pass": passed,
        **detail
    })

passed = sum(1 for x in checks if x["pass"])
total = len(checks)
failed = [x for x in checks if not x["pass"]]
pressure = round((passed / total) * 100, 1) if total else 0.0
snapped = bool(failed)
compression_state = "SNAPPED" if snapped else "COMPRESSED_STABLE"

repair_queue = [
    {
        "query_id": x["id"],
        "question": x["question"],
        "target": x["target"],
        "state": "REPAIR_REQUIRED"
    }
    for x in failed
]

now = datetime.now(timezone.utc).isoformat()

receipt = {
    "schema": "COMPRESSION_AUDIT_V0_2",
    "governor": cfg["governor"],
    "center_object": cfg["center_object"],
    "query_source": CFG.relative_to(ROOT).as_posix(),
    "run_at": now,
    "homepage_sha256_before": sha256(HOME),
    "center_object_sha256": sha256(CENTER),
    "queries_total": total,
    "queries_passed": passed,
    "query_pressure_percent": pressure,
    "compression_state": compression_state,
    "snap_state": "SNAPPED" if snapped else "NOT_SNAPPED",
    "failed_queries": [x["id"] for x in failed],
    "checks": checks,
    "school_standard": "NOT_PASSED_GLOBAL",
    "authority_created": False,
    "no_fake_green": True,
    "autofix_scope": cfg["autofix_scope"],
    "forbidden_autofix": cfg["forbidden_autofix"]
}
AUDIT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

scaffold = {
    "schema": "SCHOOL_OF_WISDOM_HOMEPAGE_SCAFFOLD_V0_2",
    "generated_at": now,
    "center_object": center["object_id"],
    "center_object_sha256": sha256(CENTER),
    "compression_state": compression_state,
    "snap_state": "SNAPPED" if snapped else "NOT_SNAPPED",
    "query_pressure_percent": pressure,
    "passed_queries": passed,
    "total_queries": total,
    "repair_queue": repair_queue,
    "homepage_features": cfg["homepage_features"],
    "sections": [
        "hero",
        "freshness",
        "query-pressure",
        "claim-proof-play-repair",
        "school-standard-joke",
        "compression-audit",
        "scaffold-matrix",
        "repair-queue"
    ],
    "authority_created": False,
    "no_fake_green": True
}
SCAFFOLD.write_text(json.dumps(scaffold, indent=2) + "\n", encoding="utf-8")

start = "<!-- COMPRESSION_AUDIT_STATUS_START -->"
end = "<!-- COMPRESSION_AUDIT_STATUS_END -->"
repair_html = "".join(
    f"<li><strong>{item['query_id']}</strong> — {item['question']}</li>"
    for item in repair_queue
) or "<li>None in this scoped query set.</li>"

block = f'''{start}
    <div id="compression-audit-status">
      <p><strong>CompressionAudit:</strong> <span class="audit-state">{compression_state}</span></p>
      <p><strong>Governor:</strong> {cfg["governor"]}</p>
      <p><strong>Query source:</strong> CompressionQueries V0.2</p>
      <p><strong>Query pressure:</strong> {pressure}% ({passed} / {total})</p>
      <p><strong>Snap state:</strong> {"SNAPPED — repair queue opened" if snapped else "NOT SNAPPED — center object survived current queries"}</p>
      <p><strong>School standard:</strong> NOT PASSED GLOBAL — work in progress</p>
      <p><strong>AutoFix scope:</strong> generated status + scaffold + audit only</p>
      <div class="pressure-track"><span style="width:{pressure}%"></span></div>
      <ul class="repair-list">{repair_html}</ul>
    </div>
    {end}'''

pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
if not pattern.search(home):
    print("HOLD: generated compression block markers missing", file=sys.stderr)
    sys.exit(2)

updated = pattern.sub(block, home, count=1)
if updated != home:
    HOME.write_text(updated, encoding="utf-8")

receipt["homepage_sha256_after"] = sha256(HOME)
AUDIT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "compression_state": compression_state,
    "snap_state": receipt["snap_state"],
    "queries_passed": passed,
    "queries_total": total,
    "query_pressure_percent": pressure,
    "repairs": len(repair_queue)
}))
sys.exit(1 if snapped else 0)
