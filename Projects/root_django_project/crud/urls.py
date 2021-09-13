
from django.urls import path

from .views import detail_view_of_users, list_all_user

urlpatterns = [
    # crud/
    path('list/', list_all_user),
    # capturing value
    path('detail/<int:user_id>/', detail_view_of_users),
]