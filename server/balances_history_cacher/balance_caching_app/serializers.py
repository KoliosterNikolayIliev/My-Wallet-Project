from math import trunc
from django.utils import timezone
from django.utils.datetime_safe import date
from rest_framework import serializers
from balance_caching_app.models import UserData
from balance_caching_app.serializers_validators import validate_user_identifier
from balance_caching_app.utils import add_balance


class BalancesSerializer(serializers.Serializer):
    balance = serializers.FloatField()
    timestamp = serializers.DateTimeField(default=timezone.now())

    def validate(self, attrs):
        user_identifier = self.context['request'].data.get('id')
        validate_user_identifier(user_identifier)

        return super().validate(attrs)

    def create(self, validated_data):
        user_identifier = self.context['request'].data['id']
        user = UserData.objects.filter(user_identifier=user_identifier).first()
        if not user:
            user = UserData.objects.create(user_identifier=user_identifier)

        if not user.balances_history:
            user.balances_history = []
        validated_data['balance'] = trunc(validated_data['balance'])
        user.balances_history = add_balance(user.balances_history, validated_data)
        user.last_login = timezone.now()
        user.save()

        return validated_data


class UserBalancesSerializer(serializers.ModelSerializer):
    balances_history = BalancesSerializer(many=True)

    class Meta:
        model = UserData
        fields = "__all__"
