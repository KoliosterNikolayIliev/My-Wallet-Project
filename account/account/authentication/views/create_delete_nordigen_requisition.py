import io

from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import mixins

from authentication.common_shared.utils import create_nordigen_requisition, return_request_user, \
    delete_nordigen_requisition
from authentication.models import NordigenRequisition, UserProfile
from authentication.serializers import NordigenRequisitionSerializer


class CreateDeleteNordigenRequisition(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                      generics.GenericAPIView):
    queryset = NordigenRequisition.objects.all()
    serializer_class = NordigenRequisitionSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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
        data = create_nordigen_requisition(institution_id)
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
        requisition_id = request_data.get('requisition_id')
        if not request_user:
            return Response('UNAUTHORIZED!', status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = UserProfile.objects.get(user_identifier=request_user)
        except UserProfile.DoesNotExist:
            return Response('UNAUTHORIZED OR USER NOT SET!', status=status.HTTP_401_UNAUTHORIZED)
        try:
            instance = user.nordigenrequisition_set.get(requisition_id=requisition_id)
        except NordigenRequisition.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.perform_destroy(instance)
        delete_nordigen_requisition(requisition_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
