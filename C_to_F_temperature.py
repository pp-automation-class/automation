print("Celsius to Fahrenheit")

celsius = float(input("Enter temperature in C: "))

if celsius < 20 or celsius > 40:
    print("out of range")
else:
    fahrenheit = celsius * 9 / 5 + 32
    print("F:", fahrenheit)
