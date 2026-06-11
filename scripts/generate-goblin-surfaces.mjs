#!/usr/bin/env node

/**
 * Goblin Unified Surface Generator V0.1
 *
 * Anchored blueprint:
 * docs/goblin/GOBLIN_UNIFIED_SURFACE_GENERATION_BLUEPRINT_V0_1.md
 * commit: 5ef43e6d19f77f4321d2068c7fd26ed5e9a94517
 *
 * Writes only:
 * - artifacts/goblin_constellation_terrain_v0_1.json
 * - artifacts/goblin_constellation_paths_v0_1.json
 *
 * No content scanning.
 * No semantic inference.
 * No authority promotion.
 */

import fs from "node:fs/promises";
import path from "node:path";

const CONFIG_PATH = "scripts/wisdom-constellation.config.json";
const TERRAIN_OUTPUT = "artifacts/goblin_constellation_terrain_v0_1.json";
const PATH_OUTPUT = "artifacts/goblin_constellation_paths_v0_1.json";
const GITHUB_API = "https://api.github.com";

function stableJson(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

export async function loadWisdomConstellationConfig(configPath = CONFIG_PATH) {
  const raw = await fs.readFile(configPath, "utf8");
  const config = JSON.parse(raw);

  return {
    version: config.version,
    subject: config.subject,
    court: config.court,
    authority: false,
    no_fake_green: true,
    repos: [...config.repos]
      .map((repo) => ({
        org: repo.org,
        name: repo.name,
        branch: repo.branch ?? "main"
      }))
      .sort((a, b) => `${a.org}/${a.name}`.localeCompare(`${b.org}/${b.name}`))
  };
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      "Accept": "application/vnd.github+json",
      "User-Agent": "jsonwisdom-goblin-surface-generator-v0-1"
    }
  });

  if (!response.ok) {
    return { ok: false, status: response.status, data: null };
  }

  return { ok: true, status: response.status, data: await response.json() };
}

export async function fetchRepoTerrain(repoConfig) {
  const repo = `${repoConfig.org}/${repoConfig.name}`;
  const repoResponse = await fetchJson(`${GITHUB_API}/repos/${repo}`);

  if (!repoResponse.ok) {
    return {
      repo,
      exists: false,
      reachable: false,
      public: false,
      default_branch: repoConfig.branch,
      default_branch_sha: null,
      last_commit_time: null,
      tree_sha: null,
      status: "UNREACHABLE"
    };
  }

  const defaultBranch = repoResponse.data.default_branch ?? repoConfig.branch;
  const branchResponse = await fetchJson(`${GITHUB_API}/repos/${repo}/branches/${defaultBranch}`);

  if (!branchResponse.ok) {
    return {
      repo,
      exists: true,
      reachable: false,
      public: !Boolean(repoResponse.data.private),
      default_branch: defaultBranch,
      default_branch_sha: null,
      last_commit_time: null,
      tree_sha: null,
      status: "TREE_UNREACHABLE"
    };
  }

  return {
    repo,
    exists: true,
    reachable: true,
    public: !Boolean(repoResponse.data.private),
    default_branch: defaultBranch,
    default_branch_sha: branchResponse.data.commit?.sha ?? null,
    last_commit_time: branchResponse.data.commit?.commit?.committer?.date ?? null,
    tree_sha: branchResponse.data.commit?.commit?.tree?.sha ?? null,
    status: "HEALTHY"
  };
}

export async function fetchRepoTreePaths(terrainRecord) {
  if (!terrainRecord.reachable || !terrainRecord.tree_sha) {
    return { paths: [], failure: terrainRecord.repo };
  }

  const treeResponse = await fetchJson(
    `${GITHUB_API}/repos/${terrainRecord.repo}/git/trees/${terrainRecord.tree_sha}?recursive=1`
  );

  if (!treeResponse.ok) {
    return { paths: [], failure: terrainRecord.repo };
  }

  const paths = treeResponse.data.tree
    .filter((entry) => entry.type === "blob")
    .map((entry) => ({
      repo: terrainRecord.repo,
      path: entry.path,
      sha: entry.sha,
      size: entry.size ?? null,
      url: `https://github.com/${terrainRecord.repo}/blob/${terrainRecord.default_branch}/${entry.path}`
    }))
    .sort((a, b) => `${a.repo}/${a.path}`.localeCompare(`${b.repo}/${b.path}`));

  return { paths, failure: null };
}

export async function buildTerrainSurface(config) {
  const terrainRecords = [];

  for (const repo of config.repos) {
    terrainRecords.push(await fetchRepoTerrain(repo));
  }

  terrainRecords.sort((a, b) => a.repo.localeCompare(b.repo));

  return {
    scanner_version: "0.1.0-level0-terrain",
    generated_at: new Date().toISOString(),
    terrain: terrainRecords,
    authority: false,
    no_fake_green: true
  };
}

export async function buildPathSurface(terrainSurface) {
  const pathEntries = [];
  const failures = [];

  for (const terrainRecord of terrainSurface.terrain) {
    const result = await fetchRepoTreePaths(terrainRecord);
    pathEntries.push(...result.paths);
    if (result.failure) failures.push(result.failure);
  }

  pathEntries.sort((a, b) => `${a.repo}/${a.path}`.localeCompare(`${b.repo}/${b.path}`));
  failures.sort();

  return {
    scanner_version: "0.1.0-level1-paths",
    generated_at: new Date().toISOString(),
    path_surface: pathEntries,
    failures,
    authority: false,
    no_fake_green: true
  };
}

export async function writeSurfaceArtifacts(terrainSurface, pathSurface) {
  await fs.mkdir(path.dirname(TERRAIN_OUTPUT), { recursive: true });
  await fs.writeFile(TERRAIN_OUTPUT, stableJson(terrainSurface), "utf8");
  await fs.writeFile(PATH_OUTPUT, stableJson(pathSurface), "utf8");

  return {
    surface_generation: pathSurface.failures.length === 0 ? "COMPLETE" : "HOLD",
    terrain_output: TERRAIN_OUTPUT,
    path_output: PATH_OUTPUT,
    repos_checked: terrainSurface.terrain.length,
    path_entries: pathSurface.path_surface.length,
    failures: pathSurface.failures,
    authority: false,
    no_fake_green: true
  };
}

export async function generateUnifiedGoblinSurfaces() {
  const config = await loadWisdomConstellationConfig();
  const terrainSurface = await buildTerrainSurface(config);
  const pathSurface = await buildPathSurface(terrainSurface);
  return writeSurfaceArtifacts(terrainSurface, pathSurface);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  generateUnifiedGoblinSurfaces()
    .then((receipt) => {
      console.log(stableJson(receipt));
    })
    .catch((error) => {
      console.error(error);
      process.exitCode = 1;
    });
}
