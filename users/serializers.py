from typing import Any
from rest_framework import serializers

from .models import (
    CustomUser, OwnPatient, PastPatient
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'role',)


class PastPatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PastPatient
        fields = ('id', 'doctor', 'patients',)


class OwnPatientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OwnPatient
        fields = ('id', 'doctor', 'patients',)
