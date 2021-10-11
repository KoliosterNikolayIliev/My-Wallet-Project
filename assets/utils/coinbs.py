from coinbase.wallet.client import Client

API_KEY = 'Zc0NlXIXe1nQt2AA'
API_SECRET = 'Nz3CySHqHrxppLr8nPePoIv72UimfMHE'


client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET
)


""" Check all existing client wallets on Coinbase """
client_accounts = client.get_accounts()


""" Iterate through all wallets and extract balance data """

def get_account_balances():
    data = []
    for account in client_accounts["data"]:
        data.append({"account_balance": account["balance"].amount, "account_currency": account["balance"].currency})
    return data


""" Iterate through all wallets and extract all transactions"""


def get_account_transactions():
    data = []
    for account in client_accounts["data"]:
        data = client.get_transactions(account["id"])
    return data
