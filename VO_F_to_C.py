print("Fahrenheit to Celsius")

fahrenheit = float(input("Enter temperature in F: "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} F = {celsius} C")

if celsius < 0:
    print("Freezing")
elif celsius <= 15:
    print("Cool")
elif celsius <= 25:
    print("Warm")
else:
    print("Hot")
