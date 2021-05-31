from django.urls import path

from . import views

urlpatterns = [
    path('<int:service_id>', views.getServiceDetail, name='serviceDescription'),
]
