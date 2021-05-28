from django.shortcuts import render
from .models import Service, Courses


def service(request):
    service = Service.objects.get(pk=1)
    courses = Courses.objects.all()

    context = {
        'service': service,
        'courses': courses,
    }
    return render(request, 'pages/service.html', context)
