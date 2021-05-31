from django.db import models
from pages.img_compression import compressImage


class AboutCompany(models.Model):
    about_title = models.CharField(max_length=200, blank=True)
    hero_img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    about_img = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    seo_tag = models.CharField(max_length=100, blank=True)
    about_description = models.TextField(blank=True)
    about_description_sub = models.TextField(blank=True)
    about_description_sub_I = models.TextField(blank=True)

    def __str__(self):
        return self.about_title

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.about_img, self.hero_img)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)
