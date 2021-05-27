from django.shortcuts import render


def meetourteam(request):
    return render(request, 'pages/meetourteam.html')
