from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PatientViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', UserViewSet, basename='patients')
urlpatterns = router.urls
