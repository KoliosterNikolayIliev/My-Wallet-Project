from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserAssets, CryptoAsset
from api.serializers import CryptoAssetSerializer, UserAssetsSerializer, StockAssetSerializer, CurrencyAssetSerializer
from api.utils.delete_asset import delete_asset


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CryptoAssetSerializer

    def delete(self, request):
        user_assets = UserAssets.objects.filter(user_key=request.data.get('user-key')).first()

        if not user_assets:
            return Response('User does not exist', status=400)

        if not delete_asset(user_assets.crypto_assets, request.data.get('asset')):
            return Response('asset not found', status=400)

        user_assets.save()

        return Response('success', status=200)


class CreateStockAsset(CreateAPIView):
    serializer_class = StockAssetSerializer

    def delete(self, request):
        user_assets = UserAssets.objects.filter(user_key=request.data.get('user-key')).first()

        if not user_assets:
            return Response('User does not exist', status=400)

        if not delete_asset(user_assets.stock_assets, request.data.get('asset')):
            return Response('asset not found', status=400)

        user_assets.save()

        return Response('success', status=200)


class CreateCurrencyAsset(CreateAPIView):
    serializer_class = CurrencyAssetSerializer

    def delete(self, request):
        user_assets = UserAssets.objects.filter(user_key=request.data.get('user-key')).first()

        if not user_assets:
            return Response('User does not exist', status=400)

        if not delete_asset(user_assets.currency_assets, request.data.get('asset')):
            return Response('asset not found', status=400)

        user_assets.save()

        return Response('success', status=200)


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
