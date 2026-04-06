# ES Error Codes

Reference for ES exit codes and error levels.

> **When to load this file**: When debugging ES command failures or interpreting return codes from scripts.

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | No known error, search successful |
| `1` | Failed to register window class |
| `2` | Failed to create listening window |
| `3` | Out of memory |
| `4` | Expected an additional command line option with the specified switch |
| `5` | Failed to create export output file |
| `6` | Unknown switch |
| `7` | Failed to send Everything IPC a query |
| `8` | No Everything IPC window — make sure the Everything search client is running |
| `9` | No results found (only when used with `-no-result-error`) |

## Common Troubleshooting

### Exit Code 8 — Everything Not Running

The most common error. ES requires the Everything search client to be running in the background.

**Fix**: Launch Everything (the GUI application) before running ES commands.

### Exit Code 5 — Export File Failed

The output path for `-export-*` options is invalid or inaccessible.

**Fix**: Ensure the directory exists and you have write permissions.

### Exit Code 6 — Unknown Switch

A command-line option is misspelled or not recognized.

**Fix**: Check option spelling. Internal `-` characters can be omitted (e.g., `-doublequote` works for `-double-quote`).

### Exit Code 7 — IPC Query Failed

Communication with Everything failed mid-query.

**Fix**: Restart Everything and try again. Check for firewall interference.

## Using Error Codes in Scripts

### PowerShell

```powershell
.\es.exe "searchterm" -instance 1.5a -no-result-error
if ($LASTEXITCODE -eq 9) {
    Write-Host "No results found"
} elseif ($LASTEXITCODE -ne 0) {
    Write-Host "Error code: $LASTEXITCODE"
}
```

### Batch

```batch
es.exe "searchterm" -instance 1.5a -no-result-error
if %ERRORLEVEL% EQU 9 (
    echo No results found
) else if %ERRORLEVEL% NEQ 0 (
    echo Error code: %ERRORLEVEL%
)
```

## Sources

- [GitHub Repository](https://github.com/voidtools/es)
- [Official Documentation](https://www.voidtools.com/support/everything/command_line_interface/)
