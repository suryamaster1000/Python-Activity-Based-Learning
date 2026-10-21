print("WEEKLY ELECTRICITY CONSUMPTION MATRIX")
print("--------------------------------------")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
high_usage_limit = 15

week_count = int(input("Enter number of weeks to analyse: "))
while week_count < 1:
    print("Please enter at least one week.")
    week_count = int(input("Enter number of weeks to analyse: "))

consumption_matrix = []

for i in range(week_count):
    print("\nEnter daily electricity use for Week", i + 1, "(kWh)")
    week_usage = []

    for j in range(7):
        units = float(input(days[j] + ": "))
        while units < 0:
            print("Consumption cannot be negative.")
            units = float(input(days[j] + ": "))
        week_usage.append(units)

    consumption_matrix.append(week_usage)

weekly_totals = []
for i in range(week_count):
    week_total = 0
    for j in range(7):
        week_total = week_total + consumption_matrix[i][j]
    weekly_totals.append(week_total)

print("\nWEEKLY CONSUMPTION REPORT")
print("-------------------------")
print("High-use alert is set for daily consumption above", high_usage_limit, "kWh.")

for i in range(week_count):
    daily_average = weekly_totals[i] / 7
    print("Week", i + 1, "| Total:", format(weekly_totals[i], ".2f"),
          "kWh | Daily average:", format(daily_average, ".2f"), "kWh")

    if i > 0:
        change = weekly_totals[i] - weekly_totals[i - 1]
        if change > 0:
            direction = "increase"
        elif change < 0:
            direction = "decrease"
        else:
            direction = "no change"

        print("  Compared with Week", i, ":", direction,
              "of", format(abs(change), ".2f"), "kWh")

        if weekly_totals[i - 1] != 0:
            percent_change = (change / weekly_totals[i - 1]) * 100
            print("  Percentage change:", format(percent_change, ".2f"), "%")
        else:
            print("  Percentage change: unavailable because previous weekly total is zero")

highest_units = consumption_matrix[0][0]
lowest_units = consumption_matrix[0][0]
highest_week = 1
highest_day = days[0]
lowest_week = 1
lowest_day = days[0]
high_usage_days = 0
overall_total = 0

print("\nDAILY HIGH-USAGE ALERTS")
print("-----------------------")
for i in range(week_count):
    for j in range(7):
        units = consumption_matrix[i][j]
        overall_total = overall_total + units

        if units > highest_units:
            highest_units = units
            highest_week = i + 1
            highest_day = days[j]

        if units < lowest_units:
            lowest_units = units
            lowest_week = i + 1
            lowest_day = days[j]

        if units > high_usage_limit:
            high_usage_days = high_usage_days + 1
            print("Week", i + 1, days[j], ":", format(units, ".2f"), "kWh")

if high_usage_days == 0:
    print("No days exceeded the high-use alert limit.")

print("\nOVERALL SUMMARY")
print("---------------")
print("Weeks analysed:", week_count)
print("Days analysed:", week_count * 7)
print("Total electricity consumption:", format(overall_total, ".2f"), "kWh")
print("Average daily consumption:", format(overall_total / (week_count * 7), ".2f"), "kWh")
print("Highest daily consumption:", format(highest_units, ".2f"), "kWh - Week", highest_week, highest_day)
print("Lowest daily consumption:", format(lowest_units, ".2f"), "kWh - Week", lowest_week, lowest_day)
print("Days above the high-use alert limit:", high_usage_days)
print("\nAnalysis complete. The alert limit is an example setting, not a utility rule.")
