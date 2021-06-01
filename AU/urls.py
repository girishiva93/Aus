from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('gallery/', include('gallery.urls')),
    path('about/', include('indexabout.urls')),
    path('visafacts/', include('visafacts.urls')),
    path('servicePage/', include('servicePage.urls')),
    path('meet-our-team/', include('meetteam.urls')),
    path('service/', include('service.urls')),
    path('blog/', include('indexblog.urls')),
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
