print("Simple Calculator (+ - * /)")
while True:
    a_text = input("Enter first number or q to exit: ")
    if a_text == "q":
        break
    a = float(a_text)
    op = input("Enter + or - or * or /: ")
    b = float(input("Enter second number: "))

    values = [a, op, b]

    if values[1] == "+":
        result = values[0] + values[2]
    elif values[1] == "-":
        result = values[0] - values[2]
    elif values[1] == "*":
        result = values[0] * values[2]
    elif values[1] == "/":
        result = values[0] / values[2]
    else:
        print("Unknown operator")
        continue

    print(f"Result: {values[0]} {values[1]} {values[2]} = {result}")
