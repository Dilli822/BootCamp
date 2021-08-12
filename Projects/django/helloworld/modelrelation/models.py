from django.db import models

from django.core.exceptions import ValidationError

class User(models.Model):
    name = models.CharField(max_length=100)

class Address (models.Model):
    street = models.CharField(max_length=100)

class UserDetail(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # as foreign key
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    
