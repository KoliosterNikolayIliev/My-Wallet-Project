from rest_framework import serializers
from api.models import UserAssets
from api.utils.serializer_validators import validate_user_key


class CryptoAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=5)
    amount = serializers.FloatField()

    def validate(self, attrs):
        # get user_key from request data, in attrs is only data about serializer fields
        user_key = self.context['request'].data.get('user-key')
        validate_user_key(user_key)

        return super().validate(attrs)

    def create(self, validated_data):
        user_key = self.context['request'].data['user-key']
        user_assets = UserAssets.objects.get(user_key=user_key)

        # when we create new user asset we pass only user_key so any other field is null
        if not user_assets.crypto_assets:
            user_assets.crypto_assets = []

        user_assets.crypto_assets.append(validated_data)
        user_assets.save()

        return validated_data


class StockAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=5)
    amount = serializers.IntegerField()

    def validate(self, attrs):
        # get user_key from request data, in attrs is only data about serializer fields
        user_key = self.context['request'].data.get('user-key')
        validate_user_key(user_key)

        return super().validate(attrs)

    def create(self, validated_data):
        user_key = self.context['request'].data['user-key']
        user_assets = UserAssets.objects.get(user_key=user_key)

        # when we create new user asset we pass only user_key so any other field is null
        if not user_assets.stock_assets:
            user_assets.stock_assets = []

        user_assets.stock_assets.append(validated_data)
        user_assets.save()

        return validated_data


class UserAssetsSerializer(serializers.ModelSerializer):
    crypto_assets = CryptoAssetSerializer(many=True)
    stock_assets = StockAssetSerializer(many=True)

    class Meta:
        model = UserAssets
        fields = ('crypto_assets', 'stock_assets')
