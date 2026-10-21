# Project 07 — Test Cases

## Test Case 1: Three students and three subjects

**Subject order:** Python, Mathematics, English

| Student | Python | Mathematics | English | Total | Average | Expected result |
|---|---:|---:|---:|---:|---:|---|
| Anu | 78 | 85 | 69 | 232 | 77.33 | PASS |
| Balu | 56 | 40 | 62 | 158 | 52.67 | PASS |
| Charan | 35 | 48 | 52 | 135 | 45.00 | FAIL |

**Expected subject summary**

| Subject | Total | Average |
|---|---:|---:|
| Python | 169 | 56.33 |
| Mathematics | 173 | 57.67 |
| English | 183 | 61.00 |

**Expected overall summary**

- Students analysed: 3
- Subjects analysed: 3
- Overall average mark: 58.33
- Students passed all subjects: 2
- Students who need improvement: 1
- Highest mark: 85 — Anu — Mathematics
- Lowest mark: 35 — Charan — Python

## Additional tests

| Test | Input condition | Expected result |
|---|---|---|
| 2 | A student receives 40 in every subject | PASS because the example threshold is inclusive |
| 3 | A student receives 39 in one subject and 80 in all others | FAIL because every subject must meet the threshold |
| 4 | A mark is entered as -1 or 101 | Program asks for a mark between 0 and 100 again |
| 5 | One student and one subject | Matrix calculations still work |
| 6 | Student count or subject count is 0 | Program asks for a value of at least 1 again |

The program expects valid numeric input for counts and marks; entering text at a numeric prompt is outside this test scope.
