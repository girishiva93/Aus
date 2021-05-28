from django.db import models


class Service(models.Model):
    hero_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    hero_title = models.CharField(max_length=300)
    hero_slogan = models.CharField(max_length=300)
    hero_subject_name = models.CharField(max_length=100)
    hero_subject_name_I = models.CharField(max_length=100)
    hero_button_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hero_subject_name


class Courses(models.Model):
    course_img = models.ImageField(upload_to='photos/%Y/%m/%d')
    course_name = models.CharField(max_length=300)
    teacher_name = models.CharField(max_length=100)
    course_start_date = models.DateField()
    course_description = models.TextField(max_length=200)
    course_button_name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
