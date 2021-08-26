
from .views import add_two_numbers, add_two_numbers_in_rest
from django.urls import path

urlpatterns = [
    #rest/add/
    path('add/', add_two_numbers),
    path('v2/add/', add_two_numbers_in_rest),    
]