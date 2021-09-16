from typing import Any
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'role',)


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password', 'password2', ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_email(self, email):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a
        # username.
        try:
            match = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise serializers.ValidationError(
            'This email address is already in use.')

    def save(self, request):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role=self.validated_data['role'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user.set_password(password)
        user.user_permissions.set(['is_active'], True)
        user.save()
        return user
