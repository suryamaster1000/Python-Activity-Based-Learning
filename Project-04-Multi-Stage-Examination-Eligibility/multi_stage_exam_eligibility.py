# Project 04: Multi-Stage Examination Eligibility System
# Beginner Python: input/output, variables, conditions, loops, and lists.

students = []
student_count = int(input("How many students do you want to check? "))
while student_count <= 0:
    print("Enter a number greater than zero.")
    student_count = int(input("How many students do you want to check? "))

for number in range(1, student_count + 1):
    print("\nStudent", number)
    name = input("Enter student name: ").strip()
    while name == "":
        print("Name cannot be blank.")
        name = input("Enter student name: ").strip()

    attendance = float(input("Enter attendance percentage (0-100): "))
    while attendance < 0 or attendance > 100:
        print("Attendance must be between 0 and 100.")
        attendance = float(input("Enter attendance percentage (0-100): "))

    labs = int(input("Enter completed lab count (0 or more): "))
    while labs < 0:
        print("Lab count cannot be negative.")
        labs = int(input("Enter completed lab count (0 or more): "))

    marks = float(input("Enter internal marks (0-100): "))
    while marks < 0 or marks > 100:
        print("Internal marks must be between 0 and 100.")
        marks = float(input("Enter internal marks (0-100): "))

    fees = input("Are fees cleared? (yes/no): ").strip().lower()
    while fees != "yes" and fees != "no":
        print("Please enter yes or no.")
        fees = input("Are fees cleared? (yes/no): ").strip().lower()

    reasons = []
    if attendance < 75:
        reasons.append("Attendance below 75%")
    if labs < 1:
        reasons.append("Required laboratory work not completed")
    if marks < 40:
        reasons.append("Internal marks below 40")
    if fees == "no":
        reasons.append("Fee clearance pending")

    if len(reasons) == 0:
        status = "ELIGIBLE"
    else:
        status = "NOT ELIGIBLE"

    students.append([name, status, reasons])
    print("\nResult for", name)
    print("Status:", status)
    if len(reasons) == 0:
        print("All examination requirements are satisfied.")
    else:
        print("Requirements to resolve:")
        for reason in reasons:
            print("-", reason)

eligible_count = 0
not_eligible_count = 0
print("\n========== ELIGIBILITY SUMMARY ==========")
for student in students:
    print(student[0], "|", student[1])
    if student[1] == "ELIGIBLE":
        eligible_count += 1
    else:
        not_eligible_count += 1
print("Total students checked:", len(students))
print("Eligible:", eligible_count)
print("Not eligible:", not_eligible_count)
print("Eligibility check completed.")
