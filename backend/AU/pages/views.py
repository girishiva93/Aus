from django.shortcuts import get_object_or_404, render
from .models import HeroSlider, UniversityLogo, Testimonial, popup
from indexblog.models import Blog
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
    popup_message = popup.objects.first
    heroSlider = HeroSlider.objects.all()
    universityLogos = UniversityLogo.objects.all()
    testimonials = Testimonial.objects.all()
    message = Message.objects.all()
    blogs = Blog.objects.all()
    context = {
        'popup_message': popup_message,
        'heroSlider': heroSlider,
        'universityLogos': universityLogos,
        'testimonials': testimonials,
        'message': message,
        'blogs': blogs
    }
    return render(request, "pages/index.html", context)
