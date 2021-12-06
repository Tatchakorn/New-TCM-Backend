from rest_framework import serializers
from .models import FangMedicines, YaoMedicines


class YaoMedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = YaoMedicines
        fields = '__all__'

class FangMedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FangMedicines
        fields = '__all__'
