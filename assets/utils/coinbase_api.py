import os

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
    try:
        for account in client_accounts["data"]:
            if float(account["balance"].amount) > 0:
                data[account["id"]] = ({"symbol": account["balance"].currency, "quantity": account["balance"].amount,
                                        "value": account["native_balance"]})
    except:
        return {'status': 'failed', 'content': f"Error: unknown error"}
    return {'status': 'success', 'content': data}


def get_transactions(api_key, api_secret):
    if os.environ.get('USE_MOCK') == 'True':
        return {
            "status": "success",
            "content": {
                "DOGE Wallet": {
                    "6f26d0a9-15c3-58b3-8c1e-cd974fdcdebf": {
                        "amount": "-200.00000000",
                        "currency": "DOGE"
                    },
                    "ae203706-4a5c-5524-b804-723a95800e0e": {
                        "amount": "-9995.00000000",
                        "currency": "DOGE"
                    },
                    "a4adf54c-f3da-584f-8f09-5a4de77fcbb4": {
                        "amount": "19995.00000000",
                        "currency": "DOGE"
                    }
                }
            }
        }
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e}"}

    try:
        client_accounts = client.get_accounts()
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e.message}"}

    data = {}
    try:
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
    except:
        return {'status': 'failed', 'content': f"Error: unknown error"}

    return {'status': 'success', 'content': data}
