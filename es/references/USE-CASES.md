# ES Use Cases

Practical examples and workflows for common file search tasks using `es.exe`.

> **When to load this file**: When you need concrete examples for specific search scenarios or want to combine multiple ES features.

## Prerequisites

Everything search client must be running. Install ES to PATH:

```powershell
# Recommended install location
%LOCALAPPDATA%\Microsoft\WindowsApps
```

## Base Command

```powershell
.\es.exe <searchterm> -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## File Discovery

### Find a file by name

```powershell
.\es.exe "report.pdf" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files by extension

```powershell
.\es.exe "ext:py" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find multiple extensions

```powershell
.\es.exe "ext:jpg;png;gif" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files in a specific directory

```powershell
.\es.exe "ext:md" -path "C:\projects\myapp" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files matching a pattern

```powershell
.\es.exe "readme*" -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## Size-Based Searches

### Find large files

```powershell
.\es.exe "size:>1gb" -instance 1.5a -double-quote -size -dc -dm -csv -sort size -sort-descending
```

### Find files in a size range

```powershell
.\es.exe "size:10mb..100mb" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find empty folders

```powershell
.\es.exe "empty:" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files by size category

```powershell
.\es.exe "size:gigantic" -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## Date-Based Searches

### Find files modified today

```powershell
.\es.exe "dm:today" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files modified this week

```powershell
.\es.exe "dm:thisweek" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files created in a date range

```powershell
.\es.exe "dc:2024-01-01..2024-12-31" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files modified in the last 7 days

```powershell
.\es.exe "dm:last7days" -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## Attribute-Based Searches

### Find hidden files

```powershell
.\es.exe "/ah" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find system files

```powershell
.\es.exe "/as" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find read-only files

```powershell
.\es.exe "/ar" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find compressed files

```powershell
.\es.exe "/ac" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Exclude hidden files

```powershell
.\es.exe "/a-H" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find folders only

```powershell
.\es.exe "/ad" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files only

```powershell
.\es.exe "/a-d" -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## Advanced Searches

### Regex search

```powershell
.\es.exe -regex "^\d{4}-\d{2}-\d{2}.*\.log$" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Case-sensitive search

```powershell
.\es.exe "README" -i -instance 1.5a -double-quote -size -dc -dm -csv
```

### Whole word search

```powershell
.\es.exe "config" -w -instance 1.5a -double-quote -size -dc -dm -csv
```

### Search full path

```powershell
.\es.exe "node_modules" -p -instance 1.5a -double-quote -size -dc -dm -csv
```

### Exclude terms

```powershell
.\es.exe "report !draft" -instance 1.5a -double-quote -size -dc -dm -csv
```

### OR search

```powershell
.\es.exe "todo|task|checklist" -instance 1.5a -double-quote -size -dc -dm -csv
```

---

## Export and Output

### Export to CSV file

```powershell
.\es.exe "ext:jpg" -path "C:\Photos" -export-csv "C:\output\photos.csv" -instance 1.5a -no-header
```

### Export to JSON

```powershell
.\es.exe "ext:py" -path "C:\projects\app" -export-json "C:\output\files.json" -instance 1.5a
```

### Export to text file

```powershell
.\es.exe "*.log" -dm:today -export-txt "C:\output\today_logs.txt" -instance 1.5a
```

### Limit results

```powershell
.\es.exe "ext:tmp" -n 50 -instance 1.5a -double-quote -size -dc -dm -csv
```

### Sort by date modified

```powershell
.\es.exe "ext:docx" -instance 1.5a -double-quote -size -dc -dm -csv -sort date-modified -sort-descending
```

---

## Query Information

### Count results without displaying

```powershell
.\es.exe "ext:exe" -get-result-count -instance 1.5a
```

### Get total size of results

```powershell
.\es.exe "ext:mp4" -path "C:\Videos" -get-total-size -instance 1.5a
```

### Get run count for a file

```powershell
.\es.exe -get-run-count "C:\tools\es.exe" -instance 1.5a
```

---

## Everything Management

### Force reindex

```powershell
.\es.exe -reindex -instance 1.5a
```

### Save database

```powershell
.\es.exe -save-db -instance 1.5a
```

### Exit Everything

```powershell
.\es.exe -exit -instance 1.5a
```

### Get Everything version

```powershell
.\es.exe -get-everything-version -instance 1.5a
```

---

## Combined Workflows

### Find and export all config files modified this week

```powershell
.\es.exe "ext:json;yaml;yml;toml;ini" -dm:thisweek -export-csv "C:\output\configs_this_week.csv" -instance 1.5a -no-header
```

### Find large video files sorted by size

```powershell
.\es.exe "ext:mp4;mkv;avi size:>500mb" -instance 1.5a -double-quote -size -dc -dm -csv -sort size -sort-descending
```

### Find duplicate-named files

```powershell
.\es.exe "dupe: ext:jpg" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find files with non-ASCII names

```powershell
.\es.exe -regex "[^\x00-\x7f]" -instance 1.5a -double-quote -size -dc -dm -csv
```

### Find all Python files excluding virtual environments

```powershell
.\es.exe "ext:py !venv !__pycache__ !.venv" -instance 1.5a -double-quote -size -dc -dm -csv
```

## Sources

- [GitHub Repository](https://github.com/voidtools/es)
- [Official Documentation](https://www.voidtools.com/support/everything/command_line_interface/)
- [Search Syntax Reference](https://www.voidtools.com/support/everything/searching/)
