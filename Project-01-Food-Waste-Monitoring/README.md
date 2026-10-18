# Project 01: Food Waste Monitoring System

**Case Study:** 53  
**Language:** Python 3

## 1. Problem statement

A canteen may prepare more meals than people eat. This program records meals prepared and served for seven days, calculates leftovers and wastage, and warns when wastage is more than 10%.

## 2. Python topics used

This version uses only topics from the completed Units I–III:

- Variables and numeric data types
- `int()` for input conversion
- Arithmetic operators
- `if-else` and logical operators
- `for` loops with `range()`
- `while` loops
- Lists, indexing, and `append()`
- `round()` to display percentages neatly

It does not use user-defined functions, `try-except`, imports, classes, or advanced Python features.

## 3. Formula

- Leftover meals = Meals prepared - Meals served
- Wastage percentage = (Leftover meals / Meals prepared) * 100

## 4. Algorithm

1. Create empty lists to store daily meal details.
2. Repeat for seven days.
3. Read the number of meals prepared. Ask again if it is not greater than zero.
4. Read the number of meals served. Ask again if it is less than zero or more than meals prepared.
5. Calculate leftovers and wastage percentage.
6. Store the daily values in lists using `append()`.
7. Use `if-else` to show a warning when wastage is more than 10%.
8. Use a loop to calculate weekly totals and display the summary.

## 5. Run the program

Open a terminal in this folder and run:

```bash
python food_waste_monitoring.py
```

Enter whole numbers when asked. The program validates meal counts, but letters such as `abc` are not accepted as numeric input.

## 6. Manual test cases

Try these prepared/served values on a day and compare the result:

| Prepared | Served | Expected result |
|---:|---:|---|
| 100 | 95 | 5 leftovers, 5% wastage, within limit |
| 100 | 85 | 15 leftovers, 15% wastage, warning |
| 200 | 180 | 20 leftovers, 10% wastage, within limit |
| 50 | 50 | 0 leftovers, 0% wastage |
| 100 | 120 | Rejected; asks for served count again |
| 0 | 0 | Rejected; asks for prepared count again |

For the weekly summary, enter valid values for all seven days.

## 7. Learning outcome

This project practices variables, input conversion, arithmetic, conditions, loops, lists, and list indexing using beginner-level Python.

## 8. Screenshots for submission

Capture:
- A normal result (100 prepared, 95 served)
- A high-waste warning (100 prepared, 85 served)
- The weekly summary
