#!/usr/bin/env node

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { dirname } from 'path';

const SCANNER_VERSION = "0.1.1-level1-paths-no-deps";

function arg(name, fallback = null) {
  const i = process.argv.indexOf(name);
  return i === -1 ? fallback : process.argv[i + 1];
}

function has(name) {
  return process.argv.includes(name);
}

async function githubGet(url) {
  const headers = {
    Accept: 'application/vnd.github+json',
    'User-Agent': 'jsonwisdom-path-scanner'
  };

  if (process.env.GITHUB_TOKEN) {
    headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  }

  const res = await fetch(url, { headers });
  const data = await res.json();

  if (!res.ok) {
    throw Object.assign(new Error(data.message || `GitHub request failed ${res.status}`), {
      status: res.status
    });
  }

  return data;
}

async function scanRepoTerrain(repoDesc) {
  try {
    const repo = await githubGet(`https://api.github.com/repos/${repoDesc.org}/${repoDesc.name}`);
    const branchName = repoDesc.defaultBranch || repoDesc.branch || 'main';
    const branch = await githubGet(`https://api.github.com/repos/${repoDesc.org}/${repoDesc.name}/branches/${branchName}`);

    return {
      exists: true,
      reachable: true,
      public: !repo.private,
      default_branch: branch.name,
      default_branch_sha: branch.commit.sha,
      last_commit_time: branch.commit.commit.author.date,
      tree_sha: branch.commit.commit.tree.sha,
      status: "HEALTHY"
    };
  } catch (error) {
    if (error.status === 404) return { status: "NOT_FOUND" };
    if (error.status === 403) return { status: "PRIVATE_OR_RATE_LIMITED" };
    return { status: "UNREACHABLE", error: error.message };
  }
}

async function enumeratePaths(repoDesc, treeSha) {
  const tree = await githubGet(
    `https://api.github.com/repos/${repoDesc.org}/${repoDesc.name}/git/trees/${treeSha}?recursive=1`
  );

  return tree.tree
    .filter(item => item.type === "blob")
    .map(item => ({
      path: item.path,
      sha: item.sha,
      size: item.size,
      url: `https://github.com/${repoDesc.org}/${repoDesc.name}/blob/${repoDesc.branch || 'main'}/${item.path}`
    }));
}

async function main() {
  const configPath = arg('--config', './scripts/wisdom-constellation.config.json');
  const repoFilter = arg('--repo', null);
  const outputJson = arg('--output-json', './docs/goblin/goblin_constellation_paths_v0_1.json');
  const write = has('--write');

  const config = JSON.parse(readFileSync(configPath, 'utf8'));
  const targetRepos = repoFilter ? config.repos.filter(r => r.name === repoFilter) : config.repos;

  const pathSurface = {
    scanner_version: SCANNER_VERSION,
    generated_at: new Date().toISOString(),
    terrain: {},
    path_surface: [],
    authority: false,
    no_fake_green: true
  };

  for (const repoDesc of targetRepos) {
    console.log(`Scanning ${repoDesc.org}/${repoDesc.name}...`);
    const terrainRecord = await scanRepoTerrain(repoDesc);
    pathSurface.terrain[repoDesc.name] = terrainRecord;

    if (terrainRecord.status === "HEALTHY") {
      const paths = await enumeratePaths(repoDesc, terrainRecord.tree_sha);
      pathSurface.path_surface.push(...paths.map(p => ({
        repo: `${repoDesc.org}/${repoDesc.name}`,
        ...p
      })));
    }
  }

  pathSurface.path_surface.sort((a, b) =>
    a.repo.localeCompare(b.repo) || a.path.localeCompare(b.path)
  );

  const json = JSON.stringify(pathSurface, null, 2) + "\n";

  if (!write) {
    console.log(json.slice(0, 1600));
    console.log("Dry run only. Add --write to save.");
    return;
  }

  if (!existsSync(dirname(outputJson))) mkdirSync(dirname(outputJson), { recursive: true });
  writeFileSync(outputJson, json, 'utf8');

  console.log(`✅ Path surface written → ${outputJson}`);
  console.log(`Total paths enumerated: ${pathSurface.path_surface.length}`);
}

main().catch(err => {
  console.error("❌ Path scanner failure:", err.message);
  process.exit(1);
});
