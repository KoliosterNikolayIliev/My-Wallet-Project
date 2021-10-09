import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from authentication.common_shared.utils import jwt_decode_token
from authentication.models import UserProfile
from authentication.serializers import ViewEditUserSerializer


# Edits profile data
# Needs research for using REST Generic views

@csrf_exempt
def edit_user_profile(request):
    if request.method == 'PUT':
        # Gets the data from request body and transforms it into python dict
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        data_for_serialisation = data

        # Get and decode token. Catches all possible errors for (wrong, too long, too short, etc.)token
        # If token is ok, passes the user for next operations.
        # here we could use external validation from Auth0 (https://dev-kbl8py41.us.auth0.com/userinfo )
        # and not use try/except.
        try:
            token = data.get('user_identifier')
            request_user = jwt_decode_token(token).get('sub')
        except Exception:
            return JsonResponse('UNAUTHORIZED!', status=401, safe=False)

        # Checks if user exist in DB. In case front end doesn't work properly
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
        except UserProfile.DoesNotExist:
            return JsonResponse('User does not exists!', status=status.HTTP_404_NOT_FOUND, safe=False)

        # The logic for editing the user
        data_for_serialisation['user_identifier'] = request_user
        serializer = ViewEditUserSerializer(user, data=data_for_serialisation)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse('Forbidden!', status=403, safe=False)
