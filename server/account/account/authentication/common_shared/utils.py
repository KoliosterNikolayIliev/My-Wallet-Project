import json
import os

import jwt
import requests

from django.contrib.auth import authenticate

# Returns Auth0 id to be saved as username to Django user. Currently not used
from rest_framework import status
from rest_framework.response import Response


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username


# Returns the username needed to make match between database and Auth0 authenticated user
def auth0user(payload):
    if payload == 'invalid identifier':
        return
    return 'auth0user'


# JWT token decoder
def jwt_decode_token(token):
    try:
        header = token.decode().split('|')
        auth = header[0]
        id_num = header[1]
        if auth == 'auth0' and len(id_num) == 24 or auth == 'google-oauth2' and len(id_num) == 21:
            return True
    except (AttributeError, IndexError):
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


def yodlee_token(yodlee_login_name, end_user=False):
    admin_login_name = os.environ.get('YODLEE_ADMIN_LOGIN_NAME')
    client_id = os.environ.get('ASSETS_YODLEE_CLIENT_ID')
    client_secret = os.environ.get('ASSETS_YODLEE_SECRET')
    managers_token_url = os.environ.get('YODLEE_GET_MANAGERS_TOKEN_URL')
    payload = {
        'clientId': client_id,
        'secret': client_secret
    }
    headers = {
        'Api-Version': '1.1',
        'loginName': admin_login_name if not end_user else yodlee_login_name
    }
    response = requests.post(managers_token_url, payload, headers=headers)
    token_dict = response.json()
    token = token_dict.get('token').get('accessToken')
    return token


def register_or_delete_yodlee_login_name(yodlee_login_name, end_user=False):
    """
    The possible error codes are (200,400,401). All of them are important to our application and not the end user.
    I suppose in this case logging is better than error handling. 400 is for user that already exists
    401 is if we have problems with our credentials
    """
    token = yodlee_token(yodlee_login_name, end_user)

    register_user_url = os.environ.get('YODLEE_REGISTER_USER_URL')
    delete_user_url = os.environ.get('YODLEE_DELETE_USER_URL')

    registry_delete_headers = {
        'Api-Version': '1.1',
        'Authorization': f'Bearer {token}',

    }
    registry_payload = json.dumps({'user': {'loginName': f'{yodlee_login_name}'}})

    if end_user:
        return requests.delete(delete_user_url, headers=registry_delete_headers)

    return requests.post(register_user_url, registry_payload, headers=registry_delete_headers)


def create_delete_nordigen_requisition(nordigen_institution_id=None, requisition_id=None):
    secret_id = os.environ.get('ASSETS_NORDIGEN_ID')
    secret_key = os.environ.get('ASSETS_NORDIGEN_KEY')
    get_token_url = os.environ.get('NORDIGEN_GET_TOKEN_URL')
    nordigen_create_requisition_url = os.environ.get('NORDIGEN_CREATE_REQUISITION_URL')
    nordigen_redirect_url = os.environ.get('NORDIGEN_REDIRECT_HOMEPAGE')
    payload = json.dumps({
        'secret_id': secret_id,
        'secret_key': secret_key,
    })
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = requests.post(get_token_url, payload, headers=headers)
    token = response.json().get('access')

    headers['Authorization'] = f'Bearer {token}'
    if requisition_id:
        return requests.delete(nordigen_create_requisition_url + requisition_id + '/', headers=headers)
    payload = json.dumps({
        'redirect': nordigen_redirect_url,
        'institution_id': nordigen_institution_id,
    })
    response = requests.post(nordigen_create_requisition_url, payload, headers=headers)
    result = response.json()
    return {
        'institution_id': nordigen_institution_id,
        'requisition_id': result.get('id'),
        'confirmation_link': result.get('link'),
    }


def return_request_user(request):
    # Get and decode token.
    token = request.headers.get('Authorization').split(' ')[1]
    url = request.get_full_path_info()
    if url == '/api/account/internal/user/cache':
        return token
    # check if user exists in Aut0 DB. Important check if user is deleted and same token is used in get or put request
    if user_does_not_exist(token):
        return False
    return jwt_decode_token(token).get('sub')
