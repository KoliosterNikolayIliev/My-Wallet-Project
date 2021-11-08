from rest_framework import serializers

from api.models import UserAssets


def validate_user_key(user_key):
    if not user_key:
        raise serializers.ValidationError('User key was not provided')

    # if there is no user assets object with that user_key we create one
    if not UserAssets.objects.filter(user_key=user_key):
        UserAssets.objects.create(user_key=user_key)


def add_or_increment_asset(user_assets, validated_data):
    asset_exist = False

    for asset in user_assets:
        if asset['type'] == validated_data['type']:
            asset_exist = True
            asset['amount'] += validated_data['amount']
            break

    if not asset_exist:
        user_assets.append(validated_data)

    return user_assets
