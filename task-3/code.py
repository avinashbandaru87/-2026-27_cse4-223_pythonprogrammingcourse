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
