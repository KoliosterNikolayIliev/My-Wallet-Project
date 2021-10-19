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
    if os.environ.get('USE_MOCK'):
        return {'status': 'success', 'content': 'token'}

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
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    data = {}
    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data for the request
        if not os.environ.get('USE_MOCK'):
            headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}

            # send the request and save the balance for each account
            response = requests.get(URL + 'accounts', headers=headers).json()

        else:
            response = {'account': [
                {'CONTAINER': 'creditCard', 'providerAccountId': 10011819, 'accountName': 'CREDIT CARD',
                 'accountStatus': 'ACTIVE', 'accountNumber': 'xxxx8614', 'aggregationSource': 'USER', 'isAsset': False,
                 'balance': {'currency': 'USD', 'amount': 1636.44}, 'id': 10017310, 'includeInNetWorth': True,
                 'providerId': '16441', 'providerName': 'Dag Site', 'isManual': False, 'accountType': 'OTHER',
                 'createdDate': '2021-09-22T10:41:58Z', 'apr': 29.99, 'cashApr': 29.99,
                 'availableCash': {'currency': 'USD', 'amount': 600.0},
                 'availableCredit': {'currency': 'USD', 'amount': 1363.0},
                 'lastPaymentAmount': {'currency': 'USD', 'amount': 250.0}, 'lastPaymentDate': '2014-01-17',
                 'lastUpdated': '2021-10-18T22:17:33Z', 'runningBalance': {'currency': 'USD', 'amount': 1636.44},
                 'totalCashLimit': {'currency': 'USD', 'amount': 600.0},
                 'totalCreditLine': {'currency': 'USD', 'amount': 3000.0}, 'dataset': [
                    {'name': 'BASIC_AGG_DATA', 'additionalStatus': 'AVAILABLE_DATA_RETRIEVED',
                     'updateEligibility': 'ALLOW_UPDATE', 'lastUpdated': '2021-10-18T22:17:33Z',
                     'lastUpdateAttempt': '2021-10-18T22:17:33Z', 'nextUpdateScheduled': '2021-10-20T05:33:52Z'}]},
                {'CONTAINER': 'bank', 'providerAccountId': 10011819, 'accountName': 'TESTDATA1',
                 'accountStatus': 'ACTIVE', 'accountNumber': 'xxxx3xxx', 'aggregationSource': 'USER', 'isAsset': True,
                 'balance': {'currency': 'USD', 'amount': 9044.78}, 'id': 10017309, 'includeInNetWorth': True,
                 'providerId': '16441', 'providerName': 'Dag Site', 'isManual': False,
                 'availableBalance': {'currency': 'USD', 'amount': 65454.78},
                 'currentBalance': {'currency': 'USD', 'amount': 9044.78}, 'accountType': 'SAVINGS',
                 'displayedName': 'accountHolder', 'createdDate': '2021-09-22T10:41:57Z',
                 'lastUpdated': '2021-10-18T22:17:28Z', 'dataset': [
                    {'name': 'BASIC_AGG_DATA', 'additionalStatus': 'AVAILABLE_DATA_RETRIEVED',
                     'updateEligibility': 'ALLOW_UPDATE', 'lastUpdated': '2021-10-18T22:17:28Z',
                     'lastUpdateAttempt': '2021-10-18T22:17:28Z', 'nextUpdateScheduled': '2021-10-19T20:10:42Z'}]},
                {'CONTAINER': 'bank', 'providerAccountId': 10011819, 'accountName': 'TESTDATA',
                 'accountStatus': 'ACTIVE', 'accountNumber': 'xxxx3xxx', 'aggregationSource': 'USER', 'isAsset': True,
                 'balance': {'currency': 'USD', 'amount': 44.78}, 'id': 10017308, 'includeInNetWorth': True,
                 'providerId': '16441', 'providerName': 'Dag Site', 'isManual': False,
                 'availableBalance': {'currency': 'USD', 'amount': 54.78},
                 'currentBalance': {'currency': 'USD', 'amount': 44.78}, 'accountType': 'CHECKING',
                 'displayedName': 'accountHolder', 'createdDate': '2021-09-22T10:41:57Z', 'classification': 'PERSONAL',
                 'lastUpdated': '2021-10-18T22:17:28Z', 'dataset': [
                    {'name': 'BASIC_AGG_DATA', 'additionalStatus': 'AVAILABLE_DATA_RETRIEVED',
                     'updateEligibility': 'ALLOW_UPDATE', 'lastUpdated': '2021-10-18T22:17:28Z',
                     'lastUpdateAttempt': '2021-10-18T22:17:28Z', 'nextUpdateScheduled': '2021-10-19T20:10:42Z'},
                    {'name': 'BASIC_AGG_DATA', 'additionalStatus': 'LOGIN_IN_PROGRESS',
                     'updateEligibility': 'DISALLOW_UPDATE', 'lastUpdated': '2021-09-22T10:41:58Z',
                     'lastUpdateAttempt': '2021-09-22T10:41:58Z', 'nextUpdateScheduled': '2021-10-19T20:10:42Z'}]}]}

        try:
            for account in response['account']:
                data[account['id']] = {"providerName": account["providerName"], "balanceData": account["balance"]}

            return {'status': 'success', 'content': data}
        except:
            # return an error if it has occured
            return {'status': 'failed', 'content': f"Error: {response['errorMessage']}"}
    else:
        return access_token


def get_transactions(loginName):
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data and query parameters for the request
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}
        params = {'top': 10}

        # send the request and save the balance for each account
        response = requests.get(URL + 'transactions', headers=headers, params=params)
        try:
            try:
                transactions = response.json()['transaction']
            except:
                return {'status': 'failed', 'content': "Error: no transactions found"}
            data = {}

            for transaction in transactions:
                # check if other transactions for this merchant are already in the data object
                transaction_parent = data.get(transaction['merchant']['name'], {})
                transaction_data = {}

                # add only the completed transactions
                if transaction['status'] == 'POSTED':
                    transaction_data[transaction['id']] = transaction['price']
                    data[transaction_parent] += transaction_data

            return {'status': 'success', 'content': response.json()}
        except:
            # return an error if it has occured
            return {'status': 'failed', 'content': f"Error: {response.json()['errorMessage']}"}
    else:
        return access_token


def get_holdings(loginName):
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    data = {}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data for the request
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}
        # send the request and save the balance for each account
        response = requests.get(URL + 'holdings', headers=headers)
        try:
            if not response.json().get('holding'):
                return {'status': 'failed', 'content': "Error: no holdings found"}
            for holding in response.json()['holding']:
                data[holding['id']] = {'symbol': holding['symbol'], 'quantity': holding['quantity'],
                                       'value': holding['value']}
            return {'status': 'success', 'content': data}
        except:
            # return an error if it has occured
            return {'status': 'failed', 'content': f"Error: {response.json()['errorMessage']}"}
    else:
        return access_token
