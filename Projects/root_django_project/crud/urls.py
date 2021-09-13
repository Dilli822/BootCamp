
from django.urls import path

from .views import list_all_user

urlpatterns = [
    path('list/', list_all_user),
]