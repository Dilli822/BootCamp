"""django_project URL Configuration

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
from django.urls import path

from django.contrib import admin
from django.urls import path
from app.views import home, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),
    # path('profile/', profile),
    # path('control/', control_center),
    # path('user/', user),
    # now we create a dynamic path with the help of path converter
    # now we format the string and use path converter to make url dynamic
    # path('profile/<str:name>/', profile),
    # path('control/<str:culprit>/', control_center),
    path('/', home),
    path('blog/<str:name>/', blog)
]
