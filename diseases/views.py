from rest_framework import viewsets
from .models import Diseases
from .serializers import DiseasesSerializer


class DiseasesViewset(viewsets.ModelViewSet):
    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializer
