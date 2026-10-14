<#
.SYNOPSIS
Title: Prepare Python and the Google Cloud CLI, then run an audit procedure.
.DESCRIPTION
Find a supported Python runtime; if unavailable, download Google's portable Windows
SDK with bundled Python and verify its published SHA-256 before extraction. The
Python runner checks the CLI, authenticates and verifies project ancestry before reads.
.LINK
https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives
.LINK
https://docs.cloud.google.com/sdk/docs/authenticate
#>
[CmdletBinding()]
param([string]$Procedure='GOV-01',[switch]$Plan,[string]$Scope,[string]$Output)
$ErrorActionPreference='Stop'
$repoRoot=Split-Path $PSScriptRoot -Parent
if ($Plan) {
    $recipes=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'recipes.json') -Raw | ConvertFrom-Json
    $recipe=$recipes.PSObject.Properties[$Procedure]
    if (-not $recipe) { throw 'Unknown procedure ID' }
    $recipe.Value | ConvertTo-Json -Depth 30
    return
}
if (-not $Scope -or -not $Output) { throw 'Provide -Scope and -Output, or use -Plan.' }
$auditPython=$null
foreach ($candidate in @('python','python3')) {
    $found=Get-Command $candidate -ErrorAction SilentlyContinue
    if ($found) {
        & $found.Source -c 'import sys; sys.exit(0 if (3,12) <= sys.version_info[:2] <= (3,15) else 1)' 2>$null
        if ($LASTEXITCODE -eq 0) { $auditPython=$found.Source; break }
    }
}
if (-not $auditPython) {
    if ($env:OS -ne 'Windows_NT' -or -not [Environment]::Is64BitOperatingSystem) { throw 'Use Python 3.12+ and scripts/audit.py on this platform.' }
    $sdkParent=Join-Path ([Environment]::GetFolderPath('UserProfile')) '.gcp-audit/sdk/589.0.0'
    $bundled=Join-Path $sdkParent 'google-cloud-sdk/platform/bundledpython/python.exe'
    if (-not (Test-Path -LiteralPath $bundled)) {
        if (Test-Path -LiteralPath $sdkParent) { throw 'An incomplete SDK directory exists; inspect it before retrying.' }
        $archive=Join-Path ([IO.Path]::GetTempPath()) ('gcp-audit-'+[guid]::NewGuid().ToString()+'.zip')
        $url='https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-589.0.0-windows-x86_64-bundled-python.zip'
        Invoke-WebRequest -Uri $url -OutFile $archive
        $expected='b9c2f4f296154f55e8a31a6979106573bc1ad8691041d4a32ea90c1834fdf995'
        if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expected) { throw 'SDK hash mismatch. Nothing was executed.' }
        Add-Type -AssemblyName System.IO.Compression.FileSystem
        $zip=[IO.Compression.ZipFile]::OpenRead($archive)
        try {
            $root=[IO.Path]::GetFullPath($sdkParent)+[IO.Path]::DirectorySeparatorChar
            foreach ($entry in $zip.Entries) {
                $target=[IO.Path]::GetFullPath((Join-Path $sdkParent $entry.FullName))
                if (-not $target.StartsWith($root,[StringComparison]::OrdinalIgnoreCase)) { throw 'Unsafe archive path' }
            }
        } finally { $zip.Dispose() }
        Expand-Archive -LiteralPath $archive -DestinationPath $sdkParent
        Remove-Item -LiteralPath $archive
    }
    $auditPython=$bundled
}
& $auditPython (Join-Path $PSScriptRoot 'audit.py') --procedure $Procedure --scope $Scope --output $Output
exit $LASTEXITCODE
