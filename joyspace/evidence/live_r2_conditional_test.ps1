# JoySpace: LIVE R2 synthetic conditional-write verification, PowerShell 5.1+
# Requires AWS CLI v2 with R2 S3 credentials configured locally.
# No child/family data. Never commit or print credentials.
$ErrorActionPreference = 'Stop'
$bucket = 'joyspace-evidence-v1'
$account = $env:CF_ACCOUNT_ID
if (-not $account) { throw 'Set CF_ACCOUNT_ID locally (Cloudflare account ID). No secrets are needed here.' }
if (-not (Get-Command aws -ErrorAction SilentlyContinue)) { throw 'AWS CLI is required.' }
if ($env:AWS_PROFILE -ne 'joyspace-r2') { throw 'Set AWS_PROFILE=joyspace-r2; refusing to use an unverified profile.' }
$endpoint = "https://$account.r2.cloudflarestorage.com"
$tmp = Join-Path $env:TEMP ("joyspace-r2-ci-" + [guid]::NewGuid().ToString('N'))
New-Item -Type Directory -Path $tmp | Out-Null
try {
  $payload = Join-Path $tmp 'synthetic.txt'
  $download = Join-Path $tmp 'readback.txt'
  $id = [guid]::NewGuid().ToString('N')
  $body = "COMPUTER WISDOM JOYSPACE synthetic-only`nrun_id=$id`ncontains_child_data=false`n"
  [System.IO.File]::WriteAllBytes($payload, [System.Text.Encoding]::UTF8.GetBytes($body))
  $hash = (Get-FileHash -LiteralPath $payload -Algorithm SHA256).Hash.ToLowerInvariant()
  $key = "ci-first/conditional/sha256-$hash.txt"
  $baseArgs = @('s3api','put-object','--bucket',$bucket,'--key',$key,
     '--body',$payload,'--if-none-match','*','--endpoint-url',$endpoint,'--no-cli-pager')
  $first = & aws @baseArgs 2>&1
  if ($LASTEXITCODE -ne 0) { throw "First conditional PUT failed; no PASS. $first" }
  # AWS returns a nonzero exit and writes an expected error to stderr. Under
  # Windows PowerShell 5.1, ErrorActionPreference=Stop can throw before
  # LASTEXITCODE and the response are inspected. Capture with Continue locally.
  $previousErrorAction = $ErrorActionPreference
  try {
    $ErrorActionPreference = 'Continue'
    $duplicate = & aws @baseArgs 2>&1
    $duplicateExit = $LASTEXITCODE
  } finally {
    $ErrorActionPreference = $previousErrorAction
  }
  if ($duplicateExit -eq 0) { throw 'FAIL: duplicate conditional PUT was accepted' }
  $dupText = ($duplicate | Out-String)
  if ($dupText -notmatch '(?i)(PreconditionFailed|\b412\b)') {
    throw 'HOLD: duplicate failed but no HTTP 412/PreconditionFailed proof'
  }
  & aws s3api get-object --bucket $bucket --key $key --endpoint-url $endpoint --no-cli-pager $download | Out-Null
  if ($LASTEXITCODE -ne 0) { throw 'GET failed; HOLD' }
  $readHash = (Get-FileHash -LiteralPath $download -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($readHash -ne $hash) { throw 'FAIL: downloaded SHA256 differs' }
  [ordered]@{
    scope='LIVE_R2_SYNTHETIC_ONLY'; conditional_put='PASS'
    duplicate_put='HTTP_412_PRECONDITION_FAILED'; readback_sha256='PASS'
    bucket=$bucket; key=$key; sha256=$hash
    production_ledger='HOLD'; guardian_approval='NOT_ESTABLISHED'
    child_publication=$false
  } | ConvertTo-Json
} finally {
  Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
}
