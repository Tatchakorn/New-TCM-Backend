from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import PatientsInfo, DiagnosisInfo
from .serializers import PatientInfoSerializer, DiagnosisInfoSerializer
from .models import DiagnosisInfo


class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer

    def post(self, request, format=None):
        print(request.data)


class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = DiagnosisInfo.objects.all()
    serializer_class = DiagnosisInfoSerializer
    # parser_classes = [FileUploadParser]

    # def post(self, request, format=None):
    #     serializers = DiagnosisInfoSerializer(data=request.data)
    #     file = request.data['file']
    #     image = DiagnosisInfo.objects.create(she=file)
    #     if serializers.is_valid():
    #         serializers.save()
    #         Response(serializers.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)

    
