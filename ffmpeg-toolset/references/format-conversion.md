# Format Conversion and Codecs

## Basic Conversion

Auto-detects codecs from output extension:

```bash
ffmpeg -i input.mp4 output.avi
ffmpeg -i input.mp3 output.ogg
```

## Codec Selection

Specify codecs with `-c:v` (video) and `-c:a` (audio):

```bash
ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mkv
ffmpeg -i input.webm -c:v vp9 -c:a libvorbis output.mkv
```

## Common Codec Choices

| Container | Video codec | Audio codec | Notes |
|-----------|-------------|-------------|-------|
| MP4 (web) | libx264 | aac | Best compatibility |
| MP4 (modern) | libx265 | aac | Smaller files, slower |
| WebM | libvpx-vp9 | libvorbis | Web-optimized |
| MKV | libx264 | flac | Flexible container |
| Audio only MP3 | — | libmp3lame | Use `-vn` to strip video |
| Audio only AAC | — | aac | Better quality than MP3 at same bitrate |
| Audio only FLAC | — | flac | Lossless |

## Quality Control

### CRF (Constant Rate Factor)

Recommended for x264/x265. Single-pass, quality-targeted encoding:

```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -c:a aac output.mp4
```

CRF scale: 0 (lossless) to 51 (worst). Default is 23.
- 18: Visually lossless
- 23: Default, good quality
- 28: Acceptable, smaller files

### Fixed Bitrate

Use when file size is a hard constraint:

```bash
ffmpeg -i input.mp4 -b:v 1M -b:a 128k output.mp4
```

### Two-Pass Encoding

For precise bitrate targets (e.g., exact file size):

```bash
# Pass 1
ffmpeg -i input.mp4 -c:v libx264 -b:v 2M -pass 1 -an -f null NUL

# Pass 2
ffmpeg -i input.mp4 -c:v libx264 -b:v 2M -pass 2 -c:a aac output.mp4
```

Windows: use `NUL`. Linux/macOS: use `/dev/null`.

### Preset (Encoding Speed vs Compression)

Controls encoding speed. Slower = better compression at same quality:

```bash
ffmpeg -i input.mp4 -c:v libx264 -preset medium output.mp4
```

Available presets (fastest to slowest): `ultrafast`, `superfast`, `veryfast`, `faster`, `fast`, `medium`, `slow`, `slower`, `veryslow`.

Default is `medium`. Use `fast` or `faster` for quick jobs, `slow` for archival.

### Pixel Format

Many players require `yuv420p`. Add when output won't play:

```bash
ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p output.mp4
```

## Stream Copy (No Re-encoding)

Fast, lossless container change:

```bash
ffmpeg -i input.mkv -c copy output.mp4
```

Only works when the input codecs are compatible with the output container.
