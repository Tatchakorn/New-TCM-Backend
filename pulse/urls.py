from rest_framework.routers import SimpleRouter
from .views import PulseViewset

router = SimpleRouter()
router.register('', PulseViewset, basename='pulse')
urlpatterns = router.urls
