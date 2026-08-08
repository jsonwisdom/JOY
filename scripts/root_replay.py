#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

EXCLUDED_DIRS = {".git", ".next", "node_modules", "dist", "build", "__pycache__"}
LARGE_FILE_BYTES = 5 * 1024 * 1024


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(root: Path) -> dict:
    files = []
    anomalies = []
    seen_casefold = {}

    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        size = path.stat().st_size
        digest = sha256(path)
        files.append({"path": rel, "size": size, "sha256": digest})

        folded = rel.casefold()
        if folded in seen_casefold and seen_casefold[folded] != rel:
            anomalies.append({"type": "CASE_COLLISION", "paths": [seen_casefold[folded], rel]})
        else:
            seen_casefold[folded] = rel

        if size > LARGE_FILE_BYTES:
            anomalies.append({"type": "LARGE_FILE", "path": rel, "size": size})
        if path.is_symlink():
            anomalies.append({"type": "SYMLINK", "path": rel})
        if os.access(path, os.X_OK) and path.suffix not in {".sh", ".py"}:
            anomalies.append({"type": "UNEXPECTED_EXECUTABLE", "path": rel})

    canonical = json.dumps(files, sort_keys=True, separators=(",", ":")).encode()
    return {
        "artifact_type": "ROOT_REPLAY_MANIFEST_V0_1",
        "authority": False,
        "root": ".",
        "file_count": len(files),
        "manifest_sha256": hashlib.sha256(canonical).hexdigest(),
        "files": files,
        "anomalies": anomalies,
        "anomaly_count": len(anomalies),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--compare")
    args = parser.parse_args()

    result = build_manifest(Path(args.root).resolve())
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    if args.compare:
        prior = json.loads(Path(args.compare).read_text())
        replay = {
            "artifact_type": "ROOT_REPLAY_COMPARISON_V0_1",
            "authority": False,
            "baseline_manifest_sha256": prior.get("manifest_sha256"),
            "replay_manifest_sha256": result["manifest_sha256"],
            "deterministic_match": prior.get("manifest_sha256") == result["manifest_sha256"],
        }
        print(json.dumps(replay, indent=2, sort_keys=True))
        return 0 if replay["deterministic_match"] else 2

    print(json.dumps({
        "manifest_sha256": result["manifest_sha256"],
        "file_count": result["file_count"],
        "anomaly_count": result["anomaly_count"],
        "authority": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
