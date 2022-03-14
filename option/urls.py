from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import (
    WenOptionCategoryViewset,
    WangOptionCategoryViewset,
    WenOptionViewset,
    WangOptionViewset,
    PulseOptionViewset,
    DiseaseOptionViewset,
    DiseaseOptionCategoryViewset)

router = SimpleRouter()
router.register('wen-category', WenOptionCategoryViewset)
router.register('wang-category', WangOptionCategoryViewset)
router.register('wen', WenOptionViewset)
router.register('wang', WangOptionViewset)
router.register('pulse', PulseOptionViewset)
router.register('disease', DiseaseOptionViewset)
router.register('disease-category', DiseaseOptionCategoryViewset)
urlpatterns = router.urls

