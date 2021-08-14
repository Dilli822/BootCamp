from django.db import models
from django.db.models.fields import CharField, EmailField

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

        