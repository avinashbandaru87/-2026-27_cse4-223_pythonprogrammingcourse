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
    print("
