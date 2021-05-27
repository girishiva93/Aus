from django.db import models


class AboutCompany(models.Model):
    about_title = models.CharField(max_length=200)
    hero_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    about_description = models.TextField()
    about_description_sub = models.TextField()
    about_description_sub_I = models.TextField()

    def __str__(self):
        return self.about_title
