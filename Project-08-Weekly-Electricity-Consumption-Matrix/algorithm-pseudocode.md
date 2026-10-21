# Project 08 — Algorithm and Pseudocode

## Algorithm

1. Start and define the seven day names and example high-use threshold of 15 kWh.
2. Ask for the number of weeks; repeat until it is at least 1.
3. For each week, read seven non-negative daily readings and store them as one row in the matrix.
4. Calculate each week's total by adding its seven readings.
5. Display each weekly total and average daily consumption.
6. Compare every week after the first with the previous week's total; show the direction and size of change.
7. Calculate percentage change if the previous weekly total is not zero.
8. Scan all readings to find the highest and lowest daily consumption and count readings greater than the alert threshold.
9. Display the overall total, average daily consumption, highest and lowest readings, and number of high-use days.
10. End.

## Pseudocode

~~~text
START
  days = Monday through Sunday
  high_usage_limit = 15
  INPUT week_count
  WHILE week_count < 1
    DISPLAY count warning
    INPUT week_count
  END WHILE

  consumption_matrix = empty list

  FOR each week
    week_usage = empty list
    FOR each of seven days
      INPUT units
      WHILE units < 0
        DISPLAY negative-value warning
        INPUT units again
      END WHILE
      APPEND units to week_usage
    END FOR
    APPEND week_usage to matrix
  END FOR

  FOR each week
    CALCULATE weekly total
    STORE weekly total
  END FOR

  FOR each week
    DISPLAY weekly total and daily average
    IF week is not the first
      change = current total - previous total
      DISPLAY increase, decrease, or no change
      IF previous total is not zero
        CALCULATE and DISPLAY percentage change
      ELSE
        DISPLAY percentage unavailable
      END IF
    END IF
  END FOR

  SCAN all daily values
  FIND highest and lowest readings
  COUNT values greater than high_usage_limit
  DISPLAY overall consumption summary
END
~~~

## Formulas

- Weekly total = sum of seven daily readings
- Weekly daily average = weekly total / 7
- Weekly change = current weekly total − previous weekly total
- Percentage change = (weekly change / previous weekly total) × 100, when the previous total is not zero
- Overall average daily consumption = total consumption / (number of weeks × 7)
