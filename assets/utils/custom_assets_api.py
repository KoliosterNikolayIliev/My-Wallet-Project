import uuid, os, requests

URL = os.environ.get('CUSTOM_ASSETS_URL')

def get_holdings(user_key):
    headers = {'user-key': user_key}
    
    try:
        response = requests.get(URL, headers=headers)
    except:
        return {'status': 'failed', 'content': 'Error: connection error'}
    
    if not response.json():
        return {'status': 'failed', 'content': 'Error: no data'}

    if response.status_code == 400:
        return {'status': 'failed', 'content': "Error: user doesn't exist"}

    data = {}
    try:
        for assets in response.json().values():
            for asset in assets:
                # generate a random id for the asset
                id = uuid.uuid4().int
                data[id] = {'symbol': asset['type'], 'quantity': asset['amount']}
    except:
        return {'status': 'failed', 'content': 'Error: unknown error'}
    
    return {'status': 'success', 'content': data}
    