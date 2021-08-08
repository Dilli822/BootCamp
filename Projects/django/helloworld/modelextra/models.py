
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    bio = models.CharField(max_length=200, blank=True)
