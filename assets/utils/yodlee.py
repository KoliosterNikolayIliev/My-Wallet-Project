import requests, os

"""
    explain how the whole thing works
 """

# get yodlee developer credentials from .env file
CLIENT_ID = ''
SECRET = ''

URL = "https://sandbox.api.yodlee.uk/ysl/"

def get_access_token(loginName):
    data = {'clientId': CLIENT_ID, 'secret': SECRET}
    headers = {'Api-Version': '1.1', 'loginName': loginName}
    try:
        response = requests.post(URL + 'auth/token', data=data, headers=headers)
        return response.json()['token']['accessToken']
    except:
        return response.json()['errorMessage']

def get_balances(loginName):
    data = {}
    try:
        headers = {'Api-Version': '1.1', 'Authorization': 'Bearer ' + get_access_token(loginName)}
        response = requests.get(URL + 'accounts', headers=headers)
        for account in response.json()['account']:
            data[account['accountName']] = account['balance']
        return data
    except:
        return 'An error occured'