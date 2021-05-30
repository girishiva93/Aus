from django.shortcuts import render
from .models import AboutTeam


def meetourteam(request):
    aboutteam = AboutTeam.objects.all()
    context = {
        'aboutteam': aboutteam,
    }
    return render(request, 'pages/meetourteam.html', context)
