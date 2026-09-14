# KISS = "Keep It Simple Stupid"
# DRY = "Don't Repeat Yourself"
# YAGNI = "You Aren't Gonna Need It"
# DOK = "Don't Overthink It"

def my_print(item, value):
    print("******************")
    print("Welcome to the Weather Applications")
    print("******************")
    print(item, value)

def greet_user():
    print("******************")
    print("Welcome to the Weather Applications")
    print("******************")
    return input("Enter your name: ")

    greet_user()

input_temperature = float(input("Enter the temperature: "))
my_print("Temperature", input_temperature)

input_humidity = float(input("Enter the humidity: "))
my_print("Humidity", input_humidity)

input_pressure = float(input("Enter the pressure: "))
my_print("Pressure", input_pressure)

input_wind_speed = float(input("Enter the wind speed: "))
my_print("Wind speed", input_wind_speed)

input_wind_direction = float(input("Enter the wind direction: "))
my_print("Wind direction", input_wind_direction)

def calculate_wind_chill(temperature, wind_speed):
    return 13.12 + 0.6215 * temperature - 11.37 * wind_speed ** 0.16 + 0.3965 * temperature * wind_speed ** 0.16

wind_chill = calculate_wind_chill(input_temperature, input_wind_speed)
my_print("Wind chill", wind_chill)  