# Common Python exceptions — try / except / else / finally


print("=== 1. ValueError (bad conversion) ===")
try:
    number = int("10A")
    print(number)
except ValueError:
    print("Cannot convert to int")

# print("=== 2. ZeroDivisionError ===")
# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print("=== 3. TypeError ===")
# try:
#     result = "5" + 2
#     print(result)
# except TypeError:
#     print("Cannot add str and int")

# print("=== 4. IndexError ===")
# browsers = ["chromium", "firefox"]
# try:
#     print(browsers[5])
# except IndexError:
#     print("Index out of range")

# print("=== 5. KeyError ===")
# user = {"name": "Ada"}
# try:
#     print(user["email"])
# except KeyError:
#     print("Key not found")

# print("=== 6. FileNotFoundError ===")
# try:
#     file = open("no_such_file.txt")
#     file.close()
# except FileNotFoundError:
#     print("File does not exist")

# print("=== 7. catch exception object ===")
# try:
#     int("abc")
# except ValueError as error:
#     print("Error message:", error)

# print("=== 8. multiple except blocks ===")
# try:
#     a = float("3.5")
#     b = float("0")
#     print(a / b)
# except ValueError:
#     print("Not a number")
# except ZeroDivisionError:
#     print("Division by zero")

# print("=== 9. else + finally ===")
# try:
#     value = int("42")
# except ValueError:
#     print("Bad number")
# else:
#     print("Success:", value)   # runs only if no error
# finally:
#     print("Always runs")       # runs always

# print("=== 10. raise your own error ===")
# age = -1
# try:
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Age:", age)
# except ValueError as error:
#     print(error)
