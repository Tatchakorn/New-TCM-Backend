from django.contrib import admin
from .models import PatientsInfo, DiagnosisInfo

admin.site.register([PatientsInfo, DiagnosisInfo])