from django.utils import timezone
from math import trunc


def add_balance(balances_history, data):
    # print(data)
    balance_not_exist = True
    for balance in balances_history:
        # TODO here I need to check with floatpoint accuracy
        current_balance = balance['balance']
        new_balance = data['balance']
        current_timestamp = str(balance['timestamp']).split(' ')[0]
        new_timestamp = str(data['timestamp']).split(' ')[0]

        if trunc(current_balance) == trunc(new_balance) and current_timestamp == new_timestamp:
            balance_not_exist = False
            balance['timestamp'] = data['timestamp']
        if trunc(current_balance) != trunc(new_balance) and current_timestamp == new_timestamp:
            balance['timestamp'] = data['timestamp']
            balance['balance'] = new_balance
            balance_not_exist = False

    if balance_not_exist:
        balances_history.append(data)

    return balances_history, balance_not_exist


def add_source_balances(source_balances_history, data):
    for tup in data:
        ready = {
            'provider': tup[0],
            'value': tup[1]
        }
        source_balances_history.append(ready)
    return source_balances_history


def user_is_not_active(timestamp):
    user_month = int(str(timestamp).split('-')[1])
    current_month = int(str(timezone.now()).split('-')[1])
    if current_month - user_month >= 3:
        print('inactive')
        return True
    print('active')
    return False


def timestamp_is_updated(last_login, timestamp):
    last_login = str(last_login).split(' ')[0]
    timestamp = str(timestamp).split(' ')[0]
    if last_login == timestamp:
        print('user not updated')
        return True
    print('user updated')
    return False
