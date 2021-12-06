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

    def delete(self, request):
        user_assets = UserAssets.objects.filter(user_key=request.data.get('user-key')).first()

        if not user_assets:
            return Response('User does not exist', status=400)

        def try_to_delete(assets: list, asset_to_delete: str):
            target_index = 0
            found = False

            for index, asset in enumerate(assets):
                if asset['type'] == asset_to_delete:
                    target_index = index
                    found = True

            if found:
                assets.pop(target_index)
                return True

            return False

        crypto_assets = user_assets.crypto_assets
        stock_assets = user_assets.stock_assets
        currency_assets = user_assets.currency_assets
        deleted = False

        if crypto_assets:
            deleted = try_to_delete(crypto_assets, request.data.get('type'))

        if stock_assets and not deleted:
            deleted = try_to_delete(stock_assets, request.data.get('type'))

        if currency_assets and not deleted:
            deleted = try_to_delete(currency_assets, request.data.get('type'))

        if not deleted:
            return Response('asset not found', status=400)

        user_assets.save()
        return Response(status=204)
