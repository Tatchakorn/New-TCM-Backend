from django.contrib import admin
from .models import (
    Acupuncture, 
    DongAcupuncture, 
    AcupunctureArea, 
    DongAcupunctureArea)


admin.site.register([
    Acupuncture, 
    DongAcupuncture, 
    AcupunctureArea, 
    DongAcupunctureArea])
