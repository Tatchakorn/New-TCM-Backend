from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import DiseasesViewset

router = SimpleRouter()
router.register('', DiseasesViewset, basename='diseases')
urlpatterns = router.urls
