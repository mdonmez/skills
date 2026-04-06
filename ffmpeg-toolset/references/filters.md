# Filters

## Video Filters (`-vf`)

### Scale

```bash
ffmpeg -i input.mp4 -vf "scale=1280:720" output.mp4
```

### Crop

```bash
ffmpeg -i input.mp4 -vf "crop=w:h:x:y" output.mp4
```

### Overlay / Watermark

```bash
ffmpeg -i input.mp4 -i watermark.png -filter_complex "[0:v][1:v]overlay=10:10" output.mp4
```

Position: `overlay=W-w-10:10` for top-right, `overlay=10:H-h-10` for bottom-left.

### Draw Text

```bash
ffmpeg -i input.mp4 -vf "drawtext=text='Hello World':fontsize=24:fontcolor=white:x=10:y=10" output.mp4
```

### Fade

```bash
# Video fade in/out
ffmpeg -i input.mp4 -vf "fade=t=in:st=0:d=1,fade=t=out:st=9:d=1" output.mp4
```

### Stabilize

```bash
# Two-pass stabilization
ffmpeg -i input.mp4 -vf "vidstabdetect=shakiness=5:accuracy=15" -f null -
ffmpeg -i input.mp4 -vf "vidstabtransform=smoothing=10:input=transforms.trf" output.mp4
```

### Denoise

```bash
ffmpeg -i input.mp4 -vf "nlmeans" output.mp4
```

### Sharpen

```bash
ffmpeg -i input.mp4 -vf "unsharp=5:5:1.0:5:5:0.0" output.mp4
```

### Color Correction

```bash
# Adjust brightness, contrast, saturation
ffmpeg -i input.mp4 -vf "eq=brightness=0.06:contrast=1.1:saturation=1.2" output.mp4
```

## Audio Filters (`-af`)

### Volume

```bash
ffmpeg -i input.mp4 -af "volume=1.5" output.mp4
```

### Loudness Normalization

```bash
ffmpeg -i input.mp4 -af "loudnorm" output.mp4
```

### Fade

```bash
ffmpeg -i input.mp4 -af "afade=t=in:st=0:d=2,afade=t=out:st=58:d=2" output.mp4
```

### Noise Reduction

```bash
ffmpeg -i input.mp3 -af "afftdn=nf=-25" output.mp3
```

### Equalizer

```bash
# Boost bass, reduce treble
ffmpeg -i input.mp3 -af "equalizer=f=100:t=h:w=100:g=5,equalizer=f=8000:t=h:w=2000:g=-3" output.mp3
```

## Complex Filtergraphs (`-filter_complex`)

Used when combining multiple inputs or applying chains that produce multiple outputs.

### Picture-in-Picture

```bash
ffmpeg -i main.mp4 -i pip.mp4 -filter_complex "[1:v]scale=320:-1[pip];[0:v][pip]overlay=W-w-10:H-h-10" output.mp4
```

### Side-by-Side

```bash
# Horizontal
ffmpeg -i left.mp4 -i right.mp4 -filter_complex "[0:v][1:v]hstack=inputs=2" output.mp4

# Vertical
ffmpeg -i top.mp4 -i bottom.mp4 -filter_complex "[0:v][1:v]vstack=inputs=2" output.mp4
```

### Grid (2x2)

```bash
ffmpeg -i tl.mp4 -i tr.mp4 -i bl.mp4 -i br.mp4 -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0" output.mp4
```

### Split Stream (apply different filters to same input)

```bash
ffmpeg -i input.mp4 -filter_complex "[0:v]split=2[a][b];[a]scale=640:-1[scaled];[b]crop=640:480[cropped];[scaled][cropped]hstack" output.mp4
```

## Filter Chain Syntax

Multiple filters in one `-vf` are comma-separated:

```bash
ffmpeg -i input.mp4 -vf "scale=1280:720,fps=30,format=yuv420p" output.mp4
```

In `-filter_complex`, use semicolons to separate filter chains and labels (`[label]`) to connect them:

```bash
ffmpeg -i input.mp4 -filter_complex "[0:v]scale=640:-1[scaled];[scaled]fps=30[out]" -map "[out]" output.mp4
```
