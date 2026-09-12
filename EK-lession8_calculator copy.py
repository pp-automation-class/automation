# print("Simple Calculator (+ - * ?)")
# while True:
#     a = input("Enter first number or q to quit: ")
#     if a == "q":
#         break
#     op = input("Enter + or - or * or /: ")
#     b = float(input("Enter second number: "))
#     a = float(a) 

#     values = [a, op, b]

#     if values[1] == "+":
#         result = (values[0] + values[2])
#     elif values[1] == "-":
#         result = (values[0] - values[2])
#     elif values[1] == "*":
#         result = (values[0] * values[2])
#     elif values[1] == "/":
#         result = (values[0] / values[2])
#     else:
#         print("Unknown operator")

#     print(f"Result: {values[0]} {values[1]} {values[2]} = {result}")

# --- previous version: one operator, four numbers ---
# while True:
#     a = input("First number (q to quit): ")
#     if a == "q":
#         break
#     a = float(a)
#     op = input("Operator + - * /: ")
#     b = float(input("Second number: "))
#     c = float(input("Third number: "))
#     d = float(input("Fourth number: "))
#     values = [a, op, b, op, c, op, d]
#     if values[1] == "+":
#         result = values[0] + values[2] + values[4] + values[6]
#     elif values[1] == "-":
#         result = values[0] - values[2] - values[4] - values[6]
#     elif values[1] == "*":
#         result = values[0] * values[2] * values[4] * values[6]
#     elif values[1] == "/":
#         result = values[0] / values[2] / values[4] / values[6]
#     else:
#         print("Unknown operator")
#         continue
#     print(f"Result: {values[0]} {values[1]} {values[2]} {values[3]} {values[4]} {values[5]} {values[6]} = {result}")

# --- new version: three different operators ---
while True:
    a = input("First number (q to quit): ")
    if a == "q":
        break
    a = float(a)
    op1 = input("First operator + - * /: ")
    b = float(input("Second number: "))
    op2 = input("Second operator + - * /: ")
    c = float(input("Third number: "))
    op3 = input("Third operator + - * /: ")
    d = float(input("Fourth number: "))

    values = [a, op1, b, op2, c, op3, d]
    result = a
    unknown = False
    for op, num in ((op1, b), (op2, c), (op3, d)):
        if op == "+":
            result = result + num
        elif op == "-":
            result = result - num
        elif op == "*":
            result = result * num
        elif op == "/":
            result = result / num
        else:
            print("Unknown operator")
            unknown = True
            break

    if unknown:
        continue

    print(
        f"Result: {values[0]} {values[1]} {values[2]} {values[3]} {values[4]} {values[5]} {values[6]} = {result}"
    )