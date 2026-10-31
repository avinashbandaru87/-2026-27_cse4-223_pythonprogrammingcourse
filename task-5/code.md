Multi-Plan Telecommunications Cost Optimization
Problem Statement

Develop a Python program to evaluate multiple mobile plans based on:

Monthly data usage
Plan validity
User budget
Included data limits
Excess usage charges

The program should:

Accept details of multiple telecom plans.
Compare plans with the user's requirements.
Calculate excess data charges if usage exceeds the plan limit.
Check whether the plan satisfies validity and budget constraints.
Identify eligible plans.
Determine the most economical eligible plan.
Display the cost analysis for all plans.
Algorithm
Start.
Input user's monthly data usage, required validity, and budget.
Input the number of mobile plans.
For each plan:
Input plan name.
Input plan cost.
Input data limit (GB).
Input validity (days).
Input excess charge per GB.
Check eligibility:
Cost must be within budget.
Validity must meet or exceed required validity.
Calculate excess usage:
If usage exceeds plan data limit, compute extra charges.
Calculate total cost:
Total Cost = Plan Cost + Excess Charges
Store all eligible plans.
Find the plan with minimum total cost.
Display plan analysis and the most economical plan.
Stop.
Flowchart
 ┌───────────┐
 │   Start   │
 └─────┬─────┘
       │
       ▼
 ┌─────────────────┐
 │ Input User      │
 │ Requirements    │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Input Plan      │
 │ Details         │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Check Budget &  │
 │ Validity        │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Calculate Extra │
 │ Charges         │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Calculate Total │
 │ Cost            │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ Store Eligible  │
 │ Plans           │
 └─────┬───────────┘
       │
       ▼
 ┌─────────────────┐
 │ More Plans ?    │
 └───┬─────────┬───┘
     │ Yes     │ No
     ▼         ▼
   Repeat   Find Best
            Plan
               │
               ▼
      ┌────────────────┐
      │ Display Result │
      └───────┬────────┘
              │
              ▼
         ┌─────────┐
         │   End   │
         └─────────┘

Python Source Code
# Multi-Plan Telecommunications Cost Optimization

usage = float(input("Enter monthly data usage (GB): "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget: "))

n = int(input("Enter number of plans: "))

eligible_plans = []

print("\nEnter Plan Details")

for i in range(n):
    print(f"\nPlan {i + 1}")

    name = input("Plan Name: ")
    cost = float(input("Plan Cost: "))
    data_limit = float(input("Data Limit (GB): "))
    validity = int(input("Validity (Days): "))
    excess_rate = float(input("Excess Charge per GB: "))

    # Calculate excess usage charges
    extra_usage = max(0, usage - data_limit)
    excess_charge = extra_usage * excess_rate

    total_cost = cost + excess_charge

    print("\n--- Plan Analysis ---")
    print("Plan Name      :", name)
    print("Extra Usage    :", extra_usage, "GB")
    print("Excess Charge  : ₹", excess_charge)
    print("Total Cost     : ₹", total_cost)

    # Check eligibility
    if cost <= budget and validity >= required_validity:
        eligible_plans.append((name, total_cost))

# Find cheapest eligible plan
if eligible_plans:
    best_plan = min(eligible_plans, key=lambda x: x[1])

    print("\nEligible Plans")
    print("-" * 40)

    for plan in eligible_plans:
        print(plan[0], "=> ₹", plan[1])

    print("\nMost Economical Plan")
    print("-" * 40)
    print("Plan Name :", best_plan[0])
    print("Total Cost: ₹", best_plan[1])

else:
    print("\nNo eligible plan found within budget and validity constraints.")

Sample Input
Enter monthly data usage (GB): 60
Enter required validity (days): 28
Enter maximum budget: 500

Enter number of plans: 3

Plan 1
Plan Name: Basic
Plan Cost: 299
Data Limit (GB): 40
Validity (Days): 28
Excess Charge per GB: 5

Plan 2
Plan Name: Smart
Plan Cost: 399
Data Limit (GB): 70
Validity (Days): 30
Excess Charge per GB: 4

Plan 3
Plan Name: Premium
Plan Cost: 599
Data Limit (GB): 100
Validity (Days): 56
Excess Charge per GB: 3

Sample Output
--- Plan Analysis ---
Plan Name      : Basic
Extra Usage    : 20.0 GB
Excess Charge  : ₹ 100.0
Total Cost     : ₹ 399.0

--- Plan Analysis ---
Plan Name      : Smart
Extra Usage    : 0 GB
Excess Charge  : ₹ 0
Total Cost     : ₹ 399.0

--- Plan Analysis ---
Plan Name      : Premium
Extra Usage    : 0 GB
Excess Charge  : ₹ 0
Total Cost     : ₹ 599.0

Eligible Plans
----------------------------------------
Basic => ₹ 399.0
Smart => ₹ 399.0

Most Economical Plan
----------------------------------------
Plan Name : Basic
Total Cost: ₹ 399.0

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Monthly Usage, Validity Requirement and Budget/]

C[/Enter Number of Plans/]

D[/Enter Plan Details/]

E[Calculate Extra Usage]

F[Calculate Excess Charges]

G[Calculate Total Cost]

H{Cost <= Budget<br>AND<br>Validity >= Required?}

I[Store Eligible Plan]

J{More Plans?}

K[Find Plan with Minimum Total Cost]

L[Display Eligible Plans]

M[Display Best Plan]

N[Display No Eligible Plan]

O([End])

A --> B
B --> C
C --> D

D --> E
E --> F
F --> G

G --> H

H -- Yes --> I
H -- No --> J

I --> J

J -- Yes --> D
J -- No --> K

K --> L

L --> M

K --> N

M --> O
N --> O

Formula Used
Extra Usage = Monthly Usage − Data Limit

Excess Charge = Extra Usage × Excess Rate

Total Cost = Plan Cost + Excess Charge

Eligibility Condition:
Plan Cost ≤ Budget
AND
Plan Validity ≥ Required Validity

Best Plan = Eligible Plan with Minimum Total Cost


This program demonstrates telecommunication plan comparison, cost optimization, budget validation, excess usage billing, and decision-making using conditional logic and loops.
