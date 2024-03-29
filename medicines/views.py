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
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class MedicineFilter(filters.FilterSet):
    class Meta:
        model = Medicine
        fields = {
            'name': ['icontains',],
            'bopomofo': ['iexact',],
            'type': ['icontains',],
            'id': ['in'],
        }


class MedicineViewset(viewsets.ModelViewSet):
    filterset_class = MedicineFilter
    pagination_class = StandardResultsSetPagination
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineRecordFilter(filters.FilterSet):
    class Meta:
        model = MedicineRecord
        fields = {
            'diagnosis_record_id' : ['exact']
        }
class MedicineRecordViewset(viewsets.ModelViewSet):
    filterset_class = MedicineRecordFilter
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


class DecoctionRecordFilter(filters.FilterSet):
    class Meta:
        model = DecoctionRecord
        fields = {
            'diagnosis_record_id' : ['exact']
        }
class DecoctionRecordViewSet(viewsets.ModelViewSet):
    filterset_class = DecoctionRecordFilter
    queryset = DecoctionRecord.objects.all()
    serializer_class = DecoctionRecordSerializers


class InjuryTreatmentViewSet(viewsets.ModelViewSet):
    
    queryset = InjuryTreatment.objects.all()
    serializer_class = InjuryTreatmentSerializers

class InjuryTreatmentRecordFilterSet(filters.FilterSet):
    class Meta:
        model = InjuryTreatmentRecord
        fields = {
            'diagnosis_id': ['exact']
        }
class InjuryTreatmentRecordViewSet(viewsets.ModelViewSet):
    filterset_class = InjuryTreatmentRecordFilterSet
    queryset = InjuryTreatmentRecord.objects.all()
    serializer_class = InjuryTreatmentRecordSerializers