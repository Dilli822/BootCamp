from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    age = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # lastly added modelfield
    bio = models.CharField(max_length=200, null=True)


    # this erro will raise because django will confuse
    # and surely ask what to do with existing
    # db table's row and cols and there is no null or default value on the bio table 

    # $ python3 manage.py makemigrations
    # You are trying to add a non-nullable field 'bio' to userinfo without a default; we can't do that (the database needs something to populate existing rows).
    # Please select a fix:
    #  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    #  2) Quit, and let me add a default in models.py
    # Select an option: 
    
    # python3 manage.py shell ORM hit,update,add,delete,save
    # full_clean() method validaiton method
    def save(self, **kwargs):
        self.full_clean()
        return super().save(**kwargs)

    
    # get() method only return unique data
    # you can put loop in obj like obj = UserInfo.objects.get(id=1)
    # for i in obj: print(i.name)