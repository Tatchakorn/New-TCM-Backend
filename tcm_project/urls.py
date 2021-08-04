from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),  # patients app
    path('api-auth/', include('rest_framework.urls')),
    path('patients/auth/', include('dj_rest_auth.urls')),
    path('patients/auth/registration', include('dj_rest_auth.registration.urls')),
]
