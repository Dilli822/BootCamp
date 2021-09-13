
from django.urls import path
from .views import manage_media, render_static

urlpatterns = [
    # static-demo/
    path('demo/', render_static),
    path('media/', manage_media)
]