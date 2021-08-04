from typing import Any
from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth import serializers as rest_auth_serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


# Use Email for authentication
class LoginSerializer(rest_auth_serializers.LoginSerializer):
    def get_fields(self) -> Any:
        fields = super(LoginSerializer, self).get_fields()
        fields['email'] = fields['username']
        del fields['username']
        return fields

    def validate(self, attrs) -> Any:
        attrs['username'] = attrs['email']
        del attrs['email']
        return super(LoginSerializer, self).validate(attrs)
