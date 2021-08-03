from rest_framework import serializers

from .models import PatientsInfo


class PatientInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientsInfo
        fields = '__all__'
