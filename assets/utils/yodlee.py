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
"""

# get yodlee developer credentials from .env file
CLIENT_ID = os.environ.get('YODLEE_CLIENT_ID')
SECRET = os.environ.get('YODLEE_SECRET')

URL = "https://sandbox.api.yodlee.uk/ysl/"

def get_access_token(loginName):
    # set up x-www-form-urlencoded data and header data for the request
    data = {'clientId': CLIENT_ID, 'secret': SECRET}
    headers = {'Api-Version': '1.1', 'loginName': loginName}
    try:
        # send the request and return the access token
        response = requests.post(URL + 'auth/token', data=data, headers=headers)
        return response.json()['token']['accessToken']
    except:
        # return an error if it has occured
        return 'An error occured'

def get_balances(loginName):
    data = {}
    # try to obtain a token and return an error if it fails
    access_token = get_access_token(loginName)
    if access_token != 'An error occured':
        try:
            # set up header data for the request
            headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + access_token}
            # send the request and save the balance for each account
            response = requests.get(URL + 'accounts', headers=headers)
            for account in response.json()['account']:
                data[account['accountName']] = account['balance']
            return data
        except:
            # return an error if it has occured
            return 'An error occured'
    else:
        return 'An error occured'