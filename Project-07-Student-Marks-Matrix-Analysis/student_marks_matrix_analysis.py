print("STUDENT MARKS MATRIX ANALYSIS")
print("------------------------------")

pass_mark = 40

student_count = int(input("Enter number of students: "))
while student_count < 1:
    print("Please enter at least one student.")
    student_count = int(input("Enter number of students: "))

subject_count = int(input("Enter number of subjects: "))
while subject_count < 1:
    print("Please enter at least one subject.")
    subject_count = int(input("Enter number of subjects: "))

student_names = []
subject_names = []
marks_matrix = []

print("\nENTER SUBJECT NAMES")
for j in range(subject_count):
    subject_name = input("Subject " + str(j + 1) + ": ")
    while subject_name == "":
        print("Subject name cannot be blank.")
        subject_name = input("Subject " + str(j + 1) + ": ")
    subject_names.append(subject_name)

for i in range(student_count):
    student_name = input("\nEnter name of student " + str(i + 1) + ": ")
    while student_name == "":
        print("Student name cannot be blank.")
        student_name = input("Enter name of student " + str(i + 1) + ": ")
    student_names.append(student_name)

    student_marks = []
    for j in range(subject_count):
        mark = float(input("Enter marks in " + subject_names[j] + " (0-100): "))
        while mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            mark = float(input("Enter marks in " + subject_names[j] + " (0-100): "))
        student_marks.append(mark)

    marks_matrix.append(student_marks)

print("\nSTUDENT-WISE ANALYSIS")
print("---------------------")
passed_students = 0
failed_students = 0
grand_total = 0

for i in range(student_count):
    student_total = 0
    all_subjects_passed = True

    for j in range(subject_count):
        student_total = student_total + marks_matrix[i][j]
        if marks_matrix[i][j] < pass_mark:
            all_subjects_passed = False

    student_average = student_total / subject_count
    grand_total = grand_total + student_total

    if all_subjects_passed:
        status = "PASS"
        passed_students = passed_students + 1
    else:
        status = "FAIL"
        failed_students = failed_students + 1

    print(student_names[i], "| Total:", student_total,
          "| Average:", student_average, "|", status)

print("\nSUBJECT-WISE ANALYSIS")
print("---------------------")
for j in range(subject_count):
    subject_total = 0
    for i in range(student_count):
        subject_total = subject_total + marks_matrix[i][j]
    subject_average = subject_total / student_count
    print(subject_names[j], "| Total:", subject_total,
          "| Average:", subject_average)

highest_mark = marks_matrix[0][0]
lowest_mark = marks_matrix[0][0]
highest_student = student_names[0]
highest_subject = subject_names[0]
lowest_student = student_names[0]
lowest_subject = subject_names[0]

for i in range(student_count):
    for j in range(subject_count):
        if marks_matrix[i][j] > highest_mark:
            highest_mark = marks_matrix[i][j]
            highest_student = student_names[i]
            highest_subject = subject_names[j]
        if marks_matrix[i][j] < lowest_mark:
            lowest_mark = marks_matrix[i][j]
            lowest_student = student_names[i]
            lowest_subject = subject_names[j]

print("\nOVERALL SUMMARY")
print("---------------")
print("Students analysed:", student_count)
print("Subjects analysed:", subject_count)
print("Overall average mark:", grand_total / (student_count * subject_count))
print("Students passed all subjects:", passed_students)
print("Students who need improvement:", failed_students)
print("Highest mark:", highest_mark, "-", highest_student, "-", highest_subject)
print("Lowest mark:", lowest_mark, "-", lowest_student, "-", lowest_subject)
print("\nAnalysis complete. Pass mark is an example rule; confirm faculty requirements.")
