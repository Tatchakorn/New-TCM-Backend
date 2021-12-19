from rest_framework.routers import SimpleRouter
from .views import (
    PatientViewSet, 
    DiagnosisViewSet, 
    SheImagesViewSet, 
    YanImagesViewSet,
    OwnedPatientsViewSet)

router = SimpleRouter()
router.register('', PatientViewSet, basename='patients')
router.register('diagnosis/info', DiagnosisViewSet, basename='diagnosis')
router.register(
    'diagnosis/images/she',
    SheImagesViewSet,
    basename='diagnosis_she')
router.register(
    'diagnosis/images/yan',
    YanImagesViewSet,
    basename='diagnosis_yan')
router.register(
    'owned-patients',
    OwnedPatientsViewSet,
    basename='owned_patients')
urlpatterns = router.urls
