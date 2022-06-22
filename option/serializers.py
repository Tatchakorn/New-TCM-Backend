from rest_framework import serializers
from .models import (
    WenOptionCategory,
    WangOptionCategory,
    WenOption,
    WangOption,
    PulseOption,
    DiseaseOptionCategory,
    DiseaseOption,
    EyeCategory,
    EyeOption,
    TongueCategory,
    TongueOption,)


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
        model = DiseaseOptionCategory
        fields = ('name',)


class DiseaseOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiseaseOption
        fields = ('option', 'category',)


class EyeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = EyeCategory
        fields = ('name',)


class EyeOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EyeOption
        fields = ('option', 'category',)


class TongueCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TongueCategory
        fields = ('name',)


class TongueOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TongueOption
        fields = ('option', 'category',)