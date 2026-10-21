# Algorithm and Pseudocode — String-Based Examination Answer Evaluation

## Algorithm

1. Start.
2. Set marks for a correct response to 4 and the penalty for an incorrect response to 1.
3. Input an answer key containing space-separated A, B, C, or D options. Reject an empty or invalid key.
4. Input the number of students. Keep asking until the number is greater than zero.
5. Set the student records and total counts to empty or zero.
6. Repeat for each student:
   - Input the student's name. Ask again if it is blank.
   - Input the student's responses as a space-separated string. Use a dash (-) for unanswered questions.
   - Check that the response count equals the answer-key length.
   - Check that each response is A, B, C, D, or a dash. Ask again if the response is invalid.
   - Compare each response with the answer at the same position in the answer key.
   - Count correct responses, incorrect responses, and unanswered questions.
   - Calculate marks by multiplying correct responses by 4 and subtracting 1 for every incorrect response.
   - Store the student's name, counts, and marks; update the class totals.
   - Display that student's results.
7. Display the class totals and each student's saved results.
8. Stop.

## Pseudocode

~~~text
BEGIN
    CORRECT_MARKS <- 4
    NEGATIVE_MARKS <- 1
    VALID_ANSWERS <- ["A", "B", "C", "D"]

    INPUT answer_key_string
    answer_key <- uppercase(answer_key_string).split_into_words()

    WHILE answer_key is empty or contains invalid options
        DISPLAY error message
        INPUT answer_key_string again
        answer_key <- uppercase(answer_key_string).split_into_words()
    END WHILE

    INPUT number_of_students
    WHILE number_of_students <= 0
        DISPLAY "Enter a number greater than zero"
        INPUT number_of_students again
    END WHILE

    student_records <- empty list
    total_correct <- 0
    total_incorrect <- 0
    total_unanswered <- 0
    total_marks <- 0

    FOR each student
        INPUT student_name
        WHILE student_name is blank
            INPUT student_name again
        END WHILE

        INPUT response_string
        student_answers <- uppercase(response_string).split_into_words()

        WHILE response count is not equal to answer-key length
              OR any response is not A, B, C, D, or "-"
            DISPLAY response-format error
            INPUT response_string again
            student_answers <- uppercase(response_string).split_into_words()
        END WHILE

        correct <- 0
        incorrect <- 0
        unanswered <- 0

        FOR each question position
            IF response is "-"
                unanswered <- unanswered + 1
            ELSE IF response equals answer at the same key position
                correct <- correct + 1
            ELSE
                incorrect <- incorrect + 1
            END IF
        END FOR

        marks <- correct * 4 - incorrect * 1
        APPEND student name, counts, and marks to student_records
        UPDATE class totals
        DISPLAY student result
    END FOR

    DISPLAY totals and student-wise results
END
~~~

## Assumed policy

The program uses 4 marks for a correct answer, a penalty of 1 mark for an incorrect answer, and zero marks for an unanswered question. The answer key contains only A/B/C/D options. A dash marks a blank response.
