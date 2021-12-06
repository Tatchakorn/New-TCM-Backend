from django.db import models
from rest_framework import serializers
from .models import PatientsInfo, DiagnosisInfo, YanImages, SheImages


class YanImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    date = serializers.DateTimeField(
        source='register_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = YanImages
        fields = ('id', 'diagnosis', 'image', 'date', 'remark',)


class SheImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    date = serializers.DateTimeField(
        source='register_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = SheImages
        fields = ('id', 'diagnosis', 'image', 'date', 'remark',)


class DiagnosisInfoSerializer(serializers.ModelSerializer):
    diagnosisData = serializers.JSONField(source='diagnosis_data')
    medicalHistory = serializers.JSONField(source='medical_history')
    diagnosisDesc = serializers.CharField(source='diagnosis_desc')
    yanImages = YanImagesSerializer(
        many=True, read_only=True, source='yan_imgs')
    sheImages = SheImagesSerializer(
        many=True, read_only=True, source='she_imgs')

    class Meta:
        model = DiagnosisInfo
        fields = (
            'id', 
            'patient', 
            'diagnosisData', 
            'yanImages', 
            'sheImages', 
            'medicalHistory',
            'diagnosisDesc',
            'physique',
        )


class PatientInfoSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='pk')
    cardId = serializers.CharField(source='card_id')
    consultationNo = serializers.IntegerField(source='consultation_no')
    medicalOrderNumber = serializers.CharField(source='medical_order_number')
    registerTime = serializers.DateTimeField(
        source='register_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    # diagnosis = DiagnosisInfoSerializer(many=True, read_only=True)

    class Meta:
        model = PatientsInfo
        fields = (
            'id',
            'name',
            'gender',
            'arrears',
            'department',
            'path',
            'period',
            'remark',
            'selected',
            'status',
            'cardId',
            'consultationNo',
            'medicalOrderNumber',
            'registerTime',
        )