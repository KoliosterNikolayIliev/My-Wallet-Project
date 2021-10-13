from api.models import CryptoAsset
from api.serializers import ViewCryptoAssetSerializer


def get_crypto_assets(custom_assets_key):
    crypto_assets = CryptoAsset.objects.filter(custom_assets_key=custom_assets_key)
    serializer = ViewCryptoAssetSerializer(crypto_assets, many=True)

    return serializer.data
