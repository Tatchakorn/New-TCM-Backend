from django.contrib import admin
from .models import Acupuncture,  AcupunctureRecord

admin.site.register([Acupuncture, AcupunctureRecord])
