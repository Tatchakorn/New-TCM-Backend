from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import PatientsInfo
from .serializers import PatientInfoSerializer, UserSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
