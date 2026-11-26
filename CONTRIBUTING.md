# Contributing to Awesome Weight-Space Programming

[Suggest a study](https://github.com/lobehub/awesome-wsp/issues/new?template=suggest-study.yml) if you have a paper to recommend. To update a citation, figure credit or broken link, use the [correction form](https://github.com/lobehub/awesome-wsp/issues/new?template=correction.yml). Contributions and corrections can also come directly as pull requests.

## Selecting a study

Look for a concrete operation on neural weights. What parameters could the programmer inspect or change? Was it allowed examples, tools, forward passes or evaluation feedback? What did the authors measure on the resulting network? Replications and negative results are welcome. For compilers and hand-built circuits, explain the connection to WSP in the Foundations section.

## Preparing a pull request

1. Search the [index](STUDIES.md) and [bibliography](references.bib) for the title and arXiv ID or DOI. A new version of an existing study usually belongs in the existing entry.
2. Add the study to the most specific section of the index. Use the full published title as the first link, then give the author credit, year and a one-sentence reading note on the weight operation and its evaluation. Attribute measured results to the authors. Add code, logs or weights when available.
3. Add the matching BibTeX record for a research study. Check title, author order, year, URL and version against the primary source. Use the same primary URL and version in both files. Run `python3 scripts/check_catalog.py --update-count` to refresh the homepage count after adding or removing a study. The Foundations resources are listed separately. For a representative example, also add a short entry to the appropriate direction on the [homepage](README.md#papers-by-direction).
4. For a figure, identify the authors, figure number and source version. Include alt text, a direct link to the original figure in the paper and the applicable credit or license. Check redistribution terms before adding a copy to the repository.
5. In the pull request, identify the changed entries and link to the evidence you checked. For a correction, include the previous value and its replacement.

Index entries use this format:

```markdown
- [Full published title](primary-source-url) · *First Author et al., 2026*. One sentence on the experiment. [Code](author-repository-url)
```

Homepage entries use this format:

```markdown
- [Paper title](primary-source-url) - One sentence on the operation and its evaluation. [Code](author-repository-url).
```

## Reuse and attribution

The original WSP collection, its annotations and its original illustrations are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). By contributing original catalog text, you agree to release it under CC0.

Paper figures, linked publications, third-party code and model weights retain their respective authors’ terms. Keep the figure credit and license with any copy. For externally hosted figures, keep the link to the original publication.

## Local checks

Run these commands from the repository root. The same checks run on pull requests.

```sh
npx --yes awesome-lint@2.3.0 README.md
python3 scripts/check_catalog.py
python3 scripts/star_history.py --check
```

## External link maintenance

The [weekly link check](https://github.com/lobehub/awesome-wsp/actions/workflows/external-links.yml) runs on Tuesdays at 03:43 UTC and can also be started manually. It checks HTTP destinations in Markdown and bibliography entries, including externally hosted figures, code and weight downloads. The Actions summary lists affected files and lines.

Two consecutive HTTP 404 or 410 responses mark a link as missing and fail the job. Rate limits are reported separately and defer the remaining URLs on that host. Access restrictions, network failures and server errors are listed for review. The report measures URL availability. Inspect the target content before replacing a source.

Run the same check locally with `python3 scripts/check_external_links.py`.
