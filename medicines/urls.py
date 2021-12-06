from rest_framework import routers, urlpatterns
from rest_framework.routers import SimpleRouter
from .views import FangMedicinesViewset, YaoMedicinesViewset

router = SimpleRouter()
router.register('fang', FangMedicinesViewset, basename='fang_medicines')
router.register('yao', YaoMedicinesViewset, basename='yao_medicines')
urlpatterns = router.urls

