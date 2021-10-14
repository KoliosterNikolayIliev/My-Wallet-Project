from rest_framework import serializers

from api.models import UserAssets


def validate_user_key(user_key):
    if not user_key:
        raise serializers.ValidationError('User key was not provided')

    # if there is no user assets object with that user_key we create one
    if not UserAssets.objects.filter(user_key=user_key):
        UserAssets.objects.create(user_key=user_key)
