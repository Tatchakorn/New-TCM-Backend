from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import MedicineViewset, MedicineRecordViewset

router = SimpleRouter()
router.register('meds', MedicineViewset, basename='medicines')
router.register('meds-record', MedicineRecordViewset, basename='medicine_record')
urlpatterns = router.urls

