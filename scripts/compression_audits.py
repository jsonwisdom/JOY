#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, sys
from datetime import datetime, timezone

ROOT=pathlib.Path(__file__).resolve().parents[1]
CFG=ROOT/"docs/school-of-wisdom/compression-queries.wiki-atom-bomb-governor.v0.1.json"
HOME=ROOT/"index.html"
OUT=ROOT/"docs/school-of-wisdom/compression-audit.latest.json"

def sha256(p: pathlib.Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

cfg=json.loads(CFG.read_text(encoding="utf-8"))
home=HOME.read_text(encoding="utf-8")
checks=[]

for marker in cfg["required_homepage_markers"]:
    checks.append({"type":"marker","target":marker,"pass":marker in home})

for rel in cfg["required_paths"]:
    p=ROOT/rel
    checks.append({
        "type":"path",
        "target":rel,
        "pass":p.exists(),
        "sha256":sha256(p) if p.exists() and p.is_file() else None
    })

all_pass=all(x["pass"] for x in checks)
state="PASS_SCOPED" if all_pass else "HOLD"

receipt={
    "schema":"COMPRESSION_AUDIT_V0_1",
    "governor":cfg["governor"],
    "query_source":CFG.relative_to(ROOT).as_posix(),
    "run_at":datetime.now(timezone.utc).isoformat(),
    "homepage_sha256":sha256(HOME),
    "checks":checks,
    "result":state,
    "school_standard":"NOT_PASSED_GLOBAL",
    "authority_created":False,
    "no_fake_green":True,
    "autofix_scope":"GENERATED_STATUS_BLOCK_ONLY"
}
OUT.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")

start="<!-- COMPRESSION_AUDIT_STATUS_START -->"
end="<!-- COMPRESSION_AUDIT_STATUS_END -->"
block=f'''{start}
    <div id="compression-audit-status">
      <p><strong>CompressionAudit:</strong> <span class="audit-state">{state}</span></p>
      <p><strong>Governor:</strong> {cfg["governor"]}</p>
      <p><strong>Query source:</strong> CompressionQueries</p>
      <p><strong>Checks passed:</strong> {sum(1 for x in checks if x["pass"])} / {len(checks)}</p>
      <p><strong>School standard:</strong> NOT PASSED GLOBAL — work in progress</p>
      <p><strong>AutoFix scope:</strong> GENERATED STATUS BLOCK ONLY</p>
    </div>
    {end}'''

pattern=re.compile(re.escape(start)+r".*?"+re.escape(end),re.S)
if not pattern.search(home):
    print("HOLD: generated block markers missing",file=sys.stderr)
    sys.exit(2)

updated=pattern.sub(block,home,count=1)
if updated != home:
    HOME.write_text(updated,encoding="utf-8")

print(json.dumps({"result":state,"checks":len(checks),"passed":sum(1 for x in checks if x["pass"])}))
sys.exit(0 if all_pass else 1)
