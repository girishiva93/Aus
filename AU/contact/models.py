from django.db import models
from django.db.models.fields import CharField
from phone_field import PhoneField


class Contact(models.Model):
    """
    Contact model

    Fields
        full_name
        email
        phone
        message
    """
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    message = models.TextField()

    def __str__(self):
        return self.full_name


class Enroll(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    qualification = models.CharField(max_length=20)
    course_completed = models.CharField(max_length=20)
    GPA = models.CharField(max_length=20)
    institution_name = models.CharField(max_length=200)
    parents_Name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    courses = models.CharField(max_length=100)
    scores = models.CharField(max_length=20)
    planning_to_take_test = models.CharField(max_length=200)
    where_to_study = models.CharField(max_length=100)
    preferred_course = models.CharField(max_length=200)
    preferred_uni = models.CharField(max_length=200)
    declare_to_use_information = models.CharField(max_length=100)
    can_use_details = models.CharField(max_length=20)
    consult_date = models.DateField(max_length=200)
    how_do_you_know_us = models.CharField(max_length=200)
