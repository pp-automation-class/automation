kilometers = float(input("Enter distance in kilometers: "))
if kilometers < 0:
    print("Distance cannot be negative.")
elif kilometers == 0:
    print("Miles:0.0")
else:
    miles = kilometers / 1.609344
    print("Miles:",miles)
