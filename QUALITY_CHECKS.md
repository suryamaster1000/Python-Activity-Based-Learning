# Quality Checks

Run the audit from the repository root with Python 3:

~~~text
python .github/scripts/repository_audit.py
~~~

The audit checks:
- all ten project folders and each folder's required documentation;
- the existence of exactly one canonical Python source file per project;
- internal links in Markdown and HTML;
- valid SVG/XML markup and basic HTML document structure;
- that documented Python run commands resolve to existing source files;
- that the root README and directory page list all ten projects;
- Python syntax for all repository Python files; and
- one scripted sample-input run of every project, with expected output assertions.

Commands in a project's `screenshots/README.md` are intentionally resolved from that project's folder, because that is where the instructions tell students to run them.

The audit uses example input data and is an automated sanity check, not a substitute for instructor review, extra edge-case testing, or genuine terminal screenshots.

External URLs are not fetched by this check; it verifies local repository paths. Review external links separately before submission.
