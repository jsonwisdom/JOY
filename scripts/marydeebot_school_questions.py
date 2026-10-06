#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, re, sys
from datetime import datetime, timezone

ROOT=pathlib.Path(__file__).resolve().parents[1]
BOT=ROOT/"docs/school-of-wisdom/marydeebot.v0.1.json"
CHAPTER_DIR=ROOT/"docs/school-of-wisdom/questions"
STATUS=CHAPTER_DIR/"status.latest.json"

bot=json.loads(BOT.read_text(encoding="utf-8"))
required_sections=[
    "## 1. Question",
    "## 2. Story",
    "## 3. Lesson",
    "## 4. Game",
    "## 5. Receipt",
    "## 6. Replay",
    "## 7. Your Turn",
]
results=[]
for path in sorted(CHAPTER_DIR.glob("*.md")):
    text=path.read_text(encoding="utf-8")
    missing=[s for s in required_sections if s not in text]
    guardrails={
        "authority_false": bool(re.search(r"Authority:\s*false",text,re.I)),
        "no_fake_green": bool(re.search(r"No Fake Green:\s*true",text,re.I)),
        "optional_your_turn": "Optional." in text or "optional" in text.lower(),
        "tested_boundary": "PLAYTESTED_WITH_REAL_FAMILY = false" in text or "Tested With Real Family: false" in text,
    }
    passed=(not missing) and all(guardrails.values())
    results.append({
        "chapter":path.relative_to(ROOT).as_posix(),
        "seven_step_shape":not missing,
        "missing_sections":missing,
        "guardrails":guardrails,
        "pass":passed
    })

all_pass=bool(results) and all(x["pass"] for x in results)
status={
    "schema":"SCHOOL_OF_QUESTIONS_STATUS_V0_1",
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "marydeebot_id":bot["bot_id"],
    "bot_label":bot["bot_label"],
    "role":bot["role"],
    "chapters_checked":len(results),
    "chapters":results,
    "result":"PASS_SCOPED" if all_pass else "HOLD",
    "tested_with_real_family":False,
    "authority_created":False,
    "no_fake_green":True
}
STATUS.write_text(json.dumps(status,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"result":status["result"],"chapters_checked":len(results)}))
sys.exit(0 if all_pass else 1)
