from rest_framework import serializers

from authentication.models import UserProfile


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_identifier',
        ]


class ViewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'base_currency',
            'source_label',
            'yodlee_login_name',
            'nordigen_requisition'
        ]


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['id']


class ViewUserSerializerInternal(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
