from django.db import models

from django.contrib.auth.models import AbstractUser

# class UserDetail(models.Model):
#     phone_number = models.CharField(max_length=100)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# swapable model
class User(AbstractUser):
    pass