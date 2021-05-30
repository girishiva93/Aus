from django.urls import path

from . import views

urlpatterns = [
    path('<int:visa_id>', views.getVisaDetail, name='visafacts'),
]
