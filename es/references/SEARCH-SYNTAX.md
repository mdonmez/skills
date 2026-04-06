# Everything Search Syntax Reference

Complete reference for Everything search syntax and functions.

> **When to load this file**: When you need to construct complex search queries, use search functions, or understand Everything's query language for use with `es.exe`.

## Core Operators

| Operator | Description |
|----------|-------------|
| ` ` (space) | AND — both terms must match |
| `\|` | OR — either term matches |
| `!` | NOT — exclude matches |
| `< >` | Grouping |
| `" "` | Exact phrase / escape spaces |

## Wildcards

| Wildcard | Description |
|----------|-------------|
| `*` | Matches zero or more characters |
| `?` | Matches exactly one character |

> Wildcards match the *whole* filename by default. Disable "Match whole filename when using wildcards" in Everything options to match anywhere.

## Macros

| Macro | Description |
|-------|-------------|
| `quot:` | Literal double quote `"` |
| `apos:` | Literal apostrophe `'` |
| `amp:` | Literal ampersand `&` |
| `lt:` | Literal less than `<` |
| `gt:` | Literal greater than `>` |
| `#<n>:` | Unicode character <n> in decimal |
| `#x<n>:` | Unicode character <n> in hexadecimal |
| `audio:` | Search for audio files |
| `zip:` | Search for compressed files |
| `doc:` | Search for document files |
| `exe:` | Search for executable files |
| `pic:` | Search for picture files |
| `video:` | Search for video files |

## Modifiers

Prefix functions or search terms with these modifiers:

| Modifier | Description |
|----------|-------------|
| `ascii:` / `noascii:` | Enable/disable fast ASCII case comparisons |
| `utf8:` | UTF-8 encoding |
| `case:` / `nocase:` | Match/ignore case |
| `diacritics:` / `nodiacritics:` | Match/ignore accent marks |
| `file:` / `files:` / `nofileonly:` | Match files only |
| `folder:` / `folders:` / `nofolderonly:` | Match folders only |
| `path:` / `nopath:` | Match full path and filename or just filename |
| `regex:` / `noregex:` | Enable/disable regex |
| `wfn:` / `wholefilename:` / `nowfn:` / `nowholefilename:` / `exact:` | Match whole filename or anywhere |
| `wholeword:` / `ww:` / `nowholeword:` / `noww:` | Match whole words or anywhere |
| `wildcards:` / `nowildcards:` | Enable/disable wildcards |

## Search Functions

### File Properties

| Function | Description |
|----------|-------------|
| `ext:<list>` | Files with matching extension (semicolon-delimited) |
| `size:<size>` | Files with specified size |
| `type:<type>` | Files with specified file type |
| `attrib:<attributes>` / `attributes:<attributes>` | Files with specified attributes |
| `len:<length>` | Files matching filename length |
| `startwith:<text>` | Filenames starting with text |
| `endwith:<text>` | Filenames ending with text |
| `empty:` | Empty folders |
| `root:` | Files/folders with no parent |
| `depth:<count>` / `parents:<count>` | Files at specified folder depth |
| `frn:<frnlist>` | Files by File Reference Numbers (semicolon-delimited) |
| `fsi:<index>` | Files in specified file system index |
| `filelist:<list>` | Files in pipe-delimited file list |
| `filelistfilename:<filename>` | Files belonging to a file list |

### Date Functions

| Function | Aliases | Description |
|----------|---------|-------------|
| `datecreated:<date>` | `dc:<date>` | Files created on date |
| `datemodified:<date>` | `dm:<date>` | Files modified on date |
| `dateaccessed:<date>` | `da:<date>` | Files accessed on date |
| `daterun:<date>` | `dr:<date>` | Files run on date |
| `recentchange:<date>` | `rc:<date>` | Files recently changed |

### Path Functions

| Function | Aliases | Description |
|----------|---------|-------------|
| `parent:<path>` | `infolder:<path>` / `nosubfolders:<path>` | Files in path, excluding subfolders |
| `child:<filename>` | | Folders containing a child with matching filename |
| `childcount:<count>` | | Folders with specified number of children |
| `childfilecount:<count>` | | Folders with specified number of files |
| `childfoldercount:<count>` | | Folders with specified number of subfolders |
| `shell:<name>` | | Known shell folders (e.g., `shell:desktop`) |

### Content Search

> **Warning**: Content searching is extremely slow. File content is not indexed. Always combine `content:` with other filters.

| Function | Description |
|----------|-------------|
| `content:<text>` | Search file content (uses iFilter or UTF-8) |
| `ansicontent:<text>` | Content as ANSI text |
| `utf8content:<text>` | Content as UTF-8 text |
| `utf16content:<text>` | Content as UTF-16 (Unicode) |
| `utf16becontent:<text>` | Content as UTF-16 (Big Endian) |

### Image Properties

> Image info is not indexed. Combine with other searches for performance. Supports jpg, png, gif, bmp.

| Function | Description |
|----------|-------------|
| `width:<width>` | Image width in pixels |
| `height:<height>` | Image height in pixels |
| `dimension:<width>x<height>` | Image dimensions |
| `orientation:<type>` | `landscape` or `portrait` |
| `bitdepth:<bitdepth>` | Bits per pixel |

### Audio/ID3 Tags

> ID3/FLAC tags are not indexed. Combine with other searches. Only mp3 ID3 tags supported.

| Function | Description |
|----------|-------------|
| `artist:<artist>` | Song artist |
| `album:<album>` | Album name |
| `title:<title>` | Song title |
| `genre:<genre>` | Track genre |
| `comment:<comment>` | Track comment |
| `track:<track>` | Track number or range |
| `year:<year>` | Year or year range |

### Duplicate Detection

| Function | Description |
|----------|-------------|
| `dupe:` | Same filename |
| `namepartdupe:` | Same name part (excluding extension) |
| `attribdupe:` | Same attributes |
| `sizedupe:` | Same size |
| `dadupe:` | Same date accessed |
| `dcdupe:` | Same date created |
| `dmdupe:` | Same date modified |

### Run Count

| Function | Description |
|----------|-------------|
| `runcount:<count>` | Files with specified run count |

### Result Limiting

| Function | Description |
|----------|-------------|
| `count:<max>` | Limit results to max |

## Function Syntax

All functions support comparison operators:

| Syntax | Description |
|--------|-------------|
| `function:value` | Equal to value |
| `function:=value` | Equal to value |
| `function:<value` | Less than value |
| `function:<=value` | Less than or equal |
| `function:>value` | Greater than value |
| `function:>=value` | Greater than or equal |
| `function:start..end` | Range (inclusive) |
| `function:start-end` | Range (inclusive) |

## Size Syntax

### Units

| Suffix | Description |
|--------|-------------|
| `kb` | Kilobytes |
| `mb` | Megabytes |
| `gb` | Gigabytes |

### Size Constants

| Constant | Range |
|----------|-------|
| `empty` | 0 bytes |
| `tiny` | 0 KB < size <= 10 KB |
| `small` | 10 KB < size <= 100 KB |
| `medium` | 100 KB < size <= 1 MB |
| `large` | 1 MB < size <= 16 MB |
| `huge` | 16 MB < size <= 128 MB |
| `gigantic` | size > 128 MB |
| `unknown` | Unknown size |

## Date Syntax

### Formats

| Format | Description |
|--------|-------------|
| `YYYY[-MM[-DD[Thh[:mm[:ss[.sss]]]]]]` | ISO-style date/time |
| `YYYYMM[DD[Thh[mm[ss[.sss]]]]]` | Compact date/time |
| `year` | Year only |
| `month/year` or `year/month` | Depends on locale |
| `day/month/year` or variants | Depends on locale |

### Date Constants

| Constant | Description |
|----------|-------------|
| `today` | Today |
| `yesterday` | Yesterday |
| `<last\|past\|prev\|current\|this\|coming\|next><year\|month\|week>` | Relative periods |
| `<last\|past\|prev\|coming\|next><x><years\|months\|weeks>` | N periods ago/ahead |
| `<last\|past\|prev\|coming\|next><x><hours\|minutes\|mins\|seconds\|secs>` | N time units |
| `january` through `december` (or `jan`-`dec`) | Month names |
| `sunday` through `saturday` (or `sun`-`sat`) | Day names |
| `unknown` | Unknown date |

## Attribute Constants

| Constant | Meaning |
|----------|---------|
| `A` | Archive |
| `C` | Compressed |
| `D` | Directory |
| `E` | Encrypted |
| `H` | Hidden |
| `I` | Not content indexed |
| `L` | Reparse point |
| `N` | Normal |
| `O` | Offline |
| `P` | Sparse file |
| `R` | Read only |
| `S` | System |
| `T` | Temporary |

## Regular Expressions

Regex overrides normal search syntax. Enable with `-regex` flag or `regex:` prefix. When using `regex:` modifier, escape `\|` and space with double quotes.

| Pattern | Description |
|---------|-------------|
| `a\|b` | Matches a or b |
| `.` | Any single character |
| `[abc]` | Single character a, b, or c |
| `[^abc]` | Any character except a, b, c |
| `[a-z]` | Character range |
| `^` | Start of filename |
| `$` | End of filename |
| `*` | Preceding element zero or more times |
| `?` | Preceding element zero or one times |
| `+` | Preceding element one or more times |
| `{x}` | Preceding element exactly x times |
| `{x,}` | Preceding element x or more times |
| `{x,y}` | Preceding element between x and y times |
| `\` | Escape special character |

## Examples

| Query | Description |
|-------|-------------|
| `ABC 123` | Files containing both "ABC" AND "123" |
| `ABC\|123` | Files containing "ABC" OR "123" |
| `!ABC` | Files NOT containing "ABC" |
| `case:ABC` | Uppercase "ABC" only |
| `*.mp3` | All MP3 files |
| `d:\|e: *.mp3` | MP3 files on D: or E: drive |
| `d: *.jpg\|*.png` | JPG or PNG files on D: drive |
| `!.` | Files/folders with no extension |
| `file:` | Files only |
| `folder:` | Folders only |
| `parent:c:\windows` | Files directly in c:\windows |
| `size:>1mb` | Files larger than 1MB |
| `size:2mb..10mb` | Files between 2MB and 10MB |
| `dm:today` | Files modified today |
| `dm:thisweek` | Files modified this week |
| `d:\music\ !child:mp3` | Folders in D:\music without MP3 files |
| `regex:[^\x00-\x7f]` | Files with non-ASCII characters |
| `count:100` | Limit to 100 results |

## Sources

- [Everything Search Documentation](https://www.voidtools.com/support/everything/searching/)
- [GitHub Repository](https://github.com/voidtools/es)
