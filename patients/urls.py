from rest_framework.routers import SimpleRouter
from .views import (
    PatientViewSet, 
    PatientRegisterRecordViewSet, 
    DiagnosisRecordViewSet, 
    EyeImageViewSet,
    TongueImageViewSet,
    OtherMediaViewSet,
    )

router = SimpleRouter()
router.register('', PatientViewSet, basename='patients')
router.register('patient/register', PatientRegisterRecordViewSet, basename='patients')
router.register('diagnosis/info', DiagnosisRecordViewSet, basename='diagnosis')
router.register(
    'diagnosis/images/eye',
    EyeImageViewSet,
    basename='diagnosis_eye')
router.register(
    'diagnosis/images/tongue',
    TongueImageViewSet,
    basename='diagnosis_tongue')
router.register(
    'diagnosis/videos',
    OtherMediaViewSet,
    basename='other_media')

urlpatterns = router.urls

