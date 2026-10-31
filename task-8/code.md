
Manufacturing Cost and Profitability Analysis
Problem Statement

Develop a Python program to calculate the total manufacturing cost of a product by considering:

Material Cost
Labour Charges
Wastage Cost
Machine Operating Cost

The program should:

Calculate total production cost.
Calculate total selling revenue.
Determine profit or loss.
Compare the actual profit with a specified profit target.
Display whether the production meets the desired profit target.
Generate a formatted profitability report.
Formulae
Wastage Cost = Material Cost × (Wastage Percentage / 100)

Total Manufacturing Cost =
Material Cost + Labour Charges + Wastage Cost + Machine Cost

Total Revenue = Units Produced × Selling Price per Unit

Profit = Total Revenue − Total Manufacturing Cost

Algorithm
Start.
Input product name.
Input material cost.
Input labour charges.
Input machine operating cost.
Input wastage percentage.
Input number of units produced.
Input selling price per unit.
Input target profit.
Calculate wastage cost.
Calculate total manufacturing cost.
Calculate total revenue.
Calculate profit/loss.
Compare actual profit with target profit.
Display profitability report.
Stop.
Flowchart
 ┌───────────────┐
 │     Start     │
 └───────┬───────┘
         │
         ▼
 ┌──────────────────┐
 │ Enter Product &  │
 │ Cost Details     │
 └───────┬──────────┘
         │
         ▼
 ┌──────────────────┐
 │ Calculate        │
 │ Wastage Cost     │
 └───────┬──────────┘
         │
         ▼
 ┌──────────────────┐
 │ Calculate Total  │
 │ Manufacturing    │
 │ Cost             │
 └───────┬──────────┘
         │
         ▼
 ┌──────────────────┐
 │ Calculate Total  │
 │ Revenue          │
 └───────┬──────────┘
         │
         ▼
 ┌──────────────────┐
 │ Calculate Profit │
 │ or Loss          │
 └───────┬──────────┘
         │
         ▼
 ┌──────────────────┐
 │ Profit >= Target │
 │ Profit ?         │
 └───┬─────────┬────┘
     │ Yes     │ No
     ▼         ▼
┌─────────┐ ┌──────────┐
│Target   │ │Target    │
│Achieved │ │Not Met   │
└────┬────┘ └────┬─────┘
     │           │
     └─────┬─────┘
           ▼
 ┌──────────────────┐
 │ Display Report   │
 └───────┬──────────┘
         │
         ▼
     ┌──────┐
     │ End  │
     └──────┘

Python Source Code
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

Sample Input
Enter Product Name: Plastic Chair
Enter Material Cost: 50000
Enter Labour Charges: 15000
Enter Machine Cost: 10000
Enter Wastage Percentage: 5

Enter Number of Units Produced: 1000
Enter Selling Price Per Unit: 100

Enter Target Profit: 20000

Sample Output
==================================================
      MANUFACTURING PROFITABILITY REPORT
==================================================
Product Name              : Plastic Chair
Material Cost             : ₹ 50000.0
Labour Charges            : ₹ 15000.0
Machine Cost              : ₹ 10000.0
Wastage Cost              : ₹ 2500.0
--------------------------------------------------
Total Manufacturing Cost  : ₹ 77500.0
Total Revenue             : ₹ 100000.0
Profit / Loss             : ₹ 22500.0
Target Profit             : ₹ 20000.0
Status                    : Target Achieved
==================================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Product Name and Cost Details/]

C[Calculate Wastage Cost]

D[Calculate Total Manufacturing Cost]

E[Calculate Total Revenue]

F[Calculate Profit or Loss]

G{Profit >= Target Profit?}

H[Target Achieved]

I[Target Not Achieved]

J[Display Profitability Report]

K([End])

A --> B
B --> C
C --> D
D --> E
E --> F

F --> G

G -- Yes --> H
H --> J

G -- No --> I
I --> J

J --> K

Formula Used
Wastage Cost = Material Cost × (Wastage Percentage / 100)

Total Manufacturing Cost =
Material Cost + Labour Charges + Machine Cost + Wastage Cost

Total Revenue =
Units Produced × Selling Price Per Unit

Profit =
Total Revenue − Total Manufacturing Cost

Profit Target Status:
If Profit ≥ Target Profit → Target Achieved
Else → Target Not Achieved


This program demonstrates manufacturing cost estimation, wastage analysis, production costing, revenue calculation, profit/loss analysis, and target-based profitability evaluation.
