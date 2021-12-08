from rest_framework import serializers
from api.models import UserAssets
from api.utils.serializer_validators import validate_user_key, add_or_increment_asset


class CryptoAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=5)
    amount = serializers.FloatField()
    asset_type = serializers.CharField(default='crypto')

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

        user_assets.crypto_assets = add_or_increment_asset(user_assets.crypto_assets, validated_data)
        user_assets.save()

        return validated_data


class StockAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=5)
    amount = serializers.IntegerField()
    asset_type = serializers.CharField(default='stock')

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

        user_assets.stock_assets = add_or_increment_asset(user_assets.stock_assets, validated_data)
        user_assets.save()

        return validated_data


class CurrencyAssetSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=3)
    amount = serializers.FloatField()
    asset_type = serializers.CharField(default='currency')

    def validate(self, attrs):
        # get user_key from request data, in attrs is only data about serializer fields
        user_key = self.context['request'].data.get('user-key')
        validate_user_key(user_key)

        return super().validate(attrs)

    def create(self, validated_data):
        user_key = self.context['request'].data['user-key']
        user_assets = UserAssets.objects.get(user_key=user_key)

        # when we create new user asset we pass only user_key so any other field is null
        if not user_assets.currency_assets:
            user_assets.currency_assets = []

        user_assets.currency_assets = add_or_increment_asset(user_assets.currency_assets, validated_data)
        user_assets.save()

        return validated_data


class UserAssetsSerializer(serializers.ModelSerializer):
    crypto_assets = CryptoAssetSerializer(many=True)
    stock_assets = StockAssetSerializer(many=True)
    currency_assets = CurrencyAssetSerializer(many=True)

    class Meta:
        model = UserAssets
        fields = ('crypto_assets', 'stock_assets', 'currency_assets')
