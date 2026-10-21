# Project 09 — Test Cases

## Test Case 1: Deposit, withdrawal, enquiry, and declined withdrawal

**Input sequence**

- Starting simulated balance: Rs. 1,000
- Choose 1 (Deposit), enter Rs. 500
- Choose 2 (Withdraw), enter Rs. 200
- Choose 3 (Balance enquiry)
- Choose 2 (Withdraw), enter Rs. 2,000
- Choose 4 (Exit)

**Expected results**

| Step | Expected result | Balance after step |
|---|---|---:|
| Deposit Rs. 500 | Deposit successful | Rs. 1,500 |
| Withdraw Rs. 200 | Withdrawal successful | Rs. 1,300 |
| Balance enquiry | Displays Rs. 1,300 | Rs. 1,300 |
| Withdraw Rs. 2,000 | Declined: insufficient funds | Rs. 1,300 |
| Exit | Ends the simulated session | Rs. 1,300 |

**Expected summary**

- Successful deposits: 1
- Successful withdrawals: 1
- Rejected deposit/withdrawal attempts: 1
- Transactions recorded: 4
- Final simulated balance: Rs. 1300.0

## Additional tests

| Test | Input condition | Expected result |
|---|---|---|
| 2 | Deposit amount 0 | Deposit rejected; balance unchanged; rejected counter increases |
| 3 | Withdrawal amount -50 | Withdrawal rejected; balance unchanged; rejected counter increases |
| 4 | Withdraw exactly the available balance | Successful withdrawal; balance becomes zero |
| 5 | Starting balance -1 | Program asks for a non-negative starting balance again |
| 6 | Choose menu option 9 | Invalid menu warning; balance unchanged |
| 7 | Choose Exit immediately | Session ends with zero transaction records and unchanged balance |

Amounts are displayed with Python's default numeric representation (for example, `1300.0`). Numeric prompts expect valid numeric input. This project demonstrates transaction sequence logic only and must not be used to handle real funds.
