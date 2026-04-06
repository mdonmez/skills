# Video Operations

## Resize / Scale

```bash
# Fixed dimensions
ffmpeg -i input.mp4 -vf "scale=1280:720" output.mp4

# Width fixed, height auto (preserve aspect ratio)
ffmpeg -i input.mp4 -vf "scale=1280:-2" output.mp4

# Height fixed, width auto
ffmpeg -i input.mp4 -vf "scale=-2:720" output.mp4

# Scale to half size
ffmpeg -i input.mp4 -vf "scale=iw/2:ih/2" output.mp4
```

Use `-2` instead of `-1` to ensure dimensions are divisible by 2 (required by most codecs).

## Change Frame Rate

```bash
# Set to 30 fps
ffmpeg -i input.mp4 -r 30 output.mp4

# Set to 60 fps (interpolates frames)
ffmpeg -i input.mp4 -r 60 -vf "minterpolate=fps=60" output.mp4
```

## Change Playback Speed

```bash
# Double speed (video only)
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" output.mp4

# Half speed (video only)
ffmpeg -i input.mp4 -vf "setpts=2.0*PTS" output.mp4

# Double speed with audio
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" -af "atempo=2.0" output.mp4

# Quarter speed with audio
ffmpeg -i input.mp4 -vf "setpts=4.0*PTS" -af "atempo=0.5,atempo=0.5" output.mp4
```

`atempo` range is 0.5-2.0 per instance. Chain multiple for larger changes.

## Rotate Video

```bash
# 90 degrees clockwise
ffmpeg -i input.mp4 -vf "transpose=1" output.mp4

# 90 degrees counter-clockwise
ffmpeg -i input.mp4 -vf "transpose=2" output.mp4

# 180 degrees
ffmpeg -i input.mp4 -vf "transpose=1,transpose=1" output.mp4
```

Transpose values: `0` = 90 CCW + vertical flip, `1` = 90 CW, `2` = 90 CCW, `3` = 90 CW + vertical flip.

## Trim / Cut Video

```bash
# Fast trim (stream copy, may have imprecise cuts at keyframe boundaries)
ffmpeg -i input.mp4 -c copy -ss 00:01:00 -to 00:02:30 output.mp4

# Precise trim (re-encodes, accurate to the frame)
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:30 -c:v libx264 -c:a aac output.mp4

# Trim by duration instead of end time
ffmpeg -i input.mp4 -c copy -ss 00:01:00 -t 30 output.mp4
```

`-ss` before `-i` = fast seeking. `-ss` after `-i` = accurate but slower. For precise cuts, put `-ss` before `-i` and re-encode.

## Concatenate Videos

### Same codec/format (fast, no re-encode)

Create a file list:

```
file 'input1.mp4'
file 'input2.mp4'
file 'input3.mp4'
```

```bash
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
```

PowerShell:
```powershell
"file 'input1.mp4'", "file 'input2.mp4'", "file 'input3.mp4'" | Set-Content list.txt
```

### Different formats (requires re-encoding)

```bash
ffmpeg -i input1.mp4 -i input2.webm -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" output.mp4
```

## Extract Frames / Thumbnails

```bash
# Single frame at timestamp
ffmpeg -i input.mp4 -ss 00:00:05 -vframes 1 thumbnail.jpg

# Frame every N seconds (every 10 seconds)
ffmpeg -i input.mp4 -vf "fps=1/10" frame_%03d.jpg

# Every Nth frame
ffmpeg -i input.mp4 -vf "select=mod(n\,100)" -vsync vfr frame_%03d.png

# Best quality thumbnail with scaling
ffmpeg -i input.mp4 -ss 00:01:00 -vframes 1 -vf "scale=320:-1" thumb.jpg
```

## Create Video from Images

```bash
# From numbered images (img_001.jpg, img_002.jpg, ...)
ffmpeg -framerate 24 -i img_%03d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4

# From a single image (still video for N seconds)
ffmpeg -loop 1 -i image.jpg -c:v libx264 -t 10 -pix_fmt yuv420p output.mp4
```

## Create GIF from Video

```bash
# Basic GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos" -loop 0 output.gif

# Higher quality with palette generation (recommended)
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -lavfi "fps=10,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

Two-pass palette generation produces much better GIF quality. Keep fps under 15 and width under 480px to control file size.

## Crop Video

```bash
# Crop to 640x480 starting at position (100, 50)
ffmpeg -i input.mp4 -vf "crop=640:480:100:50" output.mp4

# Crop center square
ffmpeg -i input.mp4 -vf "crop=ih:ih" output.mp4
```

## Flip / Mirror

```bash
# Horizontal flip
ffmpeg -i input.mp4 -vf "hflip" output.mp4

# Vertical flip
ffmpeg -i input.mp4 -vf "vflip" output.mp4
```

## Add Padding / Letterbox

```bash
# Add black padding to make 1920x1080
ffmpeg -i input.mp4 -vf "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black" output.mp4
```
