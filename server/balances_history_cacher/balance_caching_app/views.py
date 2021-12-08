from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from  balance_caching_app.utils import add_null_balances
import datetime

from balance_caching_app.models import UserData
from balance_caching_app.serializers import BalancesSerializer


class CreateBalance(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_id = request.data.get('id')
        user = UserData.objects.get(user_identifier=user_id)
        full_data = user.balances_history

        current_day = datetime.datetime.today().day
        return_data = add_null_balances(full_data, current_day)

        user_data = {
            'balances': return_data
        }
        headers = self.get_success_headers(user_data)
        return Response(user_data, status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = BalancesSerializer
