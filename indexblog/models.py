from django.db import models

from datetime import datetime
from django.urls import reverse
from pages.img_compression import compressImage


class Blog(models.Model):
    """
    Blog Model

    Fields
        blog_title
        blog_tag
        blog_image
        blog_describe
        is_published
        list_date
        ....rest
    """
    blog_title = models.CharField(max_length=700)
    blog_tag = models.CharField(max_length=400)
    blog_image = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=False, max_length=500)
    author = models.CharField(max_length=200)
    blog_describe = models.TextField(blank=False)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blogs', args=[self.id, ])

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.blog_image)
        self.blog_image = compressed_image
        super().save(*args, **kwargs)
