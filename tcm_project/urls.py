from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='TCM API',
        default_version='v1',
        description="API for TCM project",
        # terms_of_service='',
        # contact=openapi.Contact(email=''),
        # license=openapi.License(name='License'),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),  # patients app
    path('api-auth/', include('rest_framework.urls')),
    path('patients/auth/', include('dj_rest_auth.urls')),
    path('patients/auth/registration', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
