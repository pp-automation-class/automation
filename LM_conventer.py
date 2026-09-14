# converter: Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} F = {celsius} C")

if celsius < 0:
    print("Freezing")
elif celsius <= 19:
    print("Cold")
elif celsius <= 40:
    print("Comfortable")
else:
    print("Hot")
