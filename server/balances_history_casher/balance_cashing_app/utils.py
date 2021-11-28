from django.utils import timezone


def add_balance(balances_history, validated_data):
    balance_not_exist = True
    for balance in balances_history:
        if balance['balance'] == validated_data['balance']:
            balance_not_exist = False
            balance['timestamp'] = timezone.now()
            break

    if balance_not_exist:
        balances_history.append(validated_data)

    return balances_history
