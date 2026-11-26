"""Audit published links and report HTTP failures separately from rate limits."""
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import re
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"""\]\((https?://[^\s)]+)\)|(?:href|src)="(https?://[^"]+)"|^\[[^\]]+\]:\s*(https?://\S+)""")
BIB_URL = re.compile(r'\burl\s*=\s*[{"](https?://[^}"\s]+)', re.I)


def published_links():
    paths = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.md", "references.bib"],
        cwd=ROOT,
    ).decode().rstrip("\0").split("\0")
    locations = defaultdict(set)
    for name in paths:
        fence = ""
        for number, line in enumerate((ROOT / name).read_text().splitlines(), 1):
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                if not fence:
                    fence = marker[1]
                elif marker[1].startswith(fence):
                    fence = ""
                continue
            pattern = BIB_URL if name.endswith(".bib") else LINK
            if not fence:
                for match in pattern.finditer(line):
                    url = next(value for value in match.groups() if value)
                    locations[urldefrag(url).url].add(f"{name}:{number}")
    return locations


def probe(url):
    req = Request(url, headers={"User-Agent": "awesome-wsp-link-check/1.0 (github.com/lobehub/awesome-wsp)"})
    try:
        with urlopen(req, timeout=12) as response:
            return "reachable", f"HTTP {response.status}"
    except HTTPError as error:
        with error:
            status = error.code
            if status in (404, 410):
                return "missing", f"HTTP {status}"
            if status == 429 or (status == 403 and (
                error.headers.get("Retry-After") or error.headers.get("X-RateLimit-Remaining") == "0"
            )):
                return "rate limited", f"HTTP {status}"
            return "unverified", f"HTTP {status}"
    except (URLError, OSError) as error:
        return "unverified", str(error)


def check_host(urls):
    results = []
    throttle = None
    for url in sorted(urls):
        if throttle:
            results.append((url, "deferred", throttle))
            continue
        state, detail = probe(url)
        if state == "missing":
            time.sleep(1)
            state, again = probe(url)
            if state == "missing":
                state = "confirmed missing"
            detail += f", retry: {again}"
        if state == "rate limited":
            throttle = f"Host rate-limited a previous request ({detail})"
        results.append((url, state, detail))
    return results


def main():
    locations = published_links()
    if not locations:
        raise SystemExit("No published URLs found")
    hosts = defaultdict(list)
    for url in locations:
        hosts[urlsplit(url).netloc].append(url)
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = sorted(result for group in pool.map(check_host, hosts.values()) for result in group)
    counts = defaultdict(int)
    for _, state, _ in results:
        counts[state] += 1
    report = ["## Weekly external link check", "",
              f"Found {len(results)} distinct URLs. {counts['reachable']} were reachable.",
              "", "| Result | Count |", "| --- | ---: |"]
    for state in ("reachable", "confirmed missing", "rate limited", "deferred", "unverified"):
        report.append(f"| {state.capitalize()} | {counts[state]} |")
    for state in ("confirmed missing", "rate limited", "deferred", "unverified"):
        if counts[state]:
            report.extend(["", f"### {state.capitalize()}", ""])
            for url, outcome, detail in results:
                if state == outcome:
                    refs = ", ".join(f"`{ref}`" for ref in sorted(locations[url]))
                    report.append(f"- <{url}> — {detail}. {refs}")
    output = "\n".join(report) + "\n"
    print(output)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write(output)
    return 1 if counts["confirmed missing"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
