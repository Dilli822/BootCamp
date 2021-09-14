
from django.urls import path

from .views import (create_user_info, delete_user_info,
 detail_view_of_users, list_all_user, update_user_info )

urlpatterns = [
    # crud/
    path('list/', list_all_user),
    # capturing value
    path('detail/<int:user_id>/', detail_view_of_users),
    path('create/', create_user_info),
    path('update/<int:user_id>/', update_user_info),
    path('delete/<int:user_id>/', delete_user_info)
    
]