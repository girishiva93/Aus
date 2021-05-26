from django.urls import path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('aboutteam/', views.meetourteam, name='meetourteam'),
    path('messagefromCEO/', views.MessageFromCEO, name='MessageFromCEO')
]
