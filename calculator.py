print("Simple calculator (+  -  *  /)")

a = float(input("First number: "))
op = input("Operator (+ - * /): ").strip()
b = float(input("Second number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
else:
    print("Unknown operator")
    exit()

print(f"Result: {a} {op} {b} = {result}")
