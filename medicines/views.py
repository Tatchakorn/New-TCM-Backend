from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import (
    Medicine, 
    MedicineRecord,
    Decoction,
    DecoctionComponents,
    DecoctionRecord,
    )
from .serializers import (
    MedicineSerializer, 
    MedicineRecordSerializer,
    DecoctionSerializers,
    DecoctionComponentsSerializers,
    DecoctionRecordSerializers,
    )


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MedicineFilter(filters.FilterSet):
    
    class Meta:
        model = Medicine
        fields = {
            'name': ['icontains',],
            'bopomofo': ['iexact',],
            'type': ['icontains',],
        }


class MedicineViewset(viewsets.ModelViewSet):
    filterset_class = MedicineFilter
    pagination_class = StandardResultsSetPagination
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineRecordViewset(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = MedicineRecord.objects.all()
    serializer_class = MedicineRecordSerializer


class DecoctionViewSet(viewsets.ModelViewSet):
    
    queryset = Decoction.objects.all()
    serializer_class = DecoctionSerializers


class DecoctionComponentsViewSet(viewsets.ModelViewSet):
    
    queryset = DecoctionComponents.objects.all()
    serializer_class = DecoctionComponentsSerializers


class DecoctionRecordViewSet(viewsets.ModelViewSet):
    
    queryset = DecoctionRecord.objects.all()
    serializer_class = DecoctionRecordSerializers