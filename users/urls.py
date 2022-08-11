from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from .views import EmployeeViewSet, EmployeeWorkScheduleViewSet

router = SimpleRouter()

router.register('', EmployeeViewSet, basename='users')
router.register('work/schedule', EmployeeWorkScheduleViewSet, basename='employeeWorkSchedule')
urlpatterns = router.urls
