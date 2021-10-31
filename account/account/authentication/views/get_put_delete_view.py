import io
import os

import requests
from requests.structures import CaseInsensitiveDict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# from authentication.common_shared.sensitive_data import MANAGER_TOKEN_PAYLOAD, MANAGER_TOKEN_URL, DELETE_USER
from authentication.models import UserProfile, NordigenRequisition
from authentication.serializers import (
    NewUserSerializer,
    ViewUserSerializer,
    ViewUserSerializerInternal,
    EditUserSerializer,
)
from authentication.common_shared.utils import (
    is_internal_request,
    register_or_delete_yodlee_login_name,
    return_request_user,
)


# creates user profile if not existing and returns user profile data or returns user profile data
# Needs research for using REST CVB's 
@api_view(['GET', 'DELETE', 'PUT'])
def get_put_create_delete_user_profile(request):
    """
    -Gets or creates user profile if successful authentication by Auth0 and returns user profile data
    -Deletes profile
    -Edits profile
    """
    request_user = return_request_user(request)
    if not request_user:
        return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        # Checks if the user profile is already in the DB and returns it if True
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewUserSerializer(user)
            # checks if user is internal and returns all user data (for Portfolio)
            if is_internal_request(request):
                serializer = ViewUserSerializerInternal(user)

            return Response(serializer.data)

        # Creates the user profile in the DB. Makes second call to the DB to return the user profile.
        except UserProfile.DoesNotExist:
            data = {'user_identifier': request_user}
            serializer = NewUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            user = UserProfile.objects.get(user_identifier=request_user)
            serializer = ViewUserSerializer(user)

            # Yodlee login name registration here
            register_or_delete_yodlee_login_name(user.user_identifier)

            # checks if user is internal and returns all user data (for Portfolio)
            if is_internal_request(request):
                serializer = ViewUserSerializerInternal(user)

            return Response(serializer.data)

    if request.method == 'DELETE':
        try:
            # Get Manager Token for Authorisation of the delete request
            # payload = MANAGER_TOKEN_PAYLOAD
            payload = os.environ.get('MANAGER_TOKEN_PAYLOAD')
            manager_token_url = os.environ.get('MANAGER_TOKEN_URL')
            headers_get_token_request = CaseInsensitiveDict()
            headers_get_token_request['content-type'] = 'application/json'
            token_request = requests.post(f'{manager_token_url}', payload, headers=headers_get_token_request)
            manger_token = token_request.json()['access_token']
        except Exception:
            return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)

        # Send delete request
        headers_delete_request = CaseInsensitiveDict()
        headers_delete_request['Authorization'] = f'Bearer {manger_token}'
        # user_data_url = DELETE_USER
        user_data_url = os.environ.get('DELETE_USER')
        # delete request to Auth0
        requests.delete(f'{user_data_url}{request_user}', headers=headers_delete_request, )

        # Delete UserAccount from database
        user = UserProfile.objects.filter(user_identifier=request_user)[0]
        if user:
            register_or_delete_yodlee_login_name(user.user_identifier, delete=True)
            user.delete()
        # Returns Success
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':

        # Gets the data from request body and transforms it into python dict
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream)
        data['user_identifier'] = request_user

        # Checks if user exist in DB. In case front end doesn't work properly
        try:
            user = UserProfile.objects.get(user_identifier=request_user)

        except UserProfile.DoesNotExist:
            return Response('User does not exists!', status=status.HTTP_404_NOT_FOUND)
        # The logic for editing the user
        serializer = EditUserSerializer(user, data=data)

        if serializer.is_valid():
            serializer.save()
            serializer = ViewUserSerializer(user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
