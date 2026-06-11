#!/usr/bin/env node

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import yargs from 'yargs/yargs';
import { hideBin } from 'yargs/helpers';
import { Octokit } from '@octokit/rest';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SCANNER_VERSION = "0.1.0-level1-paths";

async function main() {
  const argv = yargs(hideBin(process.argv))
    .option('config', { type: 'string', demandOption: true })
    .option('repo', { type: 'string', default: null })
    .option('output-json', { type: 'string', default: './docs/goblin/goblin_constellation_paths_v0_1.json' })
    .option('dry-run', { type: 'boolean', default: true })
    .option('write', { type: 'boolean', default: false })
    .parse();

  const config = JSON.parse(readFileSync(argv.config, 'utf8'));
  const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN || undefined });

  console.log(`[Path Scanner v${SCANNER_VERSION}] Starting Level 1 path surface scan...`);

  const targetRepos = argv.repo
    ? config.repos.filter((r) => r.name === argv.repo)
    : config.repos;

  const pathSurface = {
    scanner_version: SCANNER_VERSION,
    generated_at: new Date().toISOString(),
    terrain: {},
    path_surface: [],
    authority: false,
    no_fake_green: true
  };

  for (const repoDesc of targetRepos) {
    const terrainRecord = await scanRepoTerrain(octokit, repoDesc);
    pathSurface.terrain[repoDesc.name] = terrainRecord;

    if (terrainRecord.status === "HEALTHY") {
      const paths = await enumeratePaths(octokit, repoDesc, terrainRecord.tree_sha);
      pathSurface.path_surface.push(...paths.map((p) => ({
        repo: `${repoDesc.org}/${repoDesc.name}`,
        ...p
      })));
    }
  }

  pathSurface.path_surface.sort((a, b) =>
    a.repo.localeCompare(b.repo) || a.path.localeCompare(b.path)
  );

  const jsonOutput = JSON.stringify(pathSurface, null, 2);

  if (argv.dryRun) {
    console.log("=== DRY RUN ===");
    console.log(jsonOutput.slice(0, 1200) + "...");
    return;
  }

  if (argv.write) {
    ensureDir(dirname(argv.outputJson));
    writeFileSync(argv.outputJson, jsonOutput, 'utf8');
    console.log(`✅ Path surface written → ${argv.outputJson}`);
    console.log(`Total paths enumerated: ${pathSurface.path_surface.length}`);
  }
}

async function scanRepoTerrain(octokit, repoDesc) {
  try {
    const { data: repo } = await octokit.repos.get({
      owner: repoDesc.org,
      repo: repoDesc.name
    });

    const { data: branch } = await octokit.repos.getBranch({
      owner: repoDesc.org,
      repo: repoDesc.name,
      branch: repoDesc.defaultBranch || repoDesc.branch || 'main'
    });

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

async function enumeratePaths(octokit, repoDesc, treeSha) {
  try {
    const { data } = await octokit.git.getTree({
      owner: repoDesc.org,
      repo: repoDesc.name,
      tree_sha: treeSha,
      recursive: "1"
    });

    return data.tree
      .filter((item) => item.type === "blob")
      .map((item) => ({
        path: item.path,
        sha: item.sha,
        size: item.size,
        url: `https://github.com/${repoDesc.org}/${repoDesc.name}/blob/${repoDesc.defaultBranch || repoDesc.branch || 'main'}/${item.path}`
      }));
  } catch (e) {
    console.warn(`Path enumeration failed for ${repoDesc.name}:`, e.message);
    return [];
  }
}

function ensureDir(dir) {
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
