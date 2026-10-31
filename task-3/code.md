
Hospital Billing and Patient Classification
Problem Statement

Develop a Python program to calculate a hospital patient's bill by considering:

Consultation charges
Diagnostic charges
Treatment charges
Conditional concessions (discounts)
Billing validations

The program should classify patients according to the following payment policy:

Premium Patient → Bill amount ≥ ₹20,000
Regular Patient → Bill amount between ₹10,000 and ₹19,999
Subsidized Patient → Bill amount < ₹10,000

Concessions:

Senior Citizens (Age ≥ 60): 15% concession
Children (Age < 12): 10% concession

The program must validate that all charges entered are non-negative.

Algorithm
Start the program.
Input patient name and age.
Input consultation charges.
Input diagnostic charges.
Input treatment charges.
Validate all charges are non-negative.
Calculate total bill:
Total = Consultation + Diagnostic + Treatment
Apply concession:
If age ≥ 60, apply 15% discount.
Else if age < 12, apply 10% discount.
Calculate final bill amount.
Classify patient:
Bill ≥ ₹20,000 → Premium Patient
Bill ≥ ₹10,000 and < ₹20,000 → Regular Patient
Bill < ₹10,000 → Subsidized Patient
Display bill details and classification.
Stop.
Flowchart
 ┌───────────┐
 │  Start    │
 └─────┬─────┘
       │
       ▼
 ┌─────────────────┐
 │ Input Patient   │
 │ Details         │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Input Charges   │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Validate Data   │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Calculate Total │
 │ Bill            │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Apply Eligible  │
 │ Concession      │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Classify        │
 │ Patient         │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Display Bill    │
 └─────┬───────────┘
       │
       ▼
 ┌───────────┐
 │   End     │
 └───────────┘

Python Source Code
# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
age = int(input("Enter age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validation
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Error: Charges cannot be negative.")
else:
    total_bill = consultation + diagnostic + treatment

    discount = 0

    # Concession Policy
    if age >= 60:
        discount = total_bill * 0.15
    elif age < 12:
        discount = total_bill * 0.10

    final_bill = total_bill - discount

    # Patient Classification
    if final_bill >= 20000:
        category = "Premium Patient"
    elif final_bill >= 10000:
        category = "Regular Patient"
    else:
        category = "Subsidized Patient"

    print("\n----- Hospital Bill -----")
    print("Patient Name :", name)
    print("Age          :", age)
    print("Total Bill   : ₹", total_bill)
    print("Discount     : ₹", discount)
    print("Final Bill   : ₹", final_bill)
    print("Category     :", category)

Sample Input
Enter patient name: Ravi
Enter age: 65
Enter consultation charges: 2000
Enter diagnostic charges: 5000
Enter treatment charges: 18000

Sample Output
----- Hospital Bill -----

Patient Name : Ravi
Age          : 65
Total Bill   : ₹ 25000.0
Discount     : ₹ 3750.0
Final Bill   : ₹ 21250.0
Category     : Premium Patient

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Patient Name and Age/]

C[/Enter Consultation, Diagnostic and Treatment Charges/]

D{Charges < 0?}

E[Display Error Message]

F[Calculate Total Bill]

G{Age >= 60?}

H[Apply 15% Concession]

I{Age < 12?}

J[Apply 10% Concession]

K[Calculate Final Bill]

L{Final Bill >= 20000?}

M[Premium Patient]

N{Final Bill >= 10000?}

O[Regular Patient]

P[Subsidized Patient]

Q[Display Bill Details and Category]

R([End])

A --> B
B --> C
C --> D

D -- Yes --> E
E --> R

D -- No --> F

F --> G

G -- Yes --> H
H --> K

G -- No --> I

I -- Yes --> J
J --> K

I -- No --> K

K --> L

L -- Yes --> M
M --> Q

L -- No --> N

N -- Yes --> O
O --> Q

N -- No --> P
P --> Q

Q --> R

Expected Output Classification Examples
Final Bill Amount	Classification₹25,000	Premium Patient
₹15,000	Regular Patient
₹8,000	Subsidized Patient
