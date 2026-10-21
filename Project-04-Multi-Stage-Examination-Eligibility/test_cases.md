# Project 04 — Test Cases

The expected outcomes below use the assumptions documented in the README.

## Standard test data

| Student | Attendance | Labs completed | Internal marks / 50 | Fees cleared | Expected status | Expected reasons if not eligible |
|---|---:|---|---:|---|---|---|
| Anu | 82% | Y | 35 | Y | ELIGIBLE | None |
| Ravi | 68% | Y | 36 | Y | NOT ELIGIBLE | Attendance is below 75% |
| Meena | 90% | N | 12 | Y | NOT ELIGIBLE | Labs incomplete; internal marks below 20/50 |
| Kiran | 75% | Y | 20 | Y | ELIGIBLE | None |

### Expected summary

- Students checked: 4
- Eligible students: 2
- Not eligible students: 2

## Boundary and validation tests

| # | Test input | Expected behaviour |
|---:|---|---|
| 1 | Attendance exactly 75% | Pass attendance requirement |
| 2 | Attendance 74% | Report attendance below 75% |
| 3 | Internal marks exactly 20/50 | Pass internal marks requirement |
| 4 | Internal marks 19/50 | Report internal marks below 20/50 |
| 5 | All requirements satisfied | Mark ELIGIBLE |
| 6 | Labs = N and fees = N | Report both unmet requirements |
| 7 | Attendance is -1 or 101 | Ask for an attendance value from 0 to 100 |
| 8 | Internal marks are -1 or 51 | Ask for marks from 0 to 50 |
| 9 | Lab or fee response is neither Y nor N | Ask for a valid Y/N response |
| 10 | Student count is 0 or negative | Ask for a positive student count |
| 11 | Name contains only spaces | Ask for a non-blank name |

Numeric prompts expect numeric input. Text entered where a number is requested is outside the current input assumptions because exception handling is not used.
