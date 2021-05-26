from django.db import models
from pages.img_compression import compressImage

# Create your models here.
class GalleryImage(models.Model):
    image_title = models.CharField(max_length=400)
    image = models.ImageField(upload_to = 'photos/%Y/%m/%d/')

    def __str__(self):
        return self.image_title
    
    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.image)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)