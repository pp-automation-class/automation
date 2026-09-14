while True:
    distance_text = input("Enter kilometers or q to quit: ")
    if distance_text == "q":
        break

    kilometers = float(distance_text)
    conversion = {"kilometers": kilometers, "km_per_mile": 1.609344}

    if conversion["kilometers"] < 0:
        print("Distance cannot be negative.")
    elif conversion["kilometers"] == 0:
        print("Miles: 0.0")
    else:
        miles = conversion["kilometers"] / conversion["km_per_mile"]
        print("Miles:", miles)