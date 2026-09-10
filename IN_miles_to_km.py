miles = float(input("Enter miles: "))

if miles <= 0:
    print("Distance must be greater than 0")
elif miles > 1000000:
    print("It is too complicated to count")
else:
    km = miles * 1.60934
    print(f"{miles} miles = {km} km")
