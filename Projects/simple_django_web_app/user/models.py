from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    middle_name = models.CharField(max_length=100)


    # groups = None
    # user_permissions = None

    
