from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='Traditional Chinese Medicine API',
        default_version='v1',
        description='',
        # terms_of_service='',
        # contact=openapi.Contact(email=''),
        # license=openapi.License(name='License'),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),        # patients app
    path('users/', include('users.urls')),              # users app
    path('diseases/', include('diseases.urls')),        # diseases app
    path('medicines/', include('medicines.urls')),      # medicines app
    path('pulse/', include('pulse.urls')),              # pulse app
    path('acupuncture/', include('acupuncture.urls')),  # acupuncture app
    path('option/', include('option.urls')),  # option app
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
