import asyncio
import os

TOKEN = os.environ.get('ASSETS_NORDIGEN_TOKEN')
USE_MOCK = os.environ.get('ASSETS_USE_MOCK')


MOCK_REQUISITION_DATA = {
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

headers = {'Authorization': f'Token {TOKEN}'}

async def get_bank_name(account_id, session):
    if USE_MOCK == 'True':
        return 'Sandbox Finance'

    async with session.get(f'https://ob.nordigen.com/api/accounts/{account_id}/', headers=headers) as response:
        awaited = await response.json()
        identifier = awaited["aspsp_identifier"]
        async with session.get(f'https://ob.nordigen.com/api/aspsps/{identifier}/', headers=headers) as response:
            awaited = await response.json()
            return awaited["name"]


async def validate_requisition(requisition_id, session):
    if not requisition_id:
        # return error message with false variable to say validation failed
        return {'status': 'failed', 'content': 'Error: Nordigen requisition key was not provided'}, False

    if USE_MOCK == 'True':
        mock_requisition = MOCK_REQUISITION_DATA

        return {'status': 'success', 'content': mock_requisition}, True

    async with session.get(f'https://ob.nordigen.com/api/requisitions/{requisition_id}/', headers=headers) as response:
        awaited = await response.json()

        # Check if requisition exist
        if awaited.get('status_code'):
            # return response error message with false variable to say validation failed
            return {'status': 'failed', 'content': 'Error: Nordigen requisition key is invalid'}, False

        # return json response with true variable to say validation is success
        return {'status': 'success', 'content': awaited}, True

async def get_bank_accounts(requisition_id, session):
    # validate requisition
    requisition = await validate_requisition(requisition_id, session)

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

async def get_single_account_balance(account, headers, session):
    bank_name = await get_bank_name(account, session)

    async with session.get(f'https://ob.nordigen.com/api/accounts/{account}/balances/', headers=headers) as response:
        awaited = await response.json()
        return {"id": account, "providerName": bank_name, "balanceData": awaited["balances"][0]["balanceAmount"]}

async def get_single_account_transactions(account, headers, session):
    bank_name = await get_bank_name(account, session)
    transaction_data = {}

    if USE_MOCK != 'True':
        async with session.get(f'https://ob.nordigen.com/api/accounts/{account}/transactions/', headers=headers) as response:
            transactions = await response.json()

    else:
        transactions = MOCK_TRANSACTIONS_DATA

    transactions = transactions.get('transactions').get('booked')

    for transaction in transactions:
        transaction_data[transaction["transactionId"]] = transaction["transactionAmount"]

    return {"bankName": bank_name, "transactions": transaction_data}


async def get_all_account_balances(requisition_id, session, tasks):
    # get user bank accounts from requisition
    accounts = await get_bank_accounts(requisition_id, session)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}
    if USE_MOCK == 'True':
        for account in accounts:
            response = MOCK_BALANCES_DATA
            data[response["id"]] = {"providerName": response["providerName"], "balanceData": response["balanceData"]}
    else:
        for account in accounts:
            tasks.append(asyncio.ensure_future(get_single_account_balance(account, headers, session)))
                
        responses = await asyncio.gather(*tasks)
        for response in responses:
            data[response["id"]] = {"providerName": response["providerName"], "balanceData": response["balanceData"]}

    return {"status": "success", "content": data}

    # # loop through all user bank accounts



async def get_account_transactions(requisition_id, session, tasks):
    # get user bank accounts from requisition
    accounts = await get_bank_accounts(requisition_id, session)

    # check requisition validation and check if user has bank accounts
    if not accounts[1]:
        # return error message
        return accounts[0]

    # if requisition is valid and user has bank accounts we take his accounts
    accounts = accounts[0]['content']

    data = {}
    for account in accounts:
        # request to get account transaction history data
        tasks.append(asyncio.ensure_future(get_single_account_transactions(account, headers, session)))

    responses = await asyncio.gather(*tasks)
    for response in responses:
        data[response["bankName"]] = response["transactions"]

    # return saved data
    return {'status': 'success', 'content': data}
