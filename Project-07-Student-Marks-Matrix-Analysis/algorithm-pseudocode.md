# Project 07 — Algorithm and Pseudocode

## Algorithm

1. Start and set the example pass mark to 40.
2. Read the number of students and subjects; repeat each prompt until the value is at least 1.
3. Read each subject name.
4. For each student:
   - Read the student's name.
   - Read one mark per subject.
   - Ask again if any mark is below 0 or above 100.
   - Store the marks as a row in the matrix.
5. For each student row, calculate total and average; determine whether every mark is at least the pass mark.
6. For each subject column, calculate the total and average across students.
7. Scan the matrix to find the highest and lowest mark and their student/subject names.
8. Display student-wise results, subject-wise results, and the overall summary.
9. End.

## Pseudocode

~~~text
START
  pass_mark = 40
  INPUT student_count
  REPEAT until student_count >= 1
  INPUT subject_count
  REPEAT until subject_count >= 1

  INPUT each subject name
  marks_matrix = empty list

  FOR each student
    INPUT student name
    student_marks = empty list
    FOR each subject
      INPUT mark
      WHILE mark < 0 OR mark > 100
        DISPLAY mark-range warning
        INPUT mark again
      END WHILE
      APPEND mark to student_marks
    END FOR
    APPEND student_marks to marks_matrix
  END FOR

  FOR each student row
    total the marks
    average = total / subject_count
    IF every mark >= pass_mark
      status = PASS
    ELSE
      status = FAIL
    END IF
    DISPLAY student summary
  END FOR

  FOR each subject column
    total marks across students
    average = subject total / student_count
    DISPLAY subject summary
  END FOR

  SCAN every matrix value to find maximum and minimum
  DISPLAY overall averages and pass/fail counts
END
~~~

## Formulas

- Student total = sum of marks in that student's row
- Student average = student total / number of subjects
- Subject average = total marks in that subject column / number of students
- Overall average = sum of all marks / (number of students × number of subjects)
