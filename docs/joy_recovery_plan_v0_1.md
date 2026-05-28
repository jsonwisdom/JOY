# JOY Recovery Plan V0.1 🌈🧾

## Status

Assume all local-only badge assets, receipts, manifests, and ledgers are missing from GitHub until directly verified.

## Recovery Rule

Remote canon requires visible files and real GitHub commit SHAs.

Local claims are useful notes, but they are not canon until committed to `jsonwisdom/JOY`.

## Minimum Recovery Set

Rebuild these in order:

1. `badges/badge_manifest_v0_1.json`
2. `receipts/badge_family_v0_1_closeout_receipt.json`
3. `badges/badge_manifest_v0_2.json`
4. `docs/joy_project_ledger_v0_2.md`
5. `assets/badges/*.svg`
6. `receipts/*_receipt.json`

## Known Verified Hash Claims

```json
{
  "joy_bringer": "71fdf99c84af62335d962960fbebe8c6d88cdc501f679b70609ab421861c192d",
  "kindness_keeper": "287e19f3cc4e5e7bdf054114d48a1a2904fee2a4186cd837c512a38e209f4b1e",
  "growth_guardian": "1c1a7cee6ee76d07900f68b3ecc67693ef9d0bf13a436f34aaed2dacaa4ef6cc",
  "harmony_weaver": "35a991da99be8926a33e4675dd34c4f8f1351955e17ab8f7667e0600272a5ea7",
  "resilience_thread": "504546e4e250328b514abbfdbc3428345fb4602f2ed5914fc59ff537a1cffb01",
  "wisdom_anchor": "6906082e28b3c666774900ac2cbc153159ed769075ed6747bc61006b5668f4ec"
}
```

## Recovery Command

```bash
git clone https://github.com/jsonwisdom/JOY.git
cd JOY
find . -maxdepth 4 -type f | sort
git log --oneline -10
```

## Canon Rule

Do not add new assets until the recovered tree is visible in GitHub.

SVG → local SHA-256 → receipt → manifest → ledger → GitHub commit.

## Family Before Economy

```json
{
  "family_priority": true,
  "economy_subordinate": true,
  "authority": false,
  "meme_court_safe": true
}
```
