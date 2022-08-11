from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import (
    MedicineViewset, 
    MedicineRecordViewset,
    DecoctionViewSet,
    DecoctionComponentsViewSet,
    DecoctionRecordViewSet,
    InjuryTreatmentViewSet,
    InjuryTreatmentRecordViewSet,
    )

router = SimpleRouter()
router.register('meds', MedicineViewset, basename='medicines')
router.register('meds-record', MedicineRecordViewset, basename='medicine_record')
router.register('decoction', DecoctionViewSet, basename='decoction')
router.register('decoction-component', DecoctionComponentsViewSet, basename='decoction_component')
router.register('decoction-record', DecoctionRecordViewSet, basename='decoction_record')
router.register('injury', InjuryTreatmentViewSet, basename='injury')
router.register('injury-record', InjuryTreatmentRecordViewSet, basename='injury_record')
urlpatterns = router.urls

