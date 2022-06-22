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
            'manufacturer',)


class MedicineRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MedicineRecord
        fields = (
            'medicine_id',
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
            'decoction_id',
            'medicine_id',
            'dosage',
            'unit',
        )


class DecoctionRecordSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = DecoctionRecord
        fields = (
            'decoction_id',
            'diagnosis_record_id',
            'dosage',
            'subtotal',
        )


class InjuryTreatmentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = InjuryTreatment
        fields = '__all__'


class InjuryTreatmentRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = InjuryTreatmentRecord
        fields = '__all__'
