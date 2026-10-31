Multi-Currency Travel Budget Analysis
Problem Statement

Develop a Python program to analyze travel expenses incurred in different currencies. The program should:

Accept various travel expense categories.
Convert foreign currency expenses into a home currency using supplied exchange rates.
Apply currency conversion fees.
Calculate the total travel expenditure.
Compare actual spending against a planned budget.
Identify the largest expense category.
Generate a travel budget analysis report.
Formulae
Converted Amount = Foreign Amount × Exchange Rate

Conversion Fee = Converted Amount × (Fee Percentage / 100)

Final Expense = Converted Amount + Conversion Fee

Budget Variance = Planned Budget − Total Expenses

Algorithm
Start.
Input planned travel budget.
Input number of expense categories.
Initialize total expenses to 0.
For each category:
Input category name.
Input expense amount in foreign currency.
Input exchange rate.
Input conversion fee percentage.
Convert amount into home currency.
Calculate conversion fee.
Calculate final expense.
Store category and expense.
Add expense to total expenses.
Determine the largest expense category.
Compare total expenses with budget.
If total expenses exceed budget, display budget exceeded.
Otherwise display budget remaining.
Display travel budget report.
Stop.
Flowchart
 ┌────────────┐
 │   START    │
 └─────┬──────┘
       │
       ▼
 ┌──────────────────┐
 │ Enter Travel     │
 │ Budget           │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ Enter Expense    │
 │ Category Details │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ Convert Currency │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ Calculate Fee    │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ Find Final       │
 │ Expense          │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ Add to Total     │
 └─────┬────────────┘
       │
       ▼
 ┌──────────────────┐
 │ More Categories? │
 └───┬────────┬─────┘
     │Yes     │No
     ▼        ▼
  Repeat   Find Largest
           Expense
                │
                ▼
      ┌────────────────┐
      │ Compare with   │
      │ Budget         │
      └─────┬──────────┘
            │
            ▼
      ┌────────────────┐
      │ Display Report │
      └─────┬──────────┘
            │
            ▼
          ┌────┐
          │END │
          └────┘

Python Source Code
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter Planned Travel Budget (₹): "))
n = int(input("Enter Number of Expense Categories: "))

total_expense = 0
expenses = {}

for i in range(n):
    print(f"\nExpense Category {i+1}")

    category = input("Enter Category Name: ")
    amount = float(input("Enter Expense Amount (Foreign Currency): "))
    exchange_rate = float(input("Enter Exchange Rate: "))
    fee_percent = float(input("Enter Conversion Fee (%): "))

    converted_amount = amount * exchange_rate
    fee = converted_amount * fee_percent / 100
    final_expense = converted_amount + fee

    expenses[category] = final_expense
    total_expense += final_expense

# Find Largest Expense Category
largest_category = max(expenses, key=expenses.get)

# Budget Analysis
difference = budget - total_expense

print("\n" + "=" * 55)
print("         MULTI-CURRENCY TRAVEL BUDGET REPORT")
print("=" * 55)

for category, value in expenses.items():
    print(f"{category:20s} : ₹{value:.2f}")

print("-" * 55)
print(f"Total Expenses      : ₹{total_expense:.2f}")
print(f"Planned Budget      : ₹{budget:.2f}")

if total_expense > budget:
    print(f"Budget Exceeded By  : ₹{abs(difference):.2f}")
else:
    print(f"Budget Remaining    : ₹{difference:.2f}")

print(f"Largest Expense     : {largest_category}")
print("=" * 55)

Sample Input
Enter Planned Travel Budget (₹): 100000
Enter Number of Expense Categories: 4

Expense Category 1
Enter Category Name: Hotel
Enter Expense Amount (Foreign Currency): 500
Enter Exchange Rate: 90
Enter Conversion Fee (%): 2

Expense Category 2
Enter Category Name: Food
Enter Expense Amount (Foreign Currency): 200
Enter Exchange Rate: 90
Enter Conversion Fee (%): 2

Expense Category 3
Enter Category Name: Transport
Enter Expense Amount (Foreign Currency): 150
Enter Exchange Rate: 90
Enter Conversion Fee (%): 2

Expense Category 4
Enter Category Name: Shopping
Enter Expense Amount (Foreign Currency): 300
Enter Exchange Rate: 90
Enter Conversion Fee (%): 2

Sample Output
=======================================================
         MULTI-CURRENCY TRAVEL BUDGET REPORT
=======================================================
Hotel                : ₹45900.00
Food                 : ₹18360.00
Transport            : ₹13770.00
Shopping             : ₹27540.00
-------------------------------------------------------
Total Expenses       : ₹105570.00
Planned Budget       : ₹100000.00
Budget Exceeded By   : ₹5570.00
Largest Expense      : Hotel
=======================================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Planned Travel Budget/]

C[/Enter Number of Expense Categories/]

D[/Enter Category Name, Expense Amount, Exchange Rate, Fee %/]

E[Convert Amount to Home Currency]

F[Calculate Conversion Fee]

G[Calculate Final Expense]

H[Store Expense Category]

I[Add to Total Expenses]

J{More Categories?}

K[Find Largest Expense Category]

L{Total Expense > Budget?}

M[Calculate Budget Exceeded Amount]

N[Calculate Budget Remaining]

O[Generate Travel Budget Report]

P([End])

A --> B
B --> C
C --> D

D --> E
E --> F
F --> G
G --> H
H --> I

I --> J

J -- Yes --> D
J -- No --> K

K --> L

L -- Yes --> M
M --> O

L -- No --> N
N --> O

O --> P

Formula Used
Converted Amount = Foreign Amount × Exchange Rate

Conversion Fee = Converted Amount × Fee Percentage / 100

Final Expense = Converted Amount + Conversion Fee

Total Expenses = Sum of All Final Expenses

Budget Variance = Planned Budget − Total Expenses

Largest Expense Category =
Category with Maximum Final Expense


This program demonstrates currency conversion, fee calculation, expense tracking, budget comparison, spending analysis, and identification of the highest travel expense category.
