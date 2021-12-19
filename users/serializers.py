from typing import Any
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

from patients.serializers import OwnedPatientsSerializers

class UserSerializer(serializers.ModelSerializer):
    ownedPatients = OwnedPatientsSerializers(
        many=True, read_only=True, source='owned_patients')
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'role', 'email', 'ownedPatients')


class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2', ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # def save(self, request):
    def save(self, *args, **kwargs):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        # user.user_permissions.set(['is_active'], True)
        return user
