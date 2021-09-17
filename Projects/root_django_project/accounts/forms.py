
from django import forms

class LoginForm(forms.Form):
    # max_length is 150 from models
    username = forms.CharField(max_length=100)
    # max password lenth is 128
    # putting *** this in password
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
