---
name: es
description: Command-line interface to the Everything search engine for instant file and folder searches on Windows. Use when searching for files by name, extension, size, date, or attributes, or when exporting search results. Requires Everything desktop app running. Always use this base format for searches -> es <searchterm> -instance 1.5a -double-quote -size -dc -dm -csv
compatibility: Requires Everything search client running on Windows. ES CLI installed (es.exe).
---

# ES (Everything Search CLI)

Command-line interface to the Everything search engine for instant file system searches on Windows.

## Prerequisites

Everything desktop application must be running. ES communicates via IPC.

## Base Command Format

Always use this base format for searches:

```powershell
es <searchterm> -instance 1.5a -double-quote -size -dc -dm -csv
```

Flag breakdown:

| Flag | Purpose |
|------|---------|
| `-instance 1.5a` | Connect to Everything 1.5a instance |
| `-double-quote` | Wrap paths/filenames in double quotes |
| `-size` | Show file size column |
| `-dc` | Show date created column |
| `-dm` | Show date modified column |
| `-csv` | Output in CSV format for easy parsing |

## Quick Reference

### Common Search Patterns

| Query | Description |
|-------|-------------|
| `"report.pdf"` | Find files containing "report.pdf" |
| `ext:py` | All Python files |
| `ext:jpg;png` | JPG or PNG files |
| `size:>1gb` | Files larger than 1GB |
| `dm:today` | Modified today |
| `!venv` | Exclude "venv" |
| `foo \| bar` | Contains "foo" OR "bar" |

### Most Used Flags

| Flag | Description |
|------|-------------|
| `-path <dir>` | Search within directory |
| `-n <num>` | Limit results |
| `-sort size` | Sort by size |
| `-sort-descending` | Descending order |
| `/ad` | Folders only |
| `/a-d` | Files only |
| `/ah` | Hidden files |
| `-regex` | Enable regex |
| `-export-csv <file>` | Export to CSV |
| `-get-result-count` | Count only |

## Workflows

### Find files by extension in a project

```powershell
.\es.exe "ext:py" -path "C:\projects\myapp" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find large files sorted by size

```powershell
.\es.exe "size:>1gb" -instance 1.5a -double-quote -size -dc -dm -csv -sort size -sort-descending
```

### Find recently modified files

```powershell
.\es.exe "dm:thisweek" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Export results to file

```powershell
.\es.exe "ext:jpg" -path "C:\Photos" -export-csv "C:\output\photos.csv" -instance 1.5a -no-header
```

### Exclude patterns

```powershell
.\es.exe "ext:py !venv !__pycache__" -instance 1.5a -double-quote -size -dc -dm -csv
```

## Error Handling

If ES returns a non-zero exit code, check [references/ERROR-CODES.md](references/ERROR-CODES.md). The most common error is code `8` — Everything is not running.

## Reference Files

Load these on demand for detailed information:

- **[references/CLI-REFERENCE.md](references/CLI-REFERENCE.md)** — Full CLI option reference (all flags, colors, widths, export options)
- **[references/SEARCH-SYNTAX.md](references/SEARCH-SYNTAX.md)** — Complete Everything search syntax (functions, modifiers, regex, date/size syntax)
- **[references/ERROR-CODES.md](references/ERROR-CODES.md)** — Exit codes, troubleshooting, scripting patterns
- **[references/USE-CASES.md](references/USE-CASES.md)** — Extended examples and combined workflows

## Sources

- [GitHub Repository](https://github.com/voidtools/es)
- [Official Documentation](https://www.voidtools.com/support/everything/command_line_interface/)
- [Search Syntax](https://www.voidtools.com/support/everything/searching/)
