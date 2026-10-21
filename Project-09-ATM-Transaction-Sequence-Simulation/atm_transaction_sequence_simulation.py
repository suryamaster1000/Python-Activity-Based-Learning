print("ATM TRANSACTION SEQUENCE SIMULATION")
print("-------------------------------------")
print("DEMO ONLY: This program does not connect to a bank or real account.")

balance = float(input("Enter simulated starting balance (Rs.): "))
while balance < 0:
    print("Starting balance cannot be negative.")
    balance = float(input("Enter simulated starting balance (Rs.): "))

transactions = []
deposit_count = 0
withdrawal_count = 0
declined_count = 0

choice = "0"
while choice != "4":
    print("\nATM MENU")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance enquiry")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter deposit amount (Rs.): "))
        if amount <= 0:
            message = "Deposit rejected: amount must be greater than zero."
            print(message)
            transactions.append(message)
            declined_count = declined_count + 1
        else:
            balance = balance + amount
            deposit_count = deposit_count + 1
            message = "Deposit Rs. " + str(amount) + " | Balance Rs. " + str(balance)
            print(message)
            transactions.append(message)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount (Rs.): "))
        if amount <= 0:
            message = "Withdrawal rejected: amount must be greater than zero."
            print(message)
            transactions.append(message)
            declined_count = declined_count + 1
        elif amount > balance:
            message = "Withdrawal declined: insufficient funds (requested Rs. " + str(amount) + ", balance Rs. " + str(balance) + ")"
            print(message)
            transactions.append(message)
            declined_count = declined_count + 1
        else:
            balance = balance - amount
            withdrawal_count = withdrawal_count + 1
            message = "Withdrawal Rs. " + str(amount) + " | Balance Rs. " + str(balance)
            print(message)
            transactions.append(message)

    elif choice == "3":
        message = "Balance enquiry: Rs. " + str(balance)
        print(message)
        transactions.append(message)

    elif choice == "4":
        print("ATM session ended.")

    else:
        print("Invalid menu option. Choose 1, 2, 3, or 4.")

print("\nTRANSACTION HISTORY")
print("-------------------")
if len(transactions) == 0:
    print("No transactions recorded.")
else:
    for i in range(len(transactions)):
        print(str(i + 1) + ".", transactions[i])

print("\nSESSION SUMMARY")
print("----------------")
print("Successful deposits:", deposit_count)
print("Successful withdrawals:", withdrawal_count)
print("Rejected deposit/withdrawal attempts:", declined_count)
print("Transactions recorded:", len(transactions))
print("Final simulated balance: Rs.", str(balance))
print("\nSimulation complete. No real money or bank account was accessed.")
