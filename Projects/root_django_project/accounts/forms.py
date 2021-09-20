
from django import forms
from django.contrib.auth import get_user_model
from django.forms.fields import CharField, EmailField
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    # max_length is 150 from models
    username = forms.CharField(max_length=100)
    # max password lenth is 128
    # putting *** this in password
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    user_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
