# Common Pitfalls and Gotchas

## Command Order Matters

- Options apply to the **next** file. `-c:v libx264 -i input.mp4` is wrong. It must be `-i input.mp4 -c:v libx264`.
- Global options (`-y`, `-n`, `-loglevel`) go before any `-i`.
- Input options (like `-ss` for fast seeking) go **before** `-i`.
- Output options go **after** `-i` and before the output file.

## `-c copy` Limitations

- Cannot be used with any filter (`-vf`, `-af`, `-filter_complex`).
- Cannot change codec, resolution, frame rate, or pixel format.
- May produce imprecise cuts when trimming (cuts only at keyframes).
- If the input codec is incompatible with the output container, the command will fail.

## Seeking Precision

- `-ss` **before** `-i`: Fast but may cut at the nearest keyframe (imprecise).
- `-ss` **after** `-i`: Accurate to the frame but slower (decodes from start).
- For best of both: place `-ss` before `-i` for rough seek, then trim precisely with re-encoding.

## Pixel Format Issues

Many players (especially QuickTime, Windows Media Player) require `yuv420p`. If output won't play:

```bash
ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p output.mp4
```

## PowerShell Escaping

On Windows PowerShell:
- Use double quotes around filter strings.
- Escape inner double quotes with backtick: `` "drawtext=text=`"Hello`":fontsize=24" ``
- Or use single quotes inside: `"drawtext=text='Hello':fontsize=24"`
- Backslashes in paths may need doubling: `subtitles='C:\\path\\subs.srt'`

## Audio Speed Limits

`atempo` only accepts values between 0.5 and 2.0. For larger changes, chain multiple instances:

```bash
# 4x speed
-af "atempo=2.0,atempo=2.0"

# 0.25x speed
-af "atempo=0.5,atempo=0.5"
```

## GIF File Size

GIFs can become very large. Keep them manageable:
- Width: max 480px (use `scale=480:-1`)
- FPS: max 10-15
- Duration: keep under 10 seconds
- Use two-pass palette generation for best quality/size ratio

## Two-Pass Encoding on Windows

Use `NUL` instead of `/dev/null`:

```bash
ffmpeg -i input.mp4 -c:v libx264 -b:v 2M -pass 1 -f null NUL
```

## Subtitle File Paths

The `subtitles` filter uses libavformat, which has trouble with Windows paths containing spaces or colons:

```bash
# Escape spaces and colons in Windows paths
ffmpeg -i input.mp4 -vf "subtitles='C\:\\path\\to\\my\ subs.srt'" output.mp4
```

## Stream Selection

When an input has multiple audio/subtitle streams, ffmpeg auto-selects one. To be explicit:

```bash
ffmpeg -i input.mkv -map 0:v:0 -map 0:a:1 -c copy output.mp4
```

## Hardware Acceleration

Hardware encoders exist but vary by platform:
- NVIDIA: `h264_nvenc`, `hevc_nvenc`
- Intel QSV: `h264_qsv`, `hevc_qsv`
- macOS VideoToolbox: `h264_videotoolbox`, `hevc_videotoolbox`
- AMD AMF: `h264_amf`, `hevc_amf`

These are faster but typically produce larger files at the same quality. Use software encoding (`libx264`) for best quality/size ratio.

## Memory and Large Files

- For very large files, use `-ss` before `-i` to avoid decoding the entire file.
- Use `-c copy` whenever possible to avoid re-encoding overhead.
- If ffmpeg runs out of memory, try adding `-threads 1` to limit parallelism.
