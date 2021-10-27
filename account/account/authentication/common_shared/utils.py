import json

import jwt
import requests

from django.contrib.auth import authenticate


# Returns Auth0 id to be saved as username to Django user. Currently not used
def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username


# Returns the username needed to make match between database and Auth0 authenticated user
def auth0user(payload):
    return 'auth0user'


# JWT token decoder
def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format('dev-kbl8py41.us.auth0.com')).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format('dev-kbl8py41.us.auth0.com')
    return jwt.decode(token, public_key, audience='https://dev-kbl8py41.us.auth0.com/api/v2/', issuer=issuer,
                      algorithms=['RS256'])


# checks if user exists in Auth0
def user_does_not_exist(token):
    user_exists = requests.get('https://dev-kbl8py41.us.auth0.com/userinfo',
                               headers={'Authorization': f'Bearer {token}'})
    if user_exists.status_code != 200:
        return True
    return False


# checks if request is internal
def is_internal_request(request):
    path = request.get_full_path_info()
    if 'internal' in path:
        return True
    return False


def register_yodlee_login_name(yodlee_login_name):
    payload = {
        'clientId': 'nMBh2VpFUf1s8KW3s4RQqCrQHrAOCnIW',
        'secret': 'VnASgLDozoiY4WgP'
    }
    headers = {
        'Api-Version': '1.1',
        'loginName': 'e918afdd-e759-410b-9e3a-124279032910_ADMIN'
    }
    managers_token = requests.post('https://development.api.yodlee.uk/ysl/auth/token', payload, headers=headers)
    token_dict = managers_token.json()
    token = token_dict.get('token').get('accessToken')

    registry_headers = {
        'Api-Version': '1.1',
        'Content-Type': 'application/json',
        'clientId': 'nMBh2VpFUf1s8KW3s4RQqCrQHrAOCnIW',
        'cobrand-Name': '{cobrandName}',
        'Authorization': f'Bearer {token}'

    }
    registry_payload = json.dumps({'user': {'loginName': f'{yodlee_login_name}'}})

    register_at_yodlee = requests.post('https://development.api.yodlee.uk/ysl/user/register', registry_payload,
                                       headers=registry_headers)

    # the possible error codes are (200,400,401). All of them are important to our application and not the end user
    # I suppose in this case logging is better than error handling. 400 is for user that already exists
    # 401 is if we have problems with our credentials
    print(register_at_yodlee.json())


register_yodlee_login_name('google-oauth2|11474973646491801459018')
