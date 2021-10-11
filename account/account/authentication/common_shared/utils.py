import json

import jwt
import requests

from django.contrib.auth import authenticate

# Returns Auth0 id to be saved as username to Django user. Currently not used
from django.http import JsonResponse


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
    if user_exists.status_code is not 200:
        return True
    return False
