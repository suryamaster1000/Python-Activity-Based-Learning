# Project 03: Hospital Billing and Patient Classification
# Uses beginner-level Python: variables, input/output, conditions, loops, and lists.

SENIOR_AGE = 60
SENIOR_CONCESSION_PERCENT = 10
LOW_BILL_LIMIT = 1000
MODERATE_BILL_LIMIT = 5000

number_of_patients = int(input("How many patient bills do you want to prepare? "))
while number_of_patients <= 0:
    print("Please enter a number greater than zero.")
    number_of_patients = int(input("How many patient bills do you want to prepare? "))

patient_records = []
total_gross_amount = 0
total_concession_amount = 0
total_final_amount = 0

for patient_number in range(1, number_of_patients + 1):
    print("\nPatient", patient_number)

    patient_name = input("Enter patient name: ").strip()
    while patient_name == "":
        print("Patient name cannot be blank.")
        patient_name = input("Enter patient name: ").strip()

    age = int(input("Enter patient age in years: "))
    while age < 0:
        print("Age cannot be negative.")
        age = int(input("Enter patient age in years: "))

    consultation_fee = int(input("Enter consultation fee in rupees: "))
    while consultation_fee < 0:
        print("Fee cannot be negative.")
        consultation_fee = int(input("Enter consultation fee in rupees: "))

    diagnostic_fee = int(input("Enter diagnostic fee in rupees: "))
    while diagnostic_fee < 0:
        print("Fee cannot be negative.")
        diagnostic_fee = int(input("Enter diagnostic fee in rupees: "))

    treatment_fee = int(input("Enter treatment fee in rupees: "))
    while treatment_fee < 0:
        print("Fee cannot be negative.")
        treatment_fee = int(input("Enter treatment fee in rupees: "))

    gross_amount = consultation_fee + diagnostic_fee + treatment_fee

    if age >= SENIOR_AGE:
        concession_amount = gross_amount * SENIOR_CONCESSION_PERCENT / 100
    else:
        concession_amount = 0

    final_amount = gross_amount - concession_amount

    if final_amount <= LOW_BILL_LIMIT:
        billing_category = "LOW"
    elif final_amount <= MODERATE_BILL_LIMIT:
        billing_category = "MODERATE"
    else:
        billing_category = "HIGH"

    patient_records.append([
        patient_name,
        age,
        consultation_fee,
        diagnostic_fee,
        treatment_fee,
        gross_amount,
        concession_amount,
        final_amount,
        billing_category,
    ])

    total_gross_amount = total_gross_amount + gross_amount
    total_concession_amount = total_concession_amount + concession_amount
    total_final_amount = total_final_amount + final_amount

    print("\nBill for", patient_name)
    print("Consultation fee: Rs.", consultation_fee)
    print("Diagnostic fee:   Rs.", diagnostic_fee)
    print("Treatment fee:    Rs.", treatment_fee)
    print("Gross bill:       Rs.", format(gross_amount, ".2f"))
    print("Senior concession: Rs.", format(concession_amount, ".2f"))
    print("Final bill:       Rs.", format(final_amount, ".2f"))
    print("Billing category:", billing_category)

print("\n========== HOSPITAL BILLING SUMMARY ==========")
print("Patients processed:", len(patient_records))
print("Total gross bills:    Rs.", format(total_gross_amount, ".2f"))
print("Total concessions:    Rs.", format(total_concession_amount, ".2f"))
print("Total amount payable: Rs.", format(total_final_amount, ".2f"))

print("\nPatient category summary:")
for category in ["LOW", "MODERATE", "HIGH"]:
    category_count = 0
    for record in patient_records:
        if record[8] == category:
            category_count = category_count + 1
    print(category + " billing category:", category_count)

print("\nHospital billing completed.")
