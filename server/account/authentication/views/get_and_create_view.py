from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from authentication.models import UserProfile
from authentication.serializers import UserSerializer
from authentication.common_shared.utils import jwt_decode_token


# creates user if not existing and returns user profile data or returns user profile data
# Needs research for using REST Generic views
@csrf_exempt
def get_and_create_user_profile(request):
    """
    get or create user if successful authentication by Auth0
    """
    try:
        token = request.headers.get('Authorization').split(' ')[1]
        request_user = jwt_decode_token(token).get('sub')
        user = UserProfile.objects.filter(user_identifier=request_user)

        if not user:
            new_user = UserProfile(user_identifier=request_user)
            new_user.save()
            # makes second call to the DB to be able to return user after first DB call
            user = UserProfile.objects.filter(user_identifier=request_user)

        if request.method == 'GET':
            serializer = UserSerializer(user, many=True)
            return JsonResponse(serializer.data, safe=False)

    except Exception:
        # Exception is intentionally too broad. Need to explore and decide which exceptions need to be caught.
        # Currently eliminates the possibility for 500 server error
        return JsonResponse('UNEXPECTED_ERROR', status=409, safe=False)
