from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from balance_caching_app.serializers import BalancesSerializer


class CreateBalance(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        modified_data = serializer.data
        sources_list = modified_data.pop('source_balances')
        it = iter(sources_list)
        sources_tuple = tuple(zip(it, it))
        modified_data['source_balances'] = dict(sources_tuple)
        headers = self.get_success_headers(modified_data)
        return Response(modified_data, status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = BalancesSerializer
