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
    # get user bank accounts from requisition
    accounts = get_bank_accounts(requisition_id)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}
    transaction_data = {}
    for account in accounts:
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
