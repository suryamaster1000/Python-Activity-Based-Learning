# Algorithm and Pseudocode — Multi-Stage Examination Eligibility System

## Algorithm

1. Start.
2. Define the minimum attendance as 75%, minimum internal marks as 20, and maximum internal marks as 50.
3. Input the number of students. Keep asking until the number is greater than zero.
4. Create an empty list for student records and set eligible and not eligible counts to zero.
5. Repeat for each student:
   - Input the student's name. Ask again if it is blank.
   - Input attendance and ask again if it is outside 0–100.
   - Input laboratory completion as Y or N. Ask again for any other response.
   - Input internal marks and ask again if they are outside 0–50.
   - Input fee clearance as Y or N. Ask again for any other response.
   - Create an empty list of unmet requirements.
   - Add a reason if attendance is below 75%.
   - Add a reason if laboratory activities are incomplete.
   - Add a reason if internal marks are below 20 out of 50.
   - Add a reason if required fees are not cleared.
   - If there are no unmet requirements, mark the student ELIGIBLE and increase the eligible count.
   - Otherwise, mark the student NOT ELIGIBLE and increase the not eligible count.
   - Store the student's details and list of unmet requirements.
   - Display the student's status and all unmet requirements.
6. Display the overall counts and the saved student-wise report.
7. Stop.

## Pseudocode

~~~text
BEGIN
    MIN_ATTENDANCE <- 75
    MIN_INTERNAL_MARKS <- 20
    MAX_INTERNAL_MARKS <- 50

    INPUT number_of_students
    WHILE number_of_students <= 0
        DISPLAY "Enter a number greater than zero"
        INPUT number_of_students again
    END WHILE

    student_records <- empty list
    eligible_count <- 0
    not_eligible_count <- 0

    FOR each student
        INPUT student_name
        WHILE student_name is blank
            INPUT student_name again
        END WHILE

        INPUT attendance
        WHILE attendance < 0 OR attendance > 100
            DISPLAY "Attendance must be from 0 to 100"
            INPUT attendance again
        END WHILE

        INPUT lab_status
        WHILE lab_status is not Y or N
            INPUT lab_status again
        END WHILE

        INPUT internal_marks
        WHILE internal_marks < 0 OR internal_marks > 50
            DISPLAY "Internal marks must be from 0 to 50"
            INPUT internal_marks again
        END WHILE

        INPUT fee_status
        WHILE fee_status is not Y or N
            INPUT fee_status again
        END WHILE

        unmet_requirements <- empty list

        IF attendance < MIN_ATTENDANCE
            APPEND attendance reason to unmet_requirements
        END IF
        IF lab_status is N
            APPEND laboratory reason to unmet_requirements
        END IF
        IF internal_marks < MIN_INTERNAL_MARKS
            APPEND internal marks reason to unmet_requirements
        END IF
        IF fee_status is N
            APPEND fee reason to unmet_requirements
        END IF

        IF unmet_requirements is empty
            status <- "ELIGIBLE"
            eligible_count <- eligible_count + 1
        ELSE
            status <- "NOT ELIGIBLE"
            not_eligible_count <- not_eligible_count + 1
        END IF

        APPEND student details, status, and unmet_requirements to student_records
        DISPLAY student's status and all unmet requirements
    END FOR

    DISPLAY eligible_count and not_eligible_count
    DISPLAY all student records
END
~~~

## Assumed policy

The program uses 75% attendance, completed laboratory activities, at least 20 out of 50 internal marks, and cleared fees as requirements. These values are sample assumptions, not an official university rule.
