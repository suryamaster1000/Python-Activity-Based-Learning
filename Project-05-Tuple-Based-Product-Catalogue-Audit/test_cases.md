# Project 05 — Test Cases

The standard run below uses four product records. The price and stock values are entered as numbers.

## Test Case 1: Mixed catalogue issues

**Input records**

| ID | Name | Category | Price | Stock |
|---|---|---|---:|---:|
| 101 | Notebook | Stationery | 25 | 20 |
| 102 | Pen | Stationery | 10 | 0 |
| 103 | Folder | Stationery | 15 | 3 |
| 102 | Pencil | Stationery | 0 | -2 |

**Expected audit findings**

| Record | Expected status |
|---|---|
| 101 Notebook | OK |
| 102 Pen | OUT OF STOCK |
| 103 Folder | LOW STOCK |
| 102 Pencil | DUPLICATE ID, INVALID PRICE, NEGATIVE STOCK |

**Expected summary**

- Product records audited: 4
- Duplicate ID records: 1
- Records with missing name/category: 0
- Records with invalid price: 1
- Records with negative stock: 1
- Products out of stock: 1
- Products with low stock (1 to 5 units): 1

## Additional tests

| Test | Input condition | Expected result |
|---|---|---|
| 2 | One product with unique ID, name/category present, price 50 and stock 10 | Status is OK; all issue counters are 0 |
| 3 | Two products use the same ID | The later record is flagged DUPLICATE ID |
| 4 | Blank product name or category | Record is flagged MISSING DETAILS |
| 5 | Price is 0 or -5 | Record is flagged INVALID PRICE |
| 6 | Stock is -1, 0, or 2 | Flagged NEGATIVE STOCK, OUT OF STOCK, or LOW STOCK respectively |
| 7 | Product count is 0 | Program asks for a count of at least 1 again |

The program assumes valid numeric input when a number is requested; entering text instead of a number is outside this exercise's test scope.
