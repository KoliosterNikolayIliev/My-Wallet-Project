import asyncio
import os

import requests

from assets.utils.measure_time import MeasuredScope

SECRET_ID = os.environ.get('ASSETS_NORDIGEN_ID')
SECRET_KEY = os.environ.get('ASSETS_NORDIGEN_KEY')
USE_MOCK = os.environ.get('ASSETS_USE_MOCK')
URL = 'https://ob.nordigen.com/api/v2/'

MOCK_REQUISITION_DATA = {
    "id": "0b998971-3726-4bc9-991a-d38dfe3be60e",
    "created": "2021-10-27T09:01:54.145314Z",
    "redirect": "https://google.com",
    "status": "LN",
    "institution_id": "SANDBOXFINANCE_SFIN0000",
    "agreement": "0a871d7c-6131-45b5-80cb-12b863df8a43",
    "reference": "0b998971-3726-4bc9-991a-d38dfe3be60e",
    "accounts": [
        "1048f194-cb13-4cee-a55c-5ef6d8661341",
        "582a6ea9-81c7-4def-952d-85709d9432cf"
    ],
    "link": "https://ob.nordigen.com/psd2/start/0b998971-3726-4bc9-991a-d38dfe3be60e/SANDBOXFINANCE_SFIN0000"
}

MOCK_BALANCES_DATA = {
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

MOCK_TRANSACTIONS_DATA = {
    "transactions": {
        "booked": [
            {
                "bankTransactionCode": "PMNT",
                "bookingDate": "2021-10-26",
                "remittanceInformationUnstructured": "PAYMENT Alderaan Coffe",
                "transactionAmount": {
                    "amount": "-15.00",
                    "currency": "EUR"
                },
                "transactionId": "2021102602749508-1",
                "valueDate": "2021-10-26"
            },
            {
                "bankTransactionCode": "PMNT",
                "bookingDate": "2021-10-26",
                "debtorAccount": {
                    "iban": "GL11SAFI05510125926"
                },
                "debtorName": "MON MOTHMA",
                "remittanceInformationUnstructured": "For the support of Restoration of the Republic foundation",
                "transactionAmount": {
                    "amount": "45.00",
                    "currency": "EUR"
                },
                "transactionId": "2021102602749501-1",
                "valueDate": "2021-10-26"
            },
            {
                "bankTransactionCode": "PMNT",
                "bookingDate": "2021-10-26",
                "debtorAccount": {
                    "iban": "GL11SAFI05510125926"
                },
                "debtorName": "MON MOTHMA",
                "remittanceInformationUnstructured": "For the support of Restoration of the Republic foundation",
                "transactionAmount": {
                    "amount": "45.00",
                    "currency": "EUR"
                },
                "transactionId": "2021102602749507-1",
                "valueDate": "2021-10-26"
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


async def get_access_token(session):
    async with session.post(URL + 'token/new/', data={'secret_id': SECRET_ID, 'secret_key': SECRET_KEY}) as res:
        response = await res.json()
        status_code = res.status

    if status_code != 200:
        return {'status': 'failed', 'content': response['detail']}

    else:
        return {'status': 'success', 'content': response['access']}


async def get_bank_name(account_id, session, headers):
    if USE_MOCK == 'True':
        return 'Sandbox Finance'

    async with session.get(URL + f'accounts/{account_id}/', headers=headers) as response:
        awaited = await response.json()

        if awaited.get('status_code'):
            return False

    identifier = awaited["institution_id"]
    async with session.get(URL + f'institutions/{identifier}/', headers=headers) as response:
        awaited = await response.json()
        return awaited["name"]


async def validate_requisition(requisition_id, session, headers):
    if not requisition_id:
        # return error message with false variable to say validation failed
        return {'status': 'failed', 'content': 'Error: Nordigen requisition key was not provided'}, False

    if USE_MOCK == 'True':
        mock_requisition = MOCK_REQUISITION_DATA

        return {'status': 'success', 'content': mock_requisition}, True

    async with session.get(URL + f'requisitions/{requisition_id}/', headers=headers) as response:
        awaited = await response.json()

        # Check if requisition exist
        if awaited.get('status_code'):
            # return response error message with false variable to say validation failed
            return {'status': 'failed', 'content': 'Error: Nordigen requisition key is invalid'}, False

        # return json response with true variable to say validation is success
        return {'status': 'success', 'content': awaited}, True


async def get_bank_accounts(requisition_id, session, headers):
    # validate requisition
    requisition = await validate_requisition(requisition_id, session, headers)

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


async def get_single_account_details(account, headers, session):
    async with session.get(URL + f'accounts/{account}/details', headers=headers) as response:
        awaited = await response.json()
    
    return awaited


async def get_single_account_balance(account, headers, session):
    bank_name = await get_bank_name(account, session, headers)

    if USE_MOCK != 'True':
        async with session.get(URL + f'accounts/{account}/balances/',
                               headers=headers) as response:
            balance_data = await response.json()
    else:
        balance_data = MOCK_BALANCES_DATA
    
    details = await get_single_account_details(account, headers, session)
    if details.get('account'):
        if details['account'].get('product'):
            details = details['account']['product']
        elif details['account'].get('name'):
            details = details['account']['name']
        else:
            details = None

    return {"id": account, "providerName": bank_name, "balanceData": balance_data["balances"][0]["balanceAmount"], "accountType": details}


async def get_all_account_balances(requisition_id, session, headers):
    # get user bank accounts from requisition
    accounts = await get_bank_accounts(requisition_id, session, headers)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}
    tasks = []
    for account in accounts:
        tasks.append(asyncio.ensure_future(get_single_account_balance(account, headers, session)))

    responses = await asyncio.gather(*tasks)
    for response in responses:
        data[response["id"]] = {"providerName": response["providerName"], "balanceData": response["balanceData"], "accountType": response["accountType"]}

    return {"status": "success", "content": data}



async def get_account_transactions(account, session):
    response = await get_access_token(session)

    if response['status'] != 'success':
        return response

    headers = {'Authorization': f'Bearer {response["content"]}'}

    bank_name = await get_bank_name(account, session, headers)
    if not bank_name:
        return {'status': 'failed', 'content': 'invalid account'}

    transaction_data = {}

    if USE_MOCK != 'True':
        async with session.get(URL + f'accounts/{account}/transactions/',
                               headers=headers) as response:
            transactions = await response.json()

    else:
        transactions = MOCK_TRANSACTIONS_DATA

    transactions = transactions.get('transactions').get('booked')

    for transaction in transactions:
        transaction_data[transaction["transactionId"]] = transaction["transactionAmount"]

    data = {bank_name: transaction_data}

    # return saved data
    return {'status': 'success', 'content': data}


async def get_all_accounts_balances(requisitions, session):
    total_time = MeasuredScope('nordigen')
    if not requisitions:
        return {
            'status': 'failed',
            'content': 'Error: list of nordigen requisition id\'s was not provided'
        }

    response = await get_access_token(session)

    if response['status'] != 'success':
        return response

    headers = {'Authorization': f'Bearer {response["content"]}'}

    tasks = []
    for requisition in requisitions:
        tasks.append(asyncio.ensure_future(
            get_all_account_balances(requisition, session=session, headers=headers)))

    responses = await asyncio.gather(*tasks)
    data = {}

    for response in responses:
        if response['status'] == 'success':
            data.update(response['content'])

    del total_time
    if data:
        return {'status': 'success', 'content': data}

    return {'status': 'failed', 'content': 'Error: there are no valid requisition id\'s'}
