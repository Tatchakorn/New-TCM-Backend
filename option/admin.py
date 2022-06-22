from django.contrib import admin

from .models import (
    WenOptionCategory,
    WenOption,
    WangOptionCategory,
    WangOption,
    DiseaseOptionCategory,
    PulseOption,
    EyeOption, 
    EyeCategory,)

admin.site.register([
    WenOptionCategory,
    WenOption,
    WangOptionCategory,
    WangOption,
    DiseaseOptionCategory,
    PulseOption,
    EyeOption, 
    EyeCategory,])