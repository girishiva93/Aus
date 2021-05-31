from django.db import models
from pages.img_compression import compressImage


class AboutTeam(models.Model):
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    hover_profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_descriptions = models.TextField(blank=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.reviewer_image)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)
