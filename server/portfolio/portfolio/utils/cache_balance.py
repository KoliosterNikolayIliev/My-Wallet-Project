import datetime
import os
from pprint import pprint

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
    try:
        response_from_balance_cache = requests.post(url + 'balances/add/', data=valid_data).json()
        if not internal:
            pprint(response_from_balance_cache)
            if response_from_balance_cache == {'source_balances': ['This field is required.']}:
                response_from_balance_cache = {
                    'balances': [{
                        'balance': 0,
                        'source_balances_history': [
                            {'provider': 'Wise', 'value': 0},
                        ],
                        'timestamp': datetime.datetime.utcnow().isoformat()},{
                        'balance': 0,
                        'source_balances_history': [
                            {'provider': 'Wise', 'value': 0},
                        ],
                        'timestamp': datetime.datetime.utcnow().isoformat()}]}
            data['balance_history'] = response_from_balance_cache

            # '{'total': 0, 'balance_history': {'source_balances': []}}'
    except Exception as e:
        print('Connection to balance cashing service failed:' + str(e))

    if internal:
        return valid_data
    return data
