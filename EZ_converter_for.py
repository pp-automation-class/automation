for attempt in range(3):
    kilometers = float(input("Enter distance in kilometers: "))
    values = [kilometers, 1.609344]
    if kilometers < 0:
        print("Distance cannot be negative.")
    elif kilometers == 0:
        print("Miles: 0.0")
    else:
        miles = values[0] / values[1]
        print("Miles:", miles)