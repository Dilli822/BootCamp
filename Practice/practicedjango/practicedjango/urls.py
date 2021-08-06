from django.urls import path, include
from app.views import home
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home),
    path('template/', include('mTemplate.urls')),

]
