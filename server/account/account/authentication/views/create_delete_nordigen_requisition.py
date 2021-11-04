import io

from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import mixins

from authentication.common_shared.utils import create_delete_nordigen_requisition, return_request_user
from authentication.models import NordigenRequisition, UserProfile
from authentication.serializers import NordigenRequisitionSerializer


class CreateDeleteNordigenRequisition(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                      generics.GenericAPIView):
    queryset = NordigenRequisition.objects.all()
    serializer_class = NordigenRequisitionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        request_user = return_request_user(request)
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
        except UserProfile.DoesNotExist:
            return Response('UNAUTHORIZED OR USER NOT SET!', status=status.HTTP_401_UNAUTHORIZED)
        queryset = user.nordigenrequisition_set
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request_user = return_request_user(request)
        stream = io.BytesIO(request.body)
        request_data = JSONParser().parse(stream)
        institution_id = request_data.get('institution_id')
        if not request_user:
            return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
        except UserProfile.DoesNotExist:
            return Response('UNAUTHORIZED OR USER NOT SET!', status=status.HTTP_401_UNAUTHORIZED)
        user_requisitions = user.nordigenrequisition_set.filter(institution_id=institution_id)
        if user_requisitions:
            return Response('NORDIGEN_REQUISITION_ALREADY_EXISTS', status=status.HTTP_400_BAD_REQUEST)
        data = create_delete_nordigen_requisition(nordigen_institution_id=institution_id)
        data['user'] = user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        request_user = return_request_user(request)
        stream = io.BytesIO(request.body)
        request_data = JSONParser().parse(stream)
        institution_id = request_data.get('institution_id')
        if not request_user:
            return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
        except UserProfile.DoesNotExist:
            return Response('UNAUTHORIZED OR USER NOT SET!', status=status.HTTP_401_UNAUTHORIZED)
        try:
            instance = user.nordigenrequisition_set.get(institution_id=institution_id)
            requisition_id = instance.requisition_id
        except NordigenRequisition.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.perform_destroy(instance)
        create_delete_nordigen_requisition(nordigen_institution_id=institution_id, requisition_id=requisition_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
