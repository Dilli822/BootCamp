from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    age = models.IntegerField()
    is_active = models.BooleanField(default=False)



    # python3 manage.py shell ORM hit,update,add,delete,save
    
    # full_clean() method validaiton method
    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)
        