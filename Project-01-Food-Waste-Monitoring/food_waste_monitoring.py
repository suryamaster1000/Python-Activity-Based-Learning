LIMIT = 10


def calculate_wastage(prepared, served):
    """Return (leftover meals, wastage percentage) for one day."""
    if prepared <= 0:
        raise ValueError("Meals prepared must be greater than zero.")
    if served < 0 or served > prepared:
        raise ValueError("Meals served must be between zero and meals prepared.")

    leftover = prepared - served
    wastage = (leftover / prepared) * 100
    return leftover, wastage


def main():
    total_prepared = 0
    total_served = 0
    total_leftover = 0

    for day in range(1, 8):
        print("\nDay", day)

        while True:
            try:
                prepared = int(input("Meals prepared: "))
                served = int(input("Meals served: "))
                leftover, wastage = calculate_wastage(prepared, served)
                break
            except ValueError as error:
                print("Invalid input!", error)

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


if __name__ == "__main__":
    main()
