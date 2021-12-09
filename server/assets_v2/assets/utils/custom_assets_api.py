import uuid, os, requests

MOCK_ASSETS_DATA = {'crypto_assets': [{'type': 'BTC', 'amount': 2.0, 'asset_type': 'crypto'}],
                    'stock_assets': [{'type': 'TSLA', 'amount': 3, 'asset_type': 'stock'}],
                    'currency_assets': [
                        {'type': 'BGN', 'amount': 20.0, 'asset_type': 'currency'},
                        {'type': 'EUR', 'amount': 20.0, 'asset_type': 'currency'}
                        ]}

URL = os.environ.get('ASSETS_CUSTOM_ASSETS_URL')
USE_MOCK = os.environ.get('ASSETS_USE_MOCK')

def format_holdings_response(response):
    data = {}
    try:
        for assets in response.values():
            if assets is not None:
                for asset in assets:
                    # generate a random id for the asset
                    id = uuid.uuid4().int
                    data[id] = {'symbol': asset['type'], 'quantity': asset['amount'], 'asset_type': asset['asset_type']}
    except:
        return {'status': 'failed', 'content': 'Error: unknown error'}

    return {'status': 'success', 'content': data}

async def get_holdings(user_key, session):
    if not user_key:
        return {'status': 'failed', 'content': 'Error: key was not provided'}

    headers = {'user-key': user_key}

    if USE_MOCK != 'True':
        try:
            async with session.get(URL, headers=headers) as response:
                awaited = await response.json()
                return format_holdings_response(awaited)
        except:
            return {'status': 'failed', 'content': 'Error: connection error'}

    else:
        return format_holdings_response(MOCK_ASSETS_DATA)

   
