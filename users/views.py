from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Employee, EmployeeWorkSchedule
from .serializers import (
    EmployeeSerializer, 
    EmployeeWorkScheduleSerializer)


class EmployeeViewSet(viewsets.ModelViewSet): 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class WorkScheduleFilter(filters.FilterSet):
    class Meta:
        model = EmployeeWorkSchedule
        fields = {
            'employee_work_schedule_day_period': ['iexact',],
        }

class EmployeeWorkScheduleViewSet(viewsets.ModelViewSet):
    filterset_class = WorkScheduleFilter
    queryset = EmployeeWorkSchedule.objects.all()
    serializer_class = EmployeeWorkScheduleSerializer
