import os
import json
from collections import defaultdict
from git import Repo

REPOS = [
    {"name": "jsonwisdom/JOY", "url": "https://github.com/jsonwisdom/JOY.git", "branch": "main"},
    {"name": "jsonwisdom/AL", "url": "https://github.com/jsonwisdom/AL.git", "branch": "master"},
    {"name": "jsonwisdom/COMPUTERWISDOM", "url": "https://github.com/jsonwisdom/COMPUTERWISDOM.git", "branch": "master"},
]

LOCAL_BASE = "./zero_trust_repos"
SUSPICIOUS_MARKERS = [
    "green", "verified", "no access", "unreachable", "manual verification required",
    "committed", "pushed", "confirmed", "should pass", "likely", "probably", "AI recommended"
]

CLASSIFICATIONS = {
    "python": [".py", ".pyx", ".ipynb"],
    "javascript": [".js", ".ts", ".jsx", ".tsx", ".vue"],
    "jvm": [".java", ".kt", ".scala", ".groovy"],
    "cpp": [".cpp", ".cxx", ".cc", ".h", ".hpp"],
    "go": [".go"],
    "rust": [".rs"],
    "documentation": [".md", ".rst", ".txt"],
    "config": [".yml", ".yaml", ".json", ".toml", ".ini", ".cfg"],
    "build": ["dockerfile", "makefile", "cmakelists"],
    "image": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"],
    "other": []
}


def classify_artifact(file_path: str) -> str:
    name = os.path.basename(file_path).lower()
    ext = os.path.splitext(file_path.lower())[1]
    for cat, exts in CLASSIFICATIONS.items():
        if ext in exts or any(x in name for x in exts if isinstance(x, str) and not x.startswith(".")):
            return cat
    return "other"


def scan_for_markers(content: str) -> list:
    lower = content.lower()
    return [marker for marker in SUSPICIOUS_MARKERS if marker.lower() in lower]


def classify_finding(marker: str) -> str:
    marker_lower = marker.lower()
    if any(x in marker_lower for x in ["verified", "confirmed", "green"]):
        return "FALSE_GREEN_RISK"
    if "unreachable" in marker_lower or "no access" in marker_lower:
        return "SEARCH_AS_404_RISK"
    if "manual" in marker_lower or "probably" in marker_lower or "likely" in marker_lower:
        return "UNVERIFIED_CLAIM"
    if any(x in marker_lower for x in ["committed", "pushed"]):
        return "REPLAY_REQUIRED"
    return "REPLAY_REQUIRED"


def get_or_clone_repo(repo_config):
    local_path = os.path.join(LOCAL_BASE, repo_config["name"].split("/")[-1])
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    if os.path.exists(os.path.join(local_path, ".git")):
        repo = Repo(local_path)
    else:
        repo = Repo.clone_from(repo_config["url"], local_path)

    branch = repo_config["branch"]
    repo.git.fetch("origin", branch)
    repo.git.checkout(branch)
    repo.git.pull("--rebase", "origin", branch)
    return repo, local_path


def inventory_repo(repo_config):
    try:
        repo, local_path = get_or_clone_repo(repo_config)
        head = repo.head.commit
        file_counts = defaultdict(int)
        suspicious_findings = []

        for root, dirs, files in os.walk(local_path):
            dirs[:] = [d for d in dirs if d != ".git"]
            for filename in files:
                full = os.path.join(root, filename)
                rel = os.path.relpath(full, local_path)
                cat = classify_artifact(rel)
                file_counts[cat] += 1

                try:
                    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                        content = fh.read()
                    for marker in scan_for_markers(content):
                        suspicious_findings.append({
                            "marker": marker,
                            "file": rel,
                            "classification": classify_finding(marker),
                        })
                except OSError:
                    pass

        return {
            "repo_name": repo_config["name"],
            "local_path": local_path,
            "branch": repo_config["branch"],
            "head_sha": head.hexsha,
            "dirty": repo.is_dirty(untracked_files=True),
            "recent_commit_message": head.message.strip().split("\n")[0],
            "file_counts_by_classification": dict(file_counts),
            "suspicious_claim_markers": suspicious_findings,
        }
    except Exception as exc:
        return {
            "repo_name": repo_config["name"],
            "local_path": None,
            "branch": repo_config["branch"],
            "head_sha": None,
            "dirty": None,
            "recent_commit_message": str(exc),
            "file_counts_by_classification": {},
            "suspicious_claim_markers": [{
                "marker": "local inventory failure",
                "classification": "REPLAY_REQUIRED",
            }],
        }


if __name__ == "__main__":
    inventory = {
        "artifact": "ZERO_TRUST_LOCAL_REPO_INVENTORY_V0_1",
        "authority": False,
        "no_fake_green": True,
        "repos": [inventory_repo(cfg) for cfg in REPOS],
    }
    print(json.dumps(inventory, indent=2, ensure_ascii=False))
