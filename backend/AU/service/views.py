from django.shortcuts import render
from .models import Service, Courses


def service(request):
    services = Service.objects.first
    courses = Courses.objects.all()

    context = {
        'services': services,
        'courses': courses,
    }
    return render(request, 'pages/service.html', context)
