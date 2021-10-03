from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import viewsets, renderers
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import PatientsInfo, DiagnosisInfo, SheImages, YanImages
from .serializers import PatientInfoSerializer, DiagnosisInfoSerializer, SheImagesSerializer, YanImagesSerializer
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


class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = DiagnosisInfo.objects.all()
    serializer_class = DiagnosisInfoSerializer


class YanImagesViewSet(viewsets.ModelViewSet):
    queryset = YanImages.objects.all()
    serializer_class = YanImagesSerializer


class SheImagesViewSet(viewsets.ModelViewSet):
    queryset = SheImages.objects.all()
    serializer_class = SheImagesSerializer
