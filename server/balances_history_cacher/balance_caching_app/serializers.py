from django.utils import timezone
from rest_framework import serializers
from balance_caching_app.models import UserData
from balance_caching_app.utils import add_balance, add_source_balances


class BalancesSerializer(serializers.Serializer):
    total_balance = serializers.FloatField()
    source_balances = serializers.ListField()
    timestamp = serializers.DateTimeField(default=timezone.now())
    id = serializers.CharField()

    def create(self, validated_data):
        user_identifier = validated_data['id']
        user = UserData.objects.filter(user_identifier=user_identifier).first()
        if not user:
            user = UserData.objects.create(user_identifier=user_identifier)

        if not user.balances_history:
            user.balances_history = []

        if not user.source_balances_history:
            user.source_balances_history = []

        validated_balance_data = {
            'balance': validated_data['total_balance'],
            'timestamp': validated_data['timestamp']
        }

        add_balance_or_not = add_balance(user.balances_history, validated_balance_data)
        user.balances_history = add_balance_or_not[0]
        can_add_balance = add_balance_or_not[1]

        if can_add_balance:
            balances_list = validated_data['source_balances']
            it = iter(balances_list)
            validated_source_data = tuple(zip(it, it))
            user.source_balances_history = add_source_balances(user.source_balances_history, validated_source_data)

        user.last_login = timezone.now()
        user.save()
        return validated_data

# class UserBalancesSerializer(serializers.ModelSerializer):
#     balances_history = BalancesSerializer(many=True)
#
#     class Meta:
#         model = UserData
#         fields = "__all__"
