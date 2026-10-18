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
Run `food_waste_monitoring.py` for the interactive seven-day program. The reusable `calculate_wastage()` function makes the calculation easier to test automatically.

## 7. Manual test cases
Run the program and enter each prepared/served pair on a day. To test invalid inputs, enter the invalid pair and confirm that the program asks again.

| Prepared | Served | Expected result |
|---:|---:|---|
| 100 | 95 | 5 leftovers; 5% wastage; within limit |
| 100 | 85 | 15 leftovers; 15% wastage; high-waste warning |
| 200 | 180 | 20 leftovers; 10% wastage; within limit |
| 50 | 50 | 0 leftovers; 0% wastage |
| 100 | 120 | Invalid input; ask again |
| 0 | 0 | Invalid input; ask again |
| Type `abc` | — | Invalid input; ask again |

## 8. Automated testing with pytest

### Install pytest
Open a terminal in this project folder and run:

```bash
python -m pip install pytest
```

### Run the automated tests
From this folder, run:

```bash
python -m pytest -v
```

The test file `test_food_waste_monitoring.py` checks valid calculations, the 10% boundary, zero waste, 100% waste, and invalid values. A successful run should report **9 passed**.

## 9. Learning outcome
This project practices variables, numeric input, arithmetic, loops, input validation, if-else decisions, reusable functions, and automated testing.

## 10. Conclusion
The program summarizes food usage and helps identify days when meal preparation could be better matched to demand.

## 11. Screenshots
For the submission, capture:
- The program showing a normal result (for example, 100 prepared and 95 served).
- The program showing the high-waste warning (for example, 100 prepared and 85 served).
- The weekly summary.
- The terminal output after running `python -m pytest -v`.

## Run the program

```bash
python food_waste_monitoring.py
```
