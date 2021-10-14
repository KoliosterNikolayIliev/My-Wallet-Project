from coinbase.wallet.client import Client


def get_account_balances(api_key, api_secret):
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return f"Error: {e}"
    
    try:
        client_accounts = client.get_accounts()
    except Exception as e:
        return f"Error: {e.message}"
    
    data = []
    for account in client_accounts["data"]:
        data.append({"balance": account["balance"].amount, "currency": account["balance"].currency})
    return data


def get_transactions(api_key, api_secret):
    client = Client(api_key, api_secret)
    client_accounts = client.get_accounts()

    data = []
    for each_wallet in client_accounts["data"]:
        wallet_id = each_wallet.id
        transactions = client.get_transactions(wallet_id)
        data.append(transactions)
    return data

