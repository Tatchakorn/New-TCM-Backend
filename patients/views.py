from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import (
    Patient,
    PatientRegisterRecord,
    DiagnosisRecord,
    EyeImage,
    TongueImage,
    # TestVid
    )
from .serializers import (
    PatientSerializer, 
    PatientRegisterRecordSerializer, 
    DiagnosisRecordSerializer, 
    EyeImageSerializer,
    TongueImageSerializer,
    # TestVidSerializer
    )


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PatientFilter(filters.FilterSet):
    
    class Meta:
        model = Patient
        fields = {
            'name': ['icontains',],
            'nhi_card_num': ['icontains',],
        }


# class DiagnosisRecordFilter(filters.FilterSet):
    
#     class Meta:
#         model = DiagnosisRecord
#         fields = ['patient_id',]


class PatientViewSet(viewsets.ModelViewSet):
    filterset_class = PatientFilter
    pagination_class = StandardResultsSetPagination
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRegisterRecordViewSet(viewsets.ModelViewSet):
    queryset = PatientRegisterRecord.objects.all()
    serializer_class = PatientRegisterRecordSerializer


class DiagnosisRecordViewSet(viewsets.ModelViewSet):
    # filterset_class = DiagnosisRecord
    queryset = DiagnosisRecord.objects.all()
    serializer_class = DiagnosisRecordSerializer


class EyeImageViewSet(viewsets.ModelViewSet):
    queryset = EyeImage.objects.all()
    serializer_class = EyeImageSerializer


class TongueImageViewSet(viewsets.ModelViewSet):
    queryset = TongueImage.objects.all()
    serializer_class = TongueImageSerializer


# class TestVidViewSet(viewsets.ModelViewSet):
#     queryset = TestVid.objects.all()
#     serializer_class = TestVidSerializer