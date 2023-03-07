import datetime

from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Construction(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title


class DataGallery(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Project(models.Model):
    klas = models.CharField(max_length=100)
    img = models.ImageField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    data_gallery = models.ForeignKey(DataGallery, on_delete=models.CASCADE)
    img_title = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)
    content = models.TextField()
    type = models.CharField(max_length=100, default='')
    dataosdelay = models.IntegerField(default=100)
    img = models.ImageField(default='service-1.jpg')
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField(default='')

    def __str__(self):
        return self.name