import requests, os

"""
    HOW THIS WHOLE THING WORKS:
    1. We need to obtain an access token
        - in order to access information for an end user, every time we need that request we need to use an access token
        - access tokens expire every 30 minutes
        - in order to generate an access token we need to know the loginName for the user(it will be stored in the DB and passed in the header)
        - in order to generate an access token we need to have developer CLIENT_ID and SECRET which are stored in a .env file
    2. We get information for a user using the access token
        - in order to get information for a user we need to use the access token, placing it in the header as follows: {'Authorization: Bearer someTokenGoesHere'}

    DEVELOPMENT v PRODUCTION:
    - in development we're using the Sandbox version of Yodlee which means:
        - we're using the sandbox URL
        - we're using the sandbox CLIENT_ID and SECRET
        - we're using the 5 sandbox loginName's that are provided and contain mock data(we can't create more)
    - for production we'll need to use the production URL
    - for production we'll need to use the production CLIENT_ID and SECRET
    - for production we'll need to generate unique loginNames for each user and store them in the DB
"""

# get yodlee developer credentials from .env file
CLIENT_ID = os.environ.get('YODLEE_CLIENT_ID')
SECRET = os.environ.get('YODLEE_SECRET')

URL = os.environ.get('YODLEE_SANDBOX_URL')

def get_access_token(loginName):
    # set up x-www-form-urlencoded data and header data for the request
    data = {'clientId': CLIENT_ID, 'secret': SECRET}
    headers = {'Api-Version': '1.1', 'loginName': loginName}

    # send the request and return the access token
    response = requests.post(URL + 'auth/token', data=data, headers=headers)
    try:
        return {'status': 'success', 'content': response.json()['token']['accessToken']}
    except:
        # return an error if it has occured
        return {'status': 'failed', 'content': f"Error: {response.json()['errorMessage']}"}

def get_balances(loginName):
    if not loginName: return {'status': 'failed', 'content':'Error: no Yodlee loginName was provided'}

    data = {}
    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data for the request
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}

        # send the request and save the balance for each account
        response = requests.get(URL + 'accounts', headers=headers)
        try:
            for account in response.json()['account']:
                data[account['id']] = {"providerName": account["providerName"], "balanceData": account["balance"]}

            return {'status': 'success', 'content': data}
        except:
            # return an error if it has occured
            return {'status': 'failed', 'content': f"Error: {response.json()['errorMessage']}"}
    else:
        return access_token

def get_transactions(loginName):
    if not loginName: return {'status': 'failed', 'content':'Error: no Yodlee loginName was provided'}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data and query parameters for the request
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}
        params = {'top': 10, 'fromDate': '2013-12-12'}
        
        # send the request and save the balance for each account
        response = requests.get(URL + 'transactions', headers=headers, params=params)
        try:
            transactions = response.json()["transaction"]
        except:
            return {'status': 'failed', 'content': "Error: no transactions found"}
        data = {}
        transaction_data = {}

        for transaction in transactions:
            # check if other transactions for this merchant are already in the data object
            if transaction.get('merchant'):
                source = transaction['merchant']['source']
            else:
                source = 'unknown'
            if not transaction_data.get(source):
                transaction_data[source] = {}

            #    add only the completed transactions
            if transaction['status'] == 'POSTED':
                transaction_data[source][transaction["id"]] = transaction['amount']
        
        data = transaction_data

        return {'status': 'success', 'content': data}
    else:
        return access_token

def get_holdings(loginName):
    if not loginName: return {'status': 'failed', 'content':'Error: no Yodlee loginName was provided'}

    data = {}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)

    if access_token['status'] == 'success':
        # set up header data for the request
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}

        # send the request and save the balance for each account
        response = requests.get(URL + 'holdings', headers=headers).json()

        try:
            if not response.get('holding'):
                return {'status': 'failed', 'content': "Error: no holdings found"}

            for holding in response['holding']:
                if holding.get('symbol') and holding.get('value'):
                    data[holding['id']] = {'symbol': holding['symbol'], 'quantity': holding['quantity'], 'value': holding['value']}
            return {'status': 'success', 'content': data}

        except:
            # return an error if it has occured
            return {'status': 'failed', 'content': f"Error: {response['errorMessage']}"}
    else:
        return access_token