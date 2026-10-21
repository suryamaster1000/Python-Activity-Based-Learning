# Project 10 — Algorithm and Pseudocode

## Algorithm

1. Start the program and ask for the number of appliances; repeat until it is at least 1.
2. For each appliance, read its name, average daily consumption before changes, and average daily consumption after changes.
3. Reject blank names and negative readings.
4. For each appliance:
   - Calculate before minus after.
   - If the result is positive, classify it as reduced use.
   - If the result is negative, classify it as increased use.
   - If the result is zero, classify it as unchanged.
   - Display the difference and the relevant percentage when the baseline is greater than zero.
5. Calculate total before and after consumption.
6. Calculate the overall difference and percentage, where defined.
7. Display counts of reduced, increased, and unchanged appliances.
8. End.

## Pseudocode

~~~text
START
  INPUT appliance_count
  REPEAT until appliance_count >= 1

  FOR each appliance
    INPUT nonblank name
    INPUT before_reading
    WHILE before_reading < 0
      ASK for a non-negative reading
      INPUT before_reading again
    END WHILE
    INPUT after_reading
    WHILE after_reading < 0
      ASK for a non-negative reading
      INPUT after_reading again
    END WHILE
    STORE appliance and readings
  END FOR

  SET totals and category counters to 0
  FOR each appliance
    difference = before_reading - after_reading
    ADD readings to before and after totals
    IF difference > 0
      COUNT reduced appliance
      CALCULATE reduction percentage if baseline > 0
    ELSE IF difference < 0
      COUNT increased appliance
      CALCULATE increase percentage if baseline > 0
    ELSE
      COUNT unchanged appliance
    END IF
    DISPLAY appliance comparison
  END FOR

  COMPARE total before and total after
  DISPLAY net daily change and percentage if defined
  DISPLAY category counts
END
~~~

## Interpretation

Lower after-consumption is a reduction for that appliance, but a simple before-and-after comparison does not prove the cause. Use comparable periods and consider factors such as weather, occupancy, and operating hours.
