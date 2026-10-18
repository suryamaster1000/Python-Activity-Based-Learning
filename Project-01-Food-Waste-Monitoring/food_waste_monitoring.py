LIMIT = 10

prepared_list = []
served_list = []
leftover_list = []
wastage_list = []

for day in range(1, 8):
    print("\nDay", day)

    prepared = int(input("Meals prepared: "))
    while prepared <= 0:
        print("Meals prepared must be greater than zero.")
        prepared = int(input("Meals prepared: "))

    served = int(input("Meals served: "))
    while served < 0 or served > prepared:
        print("Meals served must be between 0 and", prepared)
        served = int(input("Meals served: "))

    leftover = prepared - served
    wastage = leftover / prepared * 100

    prepared_list.append(prepared)
    served_list.append(served)
    leftover_list.append(leftover)
    wastage_list.append(wastage)

    print("Leftover meals:", leftover)
    print("Wastage percentage:", round(wastage, 2), "%")

    if wastage > LIMIT:
        print("Warning: High food waste!")
    else:
        print("Food waste is within the limit.")

total_prepared = 0
total_served = 0
total_leftover = 0

for day in range(7):
    total_prepared = total_prepared + prepared_list[day]
    total_served = total_served + served_list[day]
    total_leftover = total_leftover + leftover_list[day]

overall_wastage = total_leftover / total_prepared * 100

print("\n--- WEEKLY SUMMARY ---")
print("Meals prepared:", total_prepared)
print("Meals served:", total_served)
print("Leftover meals:", total_leftover)
print("Overall wastage:", round(overall_wastage, 2), "%")
