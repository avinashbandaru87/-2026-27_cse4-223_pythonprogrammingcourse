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
