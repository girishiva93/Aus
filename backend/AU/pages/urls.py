from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:message_id>', views.MessageFromCEO, name='messages'),
    # path('service/<int:service_id>',views.getServiceDetail ,name="serviceDetail")
]
