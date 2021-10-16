from coinbase.wallet.client import Client


def get_account_balances(api_key, api_secret):
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e}"}
    
    try:
        client_accounts = client.get_accounts()
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e.message}"}
    
    data = {}
    for account in client_accounts["data"]:
        if float(account["balance"].amount) > 0:
            data[account["id"]] = ({"symbol": account["balance"].currency, "quantity": account["balance"].amount, "value": account["native_balance"]})
    return {'status': 'success', 'content': data}


def get_transactions(api_key, api_secret):
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return {'status':'failed', 'content': f"Error: {e}"}
    
    try:
        client_accounts = client.get_accounts()
    except Exception as e:
        return {'status':'failed', 'content': f"Error: {e.message}"}

    data = []
    for each_wallet in client_accounts["data"]:
        wallet_id = each_wallet.id
        transactions = client.get_transactions(wallet_id)
        data.append(transactions)
    return {'status': 'success', 'content': data}

