from django.contrib import admin
from .models import PatientsInfo, DiagnosisInfo, SheImages, YanImages

admin.site.register([PatientsInfo, DiagnosisInfo, YanImages, SheImages])
