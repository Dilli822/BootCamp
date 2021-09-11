from django.urls import path
from django.urls.resolvers import URLPattern

from .views import forms_home


urlpatterns = [
    # forms/home
    path('home/', forms_home),
]
