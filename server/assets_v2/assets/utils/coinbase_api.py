import os, json, hmac, hashlib, time, httpx, asyncio, base64
from requests.utils import to_native_string
from coinbase.wallet.client import Client

USE_MOCK = os.environ.get('ASSETS_USE_MOCK')

MOCK_ACCOUNTS_DATA = {
            'data': [{
                "allow_deposits": True,
                "allow_withdrawals": True,
                "balance": {
                    "amount": "9800.00000000",
                    "currency": "DOGE"
                },
                "created_at": "2021-09-15T16:00:09Z",
                "currency": "DOGE",
                "id": "ea1afd10-87cc-5301-9445-14bc36ce4d8d",
                "name": "DOGE Wallet",
                "native_balance": {
                    "amount": "1737.54",
                    "currency": "GBP"
                },
                "primary": False,
                "resource": "account",
                "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d",
                "type": "wallet",
                "updated_at": "2021-09-26T19:27:25Z"
            }]
        }

MOCK_TRANSACTIONS_DATA = {
                    "data": [
                        {
                            "amount": {
                                "amount": "-200.00000000",
                                "currency": "DOGE"
                            },
                            "created_at": "2021-09-26T19:27:25Z",
                            "description": None,
                            "details": {
                                "header": "Sold 200.0000 DOGE (\u00a328.04)",
                                "health": "positive",
                                "payment_method_name": "GBP Wallet",
                                "subtitle": "Using GBP Wallet",
                                "title": "Sold Dogecoin"
                            },
                            "hide_native_amount": False,
                            "id": "6f26d0a9-15c3-58b3-8c1e-cd974fdcdebf",
                            "instant_exchange": False,
                            "native_amount": {
                                "amount": "-28.04",
                                "currency": "GBP"
                            },
                            "resource": "transaction",
                            "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d/transactions/6f26d0a9-15c3-58b3-8c1e-cd974fdcdebf",
                            "sell": {
                                "id": "5a10d1c9-7059-5239-9314-f4745f1f1367",
                                "resource": "sell",
                                "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d/sells/5a10d1c9-7059-5239-9314-f4745f1f1367"
                            },
                            "status": "completed",
                            "type": "sell",
                            "updated_at": "2021-09-26T19:27:25Z"
                        },
                        {
                            "amount": {
                                "amount": "-9995.00000000",
                                "currency": "DOGE"
                            },
                            "created_at": "2021-09-19T14:39:00Z",
                            "description": None,
                            "details": {
                                "header": "Sold 9,995.0000 DOGE (\u00a31,698.77)",
                                "health": "positive",
                                "payment_method_name": "GBP Wallet",
                                "subtitle": "Using GBP Wallet",
                                "title": "Sold Dogecoin"
                            },
                            "hide_native_amount": False,
                            "id": "ae203706-4a5c-5524-b804-723a95800e0e",
                            "instant_exchange": False,
                            "native_amount": {
                                "amount": "-1698.77",
                                "currency": "GBP"
                            },
                            "resource": "transaction",
                            "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d/transactions/ae203706-4a5c-5524-b804-723a95800e0e",
                            "sell": {
                                "id": "afba0b71-024f-5c10-a6e6-400248a9627d",
                                "resource": "sell",
                                "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d/sells/afba0b71-024f-5c10-a6e6-400248a9627d"
                            },
                            "status": "completed",
                            "type": "sell",
                            "updated_at": "2021-09-19T14:39:00Z"
                        },
                        {
                            "amount": {
                                "amount": "19995.00000000",
                                "currency": "DOGE"
                            },
                            "created_at": "2021-09-15T16:09:26Z",
                            "description": None,
                            "details": {
                                "header": "Received 19,995.0000 DOGE (\u00a33,399.15)",
                                "health": "positive",
                                "subtitle": "From Dogecoin address",
                                "title": "Received Dogecoin"
                            },
                            "from": {
                                "currency": "DOGE",
                                "resource": "dogecoin_network"
                            },
                            "hide_native_amount": False,
                            "id": "a4adf54c-f3da-584f-8f09-5a4de77fcbb4",
                            "instant_exchange": False,
                            "native_amount": {
                                "amount": "3399.15",
                                "currency": "GBP"
                            },
                            "network": {
                                "hash": "300145263507c516fb29812c8ae52046cdb40b2314c382e506b29d588ad7e2c7",
                                "status": "unconfirmed",
                                "status_description": "Pending (est. about 6 hours)",
                                "transaction_url": "https://live.blockcypher.com/doge/tx/300145263507c516fb29812c8ae52046cdb40b2314c382e506b29d588ad7e2c7"
                            },
                            "resource": "transaction",
                            "resource_path": "/v2/accounts/ea1afd10-87cc-5301-9445-14bc36ce4d8d/transactions/a4adf54c-f3da-584f-8f09-5a4de77fcbb4",
                            "status": "completed",
                            "type": "send",
                            "updated_at": "2021-09-15T16:09:26Z"
                        }
                    ]
                }


def format_balances_response(client_accounts):
    data = {}
    try:
        for account in client_accounts["data"]:
            if float(account["balance"]['amount']) > 0:
                data[account["id"]] = ({"symbol": account["balance"]['currency'], "quantity": account["balance"]['amount']})
    except:
        return {'status': 'failed', 'content': f"Error: unknown error"}
    return data

async def get_account_balances(api_key, api_secret):
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e}"}

    if USE_MOCK != 'True':
        try:
            client_accounts = client.get_accounts()
        except Exception as e:
            return {'status': 'failed', 'content': f"Error: {e}"}

    else:
        client_accounts = MOCK_ACCOUNTS_DATA

    data = format_balances_response(client_accounts)
    
    return {'status': 'success', 'content': data}


async def get_transactions(api_key, api_secret, account):
    try:
        client = Client(api_key, api_secret)
    except Exception as e:
        return {'status': 'failed', 'content': f"Error: {e}"}

    try:
        if USE_MOCK != 'True':
            account_name = client.get_account(account)['name']
            transactions = client.get_transactions(account)

        else:
            transactions = MOCK_TRANSACTIONS_DATA
            account_name = MOCK_ACCOUNTS_DATA['name']

        # check if there are any transactions for this wallet
        if transactions["data"]:
            transaction_data = {}
            for transaction in transactions["data"]:
                # return only the completed transactions
                if transaction["status"] == "completed":
                    transaction_data[transaction["id"]] = transaction['amount']

            data = {account_name: transaction_data}
    except:
        return {'status': 'failed', 'content': f"Error: unknown error"}

    return {'status': 'success', 'content': data}


async def get_all_transactions(api_key, api_secret, session):
    def get_auth(key, secret, path):
        timestamp = str(int(time.time()))
        message = timestamp + 'GET' + path 
        message = message.encode()
        secret_en = secret.encode()

        signature = hmac.new(secret_en, message, hashlib.sha256).hexdigest()

        headers = {
            to_native_string('CB-ACCESS-SIGN'): signature,
            to_native_string('CB-ACCESS-TIMESTAMP'): timestamp,
            to_native_string('CB-ACCESS-KEY'): key,
            # to_native_string('Content-Type'): 'application/json'
        }
        return headers

    api_url = 'https://api.coinbase.com/v2/'
    try:
        async with session.get(api_url + 'accounts', headers=get_auth(api_key, api_secret, '/v2/accounts')) as res:
            accounts = await res.json()

        async def get_transactions_async(account, session):
            data = []
            async with session.get(api_url + f'accounts/{account}/transactions', headers=get_auth(api_key, api_secret, f'/v2/accounts/{account}/transactions')) as res:
                transactions = await res.json()

            for transaction in transactions["data"]:
                if transaction["status"] == "completed":
                    data.append({transaction["id"]: {"amount": transaction['amount'], "date": transaction['created_at'][:10], "type": "crypto", "source": "coinbase"}})
            return data
        tasks = []
        for account in accounts["data"]:
            tasks.append(asyncio.ensure_future(get_transactions_async(account["id"], session)))

        responses = await asyncio.gather(*tasks)
        data = []
        for response in responses:
            if response:
                data.append(response)

        if data:
            return {'status': 'success', 'content': data}

        return {'status': 'failed', 'content': 'no transactions'}
    except Exception as e:
        print(str(e))

