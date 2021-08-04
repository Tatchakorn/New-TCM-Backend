from django.urls import path

from .views import PatientList, PatientDetial, UserList, UserDetial

urlpatterns = [
    path('<int:pk>/', PatientDetial.as_view()),
    path('', PatientList.as_view()),
    path('users/<int:pk>/', UserDetial.as_view()),
    path('users/', UserList.as_view()),
]
