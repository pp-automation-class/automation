# Common Python variable types

# str
APP_URL = "https://www.google.com"
EMAIL = 'student@example.com'
password = "this is - 'Playwright1'!"

# print(password)
# type(password)
# print(type(password))

# int
TIMEOUT_MS = 5000000000
RETRY_COUNT = -3
PORT = 0
# print(type(TIMEOUT_MS))

# float
WAIT_SECONDS = -1.5
PRICE = 19.99
# print(type(PRICE))
# bool
HEADLESS = True
DEBUG = False

# NoneType
AUTH_TOKEN = None

a = int("10A")
b = 2
print(type(a))
print(type(b))
# c = a / b
# print(type(c))
# print(c)


# # list
# BROWSERS = ["chromium", "firefox", "webkit"]
# TAGS = ["smoke", "login"]

# # tuple (immutable)
# VIEWPORT = (1280, 720)
# RGB_PRIMARY = (61, 156, 240)

# # dict
# USER = {
#     "email": EMAIL,
#     "password": PASSWORD,
#     "remember": True,
# }

# SELECTORS = {
#     "email": "#email",
#     "password": "#password",
#     "login_button": "#login-button",
#     "message": "#message",
# }

# # set (unique values)
# ALLOWED_STATUSES = {"success", "error", "pending"}

# # bytes
# RAW_HEADER = b"Content-Type: text/html"
