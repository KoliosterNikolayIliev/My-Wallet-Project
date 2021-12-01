from rest_framework import serializers


def validate_user_identifier(user_identifier):
    if not user_identifier:
        raise serializers.ValidationError('User identifier was not provided')

