
# Manufacturing Cost and Profitability Analysis

product_name = input("Enter Product Name: ")

material_cost = float(input("Enter Material Cost: "))
labour_cost = float(input("Enter Labour Charges: "))
machine_cost = float(input("Enter Machine Cost: "))
wastage_percent = float(input("Enter Wastage Percentage: "))

units_produced = int(input("Enter Number of Units Produced: "))
selling_price = float(input("Enter Selling Price Per Unit: "))

target_profit = float(input("Enter Target Profit: "))

# Wastage Cost
wastage_cost = material_cost * (wastage_percent / 100)

# Total Manufacturing Cost
total_cost = (
    material_cost +
    labour_cost +
    machine_cost +
    wastage_cost
)

# Total Revenue
total_revenue = units_produced * selling_price

# Profit / Loss
profit = total_revenue - total_cost

# Target Analysis
if profit >= target_profit:
    status = "Target Achieved"
else:
    status = "Target Not Achieved"

# Report
print("\n")
print("=" * 50)
print("      MANUFACTURING PROFITABILITY REPORT")
print("=" * 50)

print("Product Name              :", product_name)
print("Material Cost             : ₹", material_cost)
print("Labour Charges            : ₹", labour_cost)
print("Machine Cost              : ₹", machine_cost)
print("Wastage Cost              : ₹", wastage_cost)

print("-" * 50)
print("Total Manufacturing Cost  : ₹", total_cost)
print("Total Revenue             : ₹", total_revenue)
print("Profit / Loss             : ₹", profit)
print("Target Profit             : ₹", target_profit)
print("Status                    :", status)

print("=" * 50)
