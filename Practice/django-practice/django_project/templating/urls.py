
from django.urls import path
from .views import home_template

urlpatterns = [
    path('home-template/', home_template),

]