from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserAssets, CryptoAsset
from api.serializers import CryptoAssetSerializer, UserAssetsSerializer, StockAssetSerializer, CurrencyAssetSerializer


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CryptoAssetSerializer


class CreateStockAsset(CreateAPIView):
    serializer_class = StockAssetSerializer


class CreateCurrencyAsset(CreateAPIView):
    serializer_class = CurrencyAssetSerializer


class GetAssets(APIView):
    def get(self, request):
        user_key = request.headers.get('user-key')

        if not user_key:
            return Response('User key was not provided', status=400)

        user_assets = UserAssets.objects.filter(user_key=user_key).first()

        if not user_assets:
            return Response('User does not exist', status=400)

        serializer = UserAssetsSerializer(user_assets)

        return Response(serializer.data)
