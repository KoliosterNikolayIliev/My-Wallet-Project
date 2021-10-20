import uuid, os, requests

URL = os.environ.get('CUSTOM_ASSETS_URL')


def get_holdings(user_key):
    if not user_key:
        return {'status': 'failed', 'content': 'Error: key was not provided'}

    headers = {'user-key': user_key}

    if os.environ.get('USE_MOCK') != 'True':
        try:
            response = requests.get(URL, headers=headers)
        except:
            return {'status': 'failed', 'content': 'Error: connection error'}

        if not response.json():
            return {'status': 'failed', 'content': 'Error: no data'}

        if response.status_code == 400:
            return {'status': 'failed', 'content': "Error: user doesn't exist"}

        response = response.json()

    else:
        response = {'crypto_assets': [{'type': 'BTC', 'amount': 2.0}], 'stock_assets': [{'type': 'TSLA', 'amount': 3}],
                    'currency_assets': [{'type': 'BGN', 'amount': 20.0}, {'type': 'EUR', 'amount': 20.0}]}

    data = {}
    try:
        for assets in response.values():
            for asset in assets:
                # generate a random id for the asset
                id = uuid.uuid4().int
                data[id] = {'symbol': asset['type'], 'quantity': asset['amount']}
    except:
        return {'status': 'failed', 'content': 'Error: unknown error'}

    return {'status': 'success', 'content': data}
