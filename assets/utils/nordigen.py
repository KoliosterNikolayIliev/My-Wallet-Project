import os

import requests
from os import environ

token = environ.get('NORDIGEN_TOKEN')
headers = {'Authorization': f'Token {token}'}


def get_bank_name(account_id):
    if os.environ.get('USE_MOCK'):
        return 'Sandbox Finance'

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

    if os.environ.get('USE_MOCK') == 'True':
        mock_requisition = {
            "id": "c0ad1b3e-28e1-4628-b8b1-f6009df3c27f",
            "created": "2021-10-06T22:21:31.216413Z",
            "redirect": "https://test.com",
            "status": "LN",
            "agreements": [
                "f658eddc-2c4b-4f53-8c0d-1fb1995f327c"
            ],
            "accounts": [
                "1048f194-cb13-4cee-a55c-5ef6d8661341",
                "582a6ea9-81c7-4def-952d-85709d9432cf"
            ],
            "reference": "test",
            "enduser_id": "test"
        }
        return {'status': 'success', 'content': mock_requisition}, True

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
        if os.environ.get('USE_MOCK'):
            response = {
                "balances": [
                    {
                        "balanceAmount": {
                            "amount": "1913.12",
                            "currency": "EUR"
                        },
                        "balanceType": "authorised",
                        "referenceDate": "2021-10-19"
                    },
                    {
                        "balanceAmount": {
                            "amount": "1913.12",
                            "currency": "EUR"
                        },
                        "balanceType": "interimAvailable",
                        "referenceDate": "2021-10-19"
                    }
                ]
            }

        else:
            response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/balances/', headers=headers).json()

        # save only authorised balance
        data[account] = {"providerName": bank_name, "balanceData": response["balances"][0]["balanceAmount"]}

    # return saved data
    return {'status': 'success', 'content': data}


def get_account_transactions(requisition_id):
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
        if not os.environ.get('USE_MOCK'):
            response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/transactions/',
                                    headers=headers).json()

        else:
            response = {
                "transactions": {
                    "booked": [
                        {
                            "bankTransactionCode": "PMNT",
                            "bookingDate": "2021-10-08",
                            "debtorAccount": {
                                "iban": "GL11SAFI05510125926"
                            },
                            "debtorName": "MON MOTHMA",
                            "remittanceInformationUnstructured": "For the support of Restoration of the Republic foundation",
                            "transactionAmount": {
                                "amount": "45.00",
                                "currency": "EUR"
                            },
                            "transactionId": "2021100802749507-1",
                            "valueDate": "2021-10-08"
                        },
                        {
                            "bankTransactionCode": "PMNT",
                            "bookingDate": "2021-10-08",
                            "debtorAccount": {
                                "iban": "GL11SAFI05510125926"
                            },
                            "debtorName": "MON MOTHMA",
                            "remittanceInformationUnstructured": "For the support of Restoration of the Republic foundation",
                            "transactionAmount": {
                                "amount": "45.00",
                                "currency": "EUR"
                            },
                            "transactionId": "2021100802749501-1",
                            "valueDate": "2021-10-08"
                        },
                        {
                            "bankTransactionCode": "PMNT",
                            "bookingDate": "2021-10-08",
                            "remittanceInformationUnstructured": "PAYMENT Alderaan Coffe",
                            "transactionAmount": {
                                "amount": "-15.00",
                                "currency": "EUR"
                            },
                            "transactionId": "2021100802749505-1",
                            "valueDate": "2021-10-08"
                        }
                    ],
                    "pending": [
                        {
                            "valueDate": "2021-10-17",
                            "transactionAmount": {
                                "amount": "10.00",
                                "currency": "EUR"
                            },
                            "remittanceInformationUnstructured": "Reserved PAYMENT Emperor's Burgers"
                        }
                    ]
                }
            }

        # save only booked transactions
        transactions = response.get('transactions').get('booked')

        # add each transaction to the data
        for transaction in transactions:
            transaction_data[transaction["transactionId"]] = transaction["transactionAmount"]

        data[bank_name] = transaction_data

    # return saved data
    return {'status': 'success', 'content': data}
