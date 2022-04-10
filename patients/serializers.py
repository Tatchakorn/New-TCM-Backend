from rest_framework import serializers
from .models import (
    Patient,
    PatientRegisterRecord,
    DiagnosisRecord,
    EyeImage,
    TongueImage,
    OtherMedia
    )


class PatientSerializer(serializers.ModelSerializer):
    nhiCardNum = serializers.CharField(source='nhi_card_num')
    idNum = serializers.CharField(source='id_num')
    phoneNumber = serializers.CharField(source='phone_number')
    bloodType = serializers.CharField(source='blood_type')
    emergencyContactName = serializers.CharField(source='emergency_contact_name')
    emergencyContactPhone = serializers.CharField(source='emergency_contact_phone')
    emergencyContactRelation = serializers.CharField(source='emergency_contact_rel')
    eduLevel = serializers.CharField(source='edu_level')
    
    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'gender',
            'birthday',
            'nhiCardNum',
            'idNum',
            'phoneNumber',
            'address',
            'height',
            'weight',
            'bloodType',
            'emergencyContactName',
            'emergencyContactPhone',
            'emergencyContactRelation',
            'job',
            'eduLevel',
            'marriage',
            'note',
        )


class PatientRegisterRecordSerializer(serializers.ModelSerializer):
    recordTime = serializers.DateTimeField(
        source='record_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = PatientRegisterRecord
        fields = (
            'patient_id',
            'recordTime',
            'payment',)


class DiagnosisRecordSerializer(serializers.ModelSerializer):
    medHistory = serializers.CharField(source='med_history')
    mainComplaint = serializers.CharField(source='main_complaint')
    diseaseName = serializers.CharField(source='disease_name')
    medPackAmount = serializers.DecimalField(source='med_pack_amount', max_digits=10, decimal_places=2)
    medDay = serializers.IntegerField(source='med_day')
    medTotalAmount = serializers.DecimalField(source='med_total_amount', max_digits=10, decimal_places=2)
    recordTime = serializers.DateTimeField(
        source='diagnosis_record_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")


    class Meta:
        model = DiagnosisRecord
        fields = (
            'patient_register_record_id', 
            'employee_work_schedule_id',
            'patient_id',
            'employee_id',
            'medHistory',
            'mainComplaint',
            'pulse',
            'diseaseName',
            'medPackAmount',
            'medDay',
            'medTotalAmount',
            'recordTime',
        )


class EyeImageSerializer(serializers.ModelSerializer):
    uploadDate = serializers.DateTimeField(
        source='upload_date',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = EyeImage
        fields = (
            # 'diagnosis_record_id', 
            'patient_id', 
            'image', 
            'uploadDate', 
            'description',)


class TongueImageSerializer(serializers.ModelSerializer):
    uploadDate = serializers.DateTimeField(
        source='upload_date',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = TongueImage
        fields = (
            # 'diagnosis_record_id', 
            'patient_id', 
            'image', 
            'uploadDate', 
            'description',)


class OtherMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherMedia
        fields = ('patient_id', 'upload_date', 'file', 'description',)