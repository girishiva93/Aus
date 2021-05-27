from django.shortcuts import render
from .models import AboutCompany
from meetteam.models import AboutTeam


def about(request):
    aboutcompany = AboutCompany.objects.get(id=1)
    aboutteam = AboutTeam.objects.all()
    context = {
        'aboutcompany': aboutcompany,
        'aboutteam': aboutteam,
    }
    return render(request, 'pages/aboutcompany.html', context)
