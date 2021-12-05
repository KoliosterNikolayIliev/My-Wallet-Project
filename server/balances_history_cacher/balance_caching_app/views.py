

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from balance_caching_app.models import UserData
from balance_caching_app.serializers import BalancesSerializer
from balance_caching_app.utils import timestamp_is_updated


def _auto_create_balance(data):
    user_id = data['id']
    user = UserData.objects.get(user_identifier=user_id)
    if timestamp_is_updated(user.last_login, data['timestamp']):
        return True

    user.balances_history.append(data)
    return user.save()


class CreateBalance(CreateAPIView):
    def create(self, request, *args, **kwargs):
        print(request.data)
        user_id = request.data.get('id')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = UserData.objects.get(user_identifier=user_id)
        # data = [user.balances_history, user.source_balances_history]
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = BalancesSerializer


# for dev purposes only !!!
# class GetBalances(APIView):
#     def get(self, request):
#         user_identifier = request.headers.get('id')
#
#         if not user_identifier:
#             return Response('User identifier was not provided', status=status.HTTP_400_BAD_REQUEST)
#
#         user_balances = UserData.objects.filter(user_identifier=user_identifier).first()
#
#         if not user_balances:
#             return Response('User does not exist', status=status.HTTP_400_BAD_REQUEST)
#         serializer = UserBalancesSerializer(user_balances)
#
#         return Response(serializer.data)
