# Project 10 — Test Cases

## Test Case 1: Three reductions and one increase

**Input values (average kWh/day)**

| Appliance | Before | After | Expected result |
|---|---:|---:|---|
| Lights | 12 | 8 | Reduced by 4; 33.33% reduction |
| Fans | 15 | 12 | Reduced by 3; 20.00% reduction |
| Air conditioner | 20 | 16 | Reduced by 4; 20.00% reduction |
| Computer | 5 | 6 | Increased by 1; 20.00% increase |

**Expected overall summary**

- Appliances compared: 4
- Total BEFORE changes: 52.00 kWh/day
- Total AFTER changes: 42.00 kWh/day
- Net daily energy reduction: 10.00 kWh/day
- Overall reduction: 19.23%
- Appliances with reduced use: 3
- Appliances with increased use: 1
- Appliances with unchanged use: 0

## Additional tests

| Test | Input condition | Expected result |
|---|---|---|
| 2 | Same before and after reading for an appliance | No change in daily use |
| 3 | Before 10, after 0 | 10 kWh/day reduction and 100% reduction |
| 4 | Before 0, after 4 | Increase is shown; percentage is unavailable because the baseline was zero |
| 5 | Before 5, after 8 | Increase of 3 kWh/day and 60% increase |
| 6 | Negative before or after reading | Program asks for a non-negative reading again |
| 7 | Appliance count is 0 | Program asks for a count of at least 1 again |

The program expects valid numeric input at number prompts. Entered values should describe comparable periods in kWh/day for a meaningful comparison.
