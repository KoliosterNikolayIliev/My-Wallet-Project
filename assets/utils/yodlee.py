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
    response = requests.post(URL + 'auth/token', data=data, headers=headers)
    return response.json()['token']['accessToken']