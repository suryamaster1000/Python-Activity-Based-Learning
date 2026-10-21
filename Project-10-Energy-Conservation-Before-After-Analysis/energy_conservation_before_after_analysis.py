print("ENERGY CONSERVATION BEFORE-AND-AFTER ANALYSIS")
print("---------------------------------------------")
print("Enter average daily electricity use for the same period in kWh/day.")

appliance_count = int(input("Enter number of appliances to compare: "))
while appliance_count < 1:
    print("Please enter at least one appliance.")
    appliance_count = int(input("Enter number of appliances to compare: "))

appliance_names = []
before_use = []
after_use = []

for i in range(appliance_count):
    print("\nAppliance", i + 1)
    appliance_name = input("Appliance name: ").strip()
    while appliance_name == "":
        print("Appliance name cannot be blank.")
        appliance_name = input("Appliance name: ").strip()

    before_units = float(input("Average daily use BEFORE changes (kWh/day): "))
    while before_units < 0:
        print("Consumption cannot be negative.")
        before_units = float(input("Average daily use BEFORE changes (kWh/day): "))

    after_units = float(input("Average daily use AFTER changes (kWh/day): "))
    while after_units < 0:
        print("Consumption cannot be negative.")
        after_units = float(input("Average daily use AFTER changes (kWh/day): "))

    appliance_names.append(appliance_name)
    before_use.append(before_units)
    after_use.append(after_units)

before_total = 0
after_total = 0
reduced_count = 0
increased_count = 0
unchanged_count = 0

print("\nAPPLIANCE-WISE COMPARISON")
print("-------------------------")

for i in range(appliance_count):
    before_units = before_use[i]
    after_units = after_use[i]
    difference = before_units - after_units
    before_total = before_total + before_units
    after_total = after_total + after_units

    if difference > 0:
        reduced_count = reduced_count + 1
        if before_units > 0:
            percent = (difference / before_units) * 100
            print(appliance_names[i], "| Reduced:", format(difference, ".2f"),
                  "kWh/day | Reduction:", format(percent, ".2f"), "%")
        else:
            print(appliance_names[i], "| Reduced:", format(difference, ".2f"),
                  "kWh/day | Percentage unavailable (before reading was zero)")
    elif difference < 0:
        increased_count = increased_count + 1
        increase = after_units - before_units
        if before_units > 0:
            percent = (increase / before_units) * 100
            print(appliance_names[i], "| Increased:", format(increase, ".2f"),
                  "kWh/day | Increase:", format(percent, ".2f"), "%")
        else:
            print(appliance_names[i], "| Increased:", format(increase, ".2f"),
                  "kWh/day | Percentage unavailable (before reading was zero)")
    else:
        unchanged_count = unchanged_count + 1
        print(appliance_names[i], "| No change in daily use.")

net_reduction = before_total - after_total

print("\nOVERALL SUMMARY")
print("---------------")
print("Appliances compared:", appliance_count)
print("Total BEFORE changes:", format(before_total, ".2f"), "kWh/day")
print("Total AFTER changes:", format(after_total, ".2f"), "kWh/day")

if net_reduction > 0:
    print("Net daily energy reduction:", format(net_reduction, ".2f"), "kWh/day")
    if before_total > 0:
        reduction_percent = (net_reduction / before_total) * 100
        print("Overall reduction:", format(reduction_percent, ".2f"), "%")
    else:
        print("Overall percentage reduction unavailable because the before total was zero.")
elif net_reduction < 0:
    net_increase = abs(net_reduction)
    print("Net daily energy increase:", format(net_increase, ".2f"), "kWh/day")
    if before_total > 0:
        increase_percent = (net_increase / before_total) * 100
        print("Overall increase:", format(increase_percent, ".2f"), "%")
    else:
        print("Overall percentage increase unavailable because the before total was zero.")
else:
    print("Net daily energy change: 0.00 kWh/day")
    print("Overall percentage change: 0.00%")

print("Appliances with reduced use:", reduced_count)
print("Appliances with increased use:", increased_count)
print("Appliances with unchanged use:", unchanged_count)
print("\nAnalysis complete. Use comparable periods and readings for a fair comparison.")
