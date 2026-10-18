# Project 01: Food Waste Monitoring System

**Case Study:** 53  
**Language:** Python 3

## 1. Problem statement
Canteens may prepare more meals than are served, causing food waste. This program records meals prepared and served for seven days, calculates leftovers and wastage percentages, and flags days where wastage exceeds 10%.

## 2. Objectives
- Record daily meals prepared and served.
- Calculate leftover meals and daily wastage percentage.
- Identify days exceeding the 10% threshold.
- Display weekly totals and overall wastage.

## 3. Assumptions
- The program covers seven days.
- Inputs are whole numbers.
- Meals prepared must be greater than zero.
- Meals served must be between zero and meals prepared.
- Wastage greater than 10% is flagged as high waste.

## 4. Formula
- Leftover meals = Meals prepared − Meals served
- Wastage percentage = (Leftover meals ÷ Meals prepared) × 100

## 5. Algorithm
1. Set the wastage limit to 10% and initialize weekly totals.
2. Repeat for each of seven days.
3. Read meals prepared and meals served.
4. Reject invalid values and ask again.
5. Calculate leftovers and wastage percentage.
6. Display the daily result and whether wastage exceeds the limit.
7. Update weekly totals.
8. Display weekly totals and overall wastage percentage.

## 6. Python program
See the file food_waste_monitoring.py in this folder.

## 7. Test cases
| Prepared | Served | Leftovers | Wastage | Expected result |
|---:|---:|---:|---:|---|
| 100 | 95 | 5 | 5% | Within limit |
| 100 | 85 | 15 | 15% | High waste |
| 200 | 180 | 20 | 10% | Within limit |
| 50 | 50 | 0 | 0% | No leftovers |
| 100 | 120 | — | — | Invalid input |
| 0 | 0 | — | — | Invalid input |

## 8. Learning outcome
This project practices variables, numeric input, arithmetic, loops, input validation, and if-else decisions.

## 9. Conclusion
The program summarizes food usage and helps identify days when meal preparation could be better matched to demand.

## 10. Screenshots
After running the program, capture screenshots showing daily calculations and the weekly summary. Add them to a screenshots folder before final submission.

## Run
python food_waste_monitoring.py
