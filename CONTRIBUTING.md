# Contributing to Awesome Weight-Space Programming

[Suggest a study](https://github.com/lobehub/awesome-wsp/issues/new?template=suggest-study.yml) if you have a paper to recommend. To update a citation, figure credit or broken link, use the [correction form](https://github.com/lobehub/awesome-wsp/issues/new?template=correction.yml). Contributions and corrections can also come directly as pull requests.

## Selecting a study

Look for a concrete operation on neural weights. What parameters could the programmer inspect or change? Was it allowed examples, tools, forward passes or evaluation feedback? What did the authors measure on the resulting network? Replications and negative results are welcome. For compilers and hand-built circuits, explain the connection to WSP in the Foundations section.

## Preparing a pull request

1. Search the [index](STUDIES.md) and [bibliography](references.bib) for the title and arXiv ID or DOI. A new version of an existing study usually belongs in the existing entry.
2. Add the study to the most specific section of the index. Link to the paper or author-maintained project, describe the weight operation, and name the test or control. Attribute measured results to the authors. Add code, logs or weights when available.
3. Add the matching BibTeX record for a research study. Check title, author order, year, URL and version against the primary source. For a new representative example, add a short entry to the appropriate direction on the [homepage](README.md#papers-by-direction) and update the study count when the collection grows.
4. For a figure, identify the authors, figure number and source version. Include alt text, a direct link to the original figure in the paper and the applicable credit or license. Check redistribution terms before adding a copy to the repository.
5. In the pull request, identify the changed entries and link to the evidence you checked. For a correction, include the previous value and its replacement.

Homepage entries use this format:

```markdown
- [Paper title](primary-source-url) - One sentence on the operation and its evaluation. [Code](author-repository-url).
```

## Local checks

Run these commands from the repository root. The same checks run on pull requests.

```sh
npx --yes awesome-lint@2.3.0 README.md
python3 scripts/check_catalog.py
python3 scripts/star_history.py --check
```
