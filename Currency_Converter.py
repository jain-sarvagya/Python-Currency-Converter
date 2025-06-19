import requests

print("Choose your base currency:")
print("1. USD (US Dollar)")
print("2. EUR (Euro)")
print("3. INR (Indian Rupee)")
print("4. GBP (British Pound)")
print("5. JPY (Japanese Yen)")
print("6. AUD (Australian Dollar)")
print("7. CAD (Canadian Dollar)")
print("8. CHF (Swiss Franc)")
print("9. CNY (Chinese Yuan)")
print("10. NZD (New Zealand Dollar)")

choice = input("Enter the currency number i.e (1-10) from which you want to convert: ")
converted_choice = input("Enter the currency number (1-10) in which you want to convert: ")
amount = float(input("Enter amount: "))

# Mapping number to currency code
currency_map = {
    "1": "USD",
    "2": "EUR",
    "3": "INR",
    "4": "GBP",
    "5": "JPY",
    "6": "AUD",
    "7": "CAD",
    "8": "CHF",
    "9": "CNY",
    "10": "NZD"
}

base_currency = currency_map.get(choice)
target_currency = currency_map.get(converted_choice)

if base_currency is None or target_currency is None:
    print("❌ Invalid currency selection.")
else:
    url = f"https://v6.exchangerate-api.com/v6/25c489c3a2c0893f6d6ce2d9/latest/{base_currency}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["conversion_rates"].get(target_currency)

        if rate:
            result = rate * amount
            print(f"\n✅ {amount} {base_currency} = {result:.2f} {target_currency}")
        else:
            print("❌ Target currency not found in API response.")
    else:
        print("❌ Failed to fetch data:", response.status_code)
