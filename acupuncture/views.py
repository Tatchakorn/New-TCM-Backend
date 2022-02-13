from rest_framework import viewsets
from .models import Acupuncture, AcupunctureRecord
from .serializers import AcupunctureSerializer, AcupunctureRecordSerializer

class AcupunctureViewset(viewsets.ModelViewSet):
    queryset = Acupuncture.objects.all()
    serializer_class = AcupunctureSerializer


class AcupunctureRecordViewset(viewsets.ModelViewSet):
    queryset = AcupunctureRecord.objects.all()
    serializer_class = AcupunctureRecordSerializer

