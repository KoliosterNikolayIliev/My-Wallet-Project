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
        #TODO - must be handled in frontend !!!
        # if not internal:
        #     data['balance_history_GBP'] = response_from_balance_cache
        pprint(response_from_balance_cache)
    except Exception as e:
        print('Connection to balance cashing service failed:' + str(e))

    if internal:
        return valid_data
    return data
