#empty list
celsius_list = []

print("Enter temperature one by one. Type 'q' to finish.")

#collect inputs dynamically
while True:
    user_input = input("Enter temperature in Celsius: ")

    #Check if they want to quit
    if user_input == 'q':
        break

    #Convert input to float and add it to our list
    celsius_temp = float(user_input)
    celsius_list.append(celsius_temp)

print(" --Collection Complete --")
print("Your list of temperatures is: ", celsius_list)

#Loop throught the list just built and convert them
for celsius in celsius_list:
    fahrenheit = celsius*9/5+32
    print(f"{celsius}C = {fahrenheit}F")

    if celsius < -20 or celsius > 100:
        print("Out of range")



#  1. Start with an empty list
# celsius_temps = []

# # 2. Use while True to collect data continuously
# while True:
#     user_input = input("Enter a temperature in Celsius (or type 'quit' to stop): ")
    
#     # 3. The break condition to exit the loop
#     if user_input.lower() == 'quit':
#         break
        
#     # Convert input to float and add to the list directly
#     celsius = float(user_input)
#     celsius_temps.append(celsius)

# # 4. Process the list after the loop finishes
# print("\n--- Final Conversions ---")
# for c in celsius_temps:
#     f = (c * 9/5) + 32
#     print(f"{c}°C is equivalent to {f}°F.")


# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = celsius * 9 / 5 + 32
# print(f"{celsius} C = {fahrenheit} F")

# if celsius < 20 or celsius > 40:
#     print("out of range")
