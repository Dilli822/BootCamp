

from django.forms import ModelForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import user

class StatusMessage(models.Model):
    status = models.CharField(max_length=200)
    user = models.CharField(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user 