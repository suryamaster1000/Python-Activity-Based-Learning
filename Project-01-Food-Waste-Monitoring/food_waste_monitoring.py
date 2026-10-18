LIMIT = 10

total_prepared = 0
total_served = 0
total_leftover = 0

for day in range(1, 8):
    print("\nDay", day)

    while True:
        try:
            prepared = int(input("Meals prepared: "))
            served = int(input("Meals served: "))
        except ValueError:
            print("Invalid input! Enter whole numbers.")
            continue

        if prepared > 0 and 0 <= served <= prepared:
            break

        print("Invalid input! Meals prepared must be positive, and served meals must be between 0 and prepared meals.")

    leftover = prepared - served
    wastage = (leftover / prepared) * 100

    print("Leftover meals:", leftover)
    print("Wastage percentage:", round(wastage, 2), "%")

    if wastage > LIMIT:
        print("Warning: High food waste!")
    else:
        print("Food waste is within the limit.")

    total_prepared += prepared
    total_served += served
    total_leftover += leftover

print("\n--- WEEKLY SUMMARY ---")
print("Total meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total leftover meals:", total_leftover)

overall_wastage = (total_leftover / total_prepared) * 100
print("Overall wastage:", round(overall_wastage, 2), "%")
