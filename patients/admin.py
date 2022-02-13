from django.contrib import admin
from .models import (
    Patient,
    PatientRegisterRecord,
    DiagnosisRecord,
    EyeImage,
    TongueImage)

admin.site.register([
    Patient,
    PatientRegisterRecord,
    DiagnosisRecord,
    EyeImage,
    TongueImage])
