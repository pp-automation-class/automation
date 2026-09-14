def get_distance_text():
    return input("Enter kilometers or q to quit: ")


class DistanceConverter:
    def __init__(self, km_per_mile):
        self.km_per_mile = km_per_mile

    def to_miles(self, kilometers):
        return kilometers / self.km_per_mile


converter = DistanceConverter(1.609344)

while True:
    distance_text = get_distance_text()
    if distance_text == "q":
        break

    try:
        kilometers = float(distance_text)
    except ValueError:
        print("Invalid input. Enter a number or q.")
        continue

    if kilometers < 0:
        print("Distance cannot be negative.")
    elif kilometers == 0:
        print("Miles: 0.0")
    else:
        miles = converter.to_miles(kilometers)
        print("Miles:", miles)