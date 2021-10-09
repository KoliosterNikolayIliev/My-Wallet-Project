import requests

# fetch all balances using Assets
def get_balances(headers):
    res = requests.get("http://127.0.0.1:5000/balances/", headers=headers)
    return res.json()


# fetch all transactions using Assets
def get_transactions(headers):
    res = requests.get("http://127.0.0.1:5000/transactions/", headers=headers)
    return res.json()
