import requests
import json

api_key = "vK1CsIWa0XC7IAEK6svayMOoTv8gypYQ"

def convert(amount, from_currency, to_currency):
    url = f"http://data.fixer.io/api/convert?access_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["result"]

# Exemple d'utilisation:
amount = 100
from_currency = "EUR"
to_currency = "USD"

converted_amount = convert(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
