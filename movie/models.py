from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=256, null=True)
    sub_name = models.CharField(max_length=256, null=True)
    year = models.IntegerField(null=True)
    country = models.CharField(max_length=256, null=True)
    genre = models.CharField(max_length=256, null=True)
    director = models.CharField(max_length=256, null=True)
    fees = models.FloatField(null=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name