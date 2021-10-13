from rest_framework import serializers
from api.models import UserAssets


class CryptoAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=5)
    amount = serializers.FloatField()


class UserAssetsSerializer(serializers.ModelSerializer):
    crypto_assets = CryptoAssetSerializer(many=True)

    class Meta:
        model = UserAssets
        fields = ('crypto_assets',)
