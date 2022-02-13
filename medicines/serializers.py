from rest_framework import serializers
from .models import Medicine, MedicineRecord


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
            'info',)


class MedicineRecordSerializer(serializers.ModelSerializer):
    medicineId = serializers.PrimaryKeyRelatedField(source='medicine_id', many=True, read_only=True)
    diagnosisRecordId = serializers.PrimaryKeyRelatedField(source='diagnosis_record_id', many=True, read_only=True)
    class Meta:
        model = MedicineRecord
        fields = (
            'medicineId',
            'diagnosisRecordId',
            'dosage',
            'subtotal',)
