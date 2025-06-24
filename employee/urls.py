from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_employee, name='register'),
    path('success/', views.registration_success, name='success'),
]
