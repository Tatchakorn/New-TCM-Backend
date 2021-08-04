from rest_framework import viewsets

from .models import PatientsInfo
from .serializers import PatientInfoSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer
