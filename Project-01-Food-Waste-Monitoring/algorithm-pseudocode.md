# Algorithm and Pseudocode — Food Waste Monitoring System

## Algorithm
1. Start.
2. Set the wastage limit to 10%.
3. Set total prepared, served, and leftover values to zero.
4. Repeat for days 1 through 7:
   - Input prepared and served meals.
   - If prepared is not positive, served is negative, or served exceeds prepared, display an error and request the values again.
   - Calculate leftovers as prepared minus served.
   - Calculate wastage percentage as leftovers divided by prepared, multiplied by 100.
   - Display leftovers and wastage percentage.
   - If wastage percentage is greater than 10, display a high-waste warning; otherwise, display that wastage is within the limit.
   - Add the day's values to weekly totals.
5. Display weekly totals and overall wastage percentage.
6. Stop.

## Pseudocode
BEGIN
    LIMIT ← 10
    total_prepared ← 0
    total_served ← 0
    total_leftover ← 0

    FOR day ← 1 TO 7
        REPEAT
            INPUT prepared
            INPUT served
            IF prepared <= 0 OR served < 0 OR served > prepared THEN
                DISPLAY "Invalid input"
            END IF
        UNTIL prepared > 0 AND 0 <= served AND served <= prepared

        leftover ← prepared - served
        wastage ← (leftover / prepared) * 100
        DISPLAY leftover
        DISPLAY wastage

        IF wastage > LIMIT THEN
            DISPLAY "High food waste"
        ELSE
            DISPLAY "Food waste is within the limit"
        END IF

        total_prepared ← total_prepared + prepared
        total_served ← total_served + served
        total_leftover ← total_leftover + leftover
    END FOR

    DISPLAY total_prepared, total_served, total_leftover
    overall_wastage ← (total_leftover / total_prepared) * 100
    DISPLAY overall_wastage
END
