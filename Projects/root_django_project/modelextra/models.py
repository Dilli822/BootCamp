from django.db import models

# Importing validation error

from django.core.exceptions import ValidationError

# making gun for validators

def validate_my_age(age):
    if age < 20:
        raise ValidationError("You age must be more than 18 or eqauls to 18.")


class UserBio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(validators=[validate_my_age])


    bio = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.name

    # if we hit direct ORM to database it will ignore validations untill full_Clean() method is called
    # ValidationError: {'email': ['This field cannot be blank.'], 'age': ['YOu age must be more than 18 or eqauls to 18.']}


    # for model validation
    # with conditions
    def clean(self):
        if self.age > 35:
            if not self.bio:
                raise ValidationError("Bio is required when age is greater then 35 age > 35.")
