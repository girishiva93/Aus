from django.shortcuts import render,get_object_or_404
from .models import VisaDetail

# Create your views here.
def getVisaDetail(request,visa_id):
    visaDetail = get_object_or_404(VisaDetail,pk=visa_id)

    context = {
        'visaDetail' : visaDetail
    }

    return render(request,'pages/visafact.html')

