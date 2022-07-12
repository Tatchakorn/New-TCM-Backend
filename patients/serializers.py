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
    
    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'gender',
            'birthday',
            'nhi_card_num',
            'id_num',
            'phone_number',
            'address',
            'height',
            'weight',
            'blood_type',
            'med_history',
            'body_fitness',
            'physique',
            'emergency_contact_name',
            'emergency_contact_phone',
            'emergency_contact_rel',
            'job',
            'edu_level',
            'marriage',
            'note',
        )


class PatientRegisterRecordSerializer(serializers.ModelSerializer):
    record_time = serializers.DateTimeField(
        format=r"%a, %d %b %Y %H:%M:%S %Z",
        read_only=True)
    
    class Meta:
        model = PatientRegisterRecord
        fields = (
            'patient_id',
            'record_time',
            'payment',)


class DiagnosisRecordSerializer(serializers.ModelSerializer):
    record_time = serializers.DateTimeField(
        source='diagnosis_record_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z",
        read_only=True)


    class Meta:
        model = DiagnosisRecord
        fields = ( 
            'patient_register_record_id', 
            'employee_work_schedule_id',
            'patient_id',
            'employee_id',
            'main_complaint',
            'pulse',
            'disease_icd_code',
            'codisease_icd_code',
            'codisease_icd_code_2',
            'medicine_way',
            'decoction_pack_amout',
            'decoction_cook_way',
            'decoction_way',
            'decoction_total_amount',
            'med_pack_amount',
            'med_day',
            'med_total_amount',
            'record_time',
        )


class EyeImageSerializer(serializers.ModelSerializer):
    upload_date = serializers.DateTimeField(
        format=r"%a, %d %b %Y %H:%M:%S %Z",
        read_only=True)
    
    class Meta:
        model = EyeImage
        fields = (
            # 'diagnosis_record_id', 
            'patient_id', 
            'image', 
            'upload_date', 
            'description',)


class TongueImageSerializer(serializers.ModelSerializer):
    upload_date = serializers.DateTimeField(
        format=r"%a, %d %b %Y %H:%M:%S %Z",
        read_only=True)
    
    class Meta:
        model = TongueImage
        fields = (
            # 'diagnosis_record_id', 
            'patient_id', 
            'image', 
            'upload_date', 
            'description',)


class OtherMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherMedia
        fields = ('patient_id', 'upload_date', 'file', 'description',)