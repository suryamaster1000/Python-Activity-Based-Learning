# Project 02 — Test Cases

The source policy is a classroom example: minimum 8 characters, uppercase, lowercase, digit, special character, no spaces, no character repeated three times consecutively, and no case-insensitive occurrence of `password`, `123456`, or `qwerty`.

| # | Sample input | Main rule tested | Expected result |
|---:|---|---|---|
| 1 | `Strong#2026` | Meets all checks | Accept |
| 2 | `Ab1!` | Shorter than 8 characters | Reject: length |
| 3 | `lowercase1!` | Missing uppercase | Reject: uppercase |
| 4 | `UPPERCASE1!` | Missing lowercase | Reject: lowercase |
| 5 | `NoDigits!!` | Missing digit | Reject: digit |
| 6 | `NoSpecial123` | Missing special character | Reject: special character |
| 7 | `AAAabc1!` | Three repeated characters in a row | Reject: repetition |
| 8 | `MyPassword12!` | Contains prohibited substring `password` | Reject: prohibited substring |
| 9 | `Space Pass1!` | Contains a space | Reject: spaces |
| 10 | `Aa1!bcde` | Exactly 8 characters and otherwise valid | Accept |

Do not enter a real personal password into this educational program. Numeric prompts expect a whole number.
