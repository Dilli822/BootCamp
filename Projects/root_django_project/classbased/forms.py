# we could have linked the crud forms.py but
# in this case we have copied mannually
from django.forms import ModelForm

from .models import UserInfo


class UserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'middle_name', 'last_name',
        'email', 'dob']

        