from rest_framework import viewsets
from .models import (
    Acupuncture, 
    DongAcupuncture, 
    AcupunctureArea, 
    DongAcupunctureArea)
from .serializers import (
    AcupunctureSerializer,
    DongAcupunctureSerializer,
    AcupunctureAreaSerializer,
    DongAcupunctureAreaSerializer)


class AcupunctureViewset(viewsets.ModelViewSet):
    queryset = Acupuncture.objects.all()
    serializer_class = AcupunctureSerializer


class DongAcupunctureViewset(viewsets.ModelViewSet):
    queryset = DongAcupuncture.objects.all()
    serializer_class = DongAcupunctureSerializer


class AcupunctureAreaViewset(viewsets.ModelViewSet):
    queryset = AcupunctureArea.objects.all()
    serializer_class = AcupunctureAreaSerializer


class DongAcupunctureAreaViewset(viewsets.ModelViewSet):
    queryset = DongAcupunctureArea.objects.all()
    serializer_class = DongAcupunctureAreaSerializer