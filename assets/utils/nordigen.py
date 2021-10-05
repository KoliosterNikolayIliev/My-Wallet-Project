import requests

headers = {'Authorization': 'Token 201ad808f1e2dd3136777f56db2568a08fbfc219'}


def validate_requisition(requisition_id):
    if not requisition_id:
        return {'message': 'Nordigen requisition key was not provided'}, False

    response = requests.get(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/', headers=headers)

    if response.status_code != 200:
        return response.json(), False

    return response.json(), True


def get_bank_accounts(requisition_id):
    requisition = validate_requisition(requisition_id)

    if not requisition[1]:
        return requisition[0], False

    requisition = requisition[0]

    accounts = requisition.get('accounts')

    if not accounts:
        return {'message': 'No bank accounts'}, False

    return accounts, True


def get_account_balances(requisition_id):
    accounts = get_bank_accounts(requisition_id)

    if not accounts[1]:
        return accounts[0]

    accounts = accounts[0]

    data = {}
    for account in accounts:
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/balances/', headers=headers)
        data[account] = response.json().get('balances')[0]

    return data


def get_account_transactions(requisition_id):
    accounts = get_bank_accounts(requisition_id)

    if not accounts[1]:
        return accounts[0]

    accounts = accounts[0]

    data = {}
    for account in accounts:
        response = requests.get(f'https://ob.nordigen.com/api/accounts/{account}/transactions/', headers=headers)
        data[account] = response.json().get('transactions').get('booked')

    return data

