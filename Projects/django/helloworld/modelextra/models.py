from django.db import models

from django.core.exceptions import ValidationError
from django.db.models.fields import CharField

def my_age_validator(age):
    if age < 16:
        raise ValidationError("You must be 16 years old to get full access!")

def clean(age):
    if age > 40:
        if not age.bio:
            raise ValidationError("Bio is required for age over 40")

class UserInfo(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[my_age_validator])
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, null=True)

    bio = models.TextField(max_length=200, blank=True)


    def __str__(self):
        return self.name
    
    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)