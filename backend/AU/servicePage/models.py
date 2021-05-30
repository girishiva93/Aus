from django.db import models
from pages.img_compression import compressImage

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=300)
    service_description = models.TextField()
    service_img = models.ImageField(upload_to = 'photos/%Y/%m/%d/')

    def __str__(self):
        return self.service_title

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.service_img)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)