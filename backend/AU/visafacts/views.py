from django.shortcuts import render, get_object_or_404
from .models import VisaDetail

# Create your views here.


def getVisaDetail(request):
    visaDetail = get_object_or_404(VisaDetail)

    context = {
        'visaDetail': visaDetail
    }

<<<<<<< HEAD
    return render(request, 'pages/visafact.html', context)
=======
    return render(request,'pages/visafact.html',context)

>>>>>>> da8cb9644141ce94c3b2320d35773329453cdad6
