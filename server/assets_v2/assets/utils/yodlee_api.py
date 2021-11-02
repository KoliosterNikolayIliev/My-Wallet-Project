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
CLIENT_ID = os.environ.get('ASSETS_YODLEE_CLIENT_ID')
SECRET = os.environ.get('ASSETS_YODLEE_SECRET')
URL = os.environ.get('YODLEE_DEVELOPMENT_URL')
USE_MOCK = os.environ.get('ASSETS_USE_MOCK')

BALANCES_MOCK_DATA = {'account': [
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


HOLDINGS_MOCK_DATA = {'holding': [
                {'id': 10010734, 'holdingType': 'bond', 'providerAccountId': 10012100, 'accountId': 10017272,
                 'createdDate': '2021-09-22T13:10:06Z', 'lastUpdated': '2021-10-18T23:21:44Z',
                 'description': 'NEW YORK N Y GO BDS FISCAL GO DATED 10/04/07 DUE 10/01/22 5.00% PAR CALL 10/01/',
                 'optionType': 'unknown', 'price': {'amount': 101.14, 'currency': 'USD'}, 'quantity': 5,
                 'value': {'amount': 5.05, 'currency': 'USD'}},
                {'id': 10010800, 'holdingType': 'moneyMarketFund', 'providerAccountId': 10012100, 'accountId': 10017274,
                 'createdDate': '2021-09-22T13:10:07Z', 'lastUpdated': '2021-10-18T23:21:44Z',
                 'description': 'FDIC INSURED DEPOSIT AT FIFTH THIRD IRA NOT COVERED BY SIPC', 'optionType': 'unknown',
                 'price': {'amount': 1.0, 'currency': 'USD'}, 'quantity': 54.99, 'symbol': 'QPIKQ',
                 'value': {'amount': 54.99, 'currency': 'USD'}},
                {'id': 10010733, 'holdingType': 'moneyMarketFund', 'providerAccountId': 10012100, 'accountId': 10017272,
                 'createdDate': '2021-09-22T13:10:06Z', 'lastUpdated': '2021-10-18T23:21:44Z',
                 'description': 'FDIC INSURED DEPOSIT AT FIFTH THIRD IRA NOT COVERED BY SIPC', 'optionType': 'unknown',
                 'price': {'amount': 1.0, 'currency': 'USD'}, 'quantity': 37612.44, 'symbol': 'QPIKQ',
                 'value': {'amount': 37612.44, 'currency': 'USD'}}]}


TRANSACTIONS_MOCK_DATA = {'transaction': [
                {'CONTAINER': 'bank', 'id': 10302155, 'amount': {'amount': 59.69, 'currency': 'USD'},
                 'baseType': 'DEBIT', 'categoryType': 'EXPENSE', 'categoryId': 20, 'category': 'Personal/Family',
                 'detailCategoryId': 1527, 'categorySource': 'SYSTEM', 'highLevelCategoryId': 10000010,
                 'createdDate': '2021-09-22T13:09:56Z', 'lastUpdated': '2021-09-22T13:09:56Z',
                 'description': {'original': '#7 DELLARIA SALONS  S BROOKLINE MA',
                                 'simple': '#7 DELLARIA SALONS S BROOKLINE MA'}, 'type': 'PURCHASE',
                 'subType': 'PURCHASE', 'isManual': False, 'sourceType': 'AGGREGATED', 'date': '2021-08-25',
                 'transactionDate': '2021-08-25', 'postDate': '2021-08-25', 'status': 'POSTED', 'accountId': 10017268,
                 'runningBalance': {'amount': 167757.58, 'currency': 'USD'}, 'checkNumber': '998',
                 'merchant': {'id': '10015393', 'source': 'YODLEE', 'categoryLabel': ['Retail', ' Department Stores'],
                              'address': {'country': 'UK'}}},
                {'CONTAINER': 'bank', 'id': 10302170, 'amount': {'amount': 1303.76, 'currency': 'USD'},
                 'baseType': 'CREDIT', 'categoryType': 'INCOME', 'categoryId': 227, 'category': 'Refunds/Adjustments',
                 'detailCategoryId': 1188, 'categorySource': 'SYSTEM', 'highLevelCategoryId': 10000019,
                 'createdDate': '2021-09-22T13:09:56Z', 'lastUpdated': '2021-09-22T13:09:56Z',
                 'description': {'original': 'XXX15 - GREENWAY SEL CHICAGO IL REF# XXXXXXXXX XXXXXX2000',
                                 'simple': 'XX15 - GREENWAY SEL CHICAGO IL REF# XX2000'}, 'type': 'REFUND',
                 'subType': 'REFUND', 'isManual': False, 'sourceType': 'AGGREGATED', 'date': '2021-08-24',
                 'transactionDate': '2021-08-24', 'postDate': '2021-08-24', 'status': 'POSTED', 'accountId': 10017269,
                 'runningBalance': {'amount': 161056.7, 'currency': 'USD'}, 'checkNumber': '998',
                 'merchant': {'id': '10015393', 'source': 'YODLEE', 'categoryLabel': ['Retail', ' Department Stores'],
                              'address': {'country': 'UK'}}},
                {'CONTAINER': 'bank', 'id': 10302169, 'amount': {'amount': 144.51, 'currency': 'USD'},
                 'baseType': 'DEBIT', 'categoryType': 'EXPENSE', 'categoryId': 23, 'category': 'Travel',
                 'detailCategoryId': 1686, 'categorySource': 'SYSTEM', 'highLevelCategoryId': 10000011,
                 'createdDate': '2021-09-22T13:09:56Z', 'lastUpdated': '2021-09-22T13:09:56Z',
                 'description': {'original': '1256 DOWNEAST PARK CIT PARK CITY UT',
                                 'simple': '1256 DOWNEAST PARK CIT PARK CITY UT'}, 'type': 'PURCHASE',
                 'subType': 'PURCHASE', 'isManual': False, 'sourceType': 'AGGREGATED', 'date': '2021-08-24',
                 'transactionDate': '2021-08-24', 'postDate': '2021-08-24', 'status': 'POSTED', 'accountId': 10017269,
                 'runningBalance': {'amount': 159752.94, 'currency': 'USD'}, 'checkNumber': '998',
                 'merchant': {'id': '10017962', 'source': 'YODLEE',
                              'categoryLabel': ['Retail', ' Fashion', ' Clothing and Accessories'],
                              'address': {'city': 'Garden City', 'country': 'UK'}}}]}

def format_balances_response(response):
    data = {}

    try:
        for account in response['account']:
            data[account['id']] = {"providerName": account["providerName"], "balanceData": account["balance"]}

        return {'status': 'success', 'content': data}
    except:
        # return an error if it has occured
        return {'status': 'failed', 'content': f"Error: {response['errorMessage']}"}


def format_holdings_response(response):
    data = {}

    try:
        if not response.get('holding'):
            return {'status': 'failed', 'content': "Error: no holdings found"}

        for holding in response['holding']:
            if holding.get('symbol') and holding.get('value'):
                data[holding['id']] = {'symbol': holding['symbol'], 'quantity': holding['quantity'],
                                        'value': holding['value']}
            elif holding.get('description') and holding.get('value'):
                data[holding['id']] = {'symbol': holding['description'], 'quantity': holding['quantity'], 'value': holding['value']}
        return {'status': 'success', 'content': data}

    except:
        # return an error if it has occured
        return {'status': 'failed', 'content': f"Error: {response['errorMessage']}"}


def format_transactions_response(response):
    try:
        transactions = response["transaction"]
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

def get_access_token(loginName):
    if USE_MOCK == 'True':
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


async def get_balances(loginName, session):
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        # set up header data for the request
        if USE_MOCK != 'True':
            headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}

            # send the request and save the balance for each account
            async with session.get(URL + 'accounts', headers=headers, ssl=False) as resp:
                awaited = await resp.json()
                return format_balances_response(awaited)

        else:
            response = BALANCES_MOCK_DATA
            return format_balances_response(response)

    else:
        return access_token


async def get_transactions(loginName, session, account):
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token['status'] == 'success':
        if USE_MOCK != 'True':
            # set up header data and query parameters for the request
            headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}
            params = {'top': 10, 'fromDate': '2013-12-12', 'accountId': account}

            # send the request and save the balance for each account
            async with session.get(URL + 'transactions', headers=headers, params=params, ssl=False) as resp:
                awaited = await resp.json()
                return format_transactions_response(awaited)

        else:
            response = TRANSACTIONS_MOCK_DATA
            return format_transactions_response(response)
        
    else:
        return access_token


async def get_holdings(loginName, session):
    if not loginName: return {'status': 'failed', 'content': 'Error: no Yodlee loginName was provided'}

    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)

    if access_token['status'] == 'success':
        # set up header data for the request
        if USE_MOCK != 'True':
            headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token['content']}

            # send the request and save the balance for each account
            async with session.get(URL + 'holdings', headers=headers, ssl=False) as resp:
                awaited = await resp.json()
                return format_holdings_response(awaited)

        else:
            response = HOLDINGS_MOCK_DATA
            return format_holdings_response(response)

    else:
        return access_token
