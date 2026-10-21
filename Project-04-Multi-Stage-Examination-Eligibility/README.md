# Project 04: Multi-Stage Examination Eligibility System

**Case Study:** 39  
**Language:** Python 3

## 1. Problem statement
A college may require students to satisfy several conditions before being permitted to take an examination. This program checks attendance, laboratory completion, internal marks, and fee clearance. It reports whether each student meets the assumed requirements and lists any conditions that remain unmet.

## 2. Objectives
- Check multiple examination eligibility conditions.
- Practise if statements, loops, comparisons, input/output, and lists.
- Display every unmet condition rather than only one.
- Store and summarize results for multiple students.

## 3. Assumptions
The case-study title does not specify exact college rules. For demonstration, this project assumes:
- Attendance must be at least 75%.
- At least one required laboratory exercise must be completed.
- Internal marks must be at least 40 out of 100.
- Fees must be cleared.
- A student is eligible only when all four conditions are satisfied.
These are example rules, not an official university policy. Use faculty-approved rules if provided. Numeric fields expect valid numeric input.

## 4. Algorithm and pseudocode
See [algorithm-pseudocode.md](algorithm-pseudocode.md).

## 5. Flowchart
Open [flowchart.svg](flowchart.svg).

## 6. How to run
Open a terminal in this folder and run:
    python multi_stage_exam_eligibility.py
Enter each student's name, attendance percentage, completed lab count, internal marks, and fee-clearance status (yes or no).

## 7. Test cases and output
See [test_cases.md](test_cases.md). The file [screenshots/sample_output_preview.svg](screenshots/sample_output_preview.svg) is a designed preview, not a raw terminal screenshot. Follow [screenshots/README.md](screenshots/README.md) to capture genuine terminal screenshots after running the program.

## 8. Python concepts
Variables, input(), print(), int(), float(), strip(), lower(), arithmetic, comparison and logical operators, if/else, while and for loops, range(), lists, and append(). No imports, functions, classes, external packages, or try-except are used.

## 9. Conclusion
This project demonstrates how multiple conditions can determine examination eligibility and how clear messages can show students which requirements need attention.
