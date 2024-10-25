from django.db import models

# Create your models here.

class Developer(models.Model):
    greeting = models.TextField(null=True,blank=True)
    first_name = models.CharField(null=True,blank=True,max_length=100)
    last_name = models.CharField(null=True,blank=True,max_length=100)
    who = models.CharField(null=True,blank=True,max_length=100)
    picture = models.ImageField(null=True,blank=True)

class AboutWork(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True,blank=True)

class BioCell(models.Model):
    year = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

class Bio(models.Model):
    title = models.CharField(max_length=100)
    cells = models.ManyToManyField(BioCell)

class Platform(models.Model):
    icon = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

class Work(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works/')
    url = models.CharField(max_length=255)

class Wallpaper(models.Model):
    image = models.ImageField(upload_to='wallpapers/')
    url = models.CharField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works/')
    url = models.CharField(max_length=255)

class Use(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='works/')
    url = models.CharField(max_length=255)
