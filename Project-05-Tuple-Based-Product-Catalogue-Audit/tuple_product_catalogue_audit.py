print("TUPLE-BASED PRODUCT CATALOGUE AUDIT")
print("----------------------------------")

low_stock_limit = 5
product_count = int(input("Enter number of products to audit: "))

while product_count < 1:
    print("Please enter at least one product.")
    product_count = int(input("Enter number of products to audit: "))

# Each product is stored as a tuple:
# (product ID, product name, category, price, stock quantity)
catalogue = []

for i in range(product_count):
    print("\nEnter details for product", i + 1)
    product_id = input("Product ID: ")
    product_name = input("Product name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))

    product = (product_id, product_name, category, price, stock)
    catalogue.append(product)

print("\nPRODUCT AUDIT REPORT")
print("--------------------")
print("Low-stock threshold:", low_stock_limit, "units")

duplicate_id_count = 0
missing_details_count = 0
invalid_price_count = 0
negative_stock_count = 0
out_of_stock_count = 0
low_stock_count = 0

for i in range(len(catalogue)):
    product = catalogue[i]
    product_id, product_name, category, price, stock = product
    issues = []

    # Compare this ID with the product IDs entered before it.
    duplicate_id = False
    for j in range(i):
        if catalogue[j][0] == product_id:
            duplicate_id = True

    if duplicate_id:
        issues.append("DUPLICATE ID")
        duplicate_id_count = duplicate_id_count + 1

    if product_name == "" or category == "":
        issues.append("MISSING DETAILS")
        missing_details_count = missing_details_count + 1

    if price <= 0:
        issues.append("INVALID PRICE")
        invalid_price_count = invalid_price_count + 1

    if stock < 0:
        issues.append("NEGATIVE STOCK")
        negative_stock_count = negative_stock_count + 1
    elif stock == 0:
        issues.append("OUT OF STOCK")
        out_of_stock_count = out_of_stock_count + 1
    elif stock <= low_stock_limit:
        issues.append("LOW STOCK")
        low_stock_count = low_stock_count + 1

    if len(issues) == 0:
        status = "OK"
    else:
        status = issues[0]
    for issue_number in range(1, len(issues)):
        status = status + ", " + issues[issue_number]

    print(product_id, "|", product_name, "| Price: Rs.", price,
          "| Stock:", stock, "|", status)

print("\nAUDIT SUMMARY")
print("--------------")
print("Product records audited:", len(catalogue))
print("Duplicate ID records:", duplicate_id_count)
print("Records with missing name/category:", missing_details_count)
print("Records with invalid price:", invalid_price_count)
print("Records with negative stock:", negative_stock_count)
print("Products out of stock:", out_of_stock_count)
print("Products with low stock (1 to", low_stock_limit, "units):", low_stock_count)
print("\nAudit complete. Review flagged records before updating the catalogue.")
