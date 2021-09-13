from django.urls import path
from django.urls.resolvers import URLPattern

from .views import forms_home, django_form, django_model_form


urlpatterns = [
    # forms/home
    path('home/', forms_home),
    path('django-form/', django_form),
    path('django-model-form/', django_model_form),
]
