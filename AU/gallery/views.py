from django.shortcuts import render
from .models import GalleryImage

# Create your views here.
def getGallery(request):
    images = GalleryImage.objects.all()
    context = {
        'images':images
    }
    return render(request, 'pages/gallery.html',context)