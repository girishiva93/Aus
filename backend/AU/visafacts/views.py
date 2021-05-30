from django.shortcuts import render, get_object_or_404
from .models import VisaDetail

# Create your views here.


def getVisaDetail(request):
    visaDetail = get_object_or_404(VisaDetail)

    context = {
        'visaDetail': visaDetail
    }

    return render(request, 'pages/visafact.html', context)
