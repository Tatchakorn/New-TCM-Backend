from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import (
    MedicineViewset, 
    MedicineRecordViewset,
    DecoctionViewSet,
    DecoctionComponentsViewSet,
    DecoctionRecordViewSet,
    )

router = SimpleRouter()
router.register('meds', MedicineViewset, basename='medicines')
router.register('meds-record', MedicineRecordViewset, basename='medicine_record')
router.register('decoction', DecoctionViewSet, basename='decoction')
router.register('decoction-component', DecoctionComponentsViewSet, basename='decoction_component')
router.register('decoction-record', DecoctionRecordViewSet, basename='decoction_record')
urlpatterns = router.urls

