Railway Fare and Reservation Calculator
Problem Statement

Develop a Python program to calculate railway fares for multiple passengers based on:

Distance traveled
Travel class
Age-based concessions
Reservation fees
Cancellation penalties

The program should:

Calculate fare according to distance slabs.
Apply travel class multipliers.
Provide age-based concessions.
Add reservation fees.
Calculate cancellation charges if the ticket is canceled.
Display the final payable fare for each passenger.
Generate the total fare for all passengers.
Distance Fare Slabs
Distance (km)	Rate per km (₹)Up to 100	1.5
101 - 500	2.0
Above 500	3.0
Class Multipliers
Class	MultiplierSleeper	1.0
AC 3 Tier	1.5
AC 2 Tier	2.0
Age-Based Concessions
Category	DiscountChild (Age < 12)	50%
Senior Citizen (Age ≥ 60)	30%
Others	No Discount
Reservation Fee
₹50 per passenger
Cancellation Penalty
20% of total fare after reservation fee
Algorithm
Start.
Input the number of passengers.
Initialize total collection to zero.
For each passenger:
Input passenger name, age, distance, and travel class.
Calculate base fare according to distance slab.
Apply class multiplier.
Apply age concession if eligible.
Add reservation fee.
Ask whether the ticket is canceled.
If canceled, apply 20% cancellation penalty.
Calculate final fare.
Display passenger fare details.
Add final fare to total collection.
Display total fare of all passengers.
Stop.
Flowchart
 ┌─────────────┐
 │    Start    │
 └──────┬──────┘
        │
        ▼
 ┌─────────────────┐
 │ Enter Number of │
 │ Passengers      │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Enter Passenger │
 │ Details         │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Calculate Base  │
 │ Fare            │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Apply Class     │
 │ Multiplier      │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Apply Age       │
 │ Concession      │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Add Reservation │
 │ Fee             │
 └──────┬──────────┘
        │
        ▼
 ┌─────────────────┐
 │ Ticket Cancel?  │
 └───┬─────────┬───┘
     │Yes      │No
     ▼         ▼
┌─────────┐   ┌─────────┐
│Apply    │   │Final    │
│Penalty  │   │Fare     │
└────┬────┘   └────┬────┘
     │             │
     └──────┬──────┘
            ▼
   ┌────────────────┐
   │ Display Details│
   └──────┬─────────┘
          │
          ▼
   ┌────────────────┐
   │ More Passengers│
   └───┬────────┬───┘
       │Yes     │No
       ▼        ▼
    Repeat   Display
             Total
                │
                ▼
            ┌─────┐
            │ End │
            └─────┘

Python Source Code
# Railway Fare and Reservation Calculator

num_passengers = int(input("Enter number of passengers: "))

grand_total = 0

for i in range(num_passengers):

    print(f"\nPassenger {i + 1}")

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance (km): "))
    travel_class = input("Enter class(Sleeper/AC3/AC2): ").upper()

    # Distance Fare Calculation
    if distance <= 100:
        base_fare = distance * 1.5
    elif distance <= 500:
        base_fare = distance * 2.0
    else:
        base_fare = distance * 3.0

    # Class Multiplier
    if travel_class == "AC3":
        fare = base_fare * 1.5
    elif travel_class == "AC2":
        fare = base_fare * 2.0
    else:
        fare = base_fare

    # Age Concession
    if age < 12:
        fare = fare * 0.50
    elif age >= 60:
        fare = fare * 0.70

    # Reservation Fee
    fare += 50

    cancel = input("Ticket Cancelled? (yes/no): ").lower()

    if cancel == "yes":
        penalty = fare * 0.20
        fare -= penalty
        print("Cancellation Penalty : ₹", penalty)

    print("\n------ Fare Details ------")
    print("Passenger Name :", name)
    print("Age            :", age)
    print("Distance       :", distance, "km")
    print("Class          :", travel_class)
    print("Final Fare     : ₹{:.2f}".format(fare))

    grand_total += fare

print("\n================================")
print("Total Fare Collection : ₹{:.2f}".format(grand_total))
print("================================")

Sample Input
Enter number of passengers: 2

Passenger 1
Enter passenger name: Rahul
Enter age: 30
Enter distance (km): 250
Enter class(Sleeper/AC3/AC2): AC3
Ticket Cancelled? (yes/no): no

Passenger 2
Enter passenger name: Sita
Enter age: 65
Enter distance (km): 600
Enter class(Sleeper/AC3/AC2): AC2
Ticket Cancelled? (yes/no): yes

Sample Output
Passenger 1

------ Fare Details ------
Passenger Name : Rahul
Age            : 30
Distance       : 250.0 km
Class          : AC3
Final Fare     : ₹800.00

Cancellation Penalty : ₹514.00

Passenger 2

------ Fare Details ------
Passenger Name : Sita
Age            : 65
Distance       : 600.0 km
Class          : AC2
Final Fare     : ₹2056.00

================================
Total Fare Collection : ₹2856.00
================================

Mermaid Flowchart Code
flowchart TD

A([Start])

B[/Enter Number of Passengers/]

C[/Enter Passenger Details/]

D[Calculate Distance-Based Fare]

E[Apply Travel Class Multiplier]

F{Age < 12?}

G[Apply 50% Concession]

H{Age >= 60?}

I[Apply 30% Concession]

J[Add Reservation Fee]

K{Ticket Cancelled?}

L[Apply 20% Penalty]

M[Calculate Final Fare]

N[Display Passenger Fare]

O{More Passengers?}

P[Display Total Fare Collection]

Q([End])

A --> B
B --> C

C --> D
D --> E

E --> F

F -- Yes --> G
G --> J

F -- No --> H

H -- Yes --> I
I --> J

H -- No --> J

J --> K

K -- Yes --> L
L --> M

K -- No --> M

M --> N

N --> O

O -- Yes --> C
O -- No --> P

P --> Q

Formula Used
Base Fare = Distance × Rate per km

Class Fare = Base Fare × Class Multiplier

Concession Fare = Class Fare − Applicable Discount

Fare After Reservation = Concession Fare + Reservation Fee

Final Fare = Fare After Reservation − Cancellation Penalty

Cancellation Penalty = 20% of Fare After Reservation


This program demonstrates distance-based fare calculation, class-wise pricing, age concessions, reservation fee management, cancellation charge processing, and multi-passenger billing analysis.
