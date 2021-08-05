from rest_framework import viewsets

from .models import (
    CustomUser, OwnPatient, PastPatient
)

from .serializers import (
    UserSerializer, OwnPatientSerializer, PastPatientSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class PastPatientViewSet(viewsets.ModelViewSet):
    queryset = PastPatient.objects.all()
    serializer_class = PastPatientSerializer


class OwnPatientViewSet(viewsets.ModelViewSet):
    queryset = OwnPatient.objects.all()
    serializer_class = OwnPatientSerializer

