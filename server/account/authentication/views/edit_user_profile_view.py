import io

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Edit profile data
# Needs research for using REST Generic views
from rest_framework import status
from rest_framework.parsers import JSONParser

from authentication.common_shared.utils import jwt_decode_token
from authentication.models import UserProfile
from authentication.serializers import ViewEditUserSerializer


@csrf_exempt
def edit_user_profile(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    token = data.get('user_identifier')
    request_user = jwt_decode_token(token).get('sub')
    data_for_serialisation = data
    data_for_serialisation['user_identifier'] = request_user
    try:
        user = UserProfile.objects.get(user_identifier=request_user)
    except UserProfile.DoesNotExist:
        return JsonResponse('User does not exists!', status=status.HTTP_404_NOT_FOUND, safe=False)
    if request.method == 'POST':
        serializer = ViewEditUserSerializer(user, data=data_for_serialisation)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse('Forbidden!', status=403, safe=False)
