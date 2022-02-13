from dataclasses import fields
from rest_framework import serializers
from .models import Acupuncture, AcupunctureRecord


class AcupunctureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acupuncture
        fields = ('name', 'area', 'info')


class AcupunctureRecordSerializer(serializers.ModelSerializer):
    acupunctureId = serializers.PrimaryKeyRelatedField(source='acupuncture_id', many=True, read_only=True)
    diagnosisRecordId = serializers.PrimaryKeyRelatedField(source='diagnosis_record_id', many=True, read_only=True)
    acupunctureRecordTime = serializers.CharField(source='acupuncture_record_time')
    class Meta:
        model = AcupunctureRecord
        fields = (
            'acupunctureId', 
            'diagnosisRecordId', 
            'acupunctureRecordTime',)