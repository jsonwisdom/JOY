#!/usr/bin/env python3
# render_joy_pages.py
# authority: false
# fake_green: forbidden
# boundary: render-only

import pathlib
import json
import datetime

STAGING_DIR = pathlib.Path("/tmp/docs-staging/")
DOCS_DIR = pathlib.Path("docs/")

LANGUAGE_LAYER = "MRS_WISDOM_APPROVED_JOYSPACE"


def load_staged():
    """Load staged HEIDEE artifacts."""
    staged = []
    for f in STAGING_DIR.glob("*.json"):
        with f.open() as fp:
            staged.append(json.load(fp))
    return staged


def apply_language_layer(item):
    """Apply Mrs Wisdom language layer to staged content."""
    return {
        "id": item.get("id"),
        "rendered_at": datetime.datetime.utcnow().isoformat(),
        "language_layer": LANGUAGE_LAYER,
        "content": item.get("content"),
        "joy_render": True,
        "authority": False,
        "fake_green": False,
    }


def write_docs(rendered_items):
    """Write rendered JOY pages to /docs."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for item in rendered_items:
        out = DOCS_DIR / f"{item['id']}.md"
        with out.open("w") as fp:
            fp.write("# JOY Rendered Page\n")
            fp.write(f"rendered_at: {item['rendered_at']}\n")
            fp.write(f"language_layer: {item['language_layer']}\n\n")
            fp.write(item["content"])


def main():
    staged = load_staged()
    rendered = [apply_language_layer(i) for i in staged]
    write_docs(rendered)


if __name__ == "__main__":
    main()
