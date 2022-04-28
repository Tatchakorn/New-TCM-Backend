from rest_framework.routers import SimpleRouter
from .views import (
    AcupunctureViewset,
    DongAcupunctureViewset,
    AcupunctureAreaViewset,
    DongAcupunctureAreaViewset)


router = SimpleRouter()
router.register('acupuncture', AcupunctureViewset, basename='acupuncture')
router.register('dong-acupuncture', DongAcupunctureViewset, basename='acupuncture')
router.register('acupuncture/area', AcupunctureAreaViewset, basename='acupuncture')
router.register('dong-acupuncture/area', DongAcupunctureAreaViewset, basename='acupuncture')
urlpatterns = router.urls
