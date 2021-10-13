from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CryptoAssetSerializer


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CryptoAssetSerializer


class GetAssets(APIView):
    def get(self, request):
        pass
