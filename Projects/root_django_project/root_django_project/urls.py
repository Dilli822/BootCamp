"""root_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from login.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from world.views import debug_request, home, int_converter_view, profile, RamProfile
from world.views import profile_json, int_converter_view
from login.views import open
from django.contrib.auth.views import LoginView, LogoutView
from login import views as open

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('profile/', profile, name="profile"),
    # this is  static url
    path('RamProfile/ram', RamProfile),
   
    # this is dynamic url with path converter
    path('profile/<str:username>/', profile),

    #url for profile json
    path('profile-json/<str:username>', profile_json),

    # url path converter integer into string
    # this will raise error if integer data is not sent in the url
    # http://127.0.0.1:8000/path-converter-int/string/ 
    # path('path-converter-int/<int:int_data>/', int_converter_view),
    
    # just make a simple change in path converter i.e. <str>
    # http://127.0.0.1:8000/path-converter-int/passingstringbuttpathconverterworks/
    path('path-converter-int/<str:int_data>/', int_converter_view),

    # path for test 
    # only hitting this http://127.0.0.1:8000/test-path/ will bring ValueError
    path('test-path/', debug_request, name="test-path"),


    # path for templating urls with include
    path('template/', include('templating.urls')),

    # path for formspractice
    path('forms/', include('formspractice.urls')),

    # path for staticmedia 
    path('static-demo/', include('staticmedia.urls')),

    # for crud 
    # for making a tags and link dynamic
    path('crud/', include('crud.urls', namespace='crud')),

    # for classbased 
    path('c/', include('classbased.urls', namespace='classbased')),
    

    # for login
    path('log/',include('login.urls', namespace='login')),


    # # for middleware apps
    path('', open.open, name='open'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    # path('', user_views.home, home='home')
    path('login/', open.LoginView, name='login'),
    # path('logout/', open.LogoutView, name='login'),


    # URL for accounts app
    path('accounts/', include('accounts.urls')),

]

# default static url is with static url/staticfileName
# http://127.0.0.1:8000/static/main.js
# STATIC_URL = '/static/'

# settings for serving
from django.conf import settings
from django.conf.urls.static import static

# creating new url with importing settings MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)