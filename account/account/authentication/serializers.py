from rest_framework import serializers

from authentication.models import UserProfile


class ViewEditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_identifier',
            'base_currency',
            'source_label',
            'binance_key',
            'binance_secret',
            'coinbase_api_secret',
            'coinbase_api_key',
            'coinbase_api_pass',
            'yodlee_login_name',
            'nordigen_requisition',
            'custom_assets_key',
            'first_name',
            'last_name',
        ]


class UserNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_identifier',
        ]
