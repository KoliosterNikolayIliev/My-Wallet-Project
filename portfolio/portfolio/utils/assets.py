import requests, os

URL = os.environ.get("ASSETS_URL")

# fetch all balances using Assets
def get_balances(headers):
    res = requests.get(URL + "balances/", headers=headers)
    return res.json()


# fetch all transactions using Assets
def get_transactions(headers):
    res = requests.get(URL + "transactions/", headers=headers)
    return res.json()

# fetch all holdings using Assets
def get_holdings(headers):
    res = requests.get(URL + "holdings/", headers=headers)
    return res.json()
