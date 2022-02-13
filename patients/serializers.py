from rest_framework import serializers
from .models import (
    Patient,
    PatientRegisterRecord,
    DiagnosisRecord,
    EyeImage,
    TongueImage)


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
    patientId = serializers.PrimaryKeyRelatedField(source='patient_id', many=True, read_only=True)
    recordTime = serializers.DateTimeField(
        source='record_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = PatientRegisterRecord
        fields = (
            'patientId',
            'recordTime',
            'payment',)


class DiagnosisRecordSerializer(serializers.ModelSerializer):
    patientRegisterRecordId = serializers.PrimaryKeyRelatedField(source='patient_register_record_id', many=True, read_only=True)
    employeeWorkScheduleId = serializers.PrimaryKeyRelatedField(source='employee_work_schedule_id', many=True, read_only=True)
    patientId = serializers.PrimaryKeyRelatedField(source='patient_id', many=True, read_only=True)
    employeeId = serializers.PrimaryKeyRelatedField(source='employee_id', many=True, read_only=True)
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
            'patientRegisterRecordId', 
            'employeeWorkScheduleId',
            'patientId',
            'employeeId',
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
    patientId = serializers.PrimaryKeyRelatedField(source='patient_id', many=True, read_only=True)
    diagnosisRecordId = serializers.PrimaryKeyRelatedField(source='diagnosis_record_id', many=True, read_only=True)
    uploadDate = serializers.DateTimeField(
        source='upload_date',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = EyeImage
        fields = ('diagnosisRecordId', 'patientId', 'image', 'uploadDate',)


class TongueImageSerializer(serializers.ModelSerializer):
    patientId = serializers.PrimaryKeyRelatedField(source='patient_id', many=True, read_only=True)
    diagnosisRecordId = serializers.PrimaryKeyRelatedField(source='diagnosis_record_id', many=True, read_only=True)
    uploadDate = serializers.DateTimeField(
        source='upload_date',
        format=r"%a, %d %b %Y %H:%M:%S %Z")
    
    class Meta:
        model = TongueImage
        fields = ('diagnosisRecordId', 'patientId', 'image', 'uploadDate',)
        