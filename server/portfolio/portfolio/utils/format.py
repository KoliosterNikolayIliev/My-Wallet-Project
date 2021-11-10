def group_balances(balances: dict, holdings: dict):
    result = {}
    for provider, content in balances.items():
        for account, account_content in content['content'].items():
            name = account_content['providerName']
            data = {'provider': provider, 'id': account, 'data': {key:value for (key, value) in account_content.items() if key != "providerName"}}
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
                
                if account_content['balanceData'].get('base_currency'):
                    if result[name].get('total'):
                        result[name]['total'] += account_content['balanceData']['base_currency']
                    else:
                        result[name]['total'] = account_content['balanceData']['base_currency']
            else:
                result[name] = {'accounts': [data], 'total': account_content['balanceData']['base_currency']}

    for provider, content in {key:value for (key, value) in holdings.items() if key != "yodlee"}.items():
        for asset, asset_content in content['content'].items():
            data = {'provider': provider, 'id': asset, 'data': asset_content}

            if result.get(provider):
                if result[provider].get('accounts'):
                    result[provider]['accounts'].append(data)
                else:
                    result[provider]['accounts'] = [data]

                if asset_content.get('base_currency'):
                    if result[provider].get('total'):
                        result[provider]['total'] += asset_content['base_currency']
                    else:
                        result[provider]['total'] = asset_content['base_currency']
            else:
                if asset_content.get('base_currency'):
                    result[provider] = {'accounts': [data], 'total': asset_content['base_currency']}
                else:
                    result[provider] = {'accounts': [data], 'total': 0}
    
    return result
            