LIMIT = 10


def calculate_wastage(prepared, served):
    if prepared <= 0 or served < 0 or served > prepared:
        raise ValueError("Enter valid meal counts.")
    leftover = prepared - served
    return leftover, leftover / prepared * 100


def main():
    total_prepared = total_served = total_leftover = 0

    for day in range(1, 8):
        print(f"\nDay {day}")

        while True:
            try:
                prepared = int(input("Meals prepared: "))
                served = int(input("Meals served: "))
                leftover, wastage = calculate_wastage(prepared, served)
                break
            except ValueError:
                print("Invalid input. Please try again.")

        print("Leftovers:", leftover)
        print(f"Wastage: {wastage:.2f}%")
        print("Warning: High food waste!" if wastage > LIMIT
              else "Food waste is within the limit.")

        total_prepared += prepared
        total_served += served
        total_leftover += leftover

    print("\n--- WEEKLY SUMMARY ---")
    print("Meals prepared:", total_prepared)
    print("Meals served:", total_served)
    print("Leftovers:", total_leftover)
    print(f"Overall wastage: {total_leftover / total_prepared * 100:.2f}%")


if __name__ == "__main__":
    main()
