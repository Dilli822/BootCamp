from django.urls import path

from .views import hello_templates , hello_render

urlpatterns = [

    # here url will be /templates/hello/
    # because root url conf is ready joined with it
    path('hello/', hello_templates),
    path('hello-render/', hello_render),
]
