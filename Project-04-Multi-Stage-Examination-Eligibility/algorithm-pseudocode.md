# Algorithm and Pseudocode — Multi-Stage Examination Eligibility

## Algorithm
1. Start.
2. Use the example rules: attendance at least 75%, at least one completed lab, internal marks at least 40/100, and fees cleared.
3. Input the number of students and ensure it is greater than zero.
4. For each student, input a non-blank name, attendance, lab count, internal marks, and fee status.
5. Create an empty list of unmet requirements.
6. Add a reason for every condition that is not satisfied.
7. If the reasons list is empty, mark the student ELIGIBLE; otherwise mark NOT ELIGIBLE.
8. Save and display the result.
9. Count eligible and not-eligible students, display totals, and stop.

## Pseudocode
    BEGIN
      INPUT student_count
      WHILE student_count <= 0
        DISPLAY error and INPUT again
      END WHILE
      students <- empty list
      FOR each student
        INPUT name, attendance, labs, marks, fee_status
        reasons <- empty list
        IF attendance < 75: APPEND attendance reason
        IF labs < 1: APPEND lab reason
        IF marks < 40: APPEND marks reason
        IF fee_status equals "no": APPEND fee reason
        IF reasons is empty: status <- ELIGIBLE
        ELSE: status <- NOT ELIGIBLE
        SAVE student and DISPLAY result
      END FOR
      DISPLAY eligible and not-eligible totals
    END

Note: these thresholds are illustrative assumptions, not official university policy.
