
from .views import LoginView, LogoutView
from django.urls import path 


app_name = 'login'
urlpatterns = [
    # log/login-form
    path('login/', LoginView, name='login'),

    # logout
    path('logout/', LogoutView, name='logout'),

]