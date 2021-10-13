from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UserAssets
from api.serializers import CryptoAssetSerializer, UserAssetsSerializer


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CryptoAssetSerializer


class GetAssets(APIView):
    def get(self, request):
        user_key = request.headers.get('user-key')

        if not user_key:
            return Response('User key was not provided', status=400)

        user_assets = UserAssets.objects.get(user_key=user_key)
        serializer = UserAssetsSerializer(user_assets)

        return Response(serializer.data)
