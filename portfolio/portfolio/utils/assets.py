import requests, os
import asyncio

URL = os.environ.get("ASSETS_URL")

# fetch all balances using Assets
async def get_balances(headers, session):
    async with session.get(URL + "balances", headers=headers, ssl=False) as res:
        return await res.json()



# fetch all transactions using Assets
def get_transactions(headers):
    res = requests.get(URL + "transactions", headers=headers)
    return res.json()

# fetch all holdings using Assets
async def get_holdings(headers, session):
    async with session.get(URL + "holdings", headers=headers, ssl=False) as res:
        return await res.json()
