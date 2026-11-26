"""Check local navigation, citation coverage and the homepage study count."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (ROOT / "README.md", ROOT / "STUDIES.md", ROOT / "CONTRIBUTING.md")


def check_links(page):
    # Exclude fenced examples such as the submission-format template.
    text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", page.read_text(), flags=re.M | re.S)
    targets = re.findall(r'\]\(([^()\s]+)\)|(?:href|src)="([^"]+)"|^\[[^\]]+\]:\s+(\S+)', text, re.M)
    for match in targets:
        url = urlsplit(next(value for value in match if value))
        if url.scheme or url.netloc:
            continue
        path = page.parent / unquote(url.path) if url.path else page
        if not path.is_file():
            raise ValueError(f"{page.name}: missing {path}")
        if url.fragment and path.suffix == ".md":
            content = path.read_text()
            headings = re.findall(r"^#{1,6} (.+)$", content, re.M)
            anchors = {re.sub(r"[^\w -]", "", name.lower()).replace(" ", "-") for name in headings}
            anchors.update(re.findall(r'<a (?:name|id)="([^"]+)"', content))
            if unquote(url.fragment) not in anchors:
                raise ValueError(f"{page.name}: missing {path.name}#{url.fragment}")


def main():
    for page in PAGES:
        check_links(page)
    bibliography = (ROOT / "references.bib").read_text()
    keys = re.findall(r"^@\w+\{([^,]+),", bibliography, re.M)
    if not keys or len(keys) != len(set(keys)):
        raise ValueError("Missing bibliography or duplicate citation key")
    index = (ROOT / "STUDIES.md").read_text()
    for url in re.findall(r"^\s*url\s*=\s*\{([^}]+)\}", bibliography, re.M | re.I):
        if url not in index:
            raise ValueError(f"Citation URL missing from the research index: {url}")
    match = re.search(r"\*\*(\d+) studies\*\*", (ROOT / "README.md").read_text())
    if not match or int(match[1]) != len(keys):
        raise ValueError(f"Homepage study count should be {len(keys)}")


if __name__ == "__main__":
    main()
