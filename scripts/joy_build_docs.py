#!/usr/bin/env python3
# joy_build_docs.py
# authority: false
# fake_green: forbidden
# boundary: ingestion-only

import pathlib
import datetime
import json

VOICE_DIR = pathlib.Path("voice/")
FAMILY_DIR = pathlib.Path("FAMILY/")
STAGING_DIR = pathlib.Path("/tmp/docs-staging/")


def load_voice_inputs():
    """Load raw voice/transcript artifacts."""
    transcripts = []
    for f in VOICE_DIR.glob("*.json"):
        with f.open() as fp:
            transcripts.append(json.load(fp))
    return transcripts


def apply_joy_transforms(transcripts):
    """Apply JOY ingestion transforms (HEIDEE layer)."""
    transformed = []
    for t in transcripts:
        transformed.append({
            "id": t.get("id"),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "content": t.get("content"),
            "joy_ingest": True,
            "authority": False,
            "fake_green": False,
        })
    return transformed


def stage_outputs(transformed):
    """Write staged artifacts to /tmp/docs-staging."""
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    for item in transformed:
        out = STAGING_DIR / f"{item['id']}.json"
        with out.open("w") as fp:
            json.dump(item, fp, indent=2)


def main():
    transcripts = load_voice_inputs()
    transformed = apply_joy_transforms(transcripts)
    stage_outputs(transformed)


if __name__ == "__main__":
    main()
