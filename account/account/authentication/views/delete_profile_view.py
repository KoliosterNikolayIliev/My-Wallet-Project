import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests.structures import CaseInsensitiveDict

from authentication.common_shared.sensitive_data import DELETE_USER, MANAGER_TOKEN_URL, MANAGER_TOKEN_PAYLOAD
from authentication.common_shared.utils import jwt_decode_token
from authentication.models import UserProfile


# Deletes account from Auth0 DB and Account Db
# Needs research for using REST Generic views
@csrf_exempt
def delete_user_account(request):
    if request.method == 'DELETE':
        # Get user id
        try:
            user_token = request.headers['Authorization'].split(' ')[1]
            request_user = jwt_decode_token(user_token).get('sub')
            # Get Manager Token for Authorisation of the delete request
            payload = MANAGER_TOKEN_PAYLOAD
            headers_get_token_request = CaseInsensitiveDict()
            headers_get_token_request['content-type'] = 'application/json'
            token_request = requests.post(f'{MANAGER_TOKEN_URL}', payload, headers=headers_get_token_request)
            manger_token = token_request.json()['access_token']
            token = manger_token
        except Exception:
            return JsonResponse('UNAUTHORIZED!', status=401, safe=False)

        # Send delete request
        headers_delete_request = CaseInsensitiveDict()
        headers_delete_request['Authorization'] = f'Bearer {token}'
        user_data_url = DELETE_USER
        try:
            requests.delete(f'{user_data_url}{request_user}', headers=headers_delete_request, )
        except Exception:
            return JsonResponse('UNAUTHORIZED!', status=401, safe=False)

        # Delete UserAccount from database
        user = UserProfile.objects.filter(user_identifier=request_user)
        if user:
            user.delete()
        # Returns Success
        return JsonResponse(f'DELETE SUCCESSFUL!', status=200, safe=False)
    # Returns unsuccessful deletion
    return JsonResponse('UNAUTHORIZED', status=403, safe=False)
