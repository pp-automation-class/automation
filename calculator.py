print("Simple Calculator (+ - * ?)")
while True:
    try:
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
    except ValueError:
        print("We have ValueError")
        continue
    except ZeroDivisionError:
        print("We have ZeroDivisionError")
        continue
    except Exception:
        print("We have Error")
        continue

    print(f"Result: {values[0]} {values[1]} {values[2]} = {result}")
