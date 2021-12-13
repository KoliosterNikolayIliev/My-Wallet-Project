from copy import deepcopy

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
    balance_need_update=False
    new_balance = validated_balance_data['balance']
    new_timestamp = str(validated_balance_data['timestamp']).split(' ')[0]

    for balance in balances_history:
        current_balance = balance['balance']
        current_timestamp = str(balance['timestamp']).split(' ')[0]

        if trunc(current_balance) == trunc(new_balance) and current_timestamp == new_timestamp:
            balance_not_exist = False
            balance['timestamp'] = validated_balance_data['timestamp']
        if trunc(current_balance) != trunc(new_balance) and current_timestamp == new_timestamp:
            balance_need_update=True

    if balance_need_update:
        balances_history.pop()

    if balance_not_exist or balance_need_update:
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
        
        prev_date = data[0]['timestamp'].replace(day=data[0]['timestamp'].day - 1)

        template_object = deepcopy(data[0])
        template_object['balance'] = 0

        for source in template_object['source_balances_history']:
            source['value'] = 0

        template_object['timestamp'] = prev_date
        data.insert(0, template_object)
    return data

def fill_missing_days(data):
    index = 0
    for day in range(data[0]['timestamp'].day, data[-1]['timestamp'].day):
        if index > 0:
            current_date = data[index]['timestamp']
            prev_date = data[index - 1]['timestamp']

            if current_date.day - prev_date.day > 1:
                template_object = data[index - 1].copy()
                template_object['timestamp'] = prev_date.replace(day=prev_date.day + 1)
                data.insert(index, template_object)
        index += 1
    return data


def fix_source_balances(data):
    valid_sources = [source['provider'] for source in data[-1]['source_balances_history']]
    for obj in data:
        source_balances = []
        obj_source_balances = {el['provider']: el['value'] for el in obj['source_balances_history']}
        for valid_source in valid_sources:
            if valid_source in obj_source_balances:
                source_balances.append(
                    {'provider': valid_source, 'value': obj_source_balances[valid_source]}
                )
                continue
            source_balances.append(
                {'provider': valid_source, 'value': 0}
            )

        obj['source_balances_history'] = source_balances
