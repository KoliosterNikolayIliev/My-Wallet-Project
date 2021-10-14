import requests

headers = {'Authorization': 'Token 201ad808f1e2dd3136777f56db2568a08fbfc219'}


def validate_requisition(requisition_id):
    if not requisition_id:
        # return error message with false variable to say validation failed
        return 'Error: Nordigen requisition key was not provided', False

    response = requests.get(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/', headers=headers)

    # Check if requisition exist
    if response.status_code != 200:
        # return response error message with false variable to say validation failed
        return 'Error: Nordigen requisition key is invalid', False

    # return json response with true variable to say validation is success
    return response.json(), True


def get_bank_accounts(requisition_id):
    # validate requisition
    requisition = validate_requisition(requisition_id)

    # check requisition validation
    if not requisition[1]:
        # return the error message with false variable to say validation failed
        return requisition[0], False

    # if requisition is valid we take the requisition
    requisition = requisition[0]

    # get user all accounts
    accounts = requisition.get('accounts')

    if not accounts:
        # if user don't have accounts returns message with false variable to say user don't have accounts
        return 'Error: no bank accounts', False

    # return all user account with true variable to say that he has accounts
    return accounts, True


def get_account_balances(requisition_id):
    # get user bank accounts from requisition
    accounts = get_bank_accounts(requisition_id)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]

    data = {}

    # loop through all user bank accounts
    for account in accounts:
        # request to get account balance data
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/balances/', headers=headers)
        # save only authorised balance
        data[account] = response.json().get('balances')[0]

    # return saved data
    return data


def get_account_transactions(requisition_id):
    # get user bank accounts from requisition
    accounts = get_bank_accounts(requisition_id)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]

    data = {}
    for account in accounts:
        # request to get account transaction history data
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/transactions/', headers=headers)
        # save only booked transactions
        data[account] = response.json().get('transactions').get('booked')

    # return saved data
    return data
