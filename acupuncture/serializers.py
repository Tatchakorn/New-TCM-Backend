from dataclasses import fields
from rest_framework import serializers
from .models import (
    Acupuncture, 
    DongAcupuncture, 
    AcupunctureArea, 
    DongAcupunctureArea)


class AcupunctureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acupuncture
        fields = '__all__'


class DongAcupunctureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DongAcupuncture
        fields = '__all__'


class AcupunctureAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcupunctureArea
        fields = '__all__'


class DongAcupunctureAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DongAcupunctureArea
        fields = '__all__'