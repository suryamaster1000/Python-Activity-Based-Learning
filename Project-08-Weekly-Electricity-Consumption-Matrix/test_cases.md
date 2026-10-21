# Project 08 — Test Cases

## Test Case 1: Two weeks of electricity readings

**Readings in kWh**

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Weekly total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Week 1 | 8 | 9 | 7 | 10 | 11 | 13 | 12 | 70 |
| Week 2 | 12 | 14 | 16 | 18 | 15 | 11 | 9 | 95 |

**Expected report**

- Week 1 total: 70.0 kWh; daily average: 10.0 kWh
- Week 2 total: 95.0 kWh; daily average: 13.571428571428571 kWh
- Change from Week 1 to Week 2: increase of 25.0 kWh
- Percentage change: 35.714285714285715%
- Total electricity consumption: 165.0 kWh
- Average daily consumption: 11.785714285714286 kWh
- Highest daily consumption: 18.0 kWh — Week 2 Thursday
- Lowest daily consumption: 7.0 kWh — Week 1 Wednesday
- Days above the example 15 kWh alert limit: 2 (Week 2 Wednesday and Thursday)

## Additional tests

| Test | Input condition | Expected result |
|---|---|---|
| 2 | One week of seven readings | Weekly summary appears and no week-to-week comparison is shown |
| 3 | All readings are 0 | Total and averages are 0; no alerts appear |
| 4 | Previous week total is 0 and next week total is above 0 | Change in kWh appears; percent change is reported as unavailable rather than dividing by zero |
| 5 | One daily reading is -1 | Program asks for a non-negative reading again |
| 6 | Daily reading equals 15 | It does not trigger the alert because only readings above 15 trigger it |
| 7 | Week count is 0 | Program asks for a count of at least 1 again |

Calculated values are printed with Python's default float representation rather than rounded to two decimal places. The project expects valid numeric input where a number is requested. The alert threshold is an example setting and can be adjusted.
