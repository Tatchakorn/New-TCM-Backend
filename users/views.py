from rest_framework import viewsets

from .models import Employee, EmployeeWorkSchedule
from .serializers import (
    EmployeeSerializer, 
    EmployeeWorkScheduleSerializer)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeWorkScheduleViewSet(viewsets.ModelViewSet):
    queryset = EmployeeWorkSchedule.objects.all()
    serializer_class = EmployeeWorkScheduleSerializer