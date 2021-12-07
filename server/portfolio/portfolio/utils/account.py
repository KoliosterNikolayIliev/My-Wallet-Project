import requests, os

URL = os.environ.get("PORTFOLIO_ACCOUNT_URL")


def validate_token(token):
    auto_internal = False
    try:
        user_id_check = token.split('|')
        auth = user_id_check[0]
        id_num = user_id_check[1]
        if auth == 'auth0' and len(id_num) == 24 or auth == 'google-oauth2' and len(id_num) == 21:
            endpoint = "api/account/internal/user/cache"
            headers = {'Authorization': 'Bearer ' + token}
            auto_internal = True
    except (AttributeError, IndexError):
        endpoint = "api/account/internal/user"
        headers = {'Authorization': token}
    res = requests.get(URL + endpoint, headers=headers)
    if res.status_code == 200:
        result = res.json()
        if auto_internal:
            result['internal'] = True
            result['base_currency'] = 'GBP'
        return result
    return False


def validate_auth_header(token: None):
    if not token:
        return False, 'Error: No token provided'

    user_data = validate_token(token)
    if not user_data:
        return False, 'Error, Invalid token'

    return True, user_data
