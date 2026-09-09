# In Python, arrays are usually lists: []

# browsers = ["chromium", "firefox", "webkit", "edge", "safari"]

# print(browsers[4])


# Age = 20
# Hair = "brown"
# Height = 1.80
# Is_student = True
# Is_employee = False


# users = [20, "brown", 1.80, True, False]
# managers = [45, "white", 1.80, False, False]

# for index in range(len(users)): # for index in range(0, 5)
#     print(users[index])

# List
# Dictionary
# Tuple
# Set

# users_dict = {
#     "age": 20,
#     "hair": "brown",
#     "height": 1.80,
#     "is_student": True,
#     "is_employee": False
# }

# print(users_dict["hair"])

# price = [1000, 200, 300, 400, 500]
# print(min(price))






# # create
# browsers = ["chromium", "firefox", "webkit"]
# numbers = [10, 20, 30, 40]
# mixed = ["admin", 3, True]

# print(browsers)
# print(numbers)

# # length
# print(len(browsers))

# # index — starts at 0
# print(browsers[0])   # first
# print(browsers[1])   # second
# print(browsers[-1])  # last

# # change item
# browsers[1] = "edge"
# print(browsers)

# # add item
# browsers.append("safari")
# print(browsers)

# # remove item
# browsers.remove("edge")
# print(browsers)

# # check if item exists
# if "chromium" in browsers:
#     print("chromium is in the list")

# # loop through array
# for browser in browsers:
#     print("Browser:", browser)

# # loop with index
# for i in range(len(numbers)):
#     print(i, numbers[i])
price = []
for i in range(10):
    pr = int(input("Enter price: "))
    price.append(pr)
print(price)