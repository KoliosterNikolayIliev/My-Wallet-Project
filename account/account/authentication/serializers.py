from rest_framework import serializers

from authentication.models import UserProfile, NordigenRequisition


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
        ]


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['id']


class ViewUserSerializerInternal(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class NordigenRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NordigenRequisition
        fields = ['user', 'institution_id', 'requisition_id', 'confirmation_link']

