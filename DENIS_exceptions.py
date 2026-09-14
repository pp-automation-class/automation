Common exceptions: try / except / else / finally / raise

print("=== 1. ValueError (bad conversion) ===")
try:
    number = int("10A")
    print(number)
except ValueError:
    print("That is not a number")

ZeroDivisionError — divide by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# ValueError — wrong type of value
try:
    age = int("hello")
except ValueError:
    print("That is not a number")

# TypeError — wrong type in an operation
try:
    print("age" + 10)
except TypeError:
    print("Cannot add text and a number")

# IndexError — list index does not exist
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("That index is not in the list")

# KeyError — dict key does not exist
user = {"name": "Denis"}
try:
    print(user["email"])
except KeyError:
    print("That key is not in the dict")

# FileNotFoundError — file does not exist
try:
    open("no_such_file.txt")
except FileNotFoundError:
    print("File not found")

# else — runs only if there was no error
# finally — always runs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("OK:", result)
finally:
    print("This always runs")

# raise — create your own error
try:
    raise ValueError("Something went wrong")
except ValueError as error:
    print(error)