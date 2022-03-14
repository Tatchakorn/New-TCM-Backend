from rest_framework import viewsets
from .models import (
    WenOptionCategory,
    WangOptionCategory,
    WenOption,
    WangOption,
    PulseOption,
    DiseaseOptionCategory,
    DiseaseOption)
from .serializers import (
    WenOptionCategorySerializer,
    WangOptionCategorySerializer,
    WenOptionSerializer,
    WangOptionSerializer,
    PulseOptionSerializer,
    DiseaseOptionCategorySerializer,
    DiseaseOptionSerializer)


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