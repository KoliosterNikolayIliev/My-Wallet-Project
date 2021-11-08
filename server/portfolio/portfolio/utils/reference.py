import requests, os

URL = os.environ.get("PORTFOLIO_REFERENCE_URL")


def get_crypto_prices():
    res = requests.get(URL + "crypto/prices")
    return res.json()


def get_stocks_prices():
    res = requests.get(URL + "stocks/prices")
    return res.json()


def get_currencies_prices(base):
    res = requests.get(URL + "currencies/prices", headers={'base': base})
    return res.json()


def convert_assets_value_to_base_currency(base, assets):
    balances = assets[0]
    currency_prices = get_currencies_prices(base)

    for balance in balances.values():
        for asset in balance['content'].values():
            asset["balanceData"]["base_currency"] = float(asset["balanceData"]["amount"]) / float(
                currency_prices[asset["balanceData"]["currency"]])

