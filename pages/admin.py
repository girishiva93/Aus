from django.contrib import admin
from .models import HeroSlider, UniversityLogo, Testimonial, popup

# Register your models here.
admin.site.register(popup)
admin.site.register(HeroSlider)
admin.site.register(UniversityLogo)
admin.site.register(Testimonial)
