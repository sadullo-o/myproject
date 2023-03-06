from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title