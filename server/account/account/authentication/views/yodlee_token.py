from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.common_shared.utils import return_request_user, yodlee_token


@api_view(['GET'])
def get_yodlee_token(request):
    request_user = return_request_user(request)
    if not request_user:
        return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)
    token = yodlee_token(request_user, end_user=True)
    return Response(data=token, status=status.HTTP_200_OK)
