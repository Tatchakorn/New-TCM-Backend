from rest_framework import viewsets
from .models import Pulse
from .serializers import PulseSerializer


class PulseViewset(viewsets.ModelViewSet):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer

