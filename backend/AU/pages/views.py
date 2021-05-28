from django.shortcuts import get_object_or_404, render
from .models import HeroSlider, UniversityLogo, Testimonial
from messagefromceo.models import Message
from meetteam.models import AboutTeam


def MessageFromCEO(request, message_id):

    messages = get_object_or_404(Message, pk=message_id)
    aboutteam = AboutTeam.objects.all()

    context = {
        'messages': messages,
        'aboutteam': aboutteam,
    }

    return render(request, 'pages/messagefromceo.html', context)


def index(request):
    heroSlider = HeroSlider.objects.all()
    universityLogos = UniversityLogo.objects.all()
    testimonials = Testimonial.objects.all()
    message = Message.objects.all()
    context = {
        'heroSlider': heroSlider,
        'universityLogos': universityLogos,
        'testimonials': testimonials,
        'message': message
    }
    return render(request, "pages/index.html", context)
