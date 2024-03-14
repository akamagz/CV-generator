from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    about = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    work_experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
