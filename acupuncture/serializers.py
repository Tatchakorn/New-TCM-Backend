from dataclasses import fields
from rest_framework import serializers
from .models import Acupuncture, AcupunctureRecord


class AcupunctureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acupuncture
        fields = ('name', 'area', 'info')


class AcupunctureRecordSerializer(serializers.ModelSerializer):
    acupunctureRecordTime = serializers.CharField(source='acupuncture_record_time')
    class Meta:
        model = AcupunctureRecord
        fields = (
            'acupuncture_id', 
            'diagnosis_record_id', 
            'acupunctureRecordTime',)