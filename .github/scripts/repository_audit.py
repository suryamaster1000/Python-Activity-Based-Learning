#!/usr/bin/env python3
"""Repository-wide documentation, link, structure, syntax, and smoke-test audit.

Uses only the Python standard library so it can run on a fresh GitHub Actions runner.
"""
from __future__ import annotations

import html.parser
import posixpath
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []
CHECKS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)
    print(f"FAIL: {message}")


def passed(message: str) -> None:
    CHECKS.append(message)
    print(f"PASS: {message}")


def local_target_exists(source: Path, raw_target: str) -> bool:
    target = raw_target.strip().strip("<>")
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return True
    path = unquote(parsed.path)
    if not path:  # Fragment-only links, such as #section
        return True
    if path.startswith("/"):
        candidate = ROOT / path.lstrip("/")
    else:
        candidate = source.parent / path
    candidate = Path(posixpath.normpath(str(candidate)))
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return False
    if candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate.is_file()


class LinkCollector(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key.lower() in ("href", "src") and value:
                self.links.append(value)


def main() -> int:
    all_files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and "__pycache__" not in p.parts
    )
    rel_files = {p.relative_to(ROOT).as_posix() for p in all_files}
    directories = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"Project-\d{2}-", p.name))
    project_dirs = sorted(directories, key=lambda p: p.name)

    if len(project_dirs) != 10:
        fail(f"Expected 10 project folders, found {len(project_dirs)}")
    else:
        passed("Found all 10 project folders")

    # Standard project deliverables and one canonical Python entry point per project.
    for project in project_dirs:
        base = project.relative_to(ROOT).as_posix()
        expected = [
            "README.md",
            "algorithm-pseudocode.md",
            "flowchart.svg",
            "index.html",
            "test_cases.md",
            "screenshots/README.md",
        ]
        for name in expected:
            if f"{base}/{name}" not in rel_files:
                fail(f"{base}: required file missing: {name}")
        py_files = sorted(project.glob("*.py"))
        if len(py_files) != 1:
            fail(f"{base}: expected exactly one canonical Python program, found {[p.name for p in py_files]}")
        previews = [
            p for p in project.rglob("*.svg")
            if ("output" in p.name.lower() or "preview" in p.name.lower())
        ]
        if not previews:
            fail(f"{base}: no labelled output/preview SVG found")
        readme = project / "README.md"
        if readme.is_file() and "test_cases.md" not in readme.read_text(encoding="utf-8"):
            fail(f"{base}: README does not point readers to test_cases.md")
    if not ERRORS:
        passed("Project folders have the required documents and one Python entry point")

    # Validate all internal Markdown and HTML links in the repository.
    md_link_re = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
    broken_links: list[str] = []
    for file in all_files:
        rel = file.relative_to(ROOT).as_posix()
        try:
            text = file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if file.suffix.lower() == ".md":
            for match in md_link_re.finditer(text):
                target = match.group(1).strip("<>")
                if not local_target_exists(file, target):
                    broken_links.append(f"{rel} -> {target}")
        elif file.suffix.lower() == ".html":
            parser = LinkCollector()
            try:
                parser.feed(text)
                parser.close()
            except Exception as exc:
                fail(f"{rel}: HTML parser error: {exc}")
            for target in parser.links:
                if not local_target_exists(file, target):
                    broken_links.append(f"{rel} -> {target}")
            if not re.search(r"<!doctype\s+html>", text, re.IGNORECASE):
                fail(f"{rel}: missing HTML doctype")
            if not re.search(r"<meta[^>]+charset\s*=", text, re.IGNORECASE):
                fail(f"{rel}: missing character encoding")
        elif file.suffix.lower() == ".svg":
            try:
                ET.fromstring(text)
            except ET.ParseError as exc:
                fail(f"{rel}: invalid SVG/XML: {exc}")
    if broken_links:
        for item in broken_links:
            fail(f"broken local link: {item}")
    else:
        passed("All local Markdown/HTML links resolve and all SVG files parse as XML")

    # Every documented Python run command must resolve from its document's folder.
    run_command_re = re.compile(r"\bpython(?:3)?\s+([A-Za-z0-9_./-]+\.py)\b")
    bad_commands: list[str] = []
    for file in all_files:
        if file.suffix.lower() not in (".md", ".html"):
            continue
        try:
            text = file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in run_command_re.finditer(text):
            target = match.group(1)
            candidate = (ROOT / target) if target.startswith("Project-") else (file.parent / target)
            if not candidate.is_file():
                bad_commands.append(f"{file.relative_to(ROOT).as_posix()} -> python {target}")
    if bad_commands:
        for item in bad_commands:
            fail(f"broken run command: {item}")
    else:
        passed("Documented Python run commands point to existing files")

    # Root directory must show all ten projects and use the canonical Project 04 source.
    root_readme_path = ROOT / "README.md"
    root_index_path = ROOT / "index.html"
    if not root_readme_path.is_file() or not root_index_path.is_file():
        fail("Root README.md or index.html is missing")
    else:
        root_readme = root_readme_path.read_text(encoding="utf-8")
        root_index = root_index_path.read_text(encoding="utf-8")
        list_count = len(re.findall(r"(?m)^\d+\. \[", root_readme))
        card_count = len(re.findall(r'<article class="card">', root_index))
        if list_count != 10:
            fail(f"Root README lists {list_count} projects rather than 10")
        if card_count != 10:
            fail(f"Root website contains {card_count} project cards rather than 10")
        if "multi_stage_exam_eligibility.py" in root_readme or "multi_stage_exam_eligibility.py" in root_index:
            fail("Root documentation still points at the removed duplicate Project 04 script")
        if list_count == 10 and card_count == 10:
            passed("Root README and website both list all 10 projects")

    # Compile every tracked Python program (without creating bytecode files).
    py_files = sorted(ROOT.rglob("*.py"))
    syntax_bad = []
    for file in py_files:
        if ".git" in file.parts or "__pycache__" in file.parts:
            continue
        try:
            source = file.read_text(encoding="utf-8")
            compile(source, str(file), "exec")
        except (SyntaxError, UnicodeDecodeError) as exc:
            syntax_bad.append(f"{file.relative_to(ROOT).as_posix()}: {exc}")
    if syntax_bad:
        for item in syntax_bad:
            fail(f"Python syntax error: {item}")
    else:
        passed(f"Python syntax check passed for all {len(py_files)} Python files")

    # Run a deterministic smoke test for every one of the ten project programs.
    p1_input = "\n".join(["100", "95"] * 7) + "\n"
    p2_passwords = [
        "Strong#2026", "Ab1!", "lowercase1!", "UPPERCASE1!", "NoDigits!!",
        "NoSpecial123", "AAAabc1!", "MyPassword12!", "Space Pass1!", "Aa1!bcde",
    ]
    p2_input = "\n".join([str(len(p2_passwords)), *p2_passwords]) + "\n"
    smoke_tests = [
        (
            "Project 01 Food Waste",
            "Project-01-Food-Waste-Monitoring/food_waste_monitoring.py",
            p1_input,
            ["Meals prepared: 700", "Meals served: 665", "Leftover meals: 35", "Overall wastage: 5.0 %"],
            [],
        ),
        (
            "Project 02 Password Policy",
            "Project-02-Password-Policy-Validation/password_policy_validation.py",
            p2_input,
            ["Password checking completed."],
            [("RESULT: Password meets this project's policy.", 2), ("RESULT: Password does not meet this project's policy.", 8)],
        ),
        (
            "Project 03 Answer Evaluation",
            "Project-03-String-Based-Examination-Answer-Evaluation/string_based_exam_evaluation.py",
            "A B C D A\n3\nAnu\nA B C D A\nRavi\nA B A - A\nMeena\nB A C C -\n",
            ["Combined marks for all students: 32", "Anu | Correct: 5", "Ravi | Correct: 3", "Meena | Correct: 1"],
            [],
        ),
        (
            "Project 04 Examination Eligibility",
            "Project-04-Multi-Stage-Examination-Eligibility/eligibility_checker.py",
            "4\nAnu\n82\nY\n35\nY\nRavi\n68\nY\n36\nY\nMeena\n90\nN\n12\nY\nKiran\n75\nY\n20\nY\n",
            ["Students checked: 4", "Eligible students: 2", "Not eligible students: 2"],
            [],
        ),
        (
            "Project 05 Product Catalogue Audit",
            "Project-05-Tuple-Based-Product-Catalogue-Audit/tuple_product_catalogue_audit.py",
            "4\n101\nNotebook\nStationery\n25\n20\n102\nPen\nStationery\n10\n0\n103\nFolder\nStationery\n15\n3\n102\nPencil\nStationery\n0\n-2\n",
            ["101 | Notebook", "OUT OF STOCK", "LOW STOCK", "DUPLICATE ID", "Duplicate ID records: 1", "Records with invalid price: 1"],
            [],
        ),
        (
            "Project 06 Feedback Sentiment",
            "Project-06-Student-Feedback-Sentiment-Scoring/student_feedback_sentiment_scoring.py",
            "3\nThe class was clear and helpful. Great examples!\nThe lesson was confusing and slow, with a difficult exercise.\nThe session covered the topic.\n",
            ["Positive responses: 1", "Negative responses: 1", "Neutral responses: 1", "Positive keyword matches: 3", "Negative keyword matches: 3"],
            [],
        ),
        (
            "Project 07 Marks Matrix",
            "Project-07-Student-Marks-Matrix-Analysis/student_marks_matrix_analysis.py",
            "3\n3\nPython\nMathematics\nEnglish\nAnu\n78\n85\n69\nBalu\n56\n40\n62\nCharan\n35\n48\n52\n",
            ["Overall average mark: 58.33", "Students passed all subjects: 2", "Highest mark: 85.00 - Anu - Mathematics", "Lowest mark: 35.00 - Charan - Python"],
            [],
        ),
        (
            "Project 08 Electricity Matrix",
            "Project-08-Weekly-Electricity-Consumption-Matrix/weekly_electricity_consumption_matrix.py",
            "2\n8\n9\n7\n10\n11\n13\n12\n12\n14\n16\n18\n15\n11\n9\n",
            ["Week 1 | Total: 70.00 kWh", "Week 2 | Total: 95.00 kWh", "Percentage change: 35.71", "Days above the high-use alert limit: 2"],
            [],
        ),
        (
            "Project 09 ATM Simulation",
            "Project-09-ATM-Transaction-Sequence-Simulation/atm_transaction_sequence_simulation.py",
            "1000\n1\n500\n2\n200\n3\n2\n2000\n4\n",
            ["Successful deposits: 1", "Successful withdrawals: 1", "Rejected deposit/withdrawal attempts: 1", "Transactions recorded: 4", "Final simulated balance: Rs. 1300.00"],
            [],
        ),
        (
            "Project 10 Energy Comparison",
            "Project-10-Energy-Conservation-Before-After-Analysis/energy_conservation_before_after_analysis.py",
            "4\nLights\n12\n8\nFans\n15\n12\nAir conditioner\n20\n16\nComputer\n5\n6\n",
            ["Total BEFORE changes: 52.00 kWh/day", "Total AFTER changes: 42.00 kWh/day", "Net daily energy reduction: 10.00 kWh/day", "Overall reduction: 19.23", "Appliances with reduced use: 3", "Appliances with increased use: 1"],
            [],
        ),
    ]
    smoke_bad = []
    for label, relative_script, input_data, required, count_checks in smoke_tests:
        script = ROOT / relative_script
        if not script.is_file():
            smoke_bad.append(f"{label}: program file missing: {relative_script}")
            continue
        try:
            completed = subprocess.run(
                [sys.executable, str(script)],
                input=input_data,
                capture_output=True,
                text=True,
                cwd=ROOT,
                timeout=10,
                check=False,
            )
        except subprocess.TimeoutExpired:
            smoke_bad.append(f"{label}: timed out (possible input loop)")
            continue
        if completed.returncode != 0:
            smoke_bad.append(f"{label}: exit code {completed.returncode}; stderr={completed.stderr[-500:]}")
            continue
        missing = [text for text in required if text not in completed.stdout]
        wrong_counts = [
            f"{needle!r} appeared {completed.stdout.count(needle)} times (wanted {count})"
            for needle, count in count_checks
            if completed.stdout.count(needle) != count
        ]
        if missing or wrong_counts:
            smoke_bad.append(f"{label}: missing={missing}; count_errors={wrong_counts}")
        else:
            passed(f"Smoke test passed: {label}")
    if smoke_bad:
        for item in smoke_bad:
            fail(item)

    print()
    print(f"Repository audit: {len(CHECKS)} checks passed; {len(ERRORS)} issue(s) found.")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
