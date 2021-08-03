# """helloworld URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.urls import path
# #this will tell the django where is our landing url
# from world.views import home
#
# urlpatterns = [
#         path('world/', home),
# ]

# registering new url for view in urls.py

# from django.urls import path
# from world.views import home

# urlpatterns = [
#     path('world/', home),
# ]


from django.urls import path
from django.contrib import admin

# importing views from world app folder and importiing home function
# importing debu_request function
from world.views import home, profile, profile_json, int_converter_view, debug_request


#now we need to import profile too
#from profile.views import phome, profile

# capturing values from urls
urlpatterns = [
        # path('profile/dilli/', profile),
        # path('profile/hang/', profile),
        # path('profile/peter/', profile),
        # path('profile/sam/', profile),
        # path('world/', home),
        path('profile/<str:name>/', profile),
        # crating new url for profileJSON with parameter profile_json
        path('profile-json/<str:name>/', profile_json),
        #making new url for str to int or path converter
        # path('path/<int:int_data>/', int_converter_view),
        path('path/<str:int_data>/', int_converter_view),
        # new path for test or debug
        # without capturing url value ie.with <str:int_data>
        path('test-path/', debug_request),
        path('', home),
]