from django.shortcuts import render


def indexblog(request):

    return render(request, 'pages/blog.html')
