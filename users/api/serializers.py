from rest_framework import serializers

from ..models import User


class UserSerializerForRegistration(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    stir = serializers.CharField(write_only=True)
    market = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'phone_number', 'password', 'type', 'market', 'stir')
        lookup_field = 'phone_number'
