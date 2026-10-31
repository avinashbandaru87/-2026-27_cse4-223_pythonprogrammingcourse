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
