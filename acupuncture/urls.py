from rest_framework.routers import SimpleRouter
from .views import AcupunctureViewset, AcupunctureRecordViewset

router = SimpleRouter()
router.register('acupuncture', AcupunctureViewset, basename='acupuncture')
router.register('acupuncture/record', AcupunctureRecordViewset, basename='acupuncture_record')
urlpatterns = router.urls
