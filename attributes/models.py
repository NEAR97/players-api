from django.db import models

# Create your models here.
class Attribute(models.Model):
    name = models.TextField()
    country = models.TextField()
    birth = models.TextField()
    age = models.TextField(blank=True)
    club = models.TextField()
    position = models.TextField(blank=True)
    nickname = models.TextField(blank=True)
    height = models.TextField(blank=True)
    weight = models.TextField(blank=True)
    Njersey = models.TextField(blank=True)
