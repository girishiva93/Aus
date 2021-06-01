from django.db import models
from pages.img_compression import compressImage


class AboutCompany(models.Model):
    about_title = models.CharField(max_length=200)
    hero_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    about_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    seo_tag = models.CharField(max_length=100)
    about_description = models.TextField()
    about_description_sub = models.TextField()
    about_description_sub_I = models.TextField()

    def __str__(self):
        return self.about_title

    def save(self, *args, **kwargs):
        compressed_image_hero_img = compressImage(self.hero_img)
        compressed_image = compressImage(self.about_img)
        self.about_img = compressed_image
        self.hero_img = compressed_image_hero_img
        super().save(*args, **kwargs)
