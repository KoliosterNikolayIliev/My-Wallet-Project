import os

from binance.spot import Spot
import uuid


def validate_api_key_and_api_secret(api_key, api_secret):
    if not api_key or not api_secret:
        # return false bool to say the validation failed and the error message
        return False, {'status': 'failed', 'content': 'Error: API key or API secret was not provided'}

    client = Spot(api_key, api_secret)

    # try to make a request and if it fails it means the api key or api secret is invalid
    try:
        client.account()

    except:
        # return false bool to say the validation failed and the error message
        return False, {'status': 'failed', 'content': 'Error: API key or API secret is invalid'}

    # return true bool with comma to make it tuple
    return True,


def get_balances(api_key, api_secret):
    if os.environ.get('USE_MOCK') == 'True':
        return {
            "status": "success",
            "content": {
                "19713826504519158012514033432436410360": {
                    "symbol": "BTC",
                    "quantity": "0.00069389"
                },
                "312449119748704017695817878114511750902": {
                    "symbol": "ETH",
                    "quantity": "0.00590000"
                },
                "168431868865493663656248984534282715018": {
                    "symbol": "BNB",
                    "quantity": "0.00238492"
                },
                "64884506774569230777743708680327731544": {
                    "symbol": "ADA",
                    "quantity": "0.09267368"
                },
                "334804415272661327165161730551465081020": {
                    "symbol": "SOL",
                    "quantity": "0.16079883"
                }
            }
        }

    # check validation of api key and api secret
    validation = validate_api_key_and_api_secret(api_key, api_secret)

    if not validation[0]:
        # if validation failed we return the error message
        return validation[1]

    client = Spot(api_key, api_secret)
    # gets all balances assets
    balances = client.account().get('balances')

    data = {}

    for balance in balances:
        id = uuid.uuid4().int
        # check where the current user balance is more than 0
        if float(balance['free']) > 0:
            # save crypto type with balance
            data[id] = {"symbol": balance["asset"], "quantity": balance['free']}

    return {'status': 'success', 'content': data}
