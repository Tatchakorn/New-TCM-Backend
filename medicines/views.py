from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import (
    Medicine, 
    MedicineRecord,
    Decoction,
    DecoctionComponents,
    DecoctionRecord,
    InjuryTreatment,
    InjuryTreatmentRecord,
    )
from .serializers import (
    MedicineSerializer, 
    MedicineRecordSerializer,
    DecoctionSerializers,
    DecoctionComponentsSerializers,
    DecoctionRecordSerializers,
    InjuryTreatmentSerializers,
    InjuryTreatmentRecordSerializers,
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

class DecoctionFilter(filters.FilterSet):
    
    class Meta:
        model = Decoction
        fields = {
            'bopomofo': ['iexact',],
        }
class DecoctionViewSet(viewsets.ModelViewSet):
    filterset_class = DecoctionFilter
    queryset = Decoction.objects.all()
    serializer_class = DecoctionSerializers


class DecoctionComponentsFilter(filters.FilterSet):
    class Meta:
        model = DecoctionComponents
        fields = {
            'decoction_id': ['exact',],
        }

class DecoctionComponentsViewSet(viewsets.ModelViewSet):
    filterset_class = DecoctionComponentsFilter
    queryset = DecoctionComponents.objects.all()
    serializer_class = DecoctionComponentsSerializers


class DecoctionRecordViewSet(viewsets.ModelViewSet):
    
    queryset = DecoctionRecord.objects.all()
    serializer_class = DecoctionRecordSerializers


class InjuryTreatmentViewSet(viewsets.ModelViewSet):
    
    queryset = InjuryTreatment.objects.all()
    serializer_class = InjuryTreatmentSerializers


class InjuryTreatmentRecordViewSet(viewsets.ModelViewSet):
    
    queryset = InjuryTreatmentRecord.objects.all()
    serializer_class = InjuryTreatmentRecordSerializers