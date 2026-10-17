$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) { $Python = Get-Command py -ErrorAction SilentlyContinue }
if (-not $Python) { throw 'Python 3.10+ is required. Install Python, then rerun .\install.ps1.' }

$Version = & $Python.Source -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")'
$IsSupported = & $Python.Source -c 'import sys; print(1 if sys.version_info >= (3, 10) else 0)'
if ($IsSupported -ne '1') { throw "Python 3.10+ is required; detected $Version." }
Write-Host "Python $Version detected. Running static validation..."
& $Python.Source scripts/validate_team.py
if ($LASTEXITCODE -ne 0) { throw 'Static validation failed.' }
Write-Host ''
Write-Host 'Setup checks passed.'
Write-Host 'Next: install and authenticate Claude Code using its official documentation, then launch it from this repository root.'
Write-Host 'This script does not install Claude Code, create credentials, change permissions, or launch an application project.'
