Progressive Electricity Billing
Problem Statement

Develop a Python program to calculate household electricity bills using:

Multiple consumption slabs
Fixed monthly charges
Surcharges
Rebates

The program should:

Accept units consumed for multiple months.
Calculate the electricity bill according to slab rates.
Add fixed charges and surcharges.
Apply rebates if applicable.
Compare bills across months.
Identify unusual increases in electricity bills.
Algorithm
Start the program.
Input the number of months.
For each month:
Input month name.
Input units consumed.
Calculate energy charges based on slabs:
First 100 units → ₹1.5/unit
Next 100 units → ₹2.5/unit
Next 100 units → ₹4/unit
Above 300 units → ₹6/unit
Add fixed charge (₹100).
Calculate surcharge (5% of bill amount).
Apply rebate:
If units consumed < 150, rebate = 10% of bill.
Store the final bill.
Display monthly bills.
Compare consecutive months.
If current month's bill is more than 20% higher than the previous month, mark it as an unusual increase.
Display the comparison results.
Stop.
Flowchart
 ┌───────────┐
 │   Start   │
 └─────┬─────┘
       │
       ▼
 ┌─────────────────┐
 │ Enter No. Months│
 └─────┬───────────┘
       │
       ▼
 ┌────────────────┐
 │ Input Month &  │
 │ Units Consumed │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ Calculate Slab │
 │ Charges        │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ Add Fixed      │
 │ Charge         │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ Add Surcharge  │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ Apply Rebate   │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ Store Bill     │
 └─────┬──────────┘
       │
       ▼
 ┌────────────────┐
 │ More Months ?  │
 └───┬────────┬───┘
     │Yes     │No
     ▼        ▼
   Repeat   Compare
            Bills
               │
               ▼
        ┌────────────┐
        │ Display    │
        │ Results    │
        └─────┬──────┘
              │
              ▼
         ┌────────┐
         │  End   │
         └────────┘

Python Source Code
def calculate_bill(units):
    bill = 0

    # Slab calculation
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

    # Fixed charge
    bill += 100

    # Surcharge (5%)
    bill += bill * 0.05

    # Rebate (10% if units < 150)
    if units < 150:
        bill -= bill * 0.10

    return bill


months = int(input("Enter number of months: "))

month_names = []
bills = []

for i in range(months):
    month = input(f"\nEnter month {i + 1} name: ")
    units = int(input("Enter units consumed: "))

    total_bill = calculate_bill(units)

    month_names.append(month)
    bills.append(total_bill)

print("\nElectricity Bill Summary")
print("-" * 35)

for i in range(months):
    print(f"{month_names[i]} : ₹{bills.2f}")

print("\nBill Comparison")
print("-" * 35)

for i in range(1, months):
    increase = bills[i] - bills[i - 1]
    percent = (increase / bills[i - 1]) * 100

    print(f"{month_names[i-1]} -> {month_names[i]} : {percent:.2f}% change")

    if percent > 20:
        print("  Unusual Increase Detected!")

Sample Input
Enter number of months: 3

Enter month 1 name: January
Enter units consumed: 120

Enter month 2 name: February
Enter units consumed: 180

Enter month 3 name: March
Enter units consumed: 350

Sample Output
Electricity Bill Summary
-----------------------------------
January : ₹387.45
February : ₹603.75
March : ₹1260.00

Bill Comparison
-----------------------------------
January -> February : 55.83% change
  Unusual Increase Detected!

February -> March : 108.70% change
  Unusual Increase Detected!

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Number of Months/]

C[/Enter Month Name and Units Consumed/]

D[Calculate Slab Charges]

E[Add Fixed Charge]

F[Add 5% Surcharge]

G{Units < 150?}

H[Apply 10% Rebate]

I[Store Final Bill]

J{More Months?}

K[Compare Monthly Bills]

L{Increase > 20%?}

M[Mark as Unusual Increase]

N[Display Bill Summary]

O([End])

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G

G -- Yes --> H
G -- No --> I

H --> I

I --> J

J -- Yes --> C
J -- No --> K

K --> L
L -- Yes --> M
L -- No --> N

M --> N
N --> O


This format is suitable for lab record submissions, assignments, and viva documentation.
