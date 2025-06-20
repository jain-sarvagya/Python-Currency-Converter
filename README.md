# 💱 Currency Converter Using API

This is a simple Python project that converts one currency to another using real-time exchange rates fetched from an API.

---

## 🎯 Objective

To create a currency management tool in Python that:
- Takes a base currency and target currency as input
- Fetches live exchange rates from a public API
- Calculates and displays the converted amount

---

## 📌 Features

- Choose base and target currencies from a list
- Fetch live exchange rates using API
- Supports multiple popular currencies
- Clean and user-friendly CLI interface
- Handles invalid inputs gracefully

---

## 🛠 Technologies Used

- **Python**
- **Requests** module
- **ExchangeRate API** (`https://v6.exchangerate-api.com`)
- CLI-based input/output

---

## ▶️ How to Run

1. Install the `requests` module (if not already installed):
```bash
pip install requests
Run the script:

bash
Copy
Edit
python Currency_Converter.py
Example interaction:

yaml
Copy
Edit
Choose base currency:
1. USD
2. EUR
3. INR
...
Enter the number for base currency: 1
Enter the number for target currency: 3
Enter amount: 100

✅ 100 USD = 8349.45 INR
💡 Inputs
Base currency choice (1–10)

Target currency choice (1–10)

Amount to convert

📦 API Used
ExchangeRate API:
URL Format:

bash
Copy
Edit
https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
💻 Example Code Snippet
python
Copy
Edit
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
response = requests.get(url)
data = response.json()
rate = data["conversion_rates"].get(target_currency)
converted_amount = amount * rate
✅ Requirements
Python 3.x

requests module

Internet connection

👨‍💻 Author
Sarvagya Jain