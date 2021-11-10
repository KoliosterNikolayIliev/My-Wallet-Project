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


def convert_assets_value_to_base_currency(base, balances, holdings):
    currency_prices = get_currencies_prices(base)
    currency_prices_gbp = get_currencies_prices("GBP")
    crypto_prices = get_crypto_prices()

    for balance in balances.values():
        for asset in balance["content"].values():
            asset["balanceData"]["base_currency"] = float(asset["balanceData"]["amount"]) / float(
                currency_prices[asset["balanceData"]["currency"]])

            asset["balanceData"]["monitor_currency"] = float(asset["balanceData"]["amount"]) / float(
                currency_prices_gbp[asset["balanceData"]["currency"]])

    for holding in holdings.values():
        for asset in holding['content'].values():
            if crypto_prices.get(asset["symbol"]):
                usd_currency = float(crypto_prices[asset["symbol"]]) * float(asset["quantity"])
                asset["base_currency"] = usd_currency / float(currency_prices["USD"])
                asset["monitor_currency"] = usd_currency / float(currency_prices_gbp["USD"])


def convert_transactions_currency_to_base_currency(base, transactions):
    currency_prices = get_currencies_prices(base)
    crypto_prices = get_crypto_prices()

    for transaction in transactions["content"].values():
        for amount in transaction.values():
            if currency_prices.get(amount["currency"]):
                amount["base_currency"] = float(amount["amount"]) / currency_prices[amount["currency"]]

            else:
                if crypto_prices.get(amount["currency"]):
                    usd_currency = float(crypto_prices[amount["currency"]]) * float(amount["amount"])
                    amount["base_currency"] = usd_currency / float(currency_prices["USD"])
