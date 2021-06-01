from django.shortcuts import render
from .models import AboutCompany
from meetteam.models import AboutTeam
from messagefromceo.models import Message


def about(request):
    aboutcompany = AboutCompany.objects.first
    aboutteam = AboutTeam.objects.all()
    message = Message.objects.all()
    context = {
        'aboutcompany': aboutcompany,
        'aboutteam': aboutteam,
        'message': message
    }
    return render(request, 'pages/aboutcompany.html', context)
