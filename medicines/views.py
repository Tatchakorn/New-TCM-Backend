from rest_framework import viewsets
from .models import Medicines
from .serializers import MedicinesSerializer


class MedicinesViewset(viewsets.ModelViewSet):
    queryset = Medicines.objects.all()
    serializer_class = MedicinesSerializer

