from rest_framework.serializers import ModelSerializer

from api.models import CryptoAsset


class CreateCryptoAssetSerializer(ModelSerializer):
    class Meta:
        model = CryptoAsset
        exclude = ('id',)

    def create(self, validated_data):
        # check for crypto asset obj with these asset key and crypto
        crypto_asset_obj = CryptoAsset.objects.filter(
            custom_assets_key=validated_data['custom_assets_key'],
            crypto=validated_data['crypto'],
        ).first()

        # if there is no crypto asset we create one
        if not crypto_asset_obj:
            return super().create(validated_data)

        # if there is a crypto asset we increase its amount
        crypto_asset_obj.amount += validated_data['amount']
        crypto_asset_obj.save()

        return crypto_asset_obj
