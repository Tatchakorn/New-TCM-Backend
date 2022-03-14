from rest_framework import serializers
from .models import (
    WenOptionCategory,
    WangOptionCategory,
    WenOption,
    WangOption,
    PulseOption,
    DiseaseOptionCategory,
    DiseaseOption)


class PulseOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PulseOption
        fields = ('option',)


class WenOptionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WenOptionCategory
        fields = ('name',)


class WenOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WenOption
        fields = ('option', 'category',)


class WangOptionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WangOptionCategory
        fields = ('name',)


class WangOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WangOption
        fields = ('option', 'category',)


class DiseaseOptionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WangOptionCategory
        fields = ('name',)


class DiseaseOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WangOption
        fields = ('option', 'category',)