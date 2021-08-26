from django.db import models

# Create your models here.

from django.contrib.auth.models import User as DJUser

# class UserDetail(models.Model):
#     phone_number = models.CharField(max_length=50)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class User(models.Model):
    pass 