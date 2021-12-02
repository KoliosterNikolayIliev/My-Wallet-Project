import requests, os

URL = os.environ.get("PORTFOLIO_CUSTOM_ASSETS_URL")


def create_asset(key, type, symbol, amount):
    body = {'type': symbol, 'amount': amount, "user-key": key}
    response = requests.post(f"{URL}api/{type}/", data=body)
    return response.json()