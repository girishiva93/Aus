from django.shortcuts import render


def MessageFromCEO(request):
    return render(request, 'pages/messagefromceo.html')
