from rest_framework import serializers
from .models import (
    Medicine, 
    MedicineRecord,
    Decoction,
    DecoctionComponents,
    DecoctionRecord,
    )


class MedicineSerializer(serializers.ModelSerializer):
    nhiId = serializers.CharField(source='nhi_id')
    nhiName = serializers.CharField(source='nhi_name')

    class Meta:
        model = Medicine
        fields = (
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
            'name',
            'bopomofo',
            'cost', 
            'price', 
            'info', 
        )


class DecoctionComponentsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = DecoctionComponents
        fields = (
            'decoction_id',
            'medicine_id',
            'dosage',
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


