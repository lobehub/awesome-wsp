"""Check local navigation, citation coverage and the homepage study count."""
import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (*ROOT.glob("*.md"), *ROOT.glob("docs/**/*.md"), *ROOT.glob("examples/**/*.md"))


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


def bibliography_urls(text):
    urls = set()
    keys = set()
    entries = list(re.finditer(r"^@(?!comment\b|preamble\b|string\b)\w+\s*\{\s*([^,]+),", text, re.M | re.I))
    for index, entry in enumerate(entries):
        key = entry[1].strip()
        end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        fields = text[entry.end():end]
        links = re.findall(r'(?:^|,)\s*url\s*=\s*[{"](https?://[^}"\s]+)[}"]', fields, re.I)
        if key in keys or len(links) != 1:
            raise ValueError(f"Expected a unique key and one primary URL for {key}")
        if links[0] in urls:
            raise ValueError(f"Duplicate citation URL: {links[0]}")
        keys.add(key)
        urls.add(links[0])
    if not urls:
        raise ValueError("No bibliography entries found")
    return urls


def indexed_urls(text):
    urls = set()
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        if section == "Foundations" or not line.startswith("- "):
            continue
        entry = re.match(r"^- \[[^\]]+\]\((https?://[^)]+)\) · \*.+?, \d{4}\*\. ", line)
        if not entry:
            raise ValueError(f"Expected a linked study title, author and year: {line[:100]}")
        url = entry[1]
        if url in urls:
            raise ValueError(f"Duplicate study in the index: {url}")
        urls.add(url)
    return urls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-count", action="store_true", help="Write the verified study count to README.md")
    args = parser.parse_args()
    for page in PAGES:
        check_links(page)

    index = indexed_urls((ROOT / "STUDIES.md").read_text())
    bibliography = bibliography_urls((ROOT / "references.bib").read_text())
    if index != bibliography:
        missing = sorted(index - bibliography)
        extra = sorted(bibliography - index)
        raise ValueError(f"Missing from BibTeX: {missing}\nMissing from research index: {extra}")

    readme = ROOT / "README.md"
    text = readme.read_text()
    expected = f"**{len(index)} studies**"
    updated, matches = re.subn(r"\*\*\d+ studies\*\*", expected, text)
    if matches != 1:
        raise ValueError("Expected one homepage study count")
    if updated != text:
        if not args.update_count:
            raise ValueError(f"Expected {expected}. Run python3 scripts/check_catalog.py --update-count")
        readme.write_text(updated)


if __name__ == "__main__":
    main()
