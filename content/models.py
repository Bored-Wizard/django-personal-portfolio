from django.db import models

# Create your models here.
class About(models.Model):
    profilepic = models.FileField()
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    name = models.CharField(max_length=24)
    birthdate = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField()


class Work(models.Model):
    name = models.CharField(max_length=50)
    work_url = models.URLField()
    workpic = models.FileField()


class Comments(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=255)
    comment = models.TextField(blank=False)
    picurl = models.FileField()


class Social(models.Model):
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    likedin = models.URLField(blank=True)
    twiter = models.URLField(blank=True)
    skype = models.URLField(blank=True)
    github = models.URLField(blank=True)
    