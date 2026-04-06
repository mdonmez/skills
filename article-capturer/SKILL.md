---
name: article-capturer
description: Convert pasted BibTeX paper entries into clean Markdown note entries and append them to the curated computer science papers index. Use when the user pastes BibTeX, asks to add a paper to the index, or wants bibliographic entries formatted as paper notes.
---

# Article Capturer

Use this skill to turn BibTeX into a clean paper note and add it to the index.

## Workflow

1. Take the BibTeX the user provides.
2. Convert it with `scripts/bibtex_to_markdown.py`.
3. Append the generated Markdown to the relevant index note file (explore and find this file first.).
4. Keep the output in the shared note style:
   - `###` title header
   - `**Authors:**`
   - `**Year:**`
   - `**ArXiv ID:**`
   - `**URL:**`
   - `---` separator after each paper

## Rules

- Do not include the raw BibTeX block in the note.
- Do not include a BibTeX key in the rendered note.
- Preserve the fields the user provided instead of inventing replacements.
- If a field is missing, leave it blank rather than guessing.

## Script

Use `scripts/bibtex_to_markdown.py` as the deterministic converter. It accepts BibTeX from stdin or a file path and prints the Markdown entry.
You can run it via `uv` using `uv run`.
