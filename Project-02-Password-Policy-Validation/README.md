# Project 02: Password Policy Validation Engine

**Case Study:** 29  
**Language:** Python 3

## 1. Problem statement

A password should follow a clear set of rules before it is accepted by a system. This beginner-level program checks one or more sample passwords, reports every policy condition that fails, and gives a final result for each password.

## 2. Objectives

- Check the minimum password length.
- Check for uppercase letters, lowercase letters, digits, and special characters.
- Reject spaces and three identical consecutive characters.
- Detect prohibited substrings without depending on letter case.
- Explain each failed condition instead of displaying only a pass/fail result.
- Practice strings, variables, conditions, loops, and lists.

## 3. Assumptions and policy rules

The assignment names the types of checks but does not specify exact thresholds or prohibited phrases. This implementation uses the following documented assumptions:

1. Minimum length is 8 characters.
2. At least one uppercase letter, one lowercase letter, one digit, and one special character are required.
3. Spaces are not allowed.
4. The same character must not appear three or more times consecutively (for example, `AAA`).
5. The case-insensitive substrings `password`, `123456`, and `qwerty` are prohibited.
6. A password is accepted only when all checks pass.

These are educational example rules, not a guarantee that a password is secure for a real account. Do not enter a real personal password into a class demonstration.

## 4. Algorithm

1. Start and define the minimum length, character groups, and prohibited substrings.
2. Ask how many sample passwords will be checked; ask again if the number is not positive.
3. Repeat for each password:
   - Read the password and make a lowercase copy for prohibited-substring checks.
   - Scan the characters to identify uppercase letters, lowercase letters, digits, special characters, and spaces.
   - Scan the characters again to detect three identical consecutive characters.
   - Check for each prohibited substring.
   - Display PASS or FAIL for every policy condition and explain each failure.
   - Display the final result.
4. Display that checking is complete and stop.

## 5. Flowchart

Open [flowchart.svg](flowchart.svg) to view the program flow.

## 6. Pseudocode

See [algorithm-pseudocode.md](algorithm-pseudocode.md).

## 7. Run the program

Open a terminal in this folder and run:

```bash
python password_policy_validation.py
```

Enter a positive number of sample passwords, then enter each sample when prompted. The program expects the count as a whole number; `try-except` is intentionally not used because this project is limited to the completed beginner syllabus.

## 8. Test cases and actual results

The same cases are also listed in the standalone [test_cases.md](test_cases.md). The repository quality workflow checks the documented program behaviour.

| # | Sample input | Main case being tested | Expected result | Actual result |
|---:|---|---|---|---|
| 1 | `Strong#2026` | Meets all rules | Accept | Accept |
| 2 | `Ab1!` | Fewer than 8 characters | Reject: length | Reject: length |
| 3 | `lowercase1!` | Missing uppercase | Reject: uppercase | Reject: uppercase |
| 4 | `UPPERCASE1!` | Missing lowercase | Reject: lowercase | Reject: lowercase |
| 5 | `NoDigits!!` | Missing digit | Reject: digit | Reject: digit |
| 6 | `NoSpecial123` | Missing special character | Reject: special character | Reject: special character |
| 7 | `AAAabc1!` | Three repeated consecutive characters | Reject: repetition | Reject: repetition |
| 8 | `MyPassword12!` | Contains prohibited `password` substring | Reject: prohibited substring | Reject: prohibited substring |
| 9 | `Space Pass1!` | Contains a space | Reject: spaces | Reject: spaces |
| 10 | `Aa1!bcde` | Exactly 8 characters and meets all rules | Accept | Accept |

The output summary from this execution is in [screenshots/password_test_output.svg](screenshots/password_test_output.svg). It is a designed summary of the local run, not a screenshot from an online execution service.

## 9. Python concepts used

- Variables and Boolean values
- Strings, `len()`, `lower()`, and membership using `in`
- `if`, `elif`, and `else`
- `for` and `while` loops with `range()`
- Lists and list iteration

No imports, user-defined functions, classes, or `try-except` blocks are used.

## 10. Conclusion

This project demonstrates how a list of clear rules can be converted into a step-by-step validation algorithm. It also shows how useful error messages help users understand why an input does not satisfy a policy.
