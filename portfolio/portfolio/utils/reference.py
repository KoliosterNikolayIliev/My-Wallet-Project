import requests


def get_crypto_prices():
    res = requests.get("http://127.0.0.1:5002/crypto/prices")
    return res.json()


def get_stocks_prices():
    res = requests.get("http://127.0.0.1:5002/stocks/prices")
    return res.json()
