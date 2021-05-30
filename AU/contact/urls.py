from django.urls import path
from . import views  # here . refers all data

urlpatterns = [
    path('', views.index, name='contact'),
    path('enroll/', views.enroll, name='enroll')
]
