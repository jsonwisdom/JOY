#!/usr/bin/env node
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";

const INPUT = "docs/goblin/goblin_constellation_paths_v0_1.json";
const OUTPUT = "docs/goblin/goblin_subject_surface_v0_1.json";

const SUBJECT_PATTERNS = [
  {
    id: "JOY_SURFACE",
    subject: "JOY",
    match: /(^|\/)(JOY|joy)(\/|$)/,
    reason: "Path references JOY surface"
  },
  {
    id: "GOBLIN_SURFACE",
    subject: "GOBLIN",
    match: /goblin/i,
    reason: "Path references goblin surface"
  },
  {
    id: "DOCS_SURFACE",
    subject: "DOCS",
    match: /(^|\/)docs\//i,
    reason: "Path is under docs"
  },
  {
    id: "SCRIPT_SURFACE",
    subject: "SCRIPTS",
    match: /(^|\/)scripts\//i,
    reason: "Path is under scripts"
  },
  {
    id: "TRUTH_SURFACE",
    subject: "TRUTH",
    match: /(^|\/)(_truth|truth)(\/|$)/i,
    reason: "Path references truth surface"
  },
  {
    id: "RECEIPT_SURFACE",
    subject: "RECEIPTS",
    match: /receipt/i,
    reason: "Path references receipt surface"
  },
  {
    id: "ARTIFACT_SURFACE",
    subject: "ARTIFACTS",
    match: /artifact/i,
    reason: "Path references artifact surface"
  }
];

function nowIso() {
  return new Date().toISOString();
}

function collectPaths(node, out = []) {
  if (!node || typeof node !== "object") return out;

  if (typeof node.path === "string") out.push(node.path);
  if (typeof node.file === "string") out.push(node.file);
  if (typeof node.name === "string" && node.type === "file") out.push(node.name);

  for (const value of Object.values(node)) {
    if (Array.isArray(value)) {
      for (const item of value) collectPaths(item, out);
    } else if (value && typeof value === "object") {
      collectPaths(value, out);
    }
  }

  return out;
}

function detectSubjects(paths) {
  const detections = [];

  for (const p of paths) {
    for (const pattern of SUBJECT_PATTERNS) {
      if (pattern.match.test(p)) {
        detections.push({
          path: p,
          pattern_id: pattern.id,
          subject: pattern.subject,
          reason: pattern.reason
        });
      }
    }
  }

  return detections;
}

function summarize(detections) {
  const subjects = {};

  for (const d of detections) {
    subjects[d.subject] ??= {
      count: 0,
      pattern_ids: new Set(),
      paths: []
    };

    subjects[d.subject].count += 1;
    subjects[d.subject].pattern_ids.add(d.pattern_id);
    subjects[d.subject].paths.push(d.path);
  }

  return Object.fromEntries(
    Object.entries(subjects).map(([subject, data]) => [
      subject,
      {
        count: data.count,
        pattern_ids: [...data.pattern_ids].sort(),
        paths: [...new Set(data.paths)].sort()
      }
    ])
  );
}

async function main() {
  const raw = await readFile(INPUT, "utf8");
  const level1 = JSON.parse(raw);

  const paths = [...new Set(collectPaths(level1))].sort();
  const detections = detectSubjects(paths);
  const subjects = summarize(detections);

  const surface = {
    scanner_version: "0.1.0-level2-subjects-no-github-no-content",
    generated_at: nowIso(),
    authority: false,
    no_fake_green: true,
    input: {
      source_file: INPUT,
      boundary: "LEVEL_1_PATH_SURFACE_ONLY"
    },
    rules: {
      github_api_allowed: false,
      content_inspection_allowed: false,
      path_pattern_detection_only: true
    },
    counts: {
      paths_seen: paths.length,
      detections: detections.length,
      subjects_detected: Object.keys(subjects).length
    },
    subjects,
    detections,
    replay_object: {
      level_0_terrain: "VERIFIED",
      level_1_path_surface: "VERIFIED",
      level_2_subject_surface: detections.length > 0 ? "DETECTED" : "EMPTY",
      mutation_allowed: false,
      authority: false,
      no_fake_green: true
    }
  };

  await mkdir(path.dirname(OUTPUT), { recursive: true });
  await writeFile(OUTPUT, `${JSON.stringify(surface, null, 2)}\n`);

  console.log(JSON.stringify({
    status: "LEVEL_2_SUBJECT_SURFACE_WRITTEN",
    input: INPUT,
    output: OUTPUT,
    paths_seen: paths.length,
    detections: detections.length,
    authority: false,
    no_fake_green: true
  }, null, 2));
}

main().catch((err) => {
  console.error(JSON.stringify({
    status: "LEVEL_2_SUBJECT_SCANNER_FAILED",
    error: err.message,
    authority: false,
    no_fake_green: true
  }, null, 2));
  process.exit(1);
});
