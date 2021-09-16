from rest_framework.routers import SimpleRouter
from .views import PatientViewSet, DiagnosisViewSet

router = SimpleRouter()
router.register('', PatientViewSet, basename='patients')
router.register('diagnosis', DiagnosisViewSet, basename='diagnosis')
urlpatterns = router.urls
