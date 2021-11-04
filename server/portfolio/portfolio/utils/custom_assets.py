import requests

def create_asset(key, type, symbol, amount):
    body = {'type': symbol, 'amount': amount, "user-key": key}
    response = requests.get(f"http://localhost:8000/api/{type}", body=body).json()

    return response