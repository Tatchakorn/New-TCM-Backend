from rest_framework import viewsets, renderers
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import (
    PatientsInfo, 
    DiagnosisInfo, 
    SheImages, 
    YanImages,
    OwnedPatients,
    PastPatients,)
from .serializers import (
    PatientInfoSerializer, 
    DiagnosisInfoSerializer, 
    SheImagesSerializer, 
    YanImagesSerializer,
    OwnedPatientsSerializers,
    PastPatientsSerializers,)
from .models import DiagnosisInfo


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpeg'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class PNGRenderer(renderers.BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PatientFilter(filters.FilterSet):
    
    class Meta:
        model = PatientsInfo
        fields = {
            'name': ['icontains',],
            'medical_order_number': ['iexact',],
        }


class DiagnosisFilter(filters.FilterSet):
    
    class Meta:
        model = DiagnosisInfo
        fields = ['patient',]


class PatientViewSet(viewsets.ModelViewSet):
    filterset_class = PatientFilter
    pagination_class = StandardResultsSetPagination
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    filterset_class = DiagnosisFilter
    queryset = DiagnosisInfo.objects.all()
    serializer_class = DiagnosisInfoSerializer


class YanImagesViewSet(viewsets.ModelViewSet):
    queryset = YanImages.objects.all()
    serializer_class = YanImagesSerializer


class SheImagesViewSet(viewsets.ModelViewSet):
    queryset = SheImages.objects.all()
    serializer_class = SheImagesSerializer


class OwnedPatientsViewSet(viewsets.ModelViewSet):
    queryset = OwnedPatients.objects.all()
    serializer_class = OwnedPatientsSerializers


class PastPatientsViewSet(viewsets.ModelViewSet):
    queryset = PastPatients.objects.all()
    serializer_class = PastPatientsSerializers