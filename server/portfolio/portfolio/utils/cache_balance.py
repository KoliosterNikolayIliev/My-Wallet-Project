import datetime
import os

import requests


def cache_balance(cache_balance_data, data, user_data, total_gbp, internal):
    cache_balance_data.pop('total')
    cleared_data = cache_balance_data
    source_balances = {key: value['total'] for key, value in cleared_data.items()}

    valid_data = {
        'id': user_data['user_identifier'],
        'total_balance': total_gbp,
        'source_balances': []
    }
    for key, value in source_balances.items():
        valid_data['source_balances'].append((key, value))
    url = os.environ.get('BALANCE_CACHING_SERVICE_URL')

    error_response_from_balance_cache = {
        'balances': [{
            'balance': 0,
            'source_balances_history': [
                {'provider': 'None', 'value': 0},
            ],
            'timestamp': datetime.datetime.utcnow().isoformat()}]}
    try:
        response_from_balance_cache = requests.post(url + 'balances/add/', data=valid_data).json()
        if not internal:
            if response_from_balance_cache == {'source_balances': ['This field is required.']}:
                response_from_balance_cache = error_response_from_balance_cache
            data['balance_history'] = response_from_balance_cache

    except Exception as e:
        print('Connection to balance cashing service failed:' + str(e))
        data['balance_history'] = error_response_from_balance_cache
    if internal:
        return valid_data
    return data
