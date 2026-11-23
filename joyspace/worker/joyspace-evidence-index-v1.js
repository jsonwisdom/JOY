/* COMPUTER WISDOM / JOYSPACE public evidence index v1.
 * Static information only; no private child records, trackers, storage, login, R2, D1, or approval authority.
 * Publication of this verification desk does not authorize the child-facing JoySpace experience.
 */
const STATUS = Object.freeze({
  schema:"cw-joyspace-public-evidence-index-v1",
  scope:"public-source verification desk only",
  heidee_source_tests:"PASS_19_OF_19",
  heidee_worker_test_groups:"PASS_9",
  heidee_ci:"PASS",
  joy_ci:"PASS_6_OF_6",
  heidee_pr:"DRAFT_UNMERGED",
  joy_pr:"DRAFT_UNMERGED",
  guardian_approval:"NOT_ESTABLISHED",
  child_facing_publication:false,
  real_device_validation:"NOT_RUN",
  cloudflare_r2:"BLOCKED_10042",
  production_evidence_ledger:"HOLD",
  authority_created:false,
  production_write:false,
  external_anchor:false
});
const HTML = \`<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>JoySpace · Public Evidence Desk</title>
<style>
:root{color-scheme:light;font:16px/1.55 system-ui,sans-serif;background:#fcfaf4;color:#202f3f}
*{box-sizing:border-box}body{margin:0}main{max-width:820px;margin:0 auto;padding:32px 22px 60px}
header{border-bottom:2px solid #213954;padding-bottom:24px}h1{font-size:clamp(2rem,6vw,3.6rem);line-height:1.15;margin:10px 0}
h2{font-size:1.2rem;margin:26px 0 8px}p{max-width:72ch}a{color:#084d83;text-underline-offset:3px}
.kicker{color:#3e6484;letter-spacing:.09em;font-weight:800;font-size:.8rem}
.state{display:inline-block;background:#f1e9d9;border:1px solid #92764b;padding:5px 11px;border-radius:12px;font-weight:700}
dl{display:grid;grid-template-columns:minmax(120px,1fr) minmax(130px,1fr);gap:0;border:1px solid #bac9d2;border-radius:14px;overflow:hidden}
dt,dd{margin:0;padding:12px 16px;border-bottom:1px solid #dce3e9}dt{background:#e9f0f3;font-weight:700}dd{overflow-wrap:anywhere}
dt:last-of-type,dd:last-of-type{border-bottom:0}.note{border-left:5px solid #8c6f42;padding:10px 16px;background:#f7efe0}
footer{margin-top:36px;font-size:.9rem;color:#455968}
@media(max-width:520px){dl{grid-template-columns:1fr}dt{border-bottom:0;padding-bottom:4px}dd{padding-top:4px}}
</style></head><body><main>
<header><p class="kicker">COMPUTER WISDOM · READ-ONLY VERIFICATION</p><h1>JoySpace Evidence Desk</h1>
<p>This is a public index of reproducible repository evidence and review gates—not the child-facing JoySpace app.</p>
<span class="state">Public source checks PASS · Publication approval HOLD</span></header>
<section><h2>What was independently checked?</h2>
<dl><dt>HEIDEE source gate</dt><dd>19/19 PASS on GitHub Actions</dd>
<dt>School of Wisdom checks</dt><dd>9 scope-limited groups PASS</dd>
<dt>JOY repository checks</dt><dd>6/6 workflows successful</dd>
<dt>HEIDEE PR</dt><dd>Draft, unmerged (#9)</dd>
<dt>JOY PR</dt><dd>Draft, unmerged (#129)</dd>
<dt>R2 evidence storage</dt><dd>BLOCKED (error 10042)</dd></dl></section>
<section><h2>Original evidence</h2><p>
<a href="https://github.com/jsonwisdom/HEIDEE/pull/9">HEIDEE review PR #9</a> ·
<a href="https://github.com/jsonwisdom/HEIDEE/actions/runs/45112226117">HEIDEE CI run</a> ·
<a href="https://github.com/jsonwisdom/JOY/pull/129">JOY index review PR #129</a>
</p><p><a href="/status.json">Machine-readable verification status</a></p></section>
<section class="note"><h2>What has NOT been approved?</h2>
<p>No guardian publication approval was established. The interactive child-facing site was not deployed by this page.
No child activity, family records, accounts, personal profiles, credentials or payment data are collected here.
Live-device testing and public source-byte parity of the child-facing experience remain unverified.</p>
<p><strong>NO RECEIPT = HOLD. No fake green.</strong></p></section>
<footer>Public information page. No login, scripts, tracking, uploads, wallets, R2 or D1 bindings. Evidence is about code and tests, not authority or consent.</footer>
</main></body></html>\`;
function reply(body,status,type,method){return new Response(method==="HEAD"?null:body,{status,headers:{"content-type":type,"cache-control":"no-store","content-security-policy":"default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'","x-content-type-options":"nosniff","referrer-policy":"no-referrer","x-frame-options":"DENY","permissions-policy":"camera=(), microphone=(), geolocation=()"}})}
addEventListener("fetch", event => {const r=event.request;const u=new URL(r.url);if(r.method!=="GET"&&r.method!=="HEAD"){event.respondWith(reply("Method not allowed",405,"text/plain; charset=utf-8",r.method));return;}
if(u.pathname==="/"||u.pathname==="/index.html"){event.respondWith(reply(HTML,200,"text/html; charset=utf-8",r.method));return;}
if(u.pathname==="/status.json"){event.respondWith(reply(JSON.stringify(STATUS,null,2),200,"application/json; charset=utf-8",r.method));return;}
event.respondWith(reply("Not found",404,"text/plain; charset=utf-8",r.method));});
