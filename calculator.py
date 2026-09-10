print("Simple Calculator (+ - * ?)")

a = float(input("Enter first number: "))
op = input("Enter + or - or * or /: ")
b = float(input("Enter second number: "))

if op == "+":
    result = (a + b)
elif op == "-":
    result = (a - b)
elif op == "*":
    result = (a * b)
elif op == "/":
    result = (a / b)
else:
    print("Unknown operator")
    exit()

print(f"Result: {a} {op} {b} = {result}")
