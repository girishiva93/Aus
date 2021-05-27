from django.shortcuts import render
from .models import AboutCompany


def about(request):
    aboutcompany = AboutCompany.objects.all()
    context = {
        'aboutcompany': aboutcompany,
    }
    return render(request, 'pages/aboutcompany.html', context)
