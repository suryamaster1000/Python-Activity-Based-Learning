# Project 03 — Test Cases

## Standard test

**Answer key:** A B C D A

**Marking rule:** 4 marks for each correct answer, minus 1 mark for each incorrect answer, and 0 for unanswered questions.

| Student | Submitted answers | Correct | Incorrect | Unanswered | Expected marks |
|---|---|---:|---:|---:|---:|
| Anu | A B C D A | 5 | 0 | 0 | 20 |
| Ravi | A B A - A | 3 | 1 | 1 | 11 |
| Meena | B A C C - | 1 | 3 | 1 | 1 |

### Expected class summary

- Students evaluated: 3
- Questions per student: 5
- Total correct responses: 9
- Total incorrect responses: 4
- Total unanswered questions: 2
- Combined marks: 32

## Additional test cases

| # | Input condition | Expected behaviour |
|---:|---|---|
| 1 | Answer key is empty | Ask for the answer key again |
| 2 | Answer key contains an option outside A/B/C/D | Reject the key and request it again |
| 3 | Student count is 0 or negative | Ask for a positive number |
| 4 | Student name is blank | Ask for the name again |
| 5 | Student gives fewer or more responses than the key | Ask for the full response string again |
| 6 | Student uses an invalid response such as X | Ask for a corrected response string |
| 7 | Student submits lowercase options such as a b c d a | Convert to uppercase and evaluate |
| 8 | Student uses a dash for a blank response | Count it as unanswered and give 0 marks for that question |
| 9 | All answers are incorrect | Count all as incorrect and apply the penalty to each |
| 10 | All answers are unanswered (dash dash dash dash dash) | Correct = 0, incorrect = 0, unanswered = 5, marks = 0 |

The program expects whole-number numeric input where a number is requested; invalid text in those numeric fields is outside this project's stated input assumptions.
