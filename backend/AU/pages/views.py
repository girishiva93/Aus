from django.shortcuts import render
from .models import HeroSlider,UniversityLogo, Testimonial

def index(request):
    heroSlider = HeroSlider.objects.all()
    universityLogos = UniversityLogo.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'heroSlider':heroSlider,
        'universityLogos':universityLogos,
        'testimonials':testimonials
    }
    return render(request,"pages/index.html",context)
