from users.serializers import EmployeeWorkScheduleSerializer
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
    
    patient_data = PatientSerializer(source="patient_id", read_only=True)
    employee_work_schedule_data = EmployeeWorkScheduleSerializer(source="employee_work_schedule_id", read_only=True)
    class Meta:
        model = PatientRegisterRecord
        fields = (
            'id',
            'patient_data',
            'record_time',
            'patient_id',
            'payment',
            'employee_work_schedule_id',
            'diagnosis_record_id',
            'register_sequence',
            'employee_work_schedule_data'
            )
        extra_kwargs = { 'patient_id': {'write_only': True}, 'employee_work_schedule_id': {'write_only': True, 'required': True} }



class DiagnosisRecordSerializer(serializers.ModelSerializer):
    record_time = serializers.DateTimeField(
        source='diagnosis_record_time',
        format=r"%a, %d %b %Y %H:%M:%S %Z",
        read_only=True)


    class Meta:
        model = DiagnosisRecord
        fields = ( 
            'id',
            'employee_work_schedule_id',
            'patient_id',
            'employee_id',
            'main_complaint',
            'pulse',
            'disease_name',
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