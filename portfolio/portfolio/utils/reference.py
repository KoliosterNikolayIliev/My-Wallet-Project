import requests, os

URL = os.eniron.get("REFERENCE_URL")

def get_crypto_prices():
    res = requests.get(URL + "crypto/prices")
    return res.json()

def get_stocks_prices():
    res = requests.get(URL + "stocks/prices")
    return res.json()
