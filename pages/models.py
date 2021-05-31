from django.db import models
from pages.img_compression import compressImage

# Create your models here.


class HeroSlider(models.Model):
    slider_image_name = models.CharField(max_length=200)
    slider_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    slider_image_title = models.CharField(max_length=100)
    slider_image_description = models.TextField()
    slider_image_button_name = models.CharField(max_length=20)

    def __str__(self):
        return self.slider_image_name

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.slider_image)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)


class UniversityLogo(models.Model):
    university_name = models.CharField(max_length=400)
    university_logo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.university_name

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.university_logo)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    reviewer_name = models.CharField(max_length=200)
    reviewer_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    reviewer_description = models.TextField()

    def __str__(self):
        return self.reviewer_name

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.reviewer_image)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)


class popup(models.Model):
    pop_up_heading = models.CharField(max_length=200)
    pop_up_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    button_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pop_up_heading

    def save(self, *args, **kwargs):
        compressed_image = compressImage(self.pop_up_img)
        self.slider_image = compressed_image
        super().save(*args, **kwargs)
