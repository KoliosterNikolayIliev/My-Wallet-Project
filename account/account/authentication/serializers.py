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
            'yodlee_login_name',
        ]


class UserNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_identifier',
        ]
