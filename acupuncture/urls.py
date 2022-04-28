from rest_framework.routers import SimpleRouter
from .views import (
    AcupunctureViewset,
    DongAcupunctureViewset,
    AcupunctureAreaViewset,
    DongAcupunctureAreaViewset)


router = SimpleRouter()
router.register('acu/area', AcupunctureAreaViewset, basename='area')
router.register('dong-acu/area', DongAcupunctureAreaViewset, basename='dong-area')
router.register('acupuncture', AcupunctureViewset, basename='acupuncture')
router.register('dong-acupuncture', DongAcupunctureViewset, basename='dong-acupuncture')
urlpatterns = router.urls
