from typing import Any
from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth import serializers as rest_auth_serializers

from .models import PatientsInfo


class PatientInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientsInfo
        fields = '__all__'
