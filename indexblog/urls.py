from django.urls import path
from . import views  # here . refers all data
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap


sitemaps = {
    'blogs': BlogSitemap,
}

urlpatterns = [
    path('', views.indexblog, name='blog'),
    path('<int:blog_id>', views.blog, name='blogs'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
