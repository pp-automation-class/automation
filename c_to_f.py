celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} C = {fahrenheit} F")

if celsius < 0:
    print("Freezing")
if celsius > 0 and celsius <= 19:
    print("Cold")
if celsius > 20 and celsius <= 40:
    print("Comfortable")
else:
    print("Hot")

