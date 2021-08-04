from rest_framework.routers import SimpleRouter
from .views import PatientViewSet

router = SimpleRouter()
router.register('', PatientViewSet, basename='patients')
urlpatterns = router.urls
