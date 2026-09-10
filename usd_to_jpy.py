print("Simple Currency Converter (USD to JPY)")
rate = 157
while True:
    a_text = input("Enter amount in USD or q to exit: ")
    if a_text == "q":
        break
    usd = float(a_text)
    jpy = usd * rate
    print(f"{usd} USD = {jpy} JPY")
