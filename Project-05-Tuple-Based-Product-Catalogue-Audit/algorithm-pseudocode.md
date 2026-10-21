# Project 05 — Algorithm and Pseudocode

## Algorithm

1. Start the program.
2. Set the low-stock limit to 5.
3. Ask for the number of product records; repeat the prompt until it is at least 1.
4. For every product, read its ID, name, category, price, and stock quantity.
5. Store these five values together as a tuple in a catalogue list.
6. For each catalogue tuple:
   - Compare its ID with earlier product IDs to detect a duplicate.
   - Check whether the name or category is blank.
   - Check whether the price is zero or negative.
   - Check whether stock is negative, zero, or between 1 and the low-stock limit.
   - Print the product details and any audit warnings.
7. Count each type of audit issue.
8. Print the totals and finish.

## Pseudocode

~~~text
START
  low_stock_limit = 5
  INPUT product_count
  WHILE product_count < 1
    DISPLAY "Enter at least one product"
    INPUT product_count
  END WHILE

  catalogue = empty list

  FOR each product
    INPUT product_id, name, category, price, stock
    product = (product_id, name, category, price, stock)
    APPEND product to catalogue
  END FOR

  SET all issue counters to 0

  FOR each product at position i
    GET product tuple and its values
    SET issues to empty list
    compare product ID with every earlier ID
    IF duplicate THEN add warning and update counter
    IF name or category is blank THEN add warning and update counter
    IF price <= 0 THEN add warning and update counter
    IF stock < 0 THEN add negative-stock warning
    ELSE IF stock == 0 THEN add out-of-stock warning
    ELSE IF stock <= low_stock_limit THEN add low-stock warning
    DISPLAY product details and warnings
  END FOR

  DISPLAY audit summary
END
~~~

## Complexity note

Duplicate-ID checking compares each record with earlier records, so the comparison work grows roughly with the square of the number of products. This is acceptable for a small beginner exercise.
