import datetime as dt
from collections import OrderedDict


def group_balances(balances: dict, holdings: dict, gbp_cur=False):
    cur_currency = 'base_currency'
    if gbp_cur:
        cur_currency = 'gbp_currency'
    result = {}
    total_balance = 0
    for provider, content in balances.items():
        if content['status'] != 'failed':
            for account, account_content in content['content'].items():
                name = account_content['providerName']
                data = {'provider': provider, 'id': account,
                        'data': {key: value for (key, value) in account_content.items() if key != "providerName"}}
                for key, value in holdings.items():
                    if key == "yodlee":
                        holdings_data = []
                        for asset, asset_content in value['content'].items():
                            if str(asset_content['parent']) == account:
                                holdings_data.append(asset_content)
                        data['holdings'] = holdings_data

                if result.get(name):
                    if result[name].get('accounts'):
                        result[name]['accounts'].append(data)
                    else:
                        result[name]['accounts'] = [data]

                    if account_content['balanceData'].get(cur_currency):
                        total_balance += float(account_content['balanceData'][cur_currency])
                        if result[name].get('total'):
                            result[name]['total'] += account_content['balanceData'][cur_currency]
                        else:
                            result[name]['total'] = account_content['balanceData'][cur_currency]
                else:
                    total_balance += float(account_content['balanceData'][cur_currency])
                    result[name] = {'accounts': [data], 'total': account_content['balanceData'][cur_currency]}

    for provider, content in {key: value for (key, value) in holdings.items() if key != "yodlee"}.items():
        if content['status'] != 'failed':
            for asset, asset_content in content['content'].items():
                data = {'provider': provider, 'id': asset, 'data': asset_content}

                if result.get(provider):
                    if result[provider].get('accounts'):
                        result[provider]['accounts'].append(data)
                    else:
                        result[provider]['accounts'] = [data]

                    if asset_content.get(cur_currency):
                        total_balance += float(asset_content[cur_currency])
                        if result[provider].get('total'):
                            result[provider]['total'] += asset_content[cur_currency]
                        else:
                            result[provider]['total'] = asset_content[cur_currency]
                else:
                    if asset_content.get(cur_currency):
                        total_balance += float(asset_content[cur_currency])
                        result[provider] = {'accounts': [data], 'total': asset_content[cur_currency]}
                    else:
                        result[provider] = {'accounts': [data], 'total': 0}
    result['total'] = total_balance
    return result


def set_historical_balance(starting_balance: float, transactions: list):
    data = {}
    result = {}
    balance = starting_balance
    transactions_from_this_month = [transaction for transaction in transactions if
                                    list(transaction.values())[0]['date'].split('-')[1] == str(dt.datetime.now().month)]

    if not transactions_from_this_month:
        return None

    # add a point for days where transactions were made
    for item in transactions_from_this_month:
        transaction = list(item.values())[0]
        day = int(transaction['date'].split('-')[2])
        if not data.get(day):
            data[day] = float(balance)
        balance -= float(transaction['amount']['amount'])

    # add a point for days where no transaction were made
    for i in range(dt.datetime.now().day, 0, -1):
        if not data.get(i):
            if i != 1:
                for j in range(i, 0, -1):
                    if data.get(j):
                        data[i] = data[j]
                        found = True
                        break
            if i == 1 or not found:
                for j in range(1, i + 1):
                    if data.get(j):
                        data[i] = data[j]
                        break

    result['number_of_points'] = len(data)
    result['points'] = [balance for balance in OrderedDict(sorted(data.items())).values()]

    return result
