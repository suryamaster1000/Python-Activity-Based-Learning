# Project 04 — Test Cases

Assumed rules: attendance >= 75%, labs >= 1, internal marks >= 40/100, and fees cleared.

| # | Attendance | Labs | Marks | Fees cleared | Expected status | Reason |
|---:|---:|---:|---:|---|---|---|
| 1 | 90 | 2 | 80 | yes | ELIGIBLE | All rules satisfied |
| 2 | 60 | 2 | 80 | yes | NOT ELIGIBLE | Attendance below 75% |
| 3 | 80 | 0 | 80 | yes | NOT ELIGIBLE | Lab work incomplete |
| 4 | 80 | 1 | 35 | yes | NOT ELIGIBLE | Internal marks below 40 |
| 5 | 80 | 1 | 65 | no | NOT ELIGIBLE | Fee clearance pending |
| 6 | 60 | 0 | 25 | no | NOT ELIGIBLE | All four requirements unmet |
| 7 | 75 | 1 | 40 | yes | ELIGIBLE | Exactly meets all minimums |
| 8 | 100 | 5 | 100 | yes | ELIGIBLE | All conditions satisfied |

## Additional validation tests
- Student count 0 or negative: asks for a positive count.
- Blank name: asks for the name again.
- Attendance or marks outside 0–100: asks again.
- Negative lab count: asks again.
- Fee status other than yes/no: asks again.

Numeric fields expect numeric input.
