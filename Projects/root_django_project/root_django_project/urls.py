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
from django.contrib import admin
from django.urls import path, include
from world.views import debug_request, home, int_converter_view, profile, RamProfile
from world.views import profile_json, int_converter_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('profile/', profile),
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
    path('test-path/', debug_request),


    # path for templating urls with include
    path('template/', include('templating.urls')),
    
]
