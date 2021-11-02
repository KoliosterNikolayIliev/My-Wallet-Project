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


class NordigenRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NordigenRequisition
        fields = ['user', 'institution_id', 'requisition_id', 'confirmation_link']


class ViewUserSerializerInternal(serializers.ModelSerializer):
    nordigenrequisition_set = NordigenRequisitionSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
