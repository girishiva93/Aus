from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from pages.img_compression import compressImage

# Create your models here.
class VisaDetail(models.Model):
    visa_title = models.CharField(max_length=400,blank=True)
    visa_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    visa_detail = models.TextField(blank=True)
    visa_2nd_title = models.CharField(max_length=400,blank=True)
    visa_2nd_detail = models.TextField(blank=True)

    def __str__(self):
        return self.visa_title

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.visa_img)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)