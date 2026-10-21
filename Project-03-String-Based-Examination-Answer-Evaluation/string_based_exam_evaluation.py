# Project 03: String-Based Examination Answer Evaluation
# Uses beginner-level Python: strings, variables, conditions, loops, and lists.

CORRECT_MARKS = 4
NEGATIVE_MARKS = 1
VALID_ANSWERS = ["A", "B", "C", "D"]

answer_key_text = input("Enter the answer key separated by spaces (A/B/C/D): ")
answer_key = answer_key_text.upper().split()

while len(answer_key) == 0:
    print("The answer key cannot be empty.")
    answer_key_text = input("Enter the answer key separated by spaces (A/B/C/D): ")
    answer_key = answer_key_text.upper().split()

answer_key_is_valid = True
for answer in answer_key:
    if answer not in VALID_ANSWERS:
        answer_key_is_valid = False

while answer_key_is_valid == False:
    print("Invalid answer key. Use only A, B, C, and D separated by spaces.")
    answer_key_text = input("Enter the answer key separated by spaces (A/B/C/D): ")
    answer_key = answer_key_text.upper().split()

    while len(answer_key) == 0:
        print("The answer key cannot be empty.")
        answer_key_text = input("Enter the answer key separated by spaces (A/B/C/D): ")
        answer_key = answer_key_text.upper().split()

    answer_key_is_valid = True
    for answer in answer_key:
        if answer not in VALID_ANSWERS:
            answer_key_is_valid = False

number_of_students = int(input("How many students do you want to evaluate? "))
while number_of_students <= 0:
    print("Please enter a number greater than zero.")
    number_of_students = int(input("How many students do you want to evaluate? "))

student_records = []
total_correct = 0
total_incorrect = 0
total_unanswered = 0
total_marks = 0

for student_number in range(1, number_of_students + 1):
    print("\nStudent", student_number)

    student_name = input("Enter student name: ")
    while student_name == "":
        print("Student name cannot be blank.")
        student_name = input("Enter student name: ")

    answers_text = input(
        "Enter answers separated by spaces; use - for unanswered questions: "
    )
    student_answers = answers_text.upper().split()

    answers_are_valid = True
    if len(student_answers) != len(answer_key):
        answers_are_valid = False

    for answer in student_answers:
        if answer not in VALID_ANSWERS and answer != "-":
            answers_are_valid = False

    while answers_are_valid == False:
        print(
            "Invalid response. Enter exactly", len(answer_key),
            "answers using A, B, C, D, or - separated by spaces."
        )
        answers_text = input(
            "Enter answers separated by spaces; use - for unanswered questions: "
        )
        student_answers = answers_text.upper().split()

        answers_are_valid = True
        if len(student_answers) != len(answer_key):
            answers_are_valid = False

        for answer in student_answers:
            if answer not in VALID_ANSWERS and answer != "-":
                answers_are_valid = False

    correct_count = 0
    incorrect_count = 0
    unanswered_count = 0

    for question_number in range(len(answer_key)):
        if student_answers[question_number] == "-":
            unanswered_count = unanswered_count + 1
        elif student_answers[question_number] == answer_key[question_number]:
            correct_count = correct_count + 1
        else:
            incorrect_count = incorrect_count + 1

    marks = correct_count * CORRECT_MARKS - incorrect_count * NEGATIVE_MARKS

    student_records.append([
        student_name,
        correct_count,
        incorrect_count,
        unanswered_count,
        marks,
    ])

    total_correct = total_correct + correct_count
    total_incorrect = total_incorrect + incorrect_count
    total_unanswered = total_unanswered + unanswered_count
    total_marks = total_marks + marks

    print("\nResult for", student_name)
    print("Correct answers:   ", correct_count)
    print("Incorrect answers: ", incorrect_count)
    print("Unanswered:        ", unanswered_count)
    print("Final marks:       ", marks, "out of", len(answer_key) * CORRECT_MARKS)

print("\n========== EXAMINATION SUMMARY ==========")
print("Students evaluated:", len(student_records))
print("Questions per student:", len(answer_key))
print("Marks per correct answer:", CORRECT_MARKS)
print("Penalty per incorrect answer:", NEGATIVE_MARKS)
print("Total correct answers:", total_correct)
print("Total incorrect answers:", total_incorrect)
print("Total unanswered questions:", total_unanswered)
print("Combined marks for all students:", total_marks)

print("\nStudent-wise results:")
for record in student_records:
    print(
        record[0], "| Correct:", record[1],
        "| Incorrect:", record[2],
        "| Unanswered:", record[3],
        "| Marks:", record[4]
    )

print("\nAnswer evaluation completed.")
