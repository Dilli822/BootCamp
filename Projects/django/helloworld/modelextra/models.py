
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    bio = models.CharField(max_length=200, blank=True)

    detail = models.CharField(max_length=200,null=True)

    is_active =models.BooleanField(default=False)

    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)
