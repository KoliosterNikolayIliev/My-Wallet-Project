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

    data = {}
    for wallet in client_accounts["data"]:
        transactions = client.get_transactions(wallet.id, limit=10)

        # check if there are any transactions for this wallet
        if transactions["data"]:
            transaction_data = {}
            for transaction in transactions["data"]:
                # return only the completed transactions
                if transaction["status"] == "completed":
                    transaction_data[transaction["id"]] = transaction['amount']
            
            data[wallet.name] = transaction_data

    return {'status': 'success', 'content': data}

