# Campus Event Financial Planning

import math

event_name = input("Enter Event Name: ")

venue_cost = float(input("Enter Venue Cost: "))
equipment_cost = float(input("Enter Equipment Cost: "))
catering_cost = float(input("Enter Catering Cost: "))
transport_cost = float(input("Enter Transport Cost: "))
certificate_cost = float(input("Enter Certificate Cost: "))

sponsorship = float(input("Enter Sponsorship Amount: "))
registration_fee = float(input("Enter Registration Fee per Participant: "))
participants = int(input("Enter Number of Participants: "))

# Total Event Cost
total_cost = (
    venue_cost +
    equipment_cost +
    catering_cost +
    transport_cost +
    certificate_cost
)

# Registration Income
registration_income = participants * registration_fee

# Total Income
total_income = registration_income + sponsorship

# Profit / Loss
profit_loss = total_income - total_cost

# Break-even Participants
if registration_fee > 0:
    break_even = math.ceil(
        max(0, (total_cost - sponsorship) / registration_fee)
    )
else:
    break_even = 0

# Sponsorship Analysis
if sponsorship >= total_cost:
    sponsorship_status = "Sponsorship Covers Entire Event"
    shortfall = 0
else:
    sponsorship_status = "Additional Funds Required"
    shortfall = total_cost - sponsorship

# Display Report
print("\n")
print("=" * 60)
print("         CAMPUS EVENT FINANCIAL REPORT")
print("=" * 60)

print("Event Name                :", event_name)
print("-" * 60)

print("Venue Cost                : ₹", venue_cost)
print("Equipment Cost            : ₹", equipment_cost)
print("Catering Cost             : ₹", catering_cost)
print("Transport Cost            : ₹", transport_cost)
print("Certificate Cost          : ₹", certificate_cost)

print("-" * 60)
print("Total Event Cost          : ₹", total_cost)
print("Registration Income       : ₹", registration_income)
print("Sponsorship Amount        : ₹", sponsorship)
print("Total Income              : ₹", total_income)

print("-" * 60)

if profit_loss >= 0:
    print("Profit                    : ₹", profit_loss)
else:
    print("Loss                      : ₹", abs(profit_loss))

print("Sponsorship Status        :", sponsorship_status)

if shortfall > 0:
    print("Sponsorship Shortfall     : ₹", shortfall)

print("Break-Even Participants   :", break_even)

print("=" * 60)
