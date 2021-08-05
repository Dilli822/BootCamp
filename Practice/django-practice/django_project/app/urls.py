

from django.urls import path

from app.views import first_template

urlpatterns = [
    path('first-template/', first_template),
]