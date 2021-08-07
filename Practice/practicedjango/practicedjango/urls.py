from django.urls import path, include
from django.contrib import admin
from app.views import home
from app.views import int_converter, users, user

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home),
    path('template/', include('mTemplate.urls')),\
    path('int-converter/<str:int_data>/', int_converter),
    path('users/<str:name>/', users),
    path('user/<str:name2>/', user),
]
