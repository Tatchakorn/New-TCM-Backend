from django.db.models.query import QuerySet
from rest_framework import generics

from .models import PatientsInfo
from .serializers import PatientInfoSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class PatientDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer
