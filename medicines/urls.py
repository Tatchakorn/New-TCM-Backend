from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import MedicinesViewset

router = SimpleRouter()
router.register('', MedicinesViewset, basename='medicines')
urlpatterns = router.urls

