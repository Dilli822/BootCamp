

from django.urls import path 

from .views import logout_view, login_view, profile_view, fail_view, signup_view

urlpatterns = [
    # accounts/
    path('login-view/',login_view ),
    path('profile-view/', profile_view),
    path('fail-view/', fail_view),
    path('logout-view/', logout_view),
    path('signup-view/', signup_view),
]