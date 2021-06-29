from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'agent',
            'business_owner',
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'phone_number',
            'address',
            'gender',
            'profile_picture'
        )
