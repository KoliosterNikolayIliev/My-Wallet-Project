import requests, os

URL = os.environ.get("ACCOUNT_URL")

def validate_token(token):
    headers = {'Authorization': token}
    res = requests.get("http://localhost:8001/api/account/internal/user", headers=headers)
    if res.status_code == 200:
        return res.json()
    return False

def validate_auth_header(token: None):
    if not token:
        return False, 'Error: No token provided'

    user_data = validate_token(token)
    if not user_data:
        return False, 'Error, Invalid token'

    return True, user_data