# Project 09 — Algorithm and Pseudocode

## Algorithm

1. Start the program and display the simulation-only notice.
2. Read a fictional starting balance; repeat if it is negative.
3. Create an empty transaction history and set summary counters to zero.
4. Display the ATM menu repeatedly until Exit is selected.
5. For a deposit, require an amount greater than zero; if valid, add it to the balance and record it.
6. For a withdrawal, require an amount greater than zero and no greater than the balance; if valid, subtract it and record it. Otherwise, record a rejected attempt.
7. For a balance enquiry, show the current balance and add the enquiry to the history.
8. For an invalid menu option, show a warning without changing the balance.
9. After exit, display the transaction history, counters, and final simulated balance.
10. End.

## Pseudocode

~~~text
START
  DISPLAY simulation-only notice
  INPUT starting balance
  WHILE balance < 0
    DISPLAY warning
    INPUT balance again
  END WHILE

  transactions = empty list
  SET deposit, withdrawal, and declined counters to 0

  REPEAT
    DISPLAY ATM menu
    INPUT choice

    IF choice is deposit
      INPUT amount
      IF amount <= 0
        record rejected deposit
        increase declined counter
      ELSE
        ADD amount to balance
        increase deposit counter
        record deposit
      END IF

    ELSE IF choice is withdrawal
      INPUT amount
      IF amount <= 0 OR amount > balance
        record rejected withdrawal
        increase declined counter
      ELSE
        SUBTRACT amount from balance
        increase withdrawal counter
        record withdrawal
      END IF

    ELSE IF choice is balance enquiry
      DISPLAY and record current balance

    ELSE IF choice is exit
      STOP repeating

    ELSE
      DISPLAY invalid choice
    END IF
  UNTIL exit is selected

  DISPLAY transaction history
  DISPLAY counters and final simulated balance
END
~~~

## Important note

The program is not a real banking application. Its balance is only a number kept in memory while the program runs.
