Campus Event Financial Planning
Problem Statement

Develop a Python program to plan the finances of a campus event by considering:

Venue Cost
Equipment Cost
Catering Cost
Transport Cost
Certificate Cost

The program should:

Calculate the total event expenditure.
Calculate income from participant registrations.
Consider sponsorship contributions.
Determine any sponsorship shortfall or surplus.
Calculate the minimum number of participants required to break even.
Generate a financial planning report.
Formulae
Total Cost =
Venue Cost + Equipment Cost + Catering Cost +
Transport Cost + Certificate Cost

Registration Income =
Number of Participants × Registration Fee

Total Income =
Registration Income + Sponsorship Amount

Profit/Loss =
Total Income − Total Cost

Break-Even Participants =
(Total Cost − Sponsorship Amount) / Registration Fee

Algorithm
Start.
Input venue cost.
Input equipment cost.
Input catering cost.
Input transport cost.
Input certificate cost.
Input sponsorship amount.
Input registration fee per participant.
Input number of registered participants.
Calculate total event cost.
Calculate registration income.
Calculate total income.
Calculate profit or loss.
Calculate sponsorship shortfall or surplus.
Calculate minimum participants required for break-even.
Display the financial report.
Stop.
Flowchart
 ┌──────────────┐
 │    Start     │
 └──────┬───────┘
        │
        ▼
 ┌──────────────────┐
 │ Enter Event Cost │
 │ Details          │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Enter Sponsorship│
 │ and Registration │
 │ Details          │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Calculate Total  │
 │ Event Cost       │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Calculate Total  │
 │ Income           │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Calculate Profit │
 │ or Loss          │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Calculate Break- │
 │ Even Count       │
 └──────┬───────────┘
        │
        ▼
 ┌──────────────────┐
 │ Display Financial│
 │ Report           │
 └──────┬───────────┘
        │
        ▼
     ┌──────┐
     │ End  │
     └──────┘

Python Source Code
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

Sample Input
Enter Event Name: Tech Fest

Enter Venue Cost: 30000
Enter Equipment Cost: 15000
Enter Catering Cost: 25000
Enter Transport Cost: 5000
Enter Certificate Cost: 3000

Enter Sponsorship Amount: 40000
Enter Registration Fee per Participant: 500
Enter Number of Participants: 100

Sample Output
============================================================
         CAMPUS EVENT FINANCIAL REPORT
============================================================
Event Name                : Tech Fest
------------------------------------------------------------
Venue Cost                : ₹ 30000.0
Equipment Cost            : ₹ 15000.0
Catering Cost             : ₹ 25000.0
Transport Cost            : ₹ 5000.0
Certificate Cost          : ₹ 3000.0
------------------------------------------------------------
Total Event Cost          : ₹ 78000.0
Registration Income       : ₹ 50000.0
Sponsorship Amount        : ₹ 40000.0
Total Income              : ₹ 90000.0
------------------------------------------------------------
Profit                    : ₹ 12000.0
Sponsorship Status        : Additional Funds Required
Sponsorship Shortfall     : ₹ 38000.0
Break-Even Participants   : 76
============================================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Event Cost Details/]

C[/Enter Sponsorship, Registration Fee and Participants/]

D[Calculate Total Event Cost]

E[Calculate Registration Income]

F[Calculate Total Income]

G[Calculate Profit or Loss]

H[Calculate Sponsorship Shortfall]

I[Calculate Break-Even Participants]

J{Profit/Loss >= 0?}

K[Display Profit]

L[Display Loss]

M[Generate Financial Report]

N([End])

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I

I --> J

J -- Yes --> K
J -- No --> L

K --> M
L --> M

M --> N

Formula Used
Total Event Cost =
Venue Cost + Equipment Cost + Catering Cost +
Transport Cost + Certificate Cost

Registration Income =
Participants × Registration Fee

Total Income =
Registration Income + Sponsorship Amount

Profit/Loss =
Total Income − Total Event Cost

Break-Even Participants =
(Total Event Cost − Sponsorship Amount)
÷ Registration Fee

Sponsorship Shortfall =
Total Event Cost − Sponsorship Amount


This program demonstrates financial planning, event budgeting, sponsorship analysis, income forecasting, break-even analysis, and profit/loss evaluation for campus events.
