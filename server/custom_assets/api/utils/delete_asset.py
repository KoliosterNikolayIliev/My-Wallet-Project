def delete_asset(assets: list, asset_to_delete: str):
    target_index = 0
    found = False

    for index, asset in enumerate(assets):
        if asset['type'] == asset_to_delete:
            target_index = index
            found = True

    if found:
        assets.pop(target_index)
        return True

    return False
