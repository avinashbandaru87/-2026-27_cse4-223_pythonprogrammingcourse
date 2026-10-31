Retail Billing with Multiple Discount Rules
Problem Statement

Develop a Python program to generate a retail store invoice for multiple products. The system should:

Accept product details (name, category, quantity, price).
Calculate the subtotal for each product.
Apply category-specific taxes.
Apply threshold discounts based on total purchase amount.
Enforce a maximum discount limit.
Generate an itemized invoice showing all calculations.
Display the final bill amount payable by the customer.
Category-wise Tax Rates
Category	Tax RateGrocery	5%
Electronics	18%
Clothing	12%
Others	8%
Discount Rules
Bill Amount	Discount₹5000 - ₹9999	5%
₹10000 - ₹19999	10%
₹20000 and above	15%
Maximum Discount Limit
Maximum Discount Allowed = ₹3000
Algorithm
Start.
Input the number of products.
Initialize subtotal, total tax, and total discount.
For each product:
Input product name.
Input category.
Input quantity.
Input unit price.
Calculate product amount.
Determine applicable tax rate.
Calculate tax amount.
Add values to totals.
Calculate gross bill.
Apply threshold discount based on gross bill.
If discount exceeds ₹3000, set discount to ₹3000.
Calculate final payable amount.
Display the itemized invoice.
Stop.
Flowchart
 ┌────────────┐
 │   START    │
 └─────┬──────┘
       │
       ▼
 ┌─────────────────┐
 │ Enter Number of │
 │ Products        │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Enter Product   │
 │ Details         │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Calculate Item  │
 │ Amount          │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Apply Category  │
 │ Tax             │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Add to Totals   │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ More Products?  │
 └───┬─────────┬───┘
     │Yes      │No
     ▼         ▼
  Repeat   Calculate
           Discount
               │
               ▼
      ┌────────────────┐
      │ Apply Maximum  │
      │ Discount Limit │
      └───────┬────────┘
              │
              ▼
      ┌────────────────┐
      │ Calculate      │
      │ Final Bill     │
      └───────┬────────┘
              │
              ▼
      ┌────────────────┐
      │ Print Invoice  │
      └───────┬────────┘
              │
              ▼
          ┌──────┐
          │ END  │
          └──────┘

Python Source Code
# Retail Billing with Multiple Discount Rules

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

items = []

for i in range(n):
    print(f"\nProduct {i+1}")

    name = input("Product Name: ")
    category = input("Category (Grocery/Electronics/Clothing/Others): ").lower()
    quantity = int(input("Quantity: "))
    price = float(input("Unit Price: "))

    amount = quantity * price

    # Category-specific tax
    if category == "grocery":
        tax_rate = 0.05
    elif category == "electronics":
        tax_rate = 0.18
    elif category == "clothing":
        tax_rate = 0.12
    else:
        tax_rate = 0.08

    tax = amount * tax_rate

    subtotal += amount
    total_tax += tax

    items.append([name, quantity, price, amount, tax])

gross_bill = subtotal + total_tax

# Threshold Discount
if gross_bill >= 20000:
    discount = gross_bill * 0.15
elif gross_bill >= 10000:
    discount = gross_bill * 0.10
elif gross_bill >= 5000:
    discount = gross_bill * 0.05
else:
    discount = 0

# Maximum Discount Limit
if discount > 3000:
    discount = 3000

final_bill = gross_bill - discount

# Invoice
print("\n")
print("=" * 70)
print("                     RETAIL INVOICE")
print("=" * 70)

print("{:<15}{:<10}{:<12}{:<15}{:<10}".format(
    "Product", "Qty", "Price", "Amount", "Tax"))

print("-" * 70)

for item in items:
    print("{:<15}{:<10}{:<12.2f}{:<15.2f}{:<10.2f}".format(
        item[0], item[1], item[2], item[3], item[4]))

print("-" * 70)
print("Subtotal      : ₹{:.2f}".format(subtotal))
print("Total Tax     : ₹{:.2f}".format(total_tax))
print("Gross Bill    : ₹{:.2f}".format(gross_bill))
print("Discount      : ₹{:.2f}".format(discount))
print("Final Amount  : ₹{:.2f}".format(final_bill))
print("=" * 70)

Sample Input
Enter number of products: 3

Product 1
Product Name: Rice
Category: Grocery
Quantity: 10
Unit Price: 60

Product 2
Product Name: Shirt
Category: Clothing
Quantity: 2
Unit Price: 1200

Product 3
Product Name: Mobile
Category: Electronics
Quantity: 1
Unit Price: 18000

Sample Output
======================================================================
                     RETAIL INVOICE
======================================================================
Product        Qty       Price       Amount         Tax
----------------------------------------------------------------------
Rice           10        60.00       600.00         30.00
Shirt          2         1200.00     2400.00        288.00
Mobile         1         18000.00    18000.00       3240.00
----------------------------------------------------------------------
Subtotal      : ₹21000.00
Total Tax     : ₹3558.00
Gross Bill    : ₹24558.00
Discount      : ₹3000.00
Final Amount  : ₹21558.00
======================================================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Number of Products/]

C[/Enter Product Details/]

D[Calculate Product Amount]

E{Product Category?}

F[Apply 5% Tax]

G[Apply 18% Tax]

H[Apply 12% Tax]

I[Apply 8% Tax]

J[Add Amount and Tax to Totals]

K{More Products?}

L[Calculate Gross Bill]

M{Gross Bill >= 20000?}

N[Apply 15% Discount]

O{Gross Bill >= 10000?}

P[Apply 10% Discount]

Q{Gross Bill >= 5000?}

R[Apply 5% Discount]

S[No Discount]

T{Discount > 3000?}

U[Set Discount = 3000]

V[Calculate Final Bill]

W[Generate Itemized Invoice]

X([End])

A --> B
B --> C
C --> D
D --> E

E -- Grocery --> F
E -- Electronics --> G
E -- Clothing --> H
E -- Others --> I

F --> J
G --> J
H --> J
I --> J

J --> K

K -- Yes --> C
K -- No --> L

L --> M

M -- Yes --> N
N --> T

M -- No --> O

O -- Yes --> P
P --> T

O -- No --> Q

Q -- Yes --> R
R --> T

Q -- No --> S
S --> T

T -- Yes --> U
U --> V

T -- No --> V

V --> W
W --> X

Formula Used
Item Amount = Quantity × Unit Price

Tax Amount = Item Amount × Tax Rate

Gross Bill = Subtotal + Total Tax

Discount = Gross Bill × Discount Percentage

Final Amount = Gross Bill − Discount


This program demonstrates multi-product billing, category-wise taxation, threshold-based discounts, maximum concession control, and itemized invoice generation.
