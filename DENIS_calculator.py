print("Simple Calculator (+ - * /)")
while True:
    try:
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
    except ValueError:
        print("That is not a number")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue
    except TypeError:
        print("Cannot add text and a number")
        continue
    except IndexError:
        print("List index does not exist")
        continue
    except Exception:
        print("We have Error, please try again")
        continue

    print(f"Result: {values[0]} {values[1]} {values[2]} = {result}")
