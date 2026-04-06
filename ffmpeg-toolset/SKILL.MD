---
name: ffmpeg-toolset
description: Use ffmpeg for audio/video processing including format conversion, codec selection, trimming, concatenation, scaling, subtitle embedding, GIF creation, speed adjustment, and stream manipulation. Use when working with multimedia files.
compatibility: Requires ffmpeg installed on the system. ffprobe included with ffmpeg.
metadata:
  version: "1.0"
---

# FFmpeg Toolset

Use this skill when the user needs to process, convert, edit, or inspect audio/video files.

## Prerequisites

Verify `ffmpeg` is available:

```bash
ffmpeg -version
```

If not installed, inform the user:
- Windows: `winget install ffmpeg`
- macOS: `brew install ffmpeg`
- Linux: `apt install ffmpeg` or equivalent

## Command Structure

```
ffmpeg [global_options] {[input_options] -i input_file}... {[output_options] output_file}...
```

Core rules:
- Options apply to the **next** file in the command. Place input options before `-i`, output options after.
- `-c copy` skips re-encoding (fast, lossless). Use when only the container changes or for trimming.
- Use `-y` to overwrite output without prompting. Use `-n` to never overwrite.
- On Windows PowerShell, wrap filter strings in double quotes. Escape inner quotes with backtick.

## Quick Task Reference

| Task | Reference |
|------|-----------|
| Format conversion and codecs | `references/format-conversion.md` |
| Audio operations | `references/audio-operations.md` |
| Video operations (resize, speed, trim, concat) | `references/video-operations.md` |
| Filters (video, audio, complex) | `references/filters.md` |
| Subtitles | `references/subtitles.md` |
| File inspection with ffprobe | `references/inspection.md` |
| Common pitfalls | `references/gotchas.md` |

## Workflow

1. Identify the task (convert, trim, extract, filter, etc.)
2. Load the relevant reference file for detailed commands
3. Construct the command following the syntax rules above
4. Run the command and verify output
5. If the output has issues, consult `references/gotchas.md`

## General Guidelines

- Prefer `-c copy` when no re-encoding is needed (fastest, no quality loss).
- For re-encoding video, use CRF mode (`-crf 18-28`) over fixed bitrate for better quality/size balance.
- Always ensure output pixel format is `yuv420p` for maximum compatibility: add `-pix_fmt yuv420p`.
- For long files, place `-ss` before `-i` for fast seeking.
- Use `ffprobe` to inspect files before modifying them when the input structure is unknown.
