import re
import sys
from pathlib import Path


def parse_bibtex(bibtex: str) -> dict:
    data = {}

    entry_match = re.match(r"@\w+\{([^,]+),", bibtex)
    if entry_match:
        data["key"] = entry_match.group(1)

    fields = re.findall(r"(\w+)\s*=\s*\{([^}]*)\}", bibtex, re.S)
    for field, value in fields:
        data[field.lower()] = value.strip()

    return data


def format_authors(author_str: str) -> str:
    if not author_str:
        return ""
    authors = [author.strip() for author in author_str.split(" and ") if author.strip()]
    return ", ".join(authors)


def bibtex_to_markdown(bibtex: str) -> str:
    data = parse_bibtex(bibtex)

    title = data.get("title", "Unknown Title")
    authors = format_authors(data.get("author", ""))
    year = data.get("year", "")
    url = data.get("url", "")
    arxiv_id = data.get("eprint", "")

    return f"""### {title}

**Authors:** {authors}  
**Year:** {year}  
**ArXiv ID:** {arxiv_id}  
**URL:** {url}

---
"""


def main() -> None:
    if len(sys.argv) > 1:
        bibtex_input = Path(sys.argv[1]).read_text(encoding="utf-8")
    else:
        bibtex_input = sys.stdin.read()

    bibtex_input = bibtex_input.strip()
    if not bibtex_input:
        raise SystemExit("Provide BibTeX via stdin or as a file path.")

    print(bibtex_to_markdown(bibtex_input))


if __name__ == "__main__":
    main()
