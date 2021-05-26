from django.shortcuts import render


def about(request):
    return render(request, 'pages/aboutcompany.html')


def meetourteam(request):
    return render(request, 'pages/meetourteam.html')


def MessageFromCEO(request):
    return render(request, 'pages/messagefromceo.html')
