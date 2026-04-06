# Audio Operations

## Extract Audio from Video

```bash
# Extract as MP3
ffmpeg -i input.mp4 -vn -c:a libmp3lame -q:a 2 output.mp3

# Extract as AAC
ffmpeg -i input.mp4 -vn -c:a aac -b:a 192k output.m4a

# Extract as FLAC (lossless)
ffmpeg -i input.mp4 -vn -c:a flac output.flac
```

`-vn` disables video. `-q:a 2` is VBR quality for MP3 (0=best, 9=worst, 2 is excellent).

## Replace Audio Track

```bash
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```

`-map 0:v:0` selects the first video stream from the first input. `-map 1:a:0` selects the first audio stream from the second input.

## Adjust Audio Volume

```bash
# Increase by 50%
ffmpeg -i input.mp4 -af "volume=1.5" output.mp4

# Decrease by half
ffmpeg -i input.mp4 -af "volume=0.5" output.mp4

# Set to specific dB level
ffmpeg -i input.mp4 -af "volume=3dB" output.mp4
```

## Normalize Audio

Loudness normalization (EBU R128 standard):

```bash
ffmpeg -i input.mp4 -af "loudnorm" output.mp4
```

## Convert Audio Format

```bash
# WAV to MP3
ffmpeg -i input.wav -c:a libmp3lame -q:a 2 output.mp3

# FLAC to AAC
ffmpeg -i input.flac -c:a aac -b:a 192k output.m4a

# MP3 to WAV
ffmpeg -i input.mp3 output.wav
```

## Audio Fading

```bash
# Fade in over first 2 seconds, fade out over last 2 seconds
ffmpeg -i input.mp3 -af "afade=t=in:st=0:d=2,afade=t=out:st=58:d=2" output.mp3
```

## Change Audio Speed

```bash
# Double speed
ffmpeg -i input.mp3 -af "atempo=2.0" output.mp3

# Half speed
ffmpeg -i input.mp3 -af "atempo=0.5" output.mp3
```

`atempo` range is 0.5 to 2.0. Chain for larger changes:

```bash
# 4x speed
ffmpeg -i input.mp3 -af "atempo=2.0,atempo=2.0" output.mp3
```

## Mix Audio Streams

```bash
# Mix two audio files into one
ffmpeg -i input1.mp3 -i input2.mp3 -filter_complex "amix=inputs=2:duration=first" output.mp3
```

## Trim Audio

```bash
# From 1:00 to 2:30
ffmpeg -i input.mp3 -ss 00:01:00 -to 00:02:30 -c copy output.mp3
```

## Concatenate Audio

```bash
# Same format files
ffmpeg -i "concat:input1.mp3|input2.mp3|input3.mp3" -c copy output.mp3
```

For different formats, use the concat demuxer:

```
file 'input1.mp3'
file 'input2.mp3'
file 'input3.mp3'
```

```bash
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp3
```
