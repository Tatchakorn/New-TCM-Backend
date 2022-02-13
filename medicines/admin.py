from django.contrib import admin
from .models import Medicine, MedicineRecord

admin.site.register([Medicine, MedicineRecord])
