---
name: youtube-transcript
description: Extract YouTube video transcripts as markdown files using the defuddle CLI tool. Use when the user wants to download, save, or extract a YouTube video's transcript, subtitles, or spoken content as a text or markdown file. Also use when the user shares a YouTube URL and asks to save it, transcribe it, or convert it to notes.
---

# YouTube Transcript Extractor

Extract YouTube video transcripts and save them as formatted markdown files using `defuddle parse`.

## Workflow

### 1. Parse the video

Run `defuddle parse` with the YouTube URL to extract the transcript as markdown:

```bash
npx defuddle parse "<youtube-url>" -m -o <output-path>
```

- Use `-m` (or `--md`) to output in markdown format
- Use `-o` to specify the output file path
- URL should be a standard YouTube watch URL (e.g., `https://www.youtube.com/watch?v=VIDEO_ID`)

### 2. Read the output

Read the generated file to check if the transcript was successfully extracted. Some videos may not have accessible transcripts — in that case the file will only contain the video link.

### 3. Add title header

Prepend the video title (or user-provided name) and a markdown separator to the top of the file:

```markdown
<Channel or Video Title>

---

![](https://www.youtube.com/watch?v=VIDEO_ID)

## Transcript
...
```

Use the `edit` tool to insert the title and `---` separator before the first line of content.

## Example

User shares: `https://www.youtube.com/watch?v=abc123` and says "save this as notes"

1. Run: `npx defuddle parse "https://www.youtube.com/watch?v=abc123" -m -o notes.md`
2. Read `notes.md` to verify transcript content exists
3. Edit file to add title header: `Channel Name\n\n---\n\n![](https://www.youtube.com/watch?v=abc123)`

## Troubleshooting

- **Empty transcript (only video link)**: `defuddle` could not extract the transcript. This can happen if the video has no subtitles, uses dynamic loading, or has a non-standard page structure. Try re-running once. If it still fails, inform the user.
- **Debug mode**: Add `--debug` flag to `defuddle parse` for more verbose output when troubleshooting.

## Output format

The final markdown file should look like:

```markdown
<Channel/Video Title>

---

![](https://www.youtube.com/watch?v=VIDEO_ID)

## Transcript

**0:00** · First line of transcript...
**0:15** · Next line...
```
