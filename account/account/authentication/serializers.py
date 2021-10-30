from rest_framework import serializers

from authentication.models import UserProfile, NordigenRequisition


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user_identifier',
        ]


class ViewUserSerializer(serializers.ModelSerializer):
    nordigen_requisition = serializers.PrimaryKeyRelatedField(many=True, queryset=NordigenRequisition.objects.all())

    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'base_currency',
            'source_label',
            'nordigen_requisition',
        ]


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['id']


class ViewUserSerializerInternal(serializers.ModelSerializer):
    Nordigen_requisitions = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class NordigenRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NordigenRequisition
        exclude = ['user']
