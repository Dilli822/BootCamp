


from rest.views import add_two_numbers
from django.urls import path

app_name = "rest"

urlpatterns = [
    path('add/', add_two_numbers)
  ]