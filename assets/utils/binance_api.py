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
