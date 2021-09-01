from django.db import models

# Create your models here.
# one to one modelrelation

class User(models.Model):
    name = models.CharField(max_length=100)


class UserDetail(models.Model):
    # remeber we keep DOB & calculate
    # users age dynamically
    # for demo we keep age field
    age = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # we can pollute data in the db thorugh ORM
    # python3 manage.py shell and import models
