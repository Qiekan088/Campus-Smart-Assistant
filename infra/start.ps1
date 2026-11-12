param([switch]$Database)
$ErrorActionPreference='Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
if ($Database) {
  if (!(Test-Path .env)) { throw 'Copy .env.example to .env and fill both database passwords first.' }
  $values = @{}
  foreach ($line in Get-Content .env) { if ($line -match '^\s*(MYSQL_PASSWORD|MYSQL_ROOT_PASSWORD)\s*=\s*(.*)$') { $values[$matches[1]]=$matches[2].Trim().Trim('"').Trim("'") } }
  foreach ($key in @('MYSQL_PASSWORD','MYSQL_ROOT_PASSWORD')) { if (!$values[$key]) { throw "$key must not be empty in .env" } }
  if ($values.MYSQL_PASSWORD -eq $values.MYSQL_ROOT_PASSWORD) { throw 'Use different database passwords.' }
  docker compose --profile database up -d --build --wait
} else { docker compose up -d --build --wait }
if ($LASTEXITCODE -ne 0) { throw 'Compose failed. Run docker compose logs.' }
