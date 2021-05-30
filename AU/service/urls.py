from django.urls import path

from . import views

urlpatterns = [
    path('', views.service, name='company_service'),
]
