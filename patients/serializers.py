from rest_framework import serializers
from .models import PatientsInfo, DiagnosisInfo


class PatientInfoSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(source='pk')
    cardId = serializers.CharField(source='card_id')
    consultationNo = serializers.IntegerField(source='consultation_no')
    medicalOrderNumber = serializers.CharField(source='medical_order_number')
    registerTime = serializers.DateTimeField(source='register_time', format=r"%a, %d %b %Y %H:%M:%S %Z")
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


class DiagnosisInfoSerializer(serializers.ModelSerializer):
    diagnosisData = serializers.JSONField(source='diagnosis_data')
    serializers.ImageField
    class Meta:
        model = DiagnosisInfo
        fields = ('diagnosisData', 'gan_img', 'she_img',)
    