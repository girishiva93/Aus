from django.db import models
from pages.img_compression import compressImage


class Message(models.Model):
    hero_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    message_title = models.CharField(max_length=100)
    message_description = models.TextField()
    message_description_1st = models.TextField(blank=True)
    message_description_2nd = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.message_title

    def save(self, *args, **kwargs):
        compressed_image_profile_photo = compressImage(self.profile_photo)
        compressed_image = compressImage(self.hero_img)
        self.hero_img = compressed_image
        self.profile_photo = compressed_image_profile_photo
        super().save(*args, **kwargs)
