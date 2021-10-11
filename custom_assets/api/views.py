from rest_framework.generics import CreateAPIView
from api.serializers import CreateCryptoAssetSerializer


class CreateCryptoAsset(CreateAPIView):
    serializer_class = CreateCryptoAssetSerializer
