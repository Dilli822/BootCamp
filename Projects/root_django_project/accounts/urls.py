

from django.urls import path 

from .views import login_view, profile_view

urlpatterns = [
    # accounts/
    path('login-view/',login_view ),
    path('profile-view/', profile_view),
]