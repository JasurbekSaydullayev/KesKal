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


# class UserChangePasswordSerializer(serializers.ModelSerializer):
#     old_password = serializers.CharField(max_length=128, write_only=True)
#     new_password = serializers.CharField(max_length=128, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('old_password', 'new_password')


# class UserPasswordRecoverySerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=13, write_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('phone_number', 'password')
