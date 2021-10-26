import os
from binance.spot import Spot
import uuid, hmac, time, hashlib

USE_MOCK = os.environ.get('ASSETS_USE_MOCK')

MOCK_BALANCES_DATA = {'balances': [{'asset': 'BTC', 'free': '0.00069389', 'locked': '0.00000000'},
                                   {'asset': 'LTC', 'free': '0.00000000', 'locked': '0.00000000'},
                                   {'asset': 'ETH', 'free': '0.00590000', 'locked': '0.00000000'},
                                   {'asset': 'NEO', 'free': '0.00000000', 'locked': '0.00000000'},
                                   {'asset': 'BNB', 'free': '0.00238492', 'locked': '0.00000000'},
                                   ]}


def format_balances_response(balances):
    data = {}

    try:
        for balance in balances['balances']:
            id = uuid.uuid4().int
            # check where the current user balance is more than 0
            if float(balance['free']) > 0:
                # save crypto type with balance
                data[id] = {"symbol": balance["asset"], "quantity": balance['free']}
    except:
        data = {'status': 'failed', 'content': 'Error: invalid API key or secret'}
    return data


async def get_balances(api_key, api_secret, session):
    if not api_key or not api_secret:
        # return false bool to say the validation failed and the error message
        return {'status': 'failed', 'content': 'Error: API key or API secret was not provided'}

    if USE_MOCK != 'True':
        # gets all balances assets
        timestamp = int(time.time() * 1000)
        signature = hmac.new(api_secret.encode(), f'timestamp={timestamp}'.encode(), hashlib.sha256).hexdigest()
        headers = {'X-MBX-APIKEY': api_key}
        params = {'timestamp': timestamp, 'signature': signature}
        URL = 'https://api.binance.com/api/v3/account'

        async with session.get(URL, headers=headers, params=params) as response:
            awaited = await response.json()
            data = format_balances_response(awaited)
            return data

    else:
        balances = MOCK_BALANCES_DATA

    data = format_balances_response(balances)

    return {'status': 'success', 'content': data}
