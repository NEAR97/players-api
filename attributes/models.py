from django.db import models
from django.conf import settings
# ...code

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
    jersey = models.TextField(blank=True)
    
posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attribute = models.ForeignKey('attributes.Attribute', related_name='votes', on_delete=models.CASCADE)