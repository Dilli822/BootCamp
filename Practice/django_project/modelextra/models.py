from django.db import models

from django.core.exceptions import ValidationError


# creating a small custom validator
def my_age_validator(age):
    if age < 20:
        raise ValidationError("Your age should be 20 or equals to 20!")

class UserBio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[my_age_validator])

    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


# Clean method for conditions if age is more than 40 then bio is compulsory
    def clean(self):
        if self.age > 40:
            if not self.bio:
                raise ValidationError("Bio is required when your age is more than or equals to 40")

