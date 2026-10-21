# Project 04: Multi-Stage Examination Eligibility System
# Beginner Python: variables, strings, conditions, loops, and lists.

MIN_ATTENDANCE_PERCENT = 75
MIN_INTERNAL_MARKS = 20
MAX_INTERNAL_MARKS = 50
YES_NO_OPTIONS = ["Y", "N"]

number_of_students = int(input("How many students do you want to check? "))
while number_of_students <= 0:
    print("Please enter a number greater than zero.")
    number_of_students = int(input("How many students do you want to check? "))

student_records = []
eligible_count = 0
not_eligible_count = 0

for student_number in range(1, number_of_students + 1):
    print("\nStudent", student_number)

    student_name = input("Enter student name: ")
    while student_name == "":
        print("Student name cannot be blank.")
        student_name = input("Enter student name: ")

    attendance = int(input("Enter attendance percentage (0-100): "))
    while attendance < 0 or attendance > 100:
        print("Attendance must be between 0 and 100.")
        attendance = int(input("Enter attendance percentage (0-100): "))

    lab_status = input("Are all required laboratory activities completed? (Y/N): ")
    lab_status = lab_status.upper()
    while lab_status not in YES_NO_OPTIONS:
        print("Please enter Y for yes or N for no.")
        lab_status = input("Are all required laboratory activities completed? (Y/N): ")
        lab_status = lab_status.upper()

    internal_marks = int(input("Enter internal marks out of 50: "))
    while internal_marks < 0 or internal_marks > MAX_INTERNAL_MARKS:
        print("Internal marks must be between 0 and 50.")
        internal_marks = int(input("Enter internal marks out of 50: "))

    fee_status = input("Are the required fees cleared? (Y/N): ")
    fee_status = fee_status.upper()
    while fee_status not in YES_NO_OPTIONS:
        print("Please enter Y for yes or N for no.")
        fee_status = input("Are the required fees cleared? (Y/N): ")
        fee_status = fee_status.upper()

    unmet_requirements = []

    if attendance < MIN_ATTENDANCE_PERCENT:
        unmet_requirements.append("Attendance is below 75%.")

    if lab_status == "N":
        unmet_requirements.append("Required laboratory activities are incomplete.")

    if internal_marks < MIN_INTERNAL_MARKS:
        unmet_requirements.append("Internal marks are below 20 out of 50.")

    if fee_status == "N":
        unmet_requirements.append("Required fees are not cleared.")

    if len(unmet_requirements) == 0:
        eligibility_status = "ELIGIBLE"
        eligible_count = eligible_count + 1
    else:
        eligibility_status = "NOT ELIGIBLE"
        not_eligible_count = not_eligible_count + 1

    student_records.append([
        student_name,
        attendance,
        lab_status,
        internal_marks,
        fee_status,
        eligibility_status,
        unmet_requirements,
    ])

    print("\nResult for", student_name)
    print("Eligibility:", eligibility_status)

    if len(unmet_requirements) == 0:
        print("All eligibility requirements are satisfied.")
    else:
        print("Requirements to complete:")
        for requirement in unmet_requirements:
            print("-", requirement)

print("\n========== EXAMINATION ELIGIBILITY SUMMARY ==========")
print("Students checked:", len(student_records))
print("Eligible students:", eligible_count)
print("Not eligible students:", not_eligible_count)

print("\nStudent-wise report:")
for record in student_records:
    print("\nName:", record[0])
    print("Attendance:", str(record[1]) + "%")
    print("Laboratory completed:", record[2])
    print("Internal marks:", str(record[3]) + "/50")
    print("Fees cleared:", record[4])
    print("Status:", record[5])

    if len(record[6]) == 0:
        print("Reason: All requirements satisfied.")
    else:
        print("Reasons:")
        for requirement in record[6]:
            print("-", requirement)

print("\nEligibility checking completed.")
