# File Inspection with ffprobe

`ffprobe` is included with ffmpeg and inspects media files without modifying them.

## Basic File Info

```bash
# JSON output with all stream and format info
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4
```

## Specific Queries

```bash
# Duration in seconds
ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.mp4

# File size in bytes
ffprobe -v quiet -show_entries format=size -of csv=p=0 input.mp4

# Video resolution
ffprobe -v quiet -select_streams v:0 -show_entries stream=width,height -of csv=p=0 input.mp4

# Video codec name
ffprobe -v quiet -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 input.mp4

# Audio codec and sample rate
ffprobe -v quiet -select_streams a:0 -show_entries stream=codec_name,sample_rate -of csv=p=0 input.mp4

# Number of streams
ffprobe -v quiet -show_entries format=nb_streams -of csv=p=0 input.mp4

# Bitrate
ffprobe -v quiet -show_entries format=bit_rate -of csv=p=0 input.mp4

# Frame rate
ffprobe -v quiet -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 input.mp4

# List all subtitle streams
ffprobe -v quiet -select_streams s -show_entries stream=index,codec_name,language -of csv=p=0 input.mkv
```

## Stream Mapping Overview

```bash
# Show all streams with their types and codecs
ffprobe -v quiet -show_entries stream=index,codec_type,codec_name -of csv=p=0 input.mp4
```

## Output Formats

`-of` (output format) options:
- `json` — structured JSON
- `csv=p=0` — CSV without header
- `flat` — flat key-value pairs
- `xml` — XML format

## Check if File is Valid

```bash
# Returns error code if file is corrupted
ffprobe -v error -read_intervals "%+#1" -show_entries format=duration -of csv=p=0 input.mp4
```

## Get All Chapters/Metadata

```bash
ffprobe -v quiet -show_chapters -show_entries format_tags -print_format json input.mp4
```
