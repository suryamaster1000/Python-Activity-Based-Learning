# Project 06 — Test Cases

The listed examples use the keyword lists included in the source code.

## Test Case 1: Positive, negative, and neutral comments

| Feedback | Positive matches | Negative matches | Score | Expected classification |
|---|---:|---:|---:|---|
| The class was clear and helpful. Great examples! | 3 | 0 | 3 | POSITIVE |
| The lesson was confusing and slow, with a difficult exercise. | 0 | 3 | -3 | NEGATIVE |
| The session covered the topic. | 0 | 0 | 0 | NEUTRAL |

**Expected overall summary**

- Feedback responses analysed: 3
- Positive responses: 1
- Negative responses: 1
- Neutral responses: 1
- Positive keyword matches: 3
- Negative keyword matches: 3

## Additional tests

| Test | Feedback | Expected result |
|---|---|---|
| 2 | `EXCELLENT, helpful!` | Case-insensitive matching; 2 positive matches; POSITIVE |
| 3 | `bad and poor` | 2 negative matches; NEGATIVE |
| 4 | `The session is about the topic.` | No keyword matches; NEUTRAL |
| 5 | Empty comment | Zero matches; NEUTRAL |
| 6 | `not good` | Matches the word “good”; limitation is documented because negation is not understood |
| 7 | Response count is 0 | Program asks for a count of at least 1 again |

The program expects valid numeric input for response count. Scores are simple keyword counts, not a scientifically validated measure of student satisfaction.
