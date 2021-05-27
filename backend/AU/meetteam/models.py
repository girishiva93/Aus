from django.db import models


class AboutTeam(models.Model):
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    hover_profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_descriptions = models.TextField(blank=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
