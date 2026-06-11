#!/usr/bin/env node

/**
 * Goblin Constellation JSON Generator V0.1
 *
 * Anchored spec:
 * docs/goblin/GOBLIN_CONSTELLATION_JSON_GENERATOR_SPEC_V0_1.md
 * commit: 581f369c8c0629456d14a39e96560ae91b6bdeb8
 *
 * Reads:
 * - scripts/wisdom-constellation.config.json
 * - artifacts/goblin_constellation_terrain_v0_1.json
 * - artifacts/goblin_constellation_paths_v0_1.json
 *
 * Writes only:
 * - artifacts/goblin_constellation_v0_1.json
 *
 * No content scanning.
 * No semantic inference.
 * No authority promotion.
 */

import fs from "node:fs/promises";
import path from "node:path";

const CONFIG_PATH = "scripts/wisdom-constellation.config.json";
const TERRAIN_PATH = "artifacts/goblin_constellation_terrain_v0_1.json";
const PATH_SURFACE_PATH = "artifacts/goblin_constellation_paths_v0_1.json";
const OUTPUT_PATH = "artifacts/goblin_constellation_v0_1.json";

function stableJson(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

async function readJson(filePath) {
  const raw = await fs.readFile(filePath, "utf8");
  return JSON.parse(raw);
}

export async function loadTerrainSurface(filePath = TERRAIN_PATH) {
  return readJson(filePath);
}

export async function loadPathSurface(filePath = PATH_SURFACE_PATH) {
  return readJson(filePath);
}

async function loadConfig(filePath = CONFIG_PATH) {
  const config = await readJson(filePath);
  return {
    subject: config.subject,
    court: config.court,
    authority: false,
    no_fake_green: true,
    repos: [...config.repos]
      .map((repo) => `${repo.org}/${repo.name}`)
      .sort()
  };
}

function toTerrainMap(terrainSurface) {
  return new Map(terrainSurface.terrain.map((record) => [record.repo, record]));
}

function groupPaths(pathSurface) {
  const grouped = new Map();

  for (const entry of pathSurface.path_surface) {
    if (!grouped.has(entry.repo)) grouped.set(entry.repo, []);
    grouped.get(entry.repo).push(entry.path);
  }

  for (const [repo, paths] of grouped.entries()) {
    grouped.set(repo, [...new Set(paths)].sort());
  }

  return grouped;
}

export function deriveSignals(paths) {
  const signals = new Set();

  for (const itemPath of paths) {
    const lower = itemPath.toLowerCase();
    const filename = path.basename(itemPath);

    if (lower.includes("components/goblin-gate")) {
      signals.add("path:components/goblin-gate");
    }

    if (lower.includes("docs/goblin")) {
      signals.add("path:docs/goblin");
    }

    if (filename.includes("GOBLIN")) {
      signals.add("filename:GOBLIN");
    }

    if (filename.includes("CONSTELLATION")) {
      signals.add("filename:CONSTELLATION");
    }

    if (filename.includes("INDEX")) {
      signals.add("filename:INDEX");
    }
  }

  return [...signals].sort();
}

export function deriveClassification(repos) {
  const allPaths = repos.flatMap((repo) => repo.paths);
  const allSignals = new Set(repos.flatMap((repo) => repo.signals));

  return {
    GOBLIN_GATE: allSignals.has("path:components/goblin-gate") ? "VERIFIED" : "HOLD",
    CONSTELLATION_MAPPER: allSignals.has("filename:CONSTELLATION") ? "VERIFIED" : "HOLD",
    GOBLIN_REPO_CONSTELLATION: allPaths.some((itemPath) => itemPath.includes("GOBLIN_REPO_CONSTELLATION"))
      ? "SEEDED"
      : "HOLD",
    PUBLIC_HUMAN_INDEX: allPaths.includes("index.html") || allPaths.includes("README.md") ? "PRESENT" : "HOLD"
  };
}

function mergeRepoRecords(config, terrainSurface, pathSurface) {
  const terrainMap = toTerrainMap(terrainSurface);
  const pathsByRepo = groupPaths(pathSurface);

  return config.repos.map((repo) => {
    const terrain = terrainMap.get(repo) ?? {
      exists: false,
      reachable: false,
      public: false,
      default_branch: null,
      default_branch_sha: null,
      last_commit_time: null,
      tree_sha: null,
      status: "UNKNOWN"
    };

    const paths = pathsByRepo.get(repo) ?? [];

    return {
      repo,
      default_branch: terrain.default_branch,
      terrain: {
        exists: Boolean(terrain.exists),
        reachable: Boolean(terrain.reachable),
        public: Boolean(terrain.public),
        default_branch_sha: terrain.default_branch_sha ?? null,
        last_commit_time: terrain.last_commit_time ?? null,
        tree_sha: terrain.tree_sha ?? null
      },
      paths,
      signals: deriveSignals(paths)
    };
  }).sort((a, b) => a.repo.localeCompare(b.repo));
}

export async function generateConstellationJSON() {
  const config = await loadConfig();
  const terrainSurface = await loadTerrainSurface();
  const pathSurface = await loadPathSurface();
  const repos = mergeRepoRecords(config, terrainSurface, pathSurface);

  return {
    scanner_version: "0.1.0",
    generated_at: new Date().toISOString(),
    root_identity: null,
    repos,
    subjects: [config.subject],
    courts: [config.court],
    classification: deriveClassification(repos),
    authority: false,
    no_fake_green: true
  };
}

async function writeConstellationJSON() {
  const constellation = await generateConstellationJSON();
  await fs.mkdir(path.dirname(OUTPUT_PATH), { recursive: true });
  await fs.writeFile(OUTPUT_PATH, stableJson(constellation), "utf8");

  return {
    output: OUTPUT_PATH,
    status: "GENERATED",
    repos: constellation.repos.length,
    authority: false,
    no_fake_green: true
  };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  writeConstellationJSON()
    .then((receipt) => console.log(stableJson(receipt)))
    .catch((error) => {
      console.error(error);
      process.exitCode = 1;
    });
}
