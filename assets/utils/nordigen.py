import os

import requests
from os import environ

token = environ.get('NORDIGEN_TOKEN')
headers = {'Authorization': f'Token {token}'}


def get_bank_name(account_id):
    # get the bank identifier from nordigen
    account_response = requests.get(f'https://ob.nordigen.com/api/accounts/{account_id}/', headers=headers)
    identifier = account_response.json()["aspsp_identifier"]

    # get the bank name using the identifier
    bank_response = requests.get(f'https://ob.nordigen.com/api/aspsps/{identifier}/', headers=headers)

    return bank_response.json()["name"]


def validate_requisition(requisition_id):
    if not requisition_id:
        # return error message with false variable to say validation failed
        return {'status': 'failed', 'content': 'Error: Nordigen requisition key was not provided'}, False

    response = requests.get(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/', headers=headers)

    # Check if requisition exist
    if response.status_code != 200:
        # return response error message with false variable to say validation failed
        return {'status': 'failed', 'content': 'Error: Nordigen requisition key is invalid'}, False

    # return json response with true variable to say validation is success
    return {'status': 'success', 'content': response.json()}, True


def get_bank_accounts(requisition_id):
    # validate requisition
    requisition = validate_requisition(requisition_id)

    # check requisition validation
    if not requisition[1]:
        # return the error message with false variable to say validation failed
        return requisition[0], False

    # if requisition is valid we take the requisition
    requisition = requisition[0]['content']

    # get user all accounts
    accounts = requisition.get('accounts')

    if not accounts:
        # if user don't have accounts returns message with false variable to say user don't have accounts
        return {'status': 'failed', 'content': 'Error: no bank accounts'}, False

    # return all user account with true variable to say that he has accounts
    return {'status': 'success', 'content': accounts}, True


def get_account_balances(requisition_id):
    if os.environ.get('USE_MOCK') == 'True':
        return {
            "status": "success",
            "content": {
                "582a6ea9-81c7-4def-952d-85709d9432cf": {
                    "providerName": "Sandbox Finance",
                    "balanceData": {
                        "amount": "1913.12",
                        "currency": "EUR"
                    }
                },
                "1048f194-cb13-4cee-a55c-5ef6d8661341": {
                    "providerName": "Sandbox Finance",
                    "balanceData": {
                        "amount": "1913.12",
                        "currency": "EUR"
                    }
                }
            }
        }
    # get user bank accounts from requisition
    accounts = get_bank_accounts(requisition_id)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}

    # loop through all user bank accounts
    for account in accounts:
        # get the name of the bank that the account belongs to
        bank_name = get_bank_name(account)

        # request to get account balance data
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/balances/', headers=headers)

        # save only authorised balance
        data[account] = {"providerName": bank_name, "balanceData": response.json()["balances"][0]["balanceAmount"]}

    # return saved data
    return {'status': 'success', 'content': data}


def get_account_transactions(requisition_id):
    if os.environ.get('USE_MOCK') == 'True':
        return {
            "status": "success",
            "content": {
                "Sandbox Finance": {
                    "2021101702698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101702698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101702698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101702698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101702698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101702698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101602698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101602698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101602698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101602698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101602698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101602698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101502698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101502698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101502698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101502698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101502698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101502698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101402698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101402698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101402698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101402698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101402698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101402698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101302698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101302698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101302698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101302698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101302698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101302698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101202698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101202698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101202698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101202698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101202698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101202698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101102698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101102698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101102698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101102698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101102698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101102698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101002698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101002698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101002698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101002698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021101002698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021101002698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100902698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100902698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100902698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100902698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100902698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100902698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100802698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100802698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100802698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100802698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100802698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100802698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100702698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100702698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100702698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100702698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100702698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100702698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100602698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100602698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100602698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100602698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100602698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100602698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100502698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100502698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100502698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100502698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100502698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100502698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100402698005-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100402698004-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100402698008-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    },
                    "2021100402698007-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100402698001-1": {
                        "amount": "45.00",
                        "currency": "EUR"
                    },
                    "2021100402698002-1": {
                        "amount": "-15.00",
                        "currency": "EUR"
                    }
                }
            }
        }

    # get user bank accounts from requisition
    accounts = get_bank_accounts(requisition_id)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}
    for account in accounts:
        transaction_data = {}
        # get the name of the bank that the account belongs to
        bank_name = get_bank_name(account)

        # request to get account transaction history data
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/transactions/', headers=headers)

        # save only booked transactions
        transactions = response.json().get('transactions').get('booked')

        # add each transaction to the data
        for transaction in transactions:
            transaction_data[transaction["transactionId"]] = transaction["transactionAmount"]

        data[bank_name] = transaction_data

    # return saved data
    return {'status': 'success', 'content': data}
