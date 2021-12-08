from django.utils import timezone
from datetime import datetime
from math import trunc


class AutoRequest:
    auto = False


def add_balance(balances_history, data):
    validated_balance_data = {
        'balance': data['total_balance'],
        'timestamp': data['timestamp'],
        'source_balances_history': []
    }
    balance_not_exist = True
    new_balance = validated_balance_data['balance']
    new_timestamp = str(validated_balance_data['timestamp']).split(' ')[0]

    for balance in balances_history:
        current_balance = balance['balance']
        current_timestamp = str(balance['timestamp']).split(' ')[0]

        if trunc(current_balance) == trunc(new_balance) and current_timestamp == new_timestamp:
            balance_not_exist = False
            balance['timestamp'] = validated_balance_data['timestamp']
        if trunc(current_balance) != trunc(new_balance) and current_timestamp == new_timestamp:
            balance['timestamp'] = validated_balance_data['timestamp']
            balance['balance'] = new_balance
            balance_not_exist = False

    if balance_not_exist:
        source_balances_list = data['source_balances']
        it = iter(source_balances_list)
        validated_source_data = tuple(zip(it, it))
        source_balances_history = add_source_balances(validated_source_data)
        validated_balance_data['source_balances_history'] = source_balances_history
        balances_history.append(validated_balance_data)

    return balances_history


def add_source_balances(data):
    source_balances_history = []
    for entry in data:
        balance = {
            'provider': entry[0],
            'value': entry[1]
        }
        source_balances_history.append(balance)
    return source_balances_history


def user_is_not_active(timestamp):
    user_month = int(str(timestamp).split('-')[1])
    current_month = int(str(timezone.now()).split('-')[1])
    if current_month - user_month >= 3:
        print('inactive' + f'{timezone.now()}')
        return True
    print('active' + f'{timezone.now()}')
    return False

def add_null_balances(data, today):
    if len(data) == today:
        return data
    

    for i in range(today, 0, -1):
        if len(data) == today:
            break
        
        prev_date = data[0]['timestamp'].day - 1

        template_object = data[0].copy()
        template_object['balance'] = 0
        
        for source in template_object['source_balances_history']:
            source['value'] = 0

        template_object['timestamp'] = datetime(2021, 12, prev_date, 0, 0, 0, 0)
        data.insert(0, template_object)

    return data