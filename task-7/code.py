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
print("=" *
