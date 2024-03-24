#pip install requests
import requests

#response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=Some-API-key-Token")
#response = requests.get("https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=Some-API-key-Token")
response = requests.get("https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=USD&to_symbol=BRL&interval=5min&apikey=Some-API-key-Token")

#print(response.status_code)
#print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=5)
    print(text)

jprint(response.json())