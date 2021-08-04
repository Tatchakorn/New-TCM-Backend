from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .models import PatientsInfo
from .serializers import PatientInfoSerializer, UserSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class PatientDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientsInfo.objects.all()
    serializer_class = PatientInfoSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
