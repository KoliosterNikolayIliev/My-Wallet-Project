from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from authentication.models import UserProfile
from authentication.serializers import UserNewSerializer, ViewEditUserSerializer
from authentication.common_shared.utils import jwt_decode_token


# creates user if not existing and returns user profile data or returns user profile data
# Needs research for using REST Generic views
@csrf_exempt
def get_and_create_user_profile(request):
    """
    get or create user if successful authentication by Auth0
    """
    # try:
    token = request.headers.get('Authorization').split(' ')[1]
    request_user = jwt_decode_token(token).get('sub')
    if request.method == 'GET':
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewEditUserSerializer(user)
            return JsonResponse(serializer.data)
        except UserProfile.DoesNotExist:
            data = {'user_identifier': request_user}
            serializer = UserNewSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewEditUserSerializer(user)
            return JsonResponse(serializer.data)


    # except Exception:
    #     # Exception is intentionally too broad. Need to explore and decide which exceptions need to be caught.
    #     # Currently eliminates the possibility for 500 server error
    #     return JsonResponse('UNEXPECTED_ERROR', status=409, safe=False)


"""
Needs to be caught:    
(wrong token)
raise DecodeError("Invalid crypto padding") from err
jwt.exceptions.DecodeError: Invalid crypto padding

Additional protection at backend:

We also could make additional call to use additional call to when GET and EDIT
https://dev-kbl8py41.us.auth0.com/userinfo 
this way we doublecheck the token with Auth0
if this check returns unauthorised we just return the same 

"""
