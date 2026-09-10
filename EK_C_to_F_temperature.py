print("Celsius to Fahrenheit")

celsius = float(input("Enter temperature in C: "))
fahrenheit = celsius * 9 / 5 + 32

if celsius < 20:
    print("too cold")
    print("F:", fahrenheit)
elif celsius > 40:
    print("too hot")
    print("F:", fahrenheit)
else:
    print("F:", fahrenheit)
