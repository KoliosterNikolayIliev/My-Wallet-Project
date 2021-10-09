import requests, os

URL = os.environ.get("ACCOUNT_URL")

def validate_token(token):
    headers = {'Authorization': token}
    res = requests.get(URL + "api/account/user", headers=headers)
    if res.status_code == 200:
        return res.json()
    return False
