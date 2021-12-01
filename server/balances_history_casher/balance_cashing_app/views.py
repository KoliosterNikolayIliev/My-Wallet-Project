from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from balance_cashing_app.models import UserData
from balance_cashing_app.serializers import BalancesSerializer, UserBalancesSerializer
from balance_cashing_app.utils import add_balance


def _auto_create_balance(data):
    user_id = data['id']
    user = UserData.objects.get(user_identifier=user_id)
    user.balances_history = add_balance(user.balances_history, data)
    return user.save()


class CreateBalance(CreateAPIView):
    serializer_class = BalancesSerializer


class GetBalances(APIView):
    def get(self, request):
        user_identifier = request.headers.get('id')

        if not user_identifier:
            return Response('User identifier was not provided', status=status.HTTP_400_BAD_REQUEST)

        user_balances = UserData.objects.filter(user_identifier=user_identifier).first()

        if not user_balances:
            return Response('User does not exist', status=status.HTTP_400_BAD_REQUEST)
        serializer = UserBalancesSerializer(user_balances)

        return Response(serializer.data)
