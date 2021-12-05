from django.utils import timezone
from rest_framework import serializers
from balance_caching_app.models import UserData
from balance_caching_app.utils import add_balance


class BalancesSerializer(serializers.Serializer):
    total_balance = serializers.FloatField()
    source_balances = serializers.ListField()
    timestamp = serializers.DateTimeField(default=timezone.now())
    id = serializers.CharField()

    def save(self, **kwargs):

        return super(BalancesSerializer, self).save()

    def create(self, validated_data):
        user_identifier = validated_data['id']
        user = UserData.objects.filter(user_identifier=user_identifier).first()
        if not user:
            user = UserData.objects.create(user_identifier=user_identifier)

        if not user.balances_history:
            user.balances_history = []

        user.balances_history = add_balance(user.balances_history, validated_data)
        user.last_login = timezone.now()
        user.save()
        return validated_data
