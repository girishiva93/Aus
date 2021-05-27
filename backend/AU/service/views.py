from django.shortcuts import render


def service(request):
    return render(request, 'pages/service.html')
