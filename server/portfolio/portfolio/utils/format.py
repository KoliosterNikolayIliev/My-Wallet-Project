def group_balances(balances: dict, holdings: dict):
    result = {}
    for provider, content in balances.items():
        for account, account_content in content['content'].items():
            name = account_content['providerName']
            data = {'id': account, 'data': {key:value for (key, value) in account_content.items() if key != "providerName"}}
            for key, value in holdings.items():
                if key == "yodlee":
                    holdings_data = []
                    for asset, asset_content in value['content'].items():
                        if str(asset_content['parent']) == account:
                            holdings_data.append(asset_content)
                    data['holdings'] = holdings_data
            if result.get(name):
                result[name].append(data)
            else:
                result[name] = [data]
        
    for provider, content in {key:value for (key, value) in holdings.items() if key != "yodlee"}.items():
        for asset, asset_content in content['content'].items():
            data = {'id': asset, 'data': asset_content}
            if result.get(provider):
                result[provider].append(data)
            else:
                result[provider] = [data]
    
    return result
            