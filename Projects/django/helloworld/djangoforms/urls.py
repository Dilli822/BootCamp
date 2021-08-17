
from django.urls import path

from .views import forms_home

urlpatterns = [
    path('home', forms_home),
]