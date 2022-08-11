from django.contrib import admin
from .models import Medicine, MedicineRecord, Decoction, DecoctionComponents, DecoctionRecord

admin.site.register([Medicine, MedicineRecord, Decoction, DecoctionComponents, DecoctionRecord])

