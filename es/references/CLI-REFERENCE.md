# ES CLI Reference

Complete command-line reference for `es.exe` (Everything Search Engine CLI).

> **When to load this file**: When you need the full list of options, flags, or advanced configuration not covered in the core skill instructions.

## Version

ES 1.1.0.30 (latest stable: 1.1.0.36)

## Usage

```
es.exe [options] search text
```

Example:

```
es everything ext:exe;ini
```

---

## Search Options

### Text Matching

| Flag | Aliases | Description |
|------|---------|-------------|
| `-r` | `-regex` | Search using regular expressions |
| `-i` | `-case` | Match case |
| `-w` | `-ww`, `-whole-word`, `-whole-words` | Match whole words |
| `-p` | `-match-path` | Match full path and file name |
| `-a` | `-diacritics` | Match diacritical marks |

### Result Pagination

| Flag | Aliases | Description |
|------|---------|-------------|
| `-o <offset>` | `-offset <offset>` | Show results starting from offset |
| `-n <num>` | `-max-results <num>` | Limit the number of results shown |

### Path Scoping

| Flag | Description |
|------|-------------|
| `-path <path>` | Search for subfolders and files in path |
| `-parent-path <path>` | Search for subfolders and files in the parent of path |
| `-parent <path>` | Search for files with the specified parent path |

### Attribute Filters (DIR-style)

| Flag | Description |
|------|-------------|
| `/ad` | Folders only |
| `/a-d` | Files only |
| `/a[RHSDAVNTPLCOIE]` | Attribute-based filtering (see below) |

#### Attribute Flags

| Flag | Meaning |
|------|---------|
| `R` | Read only |
| `H` | Hidden |
| `S` | System |
| `D` | Directory |
| `A` | Archive |
| `V` | Device |
| `N` | Normal |
| `T` | Temporary |
| `P` | Sparse file |
| `L` | Reparse point |
| `C` | Compressed |
| `O` | Offline |
| `I` | Not content indexed |
| `E` | Encrypted |

Prefix a flag with `-` to exclude. Example: `/a-H` excludes hidden files.

---

## Sort Options

### Simple Sort

| Flag | Description |
|------|-------------|
| `-s` | Sort by full path |

### Named Sort

```
-sort <name[-ascending|-descending]>
-sort-<name>[-ascending|-descending]
```

Available sort fields:

| Field | Description |
|-------|-------------|
| `name` | File name |
| `path` | Full path |
| `size` | File size |
| `extension` | File extension |
| `date-created` | Creation date |
| `date-modified` | Modification date |
| `date-accessed` | Last access date |
| `attributes` | File attributes |
| `file-list-file-name` | File list name |
| `run-count` | Run count |
| `date-recently-changed` | Recently changed date |
| `date-run` | Last run date |

### Sort Order

| Flag | Description |
|------|-------------|
| `-sort-ascending` | Ascending order |
| `-sort-descending` | Descending order |

### DIR-style Sorts

| Flag | Description |
|------|-------------|
| `/on` | Sort by name |
| `/o-n` | Sort by name (descending) |
| `/os` | Sort by size |
| `/o-s` | Sort by size (descending) |
| `/oe` | Sort by extension |
| `/o-e` | Sort by extension (descending) |
| `/od` | Sort by date modified |
| `/o-d` | Sort by date modified (descending) |

---

## Display Options

### Columns

Use these flags to show specific columns in output:

| Flag | Aliases | Description |
|------|---------|-------------|
| `-name` | | File name only |
| `-path-column` | | Path column |
| `-full-path-and-name` | `-filename-column` | Full path and name |
| `-extension` | `-ext` | File extension |
| `-size` | | File size |
| `-date-created` | `-dc` | Date created |
| `-date-modified` | `-dm` | Date modified |
| `-date-accessed` | `-da` | Date accessed |
| `-attributes` | `-attribs`, `-attrib` | File attributes |
| `-file-list-file-name` | | File list file name |
| `-run-count` | | Run count |
| `-date-run` | | Date run |
| `-date-recently-changed` | `-rc` | Date recently changed |

### Highlighting

| Flag | Description |
|------|-------------|
| `-highlight` | Highlight results |
| `-highlight-color <color>` | Highlight color (0x00-0xFF) |

### Output Formats

| Flag | Description |
|------|-------------|
| `-csv` | CSV format |
| `-efu` | EFU format (Everything file list) |
| `-json` | JSON format |
| `-m3u` | M3U playlist |
| `-m3u8` | M3U8 playlist (UTF-8) |
| `-tsv` | Tab-separated values |
| `-txt` | Plain text |

### Format Configuration

#### Size Format

```
-size-format <format>
```

| Value | Format |
|-------|--------|
| `0` | Auto |
| `1` | Bytes |
| `2` | KB |
| `3` | MB |

#### Date Format

```
-date-format <format>
```

| Value | Format |
|-------|--------|
| `0` | Auto |
| `1` | ISO-8601 |
| `2` | FILETIME |
| `3` | ISO-8601 (UTC) |

### Column Colors

Set column colors (0x00-0xFF):

| Flag | Aliases |
|------|---------|
| `-filename-color <color>` | |
| `-name-color <color>` | |
| `-path-color <color>` | |
| `-extension-color <color>` | |
| `-size-color <color>` | |
| `-date-created-color <color>` | `-dc-color <color>` |
| `-date-modified-color <color>` | `-dm-color <color>` |
| `-date-accessed-color <color>` | `-da-color <color>` |
| `-attributes-color <color>` | |
| `-file-list-filename-color <color>` | |
| `-run-count-color <color>` | |
| `-date-run-color <color>` | |
| `-date-recently-changed-color <color>` | `-rc-color <color>` |

### Column Widths

Set column widths (0-200):

| Flag | Aliases |
|------|---------|
| `-filename-width <width>` | |
| `-name-width <width>` | |
| `-path-width <width>` | |
| `-extension-width <width>` | |
| `-size-width <width>` | |
| `-date-created-width <width>` | `-dc-width <width>` |
| `-date-modified-width <width>` | `-dm-width <width>` |
| `-date-accessed-width <width>` | `-da-width <width>` |
| `-attributes-width <width>` | |
| `-file-list-filename-width <width>` | |
| `-run-count-width <width>` | |
| `-date-run-width <width>` | |
| `-date-recently-changed-width <width>` | `-rc-width <width>` |

### Number Formatting

| Flag | Description |
|------|-------------|
| `-no-digit-grouping` | Don't group numbers with commas |
| `-size-leading-zero` | Format size with leading zeros (use with `-no-digit-grouping`) |
| `-run-count-leading-zero` | Format run count with leading zeros |
| `-double-quote` | Wrap paths and filenames with double quotes |

---

## Export Options

### Export to File

| Flag | Description |
|------|-------------|
| `-export-csv <out.csv>` | Export to CSV file |
| `-export-efu <out.efu>` | Export to EFU file |
| `-export-json <out.json>` | Export to JSON file |
| `-export-m3u <out.m3u>` | Export to M3U playlist |
| `-export-m3u8 <out.m3u8>` | Export to M3U8 playlist |
| `-export-tsv <out.txt>` | Export to TSV file |
| `-export-txt <out.txt>` | Export to text file |

### Export Options

| Flag | Description |
|------|-------------|
| `-no-header` | Do not output a column header for CSV, EFU and TSV files |
| `-utf8-bom` | Store a UTF-8 byte order mark at the start of the exported file |

---

## General Options

### Help

| Flag | Description |
|------|-------------|
| `-h` | Display help |
| `-help` | Display help |

### Connection

| Flag | Description |
|------|-------------|
| `-instance <name>` | Connect to the unique Everything instance name |
| `-ipc1` | Use IPC version 1 |
| `-ipc2` | Use IPC version 2 |

### Output Control

| Flag | Aliases | Description |
|------|---------|-------------|
| `-pause` | `-more` | Pause after each page of output |
| `-hide-empty-search-results` | | Don't show any results when there is no search |
| `-empty-search-help` | | Show help when no search is specified |
| `-timeout <milliseconds>` | | Timeout waiting for Everything database to load |

### Run Count Management

| Flag | Description |
|------|-------------|
| `-set-run-count <filename> <count>` | Set the run count for the specified filename |
| `-inc-run-count <filename>` | Increment the run count for the specified filename by one |
| `-get-run-count <filename>` | Display the run count for the specified filename |

### Query Information

| Flag | Description |
|------|-------------|
| `-get-result-count` | Display the result count for the specified search |
| `-get-total-size` | Display the total result size for the specified search |

### Settings

| Flag | Description |
|------|-------------|
| `-save-settings` | Save settings |
| `-clear-settings` | Clear settings |

### Version and Info

| Flag | Description |
|------|-------------|
| `-version` | Display ES major.minor.revision.build version and exit |
| `-get-everything-version` | Display Everything major.minor.revision.build version and exit |

### Everything Control

| Flag | Description |
|------|-------------|
| `-exit` | Exit Everything. Returns after Everything process closes. |
| `-save-db` | Save the Everything database to disk. Returns after saving completes. |
| `-reindex` | Force Everything to reindex. Returns after indexing completes. |

### Error Handling

| Flag | Description |
|------|-------------|
| `-no-result-error` | Set the error level if no results are found |

---

## Notes

- Internal `-`'s in options can be omitted, e.g., `-nodigitgrouping`
- Switches can also start with a `/` instead of `-`
- Use double quotes to escape spaces and switches
- Switches can be disabled by prefixing with `no-`, e.g., `-no-size`
- Use a `^` prefix or wrap with double quotes (`"`) to escape `\ & | > < ^` in a command prompt

---

## Sources

- [GitHub Repository](https://github.com/voidtools/es)
- [Official Documentation](https://www.voidtools.com/support/everything/command_line_interface/)
- [Downloads](https://www.voidtools.com/downloads#cli)
