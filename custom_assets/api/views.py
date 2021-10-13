from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CreateCryptoAssetSerializer
from api.utils.get_assets import get_crypto_assets


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CreateCryptoAssetSerializer


class GetAssets(APIView):
    def get(self, request):
        custom_assets_key = request.headers.get('custom_assets_key')

        if not custom_assets_key:
            return Response('Custom assets key was not provided', status=400)

        data = {
            'crypto assets': get_crypto_assets(custom_assets_key)
        }

        return Response(data)
