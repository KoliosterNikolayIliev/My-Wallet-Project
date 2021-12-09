import asyncio

import requests, os

URL = os.environ.get("PORTFOLIO_REFERENCE_URL")


async def get_crypto_prices(session):
    async with session.get(URL + "crypto/prices") as res:
        res = await res.json()
        return res


async def get_stocks_prices(session):
    async with session.get(URL + "stocks/prices") as res:
        res = await res.json()
        return res


async def get_currencies_prices(base, session):
    async with session.get(URL + "currencies/prices", headers={'base': base}) as res:
        res = await res.json()
        return res


async def convert_assets_to_base_currency_and_get_total_gbp(base, balances, holdings, session):
    currency_prices, currency_prices_gbp, crypto_prices, stocks_prices = await asyncio.gather(
        get_currencies_prices(base, session),
        get_currencies_prices("GBP", session),
        get_crypto_prices(session),
        get_stocks_prices(session)
    )
    total_gbp = 0
    for balance in balances.values():
        if balance["status"] != "failed":
            for asset in balance["content"].values():
                asset["balanceData"]["base_currency"] = float(asset["balanceData"]["amount"]) / float(
                    currency_prices[asset["balanceData"]["currency"]])
                value = float(asset["balanceData"]["amount"]) / float(
                    currency_prices_gbp[asset["balanceData"]["currency"]])
                total_gbp += value
                asset["balanceData"]["gbp_currency"] = value

    for holding in holdings.values():
        if holding["status"] != "failed":
            for asset in holding['content'].values():
                if crypto_prices.get(asset["symbol"]):
                    usd_currency = float(crypto_prices[asset["symbol"]]) * float(asset["quantity"])
                    asset["base_currency"] = usd_currency / float(currency_prices["USD"])
                    value = usd_currency / float(currency_prices_gbp["USD"])
                    total_gbp += value
                    asset["gbp_currency"] = value

                else:
                    if type(asset.get('value')) == dict:
                        asset["base_currency"] = float(asset['value']['amount']) / float(currency_prices[asset['value']['currency']])
                    elif stocks_prices.get(asset["symbol"]):
                        usd_currency = float(stocks_prices[asset["symbol"]]) * float(asset["quantity"])
                        asset["base_currency"] = usd_currency / float(currency_prices["USD"])
                        value = usd_currency / float(currency_prices_gbp["USD"])
                        total_gbp += value
                        asset["gbp_currency"] = value

    return total_gbp


async def convert_transactions_currency_to_base_currency(base, transactions, session, recent=False):
    if transactions["status"] != "failed":
        currency_prices, crypto_prices = await asyncio.gather(
            get_currencies_prices(base, session),
            get_crypto_prices(session)
        )

        if not recent:
            for transaction in transactions["content"].values():
                for amount in transaction.values():
                    if currency_prices.get(amount["currency"]):
                        amount["amount"] = float(amount["amount"]) / currency_prices[amount["currency"]]
                        amount["currency"] = base

                    else:
                        if crypto_prices.get(amount["currency"]):
                            usd_currency = float(crypto_prices[amount["currency"]]) * float(amount["amount"])
                            amount["amount"] = usd_currency / float(currency_prices["USD"])
                            amount["currency"] = base
        else:
            for transaction in transactions['content']:
                for data in transaction.values():
                    amount = data["amount"]
                    if currency_prices.get(amount["currency"]):
                        amount["base_amount"] = float(amount["amount"]) / currency_prices[amount["currency"]]
                        amount["base_currency"] = base

                    else:
                        if crypto_prices.get(amount["currency"]):
                            usd_currency = float(crypto_prices[amount["currency"]]) * float(amount["amount"])
                            amount["base_amount"] = usd_currency / float(currency_prices["USD"])
                            amount["base_currency"] = base


def convert_balance_history_to_base_currency(data, base_currency):
    balance_history = data.get('balance_history')
    if balance_history:
        currency_prices = requests.get(URL + "currencies/prices", headers={'base': 'GBP'}).json()
        exchange_rate = currency_prices[base_currency]
        for balance in balance_history['balances']:
            balance['balance'] *= exchange_rate
            for source in balance['source_balances_history']:
                source['value'] *= exchange_rate
