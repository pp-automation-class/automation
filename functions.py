KISS = "Keep It Simple Stupid"
DRY = "Don't Repeat Yourself"
YAGNI = "You Aren't Gonna Need It"

def my_print(item: str, value: float):
    print("********************************")
    print(item, value)

def greet_user():
    print("********************************")
    print("Welcome to the weather app")
    print("********************************")


greet_user()

input_temperature = float(input("Enter temperature: "))
my_print("Temperature", input_temperature)

input_humidity = float(input("Enter humidity: "))
my_print("Humidity", input_humidity)

input_pressure = float(input("Enter pressure: "))
my_print("Pressure", input_pressure)

input_wind_speed = float(input("Enter wind speed: "))
my_print("Wind speed", input_wind_speed)

input_wind_direction = float(input("Enter wind direction: "))
my_print("Wind direction", input_wind_direction)
