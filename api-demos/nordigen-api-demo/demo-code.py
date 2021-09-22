import requests
import uuid

headers = {'Authorization': 'Token 201ad808f1e2dd3136777f56db2568a08fbfc219'}


# returns json of all banks in the given country
def get_banks_by_country(country):
    response = requests.get(f'https://ob.nordigen.com/api/aspsps/?country={country}', headers=headers)
    return response.json()


# returns the bank with the given id
def get_bank_by_id(bank_id):
    response = requests.get(f'https://ob.nordigen.com/api/aspsps/{bank_id}', headers=headers)
    return response.json()


def create_end_user_agreement(max_historical_days, enduser_id, aspsp_id):
    """
    Use this step only if you want to specify the length of transaction history you want to retrieve.
     If you skip this step, by default 90 days of transaction history will be retrieved.

    :param max_historical_days: is the length of the transaction history to be retrieved, default is 90 days
    :param enduser_id: is a unique end-user ID of someone who's using your services. Usually, it's UUID
    :param aspsp_id: is the an id of a bank
    """

    data = {'max_historical_days': max_historical_days, 'enduser_id': enduser_id, 'aspsp_id': aspsp_id}
    response = requests.post('https://ob.nordigen.com/api/agreements/enduser/', headers=headers, data=data)
    return response.json()


def create_requisition(enduser_id, reference, redirect, agreements, user_language=''):
    """
    requisition is a collection of inputs for creating links and retrieving accounts.
    For requisition API requests you will need to provide

    :param enduser_id: if you made an user agreement the id should be the same as the user agreement
    :param reference: additional layer of unique ID defined by you
    :param redirect: URL where the end user will be redirected after finishing authentication in ASPSP
    :param agreements: is an array of ID(s) from user agreement or an empty array if you didn't create
    :param user_language: optional
    :return:
    """

    data = {
        'enduser_id': enduser_id,
        'reference': reference,
        'redirect': redirect,
        'agreements': agreements,
        'user_language': user_language
    }

    response = requests.post('https://ob.nordigen.com/api/requisitions/', headers=headers, data=data)
    return response.json()


# this is will build a link for authentication in ASPSP
def build_link(requisition_id, aspsp_id):
    data = {
        'aspsp_id': aspsp_id
    }

    response = requests.post(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/links/', headers=headers,
                             data=data)
    return response.json()


# the user's bank accounts can be listed. Pass the requisition ID to view the accounts.
def list_accounts(requisition_id):
    response = requests.get(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/', headers=headers)
    return response.json()



"""
How to use nordigen api:
step 1: Get Access Token - https://ob.nordigen.com/
step 2: Choose a Bank - use get_banks_by_country() function to chose available banks.
step 3: Create an end-user agreement - (optional) if you want more than 90 transaction history days
use create_end_user_agreement() function
step 4: Create a requisition - user create_requisition function
step 5: Build a Link - when you created requisition you can build a link for authentication in ASPSP use
build_link() function
step 6: Access accounts - when you connected an account when you use list_accounts() function with the requisition_id
that you created you should see a accounts id's
step 7: Now when you connected an bank account you can use the functions bellow to get the data you need.
"""


def get_account_metadata(account_id):
    response = requests.get(f'https://ob.nordigen.com/api/accounts/{account_id}/', headers=headers)
    return response.json()


def get_account_balances(account_id):
    response = requests.get(f'https://ob.nordigen.com/api/accounts/{account_id}/balances/', headers=headers)
    return response.json()


def get_account_details(account_id):
    response = requests.get(f'https://ob.nordigen.com/api/accounts/{account_id}/details/', headers=headers)
    return response.json()


def get_account_transactions(account_id):
    response = requests.get(f'https://ob.nordigen.com/api/accounts/{account_id}/transactions/', headers=headers)
    return response.json()
