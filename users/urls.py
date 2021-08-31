from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    UserViewSet, OwnPatientViewSet, PastPatientViewSet
)

router = SimpleRouter()
router.register('user', UserViewSet, basename='users')
router.register('own', OwnPatientViewSet, basename='own_patients')
router.register('past', PastPatientViewSet, basename='past_patients')

urlpatterns = router.urls
