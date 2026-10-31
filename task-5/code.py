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

