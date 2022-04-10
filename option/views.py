from rest_framework import viewsets
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
from .serializers import (
    WenOptionCategorySerializer,
    WangOptionCategorySerializer,
    WenOptionSerializer,
    WangOptionSerializer,
    PulseOptionSerializer,
    DiseaseOptionCategorySerializer,
    DiseaseOptionSerializer,
    EyeCategorySerializer,
    EyeOptionSerializer,
    TongueCategorySerializer,
    TongueOptionSerializer,)


class WenOptionCategoryViewset(viewsets.ModelViewSet):
    queryset = WenOptionCategory.objects.all()
    serializer_class = WenOptionCategorySerializer


class WangOptionCategoryViewset(viewsets.ModelViewSet):
    queryset = WangOptionCategory.objects.all()
    serializer_class = WangOptionCategorySerializer


class WenOptionViewset(viewsets.ModelViewSet):
    queryset = WenOption.objects.all()
    serializer_class = WenOptionSerializer


class WangOptionViewset(viewsets.ModelViewSet):
    queryset = WangOption.objects.all()
    serializer_class = WangOptionSerializer


class PulseOptionViewset(viewsets.ModelViewSet):
    queryset = PulseOption.objects.all()
    serializer_class = PulseOptionSerializer


class DiseaseOptionViewset(viewsets.ModelViewSet):
    queryset = DiseaseOption.objects.all()
    serializer_class = DiseaseOptionSerializer


class DiseaseOptionCategoryViewset(viewsets.ModelViewSet):
    queryset = DiseaseOptionCategory.objects.all()
    serializer_class = DiseaseOptionCategorySerializer


class EyeOptionViewset(viewsets.ModelViewSet):
    queryset = EyeOption.objects.all()
    serializer_class = EyeOptionSerializer


class EyeCategoryViewset(viewsets.ModelViewSet):
    queryset = EyeCategory.objects.all()
    serializer_class = EyeCategorySerializer


class TongueOptionViewset(viewsets.ModelViewSet):
    queryset = TongueOption.objects.all()
    serializer_class = TongueOptionSerializer


class TongueCategoryViewset(viewsets.ModelViewSet):
    queryset = TongueCategory.objects.all()
    serializer_class = TongueCategorySerializer