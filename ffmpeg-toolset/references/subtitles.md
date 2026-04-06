# Subtitles

## Burn Subtitles into Video (Hardsub)

Renders subtitles permanently into the video frames:

```bash
# From SRT file
ffmpeg -i input.mp4 -vf "subtitles=subs.srt" output.mp4

# From ASS/SSA file (supports styling)
ffmpeg -i input.mp4 -vf "ass=subs.ass" output.mp4
```

If the subtitle file path contains spaces or special characters, escape colons:

```bash
ffmpeg -i input.mp4 -vf "subtitles='path/to/my\ subs.srt'" output.mp4
```

## Embed Subtitles as a Stream (Softsub)

Subtitles can be toggled on/off by the player:

```bash
# Embed SRT as a subtitle stream in MP4
ffmpeg -i input.mp4 -i subs.srt -c:v copy -c:a copy -c:s mov_text output.mp4

# Embed SRT into MKV (native subtitle support)
ffmpeg -i input.mp4 -i subs.srt -c copy output.mkv
```

## Extract Subtitles

```bash
# Extract first subtitle stream to SRT
ffmpeg -i input.mkv -map 0:s:0 subs.srt

# Extract specific subtitle stream by index
ffmpeg -i input.mkv -map 0:s:1 subs_eng.srt
```

## Remove Subtitles

```bash
# Remove all subtitle streams
ffmpeg -i input.mkv -c copy -sn output.mkv
```

## Convert Subtitle Formats

```bash
# SRT to ASS
ffmpeg -i input.srt output.ass

# SRT to WebVTT
ffmpeg -i input.srt output.vtt
```

## Multiple Subtitle Tracks

```bash
# Add multiple subtitle streams
ffmpeg -i input.mp4 -i subs_en.srt -i subs_es.srt -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=eng -metadata:s:s:1 language=spa output.mp4
```
