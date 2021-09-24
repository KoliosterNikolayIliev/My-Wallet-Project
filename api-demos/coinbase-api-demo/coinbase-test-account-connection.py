"""
Not ready. Needs some more time.
"""

import cbpro

import access_data

import json

api_secret = access_data.api_secret_acc
api_key = access_data.api_key_acc
api_pass = access_data.api_pass_acc
url = 'https://api-public.sandbox.pro.coinbase.com'


auth_client = cbpro.AuthenticatedClient(api_key, api_secret, api_pass, api_url=url)

all_clients = auth_client.get_accounts()   # method to check all existing clients

"""
Our test client is with ID "b0f26bb3-17ed-4281-8cad-9068ea09a96c"
"""

test_client = 'b0f26bb3-17ed-4281-8cad-9068ea09a96c'


"""
Get all available information about the client.
"""

client_data = auth_client.get_account(test_client)
print(client_data)


"""
Get history with all clients orders. Returns an object.
"""
client_history = auth_client.get_account_history(test_client)
print(client_history)


"""
Check each individual oder from the history
"""
for each in client_history:
    print(json.dumps(each, indent=1))