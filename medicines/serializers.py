from rest_framework import serializers
from .models import (
    Medicine, 
    MedicineRecord,
    Decoction,
    DecoctionComponents,
    DecoctionRecord,
    InjuryTreatment,
    InjuryTreatmentRecord,
    )


class MedicineSerializer(serializers.ModelSerializer):
    nhiId = serializers.CharField(source='nhi_id')
    nhiName = serializers.CharField(source='nhi_name')

    class Meta:
        model = Medicine
        fields = (
            'id',
            'name', 
            'type', 
            'bopomofo',
            'nhiId', 
            'nhiName', 
            'cost', 
            'price', 
            'info',
            'unit',
            'manufacturer',)


class MedicineRecordSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source="medicine_id.name", read_only=True)
    medicine_unit = serializers.CharField(source="medicine_id.unit", read_only=True)
    class Meta:
        model = MedicineRecord
        fields = (
            'medicine_id',
            'medicine_name',
            'medicine_unit',
            'diagnosis_record_id',
            'dosage',
            'subtotal',)


class DecoctionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Decoction
        fields = (
            'id',
            'name',
            'bopomofo',
            'cost', 
            'price', 
            'info',)


class DecoctionComponentsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = DecoctionComponents
        fields = (
            'id',
            'decoction_id',
            'medicine_id',
            'dosage',
            'unit',
        )


class DecoctionRecordSerializers(serializers.ModelSerializer):
    
    decoction_component_data = DecoctionComponentsSerializers(source="decoction_component_id", read_only=True)
    class Meta:
        model = DecoctionRecord
        fields = (
            'decoction_component_id',
            'diagnosis_record_id',
            'decoction_component_data',
            'dosage',
            'subtotal',
        )


class InjuryTreatmentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = InjuryTreatment
        fields = [
            'id',
            'code',
            'name',
            'unit'
        ]


class InjuryTreatmentRecordSerializers(serializers.ModelSerializer):
    injury_treatment_data = InjuryTreatmentSerializers(source="injury_treatment_id", read_only=True)
    class Meta:
        model = InjuryTreatmentRecord
        fields = [
            'id',
            'part',
            'time',
            'unit',
            'injury_treatment_id',
            'injury_treatment_data',
            'diagnosis_id'
        ]
