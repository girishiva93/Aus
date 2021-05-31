from django.shortcuts import render,get_object_or_404
from .models import Service

# Create your views here.
def getServiceDetail(request,service_id):
    serviceDetail = get_object_or_404(Service, pk=service_id)
    context = {
        'serviceDetail':serviceDetail
    }
    return render(request,'pages/serviceDetail.html',context)
