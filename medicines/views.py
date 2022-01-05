from django.db.models import fields
from django.db.models.base import Model
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import FangMedicines, YaoMedicines
from .serializers import FangMedicinesSerializer, YaoMedicinesSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class FangMedicineFilter(filters.FilterSet):
    
    class Meta:
        model = FangMedicines
        fields = {
            'name': ['icontains',],
            'bapomofo': ['iexact',],
        }


class YaoMedicineFilter(filters.FilterSet):
    
    class Meta:
        model = YaoMedicines
        fields = {
            'name': ['icontains',],
            'bapomofo': ['iexact',],
        }


class YaoMedicinesViewset(viewsets.ModelViewSet):
    filterset_class = YaoMedicineFilter
    pagination_class = StandardResultsSetPagination
    queryset = YaoMedicines.objects.all()
    serializer_class = YaoMedicinesSerializer


class FangMedicinesViewset(viewsets.ModelViewSet):
    filterset_class = FangMedicineFilter
    pagination_class = StandardResultsSetPagination
    queryset = FangMedicines.objects.all()
    serializer_class = FangMedicinesSerializer

