from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from authentication.models import UserProfile
from authentication.serializers import UserNewSerializer, ViewEditUserSerializer
from authentication.common_shared.utils import jwt_decode_token


# creates user profile if not existing and returns user profile data or returns user profile data
# Needs research for using REST Generic views
@csrf_exempt
def get_and_create_user_profile(request):
    """
    gets or creates user profile if successful authentication by Auth0 and returns user profile data
    """
    # Get and decode token. Catches all possible errors for (wrong, too long, too short, etc.)token
    # If token is ok, passes the user for next operations.
    # here we could use external validation from Auth0 (https://dev-kbl8py41.us.auth0.com/userinfo )
    # and not use try/except.
    try:
        token = request.headers.get('Authorization').split(' ')[1]
        request_user = jwt_decode_token(token).get('sub')
    except Exception:
        return JsonResponse('UNAUTHORIZED!', status=401, safe=False)

    if request.method == 'GET':
        # Checks if the user profile is already in the DB and returns it if True
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewEditUserSerializer(user)
            return JsonResponse(serializer.data)

        # Creates the user profile in the DB. Makes second call to the DB to return the user profile.
        except UserProfile.DoesNotExist:
            data = {'user_identifier': request_user}
            serializer = UserNewSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewEditUserSerializer(user)
            return JsonResponse(serializer.data)
    return JsonResponse('FORBIDDEN!', status=403, safe=False)
