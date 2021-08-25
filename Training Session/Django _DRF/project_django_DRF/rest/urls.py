
from .views import add_two_numbers
from django.urls import path

urlpatterns = [
    #rest/
    path('add/', add_two_numbers),
]