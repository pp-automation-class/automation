print("Simple Calculator (+ - * ?)")
while True:
    a = input("Enter first number or q to quit: ")
    if a == "q":
        break
    op = input("Enter + or - or * or /: ")
    b = float(input("Enter second number: "))
    a = float(a) 

    values = [a, op, b]

    if values[1] == "+":
        result = (values[0] + values[2])
    elif values[1] == "-":
        result = (values[0] - values[2])
    elif values[1] == "*":
        result = (values[0] * values[2])
    elif values[1] == "/":
        result = (values[0] / values[2])
    else:
        print("Unknown operator")

    print(f"Result: {values[0]} {values[1]} {values[2]} = {result}")
