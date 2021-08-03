from django.urls import path

from .views import PatientList, PatientDetial

urlpatterns = [
    path('<int:pk>/', PatientDetial.as_view()),
    path('', PatientList.as_view()),
]
