from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrations/', views.view_registrations, name='view_registrations'),
]
