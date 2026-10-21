# Project 03 — Test Cases

The following expected results use the assumptions documented in the README. Amounts are in Indian rupees.

| # | Age | Consultation | Diagnostic | Treatment | Expected gross | Concession | Expected final bill | Expected category |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 30 | 500 | 250 | 250 | 1000.00 | 0.00 | 1000.00 | LOW |
| 2 | 65 | 1000 | 1500 | 3500 | 6000.00 | 600.00 | 5400.00 | HIGH |
| 3 | 45 | 400 | 300 | 800 | 1500.00 | 0.00 | 1500.00 | MODERATE |
| 4 | 70 | 0 | 0 | 0 | 0.00 | 0.00 | 0.00 | LOW |
| 5 | 32 | 1000 | 2000 | 2000 | 5000.00 | 0.00 | 5000.00 | MODERATE |
| 6 | 40 | 2000 | 2000 | 1001 | 5001.00 | 0.00 | 5001.00 | HIGH |
| 7 | 60 | 1000 | 1000 | 3000 | 5000.00 | 500.00 | 4500.00 | MODERATE |

## Input-validation checks

| Input condition | Expected behaviour |
|---|---|
| Patient count is 0 or negative | Ask for a positive count again |
| Patient name is blank | Ask for the name again |
| Age is negative | Ask for age again |
| Any fee is negative | Ask for that fee again |
| Any fee is 0 | Accept it |

The program expects whole-number numeric inputs. Letters entered where a number is expected are outside the current beginner-level input assumptions because exception handling is not used.
